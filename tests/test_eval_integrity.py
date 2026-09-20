import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import evals  # noqa: E402
import eval_integrity  # noqa: E402


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


    def test_fresh_probe_definitions_are_oracle_free(self):
        self.assertEqual(eval_integrity.validate_probe_definitions(), [])

    def test_rendered_fresh_probe_bundle_contains_only_operational_allowlist(self):
        bundle = eval_integrity.render_probe_bundle("RP-41B7")
        expected = eval_integrity.probe_document()["operational_context_paths"]
        actual = [item["path"] for item in bundle["context_files"]]
        self.assertEqual(actual, expected)
        self.assertTrue(all(not path.startswith(("tests/", "tools/")) for path in actual))
        self.assertEqual(bundle["context_mode"], "isolated-repository-bundle")

    def _fresh_probe_trial(self, **updates):
        probe = eval_integrity.get_probe("RP-41B7")
        bundle = eval_integrity.render_probe_bundle("RP-41B7")
        record = {
            "probe_id": "RP-41B7",
            "probe_identity": eval_integrity.probe_identity(probe),
            "repository_revision": bundle["repository_revision"],
            "context_mode": "isolated-repository-bundle",
            "accessible_context_paths": eval_integrity.probe_document()["operational_context_paths"],
            "context_file_hashes": {
                item["path"]: item["sha256"] for item in bundle["context_files"]
            },
            "bundle_manifest": bundle["bundle_manifest"],
            "bundle_identity": bundle["bundle_identity"],
            "instance_context": {
                "provider_or_product": "test-harness",
                "model_or_configuration": "fresh-instance-fixture",
                "session_or_run_id": "test-run",
                "fresh_context_declaration": "No prior project or trial context supplied beyond the isolated bundle.",
            },
            "fresh_instance": True,
            "external_repository_access": False,
            "prior_trial_access": False,
            "oracle_access": False,
            "raw_response": json.dumps({
                "probe_id": "RP-41B7",
                "selected_action": "route",
                "claims": [],
                "preserved_states": [],
                "authority": [],
                "routing": [],
                "questions": [],
                "notes": [],
            }),
            "response_captured_before_oracle_reveal": True,
        }
        record.update(updates)
        return record

    def test_valid_fresh_probe_capture_contract_passes(self):
        self.assertEqual(eval_integrity.validate_fresh_probe_trial_record(self._fresh_probe_trial()), [])

    def test_fresh_probe_capture_rejects_oracle_access(self):
        errors = eval_integrity.validate_fresh_probe_trial_record(self._fresh_probe_trial(oracle_access=True))
        self.assertTrue(any("oracle_access=false" in error for error in errors))

    def test_fresh_probe_capture_rejects_external_repository_access(self):
        errors = eval_integrity.validate_fresh_probe_trial_record(self._fresh_probe_trial(external_repository_access=True))
        self.assertTrue(any("external_repository_access=false" in error for error in errors))

    def test_fresh_probe_capture_rejects_prior_trial_access(self):
        errors = eval_integrity.validate_fresh_probe_trial_record(self._fresh_probe_trial(prior_trial_access=True))
        self.assertTrue(any("prior_trial_access=false" in error for error in errors))

    def test_fresh_probe_capture_requires_pre_oracle_response_capture(self):
        errors = eval_integrity.validate_fresh_probe_trial_record(
            self._fresh_probe_trial(response_captured_before_oracle_reveal=False)
        )
        self.assertTrue(any("before oracle reveal" in error for error in errors))

    def test_fresh_probe_bundle_is_bound_to_git_revision_content(self):
        bundle = eval_integrity.render_probe_bundle("RP-41B7")
        revision = bundle["repository_revision"]
        for item in bundle["context_files"]:
            expected = eval_integrity._git_text_at_revision(revision, item["path"])
            self.assertEqual(item["content"], expected)
            self.assertEqual(item["sha256"], eval_integrity._sha256_text(expected))

    def test_fresh_probe_capture_rejects_bundle_identity_mismatch(self):
        record = self._fresh_probe_trial()
        record["bundle_identity"] = "sha256:" + ("0" * 64)
        errors = eval_integrity.validate_fresh_probe_trial_record(record)
        self.assertTrue(any("bundle_identity mismatch" in error for error in errors))

    def test_fresh_probe_capture_rejects_bundle_manifest_revision_mismatch(self):
        record = self._fresh_probe_trial()
        record["bundle_manifest"] = dict(record["bundle_manifest"])
        record["bundle_manifest"]["repository_revision"] = "0" * 40
        record["bundle_identity"] = eval_integrity.probe_bundle_identity(record["bundle_manifest"])
        errors = eval_integrity.validate_fresh_probe_trial_record(record)
        self.assertTrue(any("bundle_manifest repository_revision mismatch" in error for error in errors))


    def test_fresh_probe_capture_rejects_context_hash_mismatch(self):
        record = self._fresh_probe_trial()
        record["context_file_hashes"] = dict(record["context_file_hashes"])
        first = next(iter(record["context_file_hashes"]))
        record["context_file_hashes"][first] = "sha256:" + ("0" * 64)
        errors = eval_integrity.validate_fresh_probe_trial_record(record)
        self.assertTrue(any("context_file_hashes mismatch bundle_manifest" in error for error in errors))

    def test_fresh_probe_capture_requires_instance_context(self):
        record = self._fresh_probe_trial()
        del record["instance_context"]
        errors = eval_integrity.validate_fresh_probe_trial_record(record)
        self.assertTrue(any("missing fields" in error and "instance_context" in error for error in errors))

    def test_fresh_probe_capture_requires_nonempty_instance_provenance(self):
        record = self._fresh_probe_trial()
        record["instance_context"] = dict(record["instance_context"])
        record["instance_context"]["session_or_run_id"] = ""
        errors = eval_integrity.validate_fresh_probe_trial_record(record)
        self.assertTrue(any("instance_context fields must be non-empty strings" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
