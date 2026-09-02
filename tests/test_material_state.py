import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("material_state", ROOT / "tools" / "material_state.py")
material_state = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(material_state)


class MaterialStateTests(unittest.TestCase):
    def setUp(self):
        self.fixture = json.loads((ROOT / "tests" / "fixtures" / "material_state_boundary_pass.json").read_text(encoding="utf-8"))

    def test_persisted_material_state_passes_boundary(self):
        self.assertEqual(material_state.validate_packet(self.fixture), [])

    def test_unpersisted_material_state_fails_closed(self):
        packet = copy.deepcopy(self.fixture)
        packet["boundary"] = "archive"
        packet["items"][0]["persistence_status"] = "unpersisted"
        packet["items"][0]["persistent_action"] = {"type": "issue-comment", "ref": "https://github.com/esany/Wissensarbeit/issues/5"}
        errors = material_state.validate_packet(packet)
        self.assertTrue(any("not persistently externalized" in e for e in errors))

    def test_unknown_persistence_state_fails_closed(self):
        packet = copy.deepcopy(self.fixture)
        packet["items"][0].pop("persistence_status")
        errors = material_state.validate_packet(packet)
        self.assertTrue(any("(unknown)" in e for e in errors))

    def test_persistence_is_not_promotion(self):
        packet = copy.deepcopy(self.fixture)
        packet["items"][0]["disposition"] = "defer"
        packet["items"][0]["persistent_action"] = {
            "type": "issue-comment",
            "ref": "https://github.com/esany/Wissensarbeit/issues/5"
        }
        self.assertEqual(material_state.validate_packet(packet), [])

    def test_persisted_action_requires_durable_reference(self):
        packet = copy.deepcopy(self.fixture)
        packet["items"][0]["persistent_action"] = {"type": "issue-comment"}
        errors = material_state.validate_packet(packet)
        self.assertTrue(any("durable ref" in e for e in errors))

    def test_no_change_is_valid_when_reasoned(self):
        packet = copy.deepcopy(self.fixture)
        packet["items"][0]["disposition"] = "no-change"
        packet["items"][0]["persistent_action"] = {"type": "no_change", "reason": "already represented by canonical requirement and current issue"}
        self.assertEqual(material_state.validate_packet(packet), [])

    def test_cli_boundary_check(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "material_state.py"), "check", str(ROOT / "tests" / "fixtures" / "material_state_boundary_pass.json")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("MATERIAL STATE BOUNDARY PASS", proc.stdout)


if __name__ == "__main__":
    unittest.main()
