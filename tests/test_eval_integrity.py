import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import evals  # noqa: E402


class EvalTrialIntegrityTests(unittest.TestCase):
    def record(self, case_id, identity_case_id=None, result_case_id=None):
        case = evals.get_case(case_id)
        fixture_case = evals.get_case(identity_case_id or case_id)
        return {
            "case_id": case_id,
            "fixture_identity": evals.fixture_identity(fixture_case),
            "raw_response": json.dumps({"case_id": result_case_id or case_id}),
        }

    def test_matching_case_and_fixture_identity_validate(self):
        self.assertEqual(evals.validate_trial_record(self.record("WA-EVAL-019")), [])

    def test_fixture_identity_from_another_case_fails(self):
        errors = evals.validate_trial_record(self.record("WA-EVAL-019", "WA-EVAL-020"))
        self.assertTrue(any("fixture_identity mismatch" in error for error in errors))

    def test_wrong_result_case_id_fails(self):
        errors = evals.validate_trial_record(self.record("WA-EVAL-019", result_case_id="WA-EVAL-020"))
        self.assertTrue(any("result case_id mismatch" in error for error in errors))

    def test_canonical_fixture_mutation_invalidates_identity(self):
        case = evals.get_case("WA-EVAL-019")
        recorded = evals.fixture_identity(case)
        for field in ("prompt", "context", "expect"):
            changed = dict(case)
            if field == "expect":
                changed[field] = {**case[field], "notes": ["changed"]}
            else:
                changed[field] = f"{case.get(field, '')} changed"
            self.assertNotEqual(recorded, evals.fixture_identity(changed), field)

    def test_valid_input_retains_existing_grading_behavior(self):
        case = evals.get_case("WA-EVAL-006")
        result = {field: case["expect"].get(field, []) for field in (
            "selected_action", "claims", "preserved_states", "authority", "routing", "questions", "notes"
        )}
        result["case_id"] = case["id"]
        self.assertEqual(evals.grade(case, result), [])

    def test_round2_metadata_remains_readable(self):
        plan = evals.load(ROOT / "tests" / "evals" / "round2.json")
        for run in plan["runs"]:
            self.assertIsNotNone(evals.get_case(run["case_id"]))

    def test_missing_fixture_identity_fails_closed(self):
        record = self.record("WA-EVAL-019")
        del record["fixture_identity"]
        self.assertIn("trial missing fixture_identity", evals.validate_trial_record(record))


if __name__ == "__main__":
    unittest.main()
