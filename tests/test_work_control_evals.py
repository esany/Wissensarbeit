"""Issue #25: synthetic token regressions, not empirical model evidence.

Existing grader semantics apply: unknown synonyms still need review. Passing
these tests proves neither domain truth nor Owner acceptance; no promotion of
requirements, architecture, authority, Building Blocks or failure families.
"""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import evals  # noqa: E402


class WorkControlEvalTests(unittest.TestCase):
    def setUp(self):
        self.responses = evals.load(
            ROOT / "tests/fixtures/work_control_responses.json"
        )["responses"]

    def test_seven_source_scoped_cases_render_without_expectations(self):
        self.assertEqual(set(self.responses), {f"WA-EVAL-{n:03d}" for n in range(24, 31)})
        for cid in self.responses:
            with self.subTest(case=cid):
                case = evals.get_case(cid)
                self.assertIn("esany/Wissensarbeit#25", case["source_refs"])
                rendered = evals.render(case)
                self.assertIn(case["context"], rendered)
                self.assertIn(case["prompt"], rendered)
                self.assertIn("esany/Wissensarbeit", rendered)
                for tokens in case["expect"].values():
                    for token in tokens:
                        self.assertNotIn(token, rendered)

    def test_synthetic_responses_pass_existing_grader_and_identity_guard(self):
        for cid, result in self.responses.items():
            with self.subTest(case=cid):
                case = evals.get_case(cid)
                self.assertEqual(evals.grade(case, result), [])
                record = dict(case_id=cid, fixture_identity=evals.fixture_identity(case),
                              raw_response=json.dumps(result))
                self.assertEqual(evals.validate_trial_record(record), [])
                wrong = copy.deepcopy(case)
                wrong["context"] += " Different source scope."
                record["fixture_identity"] = evals.fixture_identity(wrong)
                self.assertTrue(any("fixture_identity mismatch" in error
                                    for error in evals.validate_trial_record(record)))

    def test_each_missing_boundary_is_rejected(self):
        for cid, sample in self.responses.items():
            for field in ("claims", "authority"):
                for token in sample[field]:
                    with self.subTest(case=cid, missing=token):
                        result = copy.deepcopy(sample)
                        result[field].remove(token)
                        self.assertTrue(any(f"missing expected meaning {token}" in error
                                            for error in evals.grade(evals.get_case(cid), result)))

    def test_scope_creep_is_rejected_even_with_all_positive_claims(self):
        for cid, sample in self.responses.items():
            case = evals.get_case(cid)
            for token in case["expect"]["forbidden_anywhere"]:
                for field in ("selected_action", *evals.SEMANTIC_FIELDS):
                    with self.subTest(case=cid, forbidden=token, field=field):
                        result = copy.deepcopy(sample)
                        current = result[field]
                        result[field] = ([current] if isinstance(current, str) else current) + [token]
                        self.assertIn(f"forbidden meaning present: {token}", evals.grade(case, result))

    def test_wrong_action_cannot_be_rescued_by_correct_notes(self):
        for cid, sample in self.responses.items():
            with self.subTest(case=cid):
                result = copy.deepcopy(sample)
                result["notes"] = [result["selected_action"]]
                result["selected_action"] = "unscoped-continuation"
                self.assertTrue(any(error.startswith("selected_action:")
                                    for error in evals.grade(evals.get_case(cid), result)))


if __name__ == "__main__":
    unittest.main()
