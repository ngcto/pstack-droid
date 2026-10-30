#!/usr/bin/env python3
"""Verify preservation and stage runnable pstack tools separately."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def verify(root=ROOT):
    manifest = json.loads((root / 'preservation-manifest.json').read_text())
    upstream = root / 'assets/upstream/pstack'
    expected = {entry['path'] for entry in manifest['source_files']}
    actual = {str(p.relative_to(upstream)) for p in upstream.rglob('*') if p.is_file()}
    errors = []
    if actual != expected:
        errors.append(f'Pristine file-set mismatch missing={expected-actual} extra={actual-expected}')
    for entry in manifest['source_files']:
        path = upstream / entry['path']
        if not path.is_file() or sha(path) != entry['sha256']:
            errors.append(f'Pristine hash mismatch: {entry["path"]}')
        active = root / entry['path']
        if entry['path'].startswith('skills/') and not active.is_file():
            errors.append(f'Missing active skill payload: {entry["path"]}')
    skills = list((root / 'skills').glob('*/SKILL.md'))
    names = set()
    for path in skills:
        text = path.read_text()
        parts = text.split('---', 2)
        if len(parts) != 3 or not text.startswith('---\n'):
            errors.append(f'Bad frontmatter: {path}')
            continue
        name = re.search(r'^name: ([a-z0-9-]+)\s*$', parts[1], re.M)
        if not name or name[1] in names or not re.search(r'^description:', parts[1], re.M):
            errors.append(f'Invalid/duplicate skill: {path}')
        else:
            names.add(name[1])
        for link in re.findall(r'\]\(([^)]+)\)', parts[2]):
            if '://' in link or link.startswith('#') or any(c in link for c in '<>{}'):
                continue
            target = link.split('#', 1)[0]
            if target and not (path.parent / target).exists():
                errors.append(f'Broken relative link: {path.relative_to(root)} -> {target}')
    droids = list((root / 'droids').glob('*.md'))
    for path in droids:
        text = path.read_text()
        fm = text.split('---', 2)[1]
        if not re.search(r'^name: [a-z0-9_-]+$', fm, re.M) or not re.search(r'^model: ', fm, re.M):
            errors.append(f'Invalid droid: {path}')
        if 'tools: all' in fm or 'is_background:' in fm:
            errors.append(f'Unsupported droid frontmatter: {path}')
    result = {'status':'FAIL' if errors else 'PASS','revision':manifest['revision'],'preserved_files':len(expected),'skills':len(skills),'droids':len(droids),'errors':errors}
    print(json.dumps(result, indent=2))
    return 1 if errors else 0

def execution_root():
    revision = json.loads((ROOT / 'preservation-manifest.json').read_text())['revision'][:12]
    active_hash = hashlib.sha256()
    for path in sorted((ROOT / 'skills').rglob('*')):
        if path.is_file() and '__pycache__' not in path.parts:
            active_hash.update(str(path.relative_to(ROOT)).encode())
            active_hash.update(path.read_bytes())
    revision += '-' + active_hash.hexdigest()[:12]
    base = Path(os.environ.get('PSTACK_DROID_EXECUTION_ROOT', str(Path.home()/'.local/share/droid-pstack-execution'))) / revision
    if not base.exists():
        base.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(ROOT / 'skills', base / 'skills')
    return base

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['verify','stage','run','doctor'])
    parser.add_argument('path', nargs='?')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    options = parser.parse_args()
    if options.action == 'verify':
        return verify()
    if options.action == 'doctor':
        print(json.dumps({name:shutil.which(name) for name in ['droid','node','bun','java','dot','ffmpeg','ffprobe','agent-browser','tuistory','asciinema','agg','gh','jq']}, indent=2))
        return 0
    base = execution_root()
    if options.action == 'stage':
        print(base)
        return 0
    relative = Path(options.path or '')
    if relative.is_absolute() or '..' in relative.parts or not relative.parts or relative.parts[0] != 'skills':
        parser.error('Use a plugin-relative skills/... script path without ..')
    path = base / relative
    if not path.is_file():
        parser.error(f'No script {relative}')
    ext = path.suffix
    runner = ['bash'] if ext == '.sh' else ['node'] if ext == '.mjs' else ['bun'] if ext == '.ts' else [sys.executable] if ext == '.py' else []
    args = options.args[1:] if options.args[:1] == ['--'] else options.args
    return subprocess.call([*runner,str(path),*args])

if __name__ == '__main__':
    raise SystemExit(main())
