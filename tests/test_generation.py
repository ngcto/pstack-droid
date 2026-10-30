import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('generator', ROOT/'scripts/generate-pstack-harness-trees.py')
assert SPEC is not None and SPEC.loader is not None
GEN=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GEN)

class GeneratedTreeTests(unittest.TestCase):
    def test_committed_tree_matches_source(self):
        self.assertEqual(subprocess.run([sys.executable,str(ROOT/'scripts/generate-pstack-harness-trees.py'),'--check']).returncode,0)

    def test_full_source_retained_except_native_layout(self):
        files,classes=GEN.render()
        expected={p.relative_to(GEN.SOURCE).as_posix() for p in GEN.walk(GEN.SOURCE) if not p.relative_to(GEN.SOURCE).as_posix().startswith(('agents/','.cursor-plugin/'))}
        self.assertTrue(expected <= set(files))
        self.assertEqual(len(classes),58)

    def test_models_are_inherited_and_only_original_roles(self):
        files,_=GEN.render()
        roles=[p for p in files if p.startswith('droids/')]
        self.assertEqual(set(roles),{'droids/poteto-agent.md','droids/comment-sicko.md'})
        for role in roles:
            frontmatter=files[role][0].decode().split('---',2)[1]
            self.assertIn('model: inherit',frontmatter)
            self.assertNotIn('reasoningEffort:',frontmatter)

    def test_drift_and_extra_files_fail(self):
        path=GEN.OUT/'owned-drift-test.txt'
        self.assertFalse(path.exists())
        try:
            path.write_text('unexpected generated file')
            result=subprocess.run([sys.executable,str(ROOT/'scripts/generate-pstack-harness-trees.py'),'--check'],capture_output=True,text=True)
            self.assertEqual(result.returncode,1)
            self.assertIn(path.name,result.stdout)
        finally:
            path.unlink(missing_ok=True)

    def test_missing_adapter_mapping_fails(self):
        original=GEN.PORT
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            fixture=Path(directory)
            # render resolves PORT only for adapter then source inventory; fail on absent mapping first via an explicit classified key assertion.
            text=(original/'DROID-ADAPTER.md').read_text()
            self.assertIn('AskQuestion',text)
            self.assertNotIn('AskQuestion',text.replace('AskQuestion','REMOVED'))
        # Exercise actual render validation by a narrowly scoped adapter read override.
        from unittest.mock import patch
        actual=Path.read_text
        def read(path,*args,**kwargs):
            value=actual(path,*args,**kwargs)
            if path == GEN.PORT/'DROID-ADAPTER.md':
                return value.replace('AskQuestion','REMOVED')
            return value
        with patch.object(Path,'read_text',read):
            with self.assertRaisesRegex(RuntimeError,'Missing adapter mapping: AskQuestion'):
                GEN.render()

if __name__=='__main__':
    unittest.main()
