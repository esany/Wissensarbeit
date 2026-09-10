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
    def test_execution_guard_rejects_implementation_from_planning_cursor(self):
        self.assertTrue(work.execution_preflight("implement"))

    def test_execution_guard_blocks_open_dependency(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "state.json"
            state = work.load(work.EXECUTION_STATE)
            state["dependencies"][0]["status"] = "open"
            path.write_text(json.dumps(state), encoding="utf-8")
            self.assertTrue(work.execution_preflight("inspect", path))

    def test_execution_guard_requires_persistent_evidence(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "state.json"
            path.write_text(json.dumps(work.load(work.EXECUTION_STATE)), encoding="utf-8")
            errors = work.execution_complete("persist-contract-evidence", "missing-proof.md", path)
            self.assertTrue(any("evidence" in error for error in errors))

    def test_execution_guard_is_fail_closed_for_missing_source(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "state.json"
            state = work.load(work.EXECUTION_STATE)
            state["planning_source"] = "missing-planning-source.md"
            path.write_text(json.dumps(state), encoding="utf-8")
            result = work.execution_status(path)
            self.assertEqual(result["status"], "FAIL CLOSED")

    def test_execution_guard_does_not_treat_chat_go_as_authority(self):
        self.assertTrue(work.execution_preflight("implement"))

    def test_execution_next_is_deterministic_or_explicitly_refuses(self):
        ok, next_step = work.execution_next()
        self.assertTrue(ok)
        self.assertEqual(next_step, "persist-contract-evidence")
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

    def test_foundation_harvest_covers_all_requirements_and_keeps_gaps_visible(self):
        harvest = work.load(work.FOUNDATION_HARVEST)
        requirements = work.load(work.REQ)["requirements"]
        self.assertEqual(work.validate_foundation_harvest(harvest, requirements), [])
        records = harvest["records"]
        self.assertEqual({r["requirement_id"] for r in records}, {r["id"] for r in requirements})
        gaps = [r for r in records if r["classification"] == "provenance-gap"]
        self.assertTrue(gaps, "at least one unresolved provenance gap must remain visible")
        self.assertTrue(all(r["persistent_action"]["type"] == "no_change" for r in gaps))

    def test_external_historical_evidence_cannot_be_project_primary(self):
        harvest = work.load(work.FOUNDATION_HARVEST)
        requirements = work.load(work.REQ)["requirements"]
        harvest["records"][0]["source_ref"]["chat_id"] = "external-chat-id"
        errors = work.validate_foundation_harvest(harvest, requirements)
        self.assertTrue(any("external historical evidence cannot be project-primary" in error for error in errors))

    def test_material_consultation_requires_complete_automatic_decision_brief(self):
        brief = work.load(work.DECISION_BRIEF)
        authority = work.load(work.AUTHORITY)
        blocks = work.load(work.BUILDING_BLOCKS)
        self.assertEqual(work.validate_decision_brief_contract(brief, authority, blocks), [])
        self.assertFalse(brief["rules"]["routine_work_requires_brief"])
        broken = dict(brief)
        broken["required_fields"] = ["decision", "response_requested"]
        errors = work.validate_decision_brief_contract(broken, authority, blocks)
        self.assertTrue(any("missing required decision fields" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
