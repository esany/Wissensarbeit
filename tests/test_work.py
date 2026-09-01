import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import work  # noqa: E402


class OperationalCoreTests(unittest.TestCase):
    def test_repository_contract_validates(self):
        self.assertEqual(work.validate(), [])

    def test_requirement_ids_are_unique(self):
        reqs = work.load(work.REQ)["requirements"]
        ids = [r["id"] for r in reqs]
        self.assertEqual(len(ids), len(set(ids)))

    def test_trace_returns_requirement_and_quality_context(self):
        result = work.trace("REQ-001")
        self.assertIsNotNone(result)
        self.assertEqual(result["object"]["id"], "REQ-001")
        self.assertTrue(result["qualities"])
        self.assertTrue(result["criteria"])
        self.assertTrue(result["verification"])

    def test_unknown_trace_is_not_fabricated(self):
        self.assertIsNone(work.trace("REQ-DOES-NOT-EXIST"))

    def test_integration_packet_requires_systemic_disposition(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "packet.json"
            path.write_text(json.dumps({"aspect": "new idea", "disposition": "append"}), encoding="utf-8")
            errors = work.validate_integration_packet(path)
        self.assertTrue(any("invalid disposition" in e for e in errors))
        self.assertTrue(any("missing origin" in e for e in errors))

    def test_valid_integration_packet_passes(self):
        packet = {
            "aspect": "new aspect",
            "origin": "issue-1",
            "affects": {"requirements": ["REQ-003"]},
            "supports": [],
            "conflicts_with": [],
            "disposition": "refine",
            "rationale": "clarifies an existing capability",
            "required_changes": ["clarify requirement"],
            "non_changes": ["governing objective"]
        }
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "packet.json"
            path.write_text(json.dumps(packet), encoding="utf-8")
            errors = work.validate_integration_packet(path)
        self.assertEqual(errors, [])

    def test_building_blocks_are_formalized(self):
        blocks = work.load(work.BUILDING_BLOCKS)["building_blocks"]
        self.assertGreaterEqual(len(blocks), 10)
        for block in blocks:
            for field in ("id", "name", "purpose", "inputs", "outputs", "automation"):
                self.assertTrue(block.get(field), f"{block.get('id')}: missing {field}")

    def test_authority_automates_routine_but_consults_on_material_change(self):
        authority = work.load(work.AUTHORITY)
        autonomous = authority["authorities"]["ai_autonomous_operational"]
        human = authority["authorities"]["human_consultation_required_when_material"]
        self.assertIn("maintain_required_project_operations", autonomous)
        self.assertIn("accept_material_requirement_change", human)
        self.assertTrue(authority["consultation_contract"]["explanation_required"])

    def test_cli_validate(self):
        proc = subprocess.run([sys.executable, str(ROOT / "tools" / "work.py"), "validate"], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("VALIDATION PASS", proc.stdout)


if __name__ == "__main__":
    unittest.main()
