#!/usr/bin/env python3
"""Generate the native Droid plugin from pinned upstream plus small overlays."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import stat
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'upstream/pstack'
OUT = ROOT / 'harness/pstack/droid'
ADAPTER = 'docs/harness/droid.md'
REVISION = '4dd1d05818d19792e7cd6e818f1667f95f7e1dbe'
TERMS = {
    'Task': r'`Task`|\bTask (tool|subagent|call)',
    'AskQuestion': r'AskQuestion',
    'todolist': r'\btodo ?list\b',
    'generalPurpose': r'generalPurpose',
    'poteto-agent': r'poteto-agent',
    'comment-sicko': r'comment-sicko',
    'readonly': r'readonly: (true|false)|readonly/Ask',
    'environment': r'environment: "(cloud|local)"',
    'cloud_base_branch': r'cloud_base_branch',
    'run_in_background': r'run_in_background',
    'resume': r'`resume`',
    'file_attachments': r'file_attachments',
    'provider slug': r'\bclaude-[a-z]+-\d|\bgrok-\d|\bgpt-\d',
    'inherit-parent': r'inherit-parent',
    'pstack-models.mdc': r'pstack-models\.mdc',
    '.cursor/skills/': r'\.cursor/skills/',
    '~/.cursor/plugins/': r'\.cursor/plugins|\.cursor-plugin/',
    '.cursor/rules/': r'\.cursor/rules|always-applied rule',
    'agent-transcripts': r'agent-transcripts|\.cursor/projects/',
    'Cursor-only features': r'Bugbot|Cursor [Aa]utomation|cursor\.(sh|com)/automations|[Cc]loud [Aa]gent|built-in PR tool',
}

LINK = re.compile(r'\]\(([^)\s]+)\)')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def walk(root):
    return [p for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and 'node_modules' not in p.parts]


def render():
    adapter_text = (SOURCE/ADAPTER).read_text()
    adapter = adapter_text
    coverage = {
        'provider slug': 'model, effort-bearing provider slug',
        'inherit-parent': 'per-role model rule',
        'Cursor-only features': '## Host-specific features',
        '.cursor/rules/': 'always-applied .mdc rules',
        'Run another pstack skill': 'another pstack skill',
    }
    files = {}
    def add(rel, data, executable=False):
        files[rel] = (data if isinstance(data, bytes) else data.encode(), executable)
    for path in walk(SOURCE):
        rel = path.relative_to(SOURCE).as_posix()
        if rel.startswith(('agents/', '.cursor-plugin/')):
            continue
        add(rel, path.read_bytes(), bool(path.stat().st_mode & 0o111))
    add(ADAPTER, adapter)
    manifest = json.loads((SOURCE/'plugin.json').read_text())
    manifest.pop('$schema', None)
    manifest['version'] += '-droid.1'
    add('.factory-plugin/plugin.json', json.dumps(manifest, indent=2)+'\n')
    classifications = {}
    problems = []
    names = []
    for path in sorted((SOURCE/'skills').glob('*/SKILL.md')):
        name = path.parent.name
        names.append(name)
        text = path.read_text()
        fm = re.match(r'^---\n([\s\S]*?)\n---', text)
        found = re.search(r'^name:\s*([^\n]+)', fm[1], re.M) if fm else None
        if not found or found[1].strip(' \"\'') != name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name) or len(name)>64:
            problems.append(f'Invalid source skill identity: {name}')
        subtree = '\n'.join(p.read_text() for p in walk(path.parent) if p.suffix=='.md')
        used = [key for key,pattern in TERMS.items() if re.search(pattern,subtree, re.I if key == 'todolist' else 0)]
        others = '|'.join(re.escape(p.parent.name) for p in (SOURCE/'skills').glob('*/SKILL.md') if p.parent.name != name)
        route = re.compile(r'the \*\*(?P<bold>'+others+r')\*\* skill|`/(?P<command>'+others+r')`')
        if any(any('(../'+(m.group('bold') or m.group('command'))+'/' not in line for m in route.finditer(line)) for line in subtree.splitlines()):
            used.append('Run another pstack skill')
        classifications[name] = used
        if used and re.search(r'^# ', text, re.M):
            for key in used:
                if coverage.get(key, key) not in adapter_text:
                    problems.append(f'Missing adapter mapping: {key}, used by {name}')
            pointer = f'In Droid, read [the Droid adapter](../../{ADAPTER}) once per session before following this skill. It maps the original harness names to native Droid features.'
            if re.search(r'^# ', text, re.M):
                text = re.sub(r'^(# .*)\n+',lambda m:m[1]+'\n\n'+pointer+'\n\n',text,count=1,flags=re.M)
            else:
                end = text.index('\n---', 4) + 4
                text = text[:end] + '\n\n' + pointer + '\n\n' + text[end:].lstrip('\n')
            add(f'skills/{name}/SKILL.md',text)
    for name in ('poteto-agent','comment-sicko'):
        text = (SOURCE/f'agents/{name}.md').read_text()
        end = text.index('\n---',4)
        fm = text[:end].replace('\nis_background: true','')+'\nmodel: inherit'+('\ntools: read-only' if name=='comment-sicko' else '')+'\n---'
        body = text[end+4:].lstrip('\n')
        prelude = 'Read the Droid adapter and full role contract using absolute plugin paths supplied by the parent. Translate all Cursor names with that adapter. No nested Task; return required fan-out to the parent.\n\n'
        add(f'droids/{name}.md',fm+'\n\n'+prelude+body)
    # Validate all local Markdown targets; only omitted original files are linked upstream.
    for rel,(data,mode) in list(files.items()):
        if not rel.endswith('.md'):
            continue
        text=data.decode()
        def rewrite(match):
            href=match[1]
            if href == 'url':  # Original [label](url) template placeholder.
                return match[0]
            if '://' in href or href.startswith('#') or any(c in href for c in '<>{}'):
                return match[0]
            target=(Path(rel).parent/href.split('#',1)[0]).as_posix()
            import posixpath
            target=posixpath.normpath(target)
            present=target in files or any(x.startswith(target.rstrip('/')+'/') for x in files)
            if present:
                return match[0]
            source=SOURCE/target
            if source.exists() and not target.startswith('../'):
                kind='tree' if source.is_dir() else 'blob'
                suffix='#'+href.split('#',1)[1] if '#' in href else ''
                return f'](https://github.com/cursor/plugins/{kind}/{REVISION}/pstack/{target}{suffix})'
            # Root-only installed README links may refer to caller placeholders.
            if target and not target.startswith('../'):
                problems.append(f'Broken generated link {rel}: {href}')
            return match[0]
        add(rel,LINK.sub(rewrite,text),mode)
    if problems:
        raise RuntimeError('\n'.join(problems))
    return files, classifications


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    files, classes=render()
    actual={p.relative_to(OUT).as_posix():p for p in walk(OUT)} if OUT.exists() else {}
    drift=[rel for rel in sorted(set(files)|set(actual)) if rel not in files or rel not in actual or files[rel][0]!=actual[rel].read_bytes() or files[rel][1]!=bool(actual[rel].stat().st_mode & 0o111)]
    if args.check:
        if drift:
            print('\n'.join(drift[:30]))
            print('FAIL generated harness drift; regenerate from source')
            return 1
        print(f'PASS generated Droid tree: {len(files)} files, {len(classes)} original skills, {sum(bool(v) for v in classes.values())} adapter pointers')
        return 0
    stage=OUT.with_name('droid.staging')
    if stage.exists():
        raise RuntimeError('Existing generation staging directory; inspect before replacing')
    for rel,(data,mode) in files.items():
        path=stage/rel
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(data)
        path.chmod(0o755 if mode else 0o644)
    if OUT.exists():
        shutil.rmtree(OUT)
    stage.rename(OUT)
    print(f'Generated {len(files)} files, {len(classes)} original skills; {len(drift)} changed paths')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
