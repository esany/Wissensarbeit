import copy
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCT_SPECIFIC_CORE_TOKENS = (
    "normal-chat-first",
    "work-or-codex",
    "chatgpt",
    "chrome",
    "browser",
)


def contract_policy(authority: dict) -> dict[str, bool]:
    consultation = authority["consultation_contract"]
    boundary = consultation.get("operational_responsibility_boundary", "")
    text = boundary.lower()
    encoded = json.dumps(authority, ensure_ascii=False).lower()
    return {
        "routine_ai_owned": "ai carries those routine mechanics" in text,
        "adequate_before_stronger": "checks an already adequate capability before stronger escalation" in text,
        "no_convenience_escalation": "does not escalate for convenience alone" in text,
        "technical_necessity_identified": "technical permission necessity" in text,
        "necessity_not_authorization": all(
            phrase in text
            for phrase in (
                "technical necessity does not itself authorize",
                "security- or privacy-sensitive permission",
                "accept material risk",
                "consequential external effects",
            )
        ),
        "material_authority_preserved": "transfer project, semantic, acceptance or priority authority" in text,
        "smallest_action_set": "smallest unavoidable human action set" in text,
        "bundle_only_when_sufficient": "prefer one bundled instruction when sufficient" in text,
        "per_action_fields": all(
            field in boundary
            for field in ("what_to_do", "why_needed", "exact_option", "what_not_to_decide")
        ),
        "product_neutral_core": not any(token in encoded for token in PRODUCT_SPECIFIC_CORE_TOKENS),
    }


def evaluate_owner_burden_case(authority: dict, case: dict) -> set[str]:
    """Evaluate one structured fixture against the canonical responsibility contract.

    This is deliberately a bounded deterministic contract evaluator. It does not
    model product UI/runtime behavior and it does not implement #48 or #55.
    """
    policy = contract_policy(authority)
    facts = case["facts"]
    outcomes: set[str] = set()

    if facts.get("routine_action") and facts.get("adequate_capability_available"):
        if policy["routine_ai_owned"] and policy["adequate_before_stronger"]:
            outcomes.update({"ai-selects-existing-adequate-capability", "no-human-route-decision"})
        else:
            outcomes.add("ask-human-to-choose-route")

    if (
        facts.get("stronger_capability_available")
        and not facts.get("stronger_capability_required", False)
        and facts.get("adequate_capability_available")
    ):
        if policy["adequate_before_stronger"] and policy["no_convenience_escalation"]:
            outcomes.update({"reject-unnecessary-escalation", "retain-adequate-capability"})
        else:
            outcomes.add("stronger-route-by-convenience")

    if facts.get("permission_technically_necessary"):
        if policy["technical_necessity_identified"]:
            outcomes.add("technical-necessity-identified")
        if facts.get("security_privacy_or_material_risk"):
            if policy["necessity_not_authorization"]:
                outcomes.add("authorization-remains-human-or-specialist")
            else:
                outcomes.update({"necessity-implies-authorization", "ai-accepts-material-risk"})

    independent_actions = int(facts.get("independent_unavoidable_human_actions", 0))
    if independent_actions:
        if (
            policy["smallest_action_set"]
            and policy["bundle_only_when_sufficient"]
            and policy["per_action_fields"]
            and (independent_actions == 1 or not facts.get("can_bundle_safely", True))
        ):
            outcomes.add("smallest-unavoidable-action-set")
            if independent_actions > 1 and not facts.get("can_bundle_safely", True):
                outcomes.add("both-independent-actions-explicit")
        else:
            outcomes.add("hide-second-action-to-meet-numeric-cap")

    if facts.get("routine_route_selected"):
        if policy["routine_ai_owned"]:
            outcomes.add("route-selected-operationally")
        if facts.get("material_decisions_unresolved"):
            if policy["material_authority_preserved"]:
                outcomes.add("material-authority-preserved")
            else:
                outcomes.update({"route-confers-project-authority", "route-confers-acceptance"})

    if facts.get("product_specific_incident"):
        if facts.get("incident_recorded_as_evidence"):
            outcomes.add("incident-retained-as-evidence")
        if policy["product_neutral_core"]:
            outcomes.add("canonical-authority-remains-product-neutral")
        else:
            outcomes.update({"product-route-name-promoted-to-core", "ui-prompt-promoted-to-generic-authority"})

    if not policy["no_convenience_escalation"] and facts.get("routine_action"):
        outcomes.add("escalate-for-convenience")

    return outcomes


class OwnerBurdenAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.authority = json.loads((ROOT / "system" / "authority.json").read_text(encoding="utf-8"))
        self.state = json.loads((ROOT / "project" / "execution_state.json").read_text(encoding="utf-8"))
        self.cases = json.loads((ROOT / "tests" / "fixtures" / "owner_burden_cases.json").read_text(encoding="utf-8"))["cases"]
        self.boundary = self.authority["consultation_contract"]["operational_responsibility_boundary"]

    def case(self, case_id: str) -> dict:
        return next(case for case in self.cases if case["id"] == case_id)

    def assert_case_passes(self, authority: dict, case: dict) -> None:
        actual = evaluate_owner_burden_case(authority, case)
        expected = set(case["expected"])
        forbidden = set(case["forbidden"])
        self.assertTrue(expected.issubset(actual), f"{case['id']} missing {sorted(expected - actual)} from {sorted(actual)}")
        self.assertTrue(forbidden.isdisjoint(actual), f"{case['id']} produced forbidden {sorted(forbidden & actual)}")

    def test_authority_uses_one_compact_responsibility_boundary(self):
        consultation = self.authority["consultation_contract"]
        self.assertIn("operational_responsibility_boundary", consultation)
        self.assertNotIn("operational_orchestration", consultation)
        autonomous = self.authority["authorities"]["ai_autonomous_operational"]
        self.assertNotIn("select_routine_execution_route", autonomous)
        self.assertNotIn("check_capability_and_permission_necessity", autonomous)

    def test_review_required_regression_cases_are_executed(self):
        by_id = {case["id"]: case for case in self.cases}
        required = {f"WA-EVAL-{number:03d}" for number in range(31, 37)}
        self.assertEqual(required, set(by_id))
        for case_id in sorted(required):
            case = by_id[case_id]
            self.assertEqual(case["family"], "FF-EXECUTION-PROGRESS")
            self.assertTrue(case.get("facts"), f"{case_id} needs structured scenario facts")
            self.assertTrue(case.get("expected"), f"{case_id} needs expected outcomes")
            self.assertTrue(case.get("forbidden"), f"{case_id} needs forbidden outcomes")
            self.assert_case_passes(self.authority, case)

    def test_negative_mutations_are_detected_by_fixture_forbidden_outcomes(self):
        mutations = [
            (
                "WA-EVAL-031",
                "checks an already adequate capability before stronger escalation",
                "may ask the Human to choose an execution route",
            ),
            (
                "WA-EVAL-032",
                "does not escalate for convenience alone",
                "may escalate for convenience alone",
            ),
            (
                "WA-EVAL-033",
                "Technical necessity does not itself authorize",
                "Technical necessity itself authorizes",
            ),
            (
                "WA-EVAL-034",
                "smallest unavoidable Human action set",
                "single Human action",
            ),
            (
                "WA-EVAL-035",
                "transfer project, semantic, acceptance or priority authority",
                "preserve project execution only",
            ),
        ]
        for case_id, old, new in mutations:
            mutated = copy.deepcopy(self.authority)
            boundary = mutated["consultation_contract"]["operational_responsibility_boundary"]
            self.assertIn(old, boundary, f"mutation precondition missing for {case_id}")
            mutated["consultation_contract"]["operational_responsibility_boundary"] = boundary.replace(old, new)
            actual = evaluate_owner_burden_case(mutated, self.case(case_id))
            expected = set(self.case(case_id)["expected"])
            forbidden = set(self.case(case_id)["forbidden"])
            self.assertTrue(
                bool(expected - actual) or bool(forbidden & actual),
                f"{case_id} mutation was not detected: {sorted(actual)}",
            )

        product_mutation = copy.deepcopy(self.authority)
        product_mutation["consultation_contract"]["product_route"] = "chrome"
        actual = evaluate_owner_burden_case(product_mutation, self.case("WA-EVAL-036"))
        self.assertTrue(set(self.case("WA-EVAL-036")["forbidden"]) & actual)

    def test_all_fixture_forbidden_outcomes_are_consumed(self):
        declared = {token for case in self.cases for token in case["forbidden"]}
        produced_by_negative_probes = set()

        probes = []
        for case_id, old, new in (
            ("WA-EVAL-031", "checks an already adequate capability before stronger escalation", "may ask the Human to choose an execution route"),
            ("WA-EVAL-031", "does not escalate for convenience alone", "may escalate for convenience alone"),
            ("WA-EVAL-032", "does not escalate for convenience alone", "may escalate for convenience alone"),
            ("WA-EVAL-033", "Technical necessity does not itself authorize", "Technical necessity itself authorizes"),
            ("WA-EVAL-034", "smallest unavoidable Human action set", "single Human action"),
            ("WA-EVAL-035", "transfer project, semantic, acceptance or priority authority", "preserve project execution only"),
        ):
            mutated = copy.deepcopy(self.authority)
            boundary = mutated["consultation_contract"]["operational_responsibility_boundary"]
            mutated["consultation_contract"]["operational_responsibility_boundary"] = boundary.replace(old, new)
            probes.append((mutated, self.case(case_id)))

        product_mutation = copy.deepcopy(self.authority)
        product_mutation["consultation_contract"]["product_route"] = "chrome"
        probes.append((product_mutation, self.case("WA-EVAL-036")))

        for authority, case in probes:
            produced_by_negative_probes.update(evaluate_owner_burden_case(authority, case) & set(case["forbidden"]))

        self.assertEqual(declared, produced_by_negative_probes)

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
