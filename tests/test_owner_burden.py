import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class OwnerBurdenAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.authority = json.loads((ROOT / "system" / "authority.json").read_text(encoding="utf-8"))
        self.state = json.loads((ROOT / "project" / "execution_state.json").read_text(encoding="utf-8"))
        self.cases = json.loads((ROOT / "tests" / "fixtures" / "owner_burden_cases.json").read_text(encoding="utf-8"))["cases"]
        self.boundary = self.authority["consultation_contract"]["operational_responsibility_boundary"]

    def test_authority_uses_one_compact_responsibility_boundary(self):
        consultation = self.authority["consultation_contract"]
        self.assertIn("operational_responsibility_boundary", consultation)
        self.assertNotIn("operational_orchestration", consultation)
        autonomous = self.authority["authorities"]["ai_autonomous_operational"]
        self.assertNotIn("select_routine_execution_route", autonomous)
        self.assertNotIn("check_capability_and_permission_necessity", autonomous)

    def test_routine_mechanics_stay_ai_owned_without_convenience_escalation(self):
        text = self.boundary.lower()
        self.assertIn("ai carries those routine mechanics", text)
        self.assertIn("checks an already adequate capability before stronger escalation", text)
        self.assertIn("does not escalate for convenience alone", text)

    def test_technical_necessity_does_not_grant_material_authorization(self):
        text = self.boundary.lower()
        self.assertIn("technical necessity does not itself authorize", text)
        self.assertIn("security- or privacy-sensitive permission", text)
        self.assertIn("accept material risk", text)
        self.assertIn("consequential external effects", text)
        self.assertIn("project, semantic, acceptance or priority authority", text)

    def test_human_burden_is_smallest_action_set_not_numeric_cap(self):
        encoded = json.dumps(self.authority, ensure_ascii=False)
        text = self.boundary.lower()
        self.assertNotIn("maximum_unavoidable_actions", encoded)
        self.assertIn("smallest unavoidable human action set", text)
        self.assertIn("prefer one bundled instruction when sufficient", text)
        for field in ("what_to_do", "why_needed", "exact_option", "what_not_to_decide"):
            self.assertIn(field, self.boundary)

    def test_core_authority_is_product_neutral(self):
        encoded = json.dumps(self.authority, ensure_ascii=False).lower()
        for product_specific in (
            "normal-chat-first",
            "work-or-codex",
            "chatgpt",
            "chrome",
            "browser",
        ):
            self.assertNotIn(product_specific, encoded)

    def test_review_required_regression_cases_are_present(self):
        by_id = {case["id"]: case for case in self.cases}
        required = {f"WA-EVAL-{number:03d}" for number in range(31, 37)}
        self.assertTrue(required.issubset(by_id))
        self.assertTrue(all(by_id[cid]["family"] == "FF-EXECUTION-PROGRESS" for cid in required))
        self.assertIn("no-human-route-decision", by_id["WA-EVAL-031"]["expected"])
        self.assertIn("reject-unnecessary-escalation", by_id["WA-EVAL-032"]["expected"])
        self.assertIn("authorization-remains-human-or-specialist", by_id["WA-EVAL-033"]["expected"])
        self.assertIn("both-independent-actions-explicit", by_id["WA-EVAL-034"]["expected"])
        self.assertIn("material-authority-preserved", by_id["WA-EVAL-035"]["expected"])
        self.assertIn("canonical-authority-remains-product-neutral", by_id["WA-EVAL-036"]["expected"])

    def test_correction_cursor_activates_only_issue_80_without_merge_authority(self):
        self.assertEqual(self.state["planning_source"], "github:esany/Wissensarbeit#7")
        self.assertEqual(self.state["focus"], "github:esany/Wissensarbeit#80")
        self.assertEqual(
            self.state["current_step"]["id"],
            "owner-burden-execution-routing-thin-correction",
        )
        self.assertTrue(self.state["implementation_allowed"])
        self.assertIn("implement", self.state["allowed_actions"])
        self.assertNotIn("merge", self.state["allowed_actions"])
        self.assertEqual(self.state["follow_up"]["status"], "active")
        self.assertEqual(self.state["follow_up"]["candidate"], "github:esany/Wissensarbeit#80")
        self.assertEqual(
            self.state["completion_evidence"]["WA-OWNER-BURDEN-PRIORITY-2026-10-02"],
            "https://github.com/esany/Wissensarbeit/issues/7#issuecomment-5959986881",
        )


if __name__ == "__main__":
    unittest.main()
