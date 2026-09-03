import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import evals  # noqa: E402

ROUND2 = ROOT / "tests" / "evals" / "round2.json"


class EvalRound2Tests(unittest.TestCase):
    def test_round2_matrix_is_bounded_and_resolvable(self):
        plan = json.loads(ROUND2.read_text(encoding="utf-8"))
        runs = plan["runs"]
        self.assertEqual(len(runs), 10)
        case_ids = {case["id"] for case in evals.load(evals.CASES)["cases"]}
        for run in runs:
            self.assertIn(run["case_id"], case_ids)
            self.assertGreaterEqual(run["trials"], 3)

    def test_round2_uses_fresh_independent_trials(self):
        plan = json.loads(ROUND2.read_text(encoding="utf-8"))
        policy = plan["trial_policy"]
        self.assertEqual(policy["independence"], "fresh-instance-per-trial")
        self.assertTrue(policy["same_case_retries_do_not_share_prior_output"])

    def test_failure_classification_is_small_and_evidence_gated(self):
        plan = json.loads(ROUND2.read_text(encoding="utf-8"))
        classification = plan["failure_classification"]
        self.assertEqual(set(classification["classes"]), {"model-behavior", "grader", "system-control-gap"})
        self.assertTrue(classification["no_auto_core_fix"])
        self.assertEqual(
            set(classification["required_evidence"]),
            {"case_id", "trial_id", "deterministic_grade", "semantic_review", "classification", "evidence", "next_action"},
        )

    def test_round2_contains_targeted_perturbation_dimensions(self):
        plan = json.loads(ROUND2.read_text(encoding="utf-8"))
        dimensions = {run["dimension"] for run in plan["runs"]}
        required = {
            "terse_typo",
            "natural_free_text",
            "enthusiastic_ack",
            "green_local_vs_global",
            "long_horizon_scope_growth",
            "compression_pressure",
            "false_completion_pressure",
            "identity_vs_availability",
        }
        self.assertTrue(required.issubset(dimensions))


if __name__ == "__main__":
    unittest.main()
