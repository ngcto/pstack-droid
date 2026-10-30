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
        self.assertEqual(len(list((ROOT/'droids').glob('*.md'))), 8)

    def test_traversal_rejected(self):
        result = subprocess.run([sys.executable, str(ROOT/'scripts/pstack-droid.py'), 'run', '../bad.py'], capture_output=True)
        self.assertEqual(result.returncode, 2)

    def test_missing_transcript_recency_fails_closed(self):
        text=(ROOT/'skills/poteto-mode/scripts/worktree-audit.sh').read_text()
        self.assertIn('hold-unknown-recency', text)
        self.assertIn('PSTACK_DROID_TRANSCRIPTS_DIR', text)
        self.assertNotIn('$HOME/.cursor/projects/', text)

    def test_native_control_and_authoring_routes(self):
        for name in ('control-cli','control-ui'):
            self.assertIn('`droid-control`', (ROOT/f'skills/{name}/SKILL.md').read_text())
        self.assertIn('`skill-creation`', (ROOT/'skills/create-skill/SKILL.md').read_text())

if __name__ == '__main__':
    unittest.main()
