import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import evals  # noqa: E402


class EvalHarnessTests(unittest.TestCase):
    def test_eval_corpus_contract_and_cases_validate(self):
        self.assertEqual(evals.validate(), [])

    def test_every_failure_family_has_case_coverage(self):
        families = {item["id"] for item in evals.load(evals.CORPUS)["families"]}
        covered = {item["family"] for item in evals.load(evals.CASES)["cases"]}
        self.assertEqual(families, covered)

    def test_terse_owner_intent_cases_exist(self):
        cases = evals.load(evals.CASES)["cases"]
        prompts = {item.get("prompt") for item in cases if item.get("type") == "intent_reconstruction"}
        self.assertIn("go", prompts)
        self.assertIn("das ist noch nicht richtig", prompts)

    def test_ok_does_not_imply_material_acceptance(self):
        case = evals.get_case("WA-EVAL-008")
        result = {
            "case_id": "WA-EVAL-008",
            "selected_action": "do-not-promote-material-decision",
            "claims": [],
            "preserved_states": [],
            "authority": ["silence-or-enthusiasm-not-acceptance"],
            "routing": [],
            "questions": [],
            "notes": []
        }
        self.assertEqual(evals.grade(case, result), [])
        result["authority"].append("material-decision-accepted")
        self.assertTrue(any("forbidden token" in error for error in evals.grade(case, result)))

    def test_fresh_context_unresolved_relation_cannot_be_flattened(self):
        case = evals.get_case("WA-EVAL-004")
        bad = {
            "case_id": "WA-EVAL-004",
            "selected_action": "preserve-separation",
            "claims": ["relation-unresolved", "merged-as-same"],
            "preserved_states": ["two-distinct-findings", "unresolved-relation"],
            "authority": [], "routing": [], "questions": [], "notes": []
        }
        self.assertTrue(any("forbidden token" in error for error in evals.grade(case, bad)))

    def test_rendered_eval_does_not_expose_hidden_expectations(self):
        case = evals.get_case("WA-EVAL-006")
        rendered = evals.render(case)
        self.assertIn("go", rendered)
        self.assertNotIn("continue-current-bounded-work", rendered)


if __name__ == "__main__":
    unittest.main()
