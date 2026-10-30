import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('pstack_droid', ROOT/'scripts/pstack-droid.py')
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

class PortTests(unittest.TestCase):
    def test_complete_preservation(self):
        self.assertEqual(MOD.verify(), 0)

    def test_all_original_skill_names_available(self):
        expected = {p.parent.name for p in (ROOT/'assets/upstream/pstack/skills').glob('*/SKILL.md')}
        actual = {p.parent.name for p in (ROOT/'skills').glob('*/SKILL.md')}
        self.assertTrue(expected <= actual)

    def test_native_plugin_layout(self):
        self.assertTrue((ROOT/'.factory-plugin/plugin.json').is_file())
        self.assertFalse((ROOT/'.cursor-plugin').exists())
        self.assertFalse((ROOT/'agents').exists())
        self.assertEqual({p.stem for p in (ROOT/'droids').glob('*.md')}, {'poteto-agent', 'comment-sicko'})
        for path in (ROOT/'droids').glob('*.md'):
            frontmatter = path.read_text().split('---', 2)[1]
            self.assertIn('model: inherit', frontmatter)
            self.assertNotIn('reasoningEffort:', frontmatter)

    def test_traversal_rejected(self):
        result = subprocess.run([sys.executable, str(ROOT/'scripts/pstack-droid.py'), 'run', '../bad.py'], capture_output=True)
        self.assertEqual(result.returncode, 2)

    def test_missing_transcript_recency_fails_closed(self):
        text=(ROOT/'skills/poteto-mode/scripts/worktree-audit.sh').read_text()
        self.assertIn('hold-unknown-recency', text)
        self.assertIn('PSTACK_DROID_TRANSCRIPTS_DIR', text)
        self.assertNotIn('$HOME/.cursor/projects/', text)

    def test_native_control_and_authoring_routes(self):
        text = (ROOT/'DROID-ADAPTER.md').read_text()
        for name in ('tuistory', 'agent-browser', 'droid-control', 'skill-creation'):
            self.assertIn(name, text)
        self.assertFalse((ROOT/'skills/control-cli').exists())
        self.assertFalse((ROOT/'skills/control-ui').exists())
        self.assertFalse((ROOT/'skills/create-skill').exists())

if __name__ == '__main__':
    unittest.main()
