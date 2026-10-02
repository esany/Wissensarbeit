import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class OwnerBurdenAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.authority = json.loads((ROOT / "system" / "authority.json").read_text(encoding="utf-8"))
        self.state = json.loads((ROOT / "project" / "execution_state.json").read_text(encoding="utf-8"))

    def test_routine_route_and_permission_mechanics_are_ai_owned(self):
        autonomous = self.authority["authorities"]["ai_autonomous_operational"]
        self.assertIn("select_routine_execution_route", autonomous)
        self.assertIn("check_capability_and_permission_necessity", autonomous)

        do_not_burden = self.authority["consultation_contract"]["do_not_burden_human_with"]
        self.assertIn("routine execution-route choice", do_not_burden)
        self.assertIn("capability and permission preflight when derivable", do_not_burden)
        self.assertIn("operational permission necessity when derivable", do_not_burden)

    def test_unavoidable_human_action_is_one_concrete_instruction(self):
        orchestration = self.authority["consultation_contract"]["operational_orchestration"]
        action = orchestration["human_action_when_unavoidable"]
        self.assertEqual(action["maximum_unavoidable_actions"], 1)
        self.assertEqual(
            set(action["required_instruction_fields"]),
            {"what_to_do", "why_needed", "exact_option", "what_not_to_decide"},
        )

    def test_core_orchestration_semantics_are_product_neutral(self):
        orchestration = self.authority["consultation_contract"]["operational_orchestration"]
        encoded = json.dumps(orchestration, ensure_ascii=False).lower()
        for product_specific in (
            "normal-chat-first",
            "work-or-codex",
            "chatgpt",
            "chrome",
            "browser",
        ):
            self.assertNotIn(product_specific, encoded)
        self.assertIn("product_neutrality", orchestration)

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
