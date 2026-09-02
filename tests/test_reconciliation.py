import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("reconcile", ROOT / "tools" / "reconcile.py")
reconcile = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(reconcile)


class ReconciliationGateTests(unittest.TestCase):
    def test_current_reconciliation_packet_passes(self):
        packet = reconcile.load(ROOT / "project" / "reconciliation.json")
        self.assertEqual(reconcile.validate_packet(packet), [])

    def test_material_change_requires_every_project_state_surface(self):
        packet = reconcile.load(ROOT / "project" / "reconciliation.json")
        packet["surfaces"].pop("risks")
        errors = reconcile.validate_packet(packet)
        self.assertTrue(any("missing impact surfaces" in error for error in errors))

    def test_unchanged_is_valid_when_explicitly_reasoned(self):
        packet = reconcile.load(ROOT / "project" / "reconciliation.json")
        packet["surfaces"]["risks"] = {
            "disposition": "unchanged",
            "objects": [],
            "rationale": "Reviewed and not materially affected by this change."
        }
        self.assertEqual(reconcile.validate_packet(packet), [])

    def test_unresolved_conflict_cannot_claim_systemic_integration(self):
        packet = reconcile.load(ROOT / "project" / "reconciliation.json")
        packet["unresolved"] = [{"id": "x", "status": "conflict", "reason": "material contradiction"}]
        errors = reconcile.validate_packet(packet)
        self.assertTrue(any("cannot be true" in error for error in errors))

    def test_historical_prs_would_fail_the_new_gate(self):
        cases = json.loads((ROOT / "tests" / "fixtures" / "reconciliation_historical_regressions.json").read_text(encoding="utf-8"))["cases"]
        self.assertEqual({case["id"] for case in cases}, {"PR-3", "PR-8", "PR-10", "PR-12"})
        for case in cases:
            with self.subTest(case=case["id"]):
                errors = reconcile.validate_packet(case["packet"])
                self.assertTrue(errors, f"{case['id']} should expose incomplete whole-system reconciliation")
                self.assertTrue(any("missing impact surfaces" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
