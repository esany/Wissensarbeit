import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import work  # noqa: E402


class ContextFidelityTests(unittest.TestCase):
    SNAPSHOT = "git:fixture"

    def candidates(self):
        return {
            "A": {
                "kind": "alternative",
                "status": "unresolved",
                "authority": "Candidate",
                "readiness": "Identified",
                "resource": "available",
                "priority": None,
                "next_action": "NONE",
                "purpose": None,
                "provenance": ["premise:shared"],
                "human_feedback": {"role": "symptom", "architecture_authority": False},
            },
            "B": {
                "kind": "alternative",
                "status": "unresolved",
                "authority": "Advisory",
                "readiness": "Retrievable",
                "cursor": "p2-context-fidelity-implementation",
                "support_repair": {"returns_to": "p2-context-fidelity-implementation"},
                "provenance": ["premise:shared"],
            },
            "C": {"kind": "irrelevant", "value": 3},
            "D": {"kind": "irrelevant", "value": 4},
            "E": {"kind": "irrelevant", "value": 5},
            "F": {"kind": "irrelevant", "value": 6},
        }

    def request(self):
        return {
            "work_ref": "fixture:P2",
            "question_ref": "fixture:bounded-context",
            "source_snapshot": self.SNAPSHOT,
            "authority_ref": "system/authority.json",
            "selection_basis": {
                "candidate_refs": ["A", "B", "C", "D", "E", "F"],
                "required_refs": ["A", "B"],
                "irrelevant_refs": ["C", "D", "E", "F"],
                "provenance_ref": "fixture:reviewed-judgement",
                "provenance_role": "judgement",
                "rationale": {
                    "A": "material unresolved alternative",
                    "B": "material unresolved alternative and cursor boundary",
                    "C": "not required for this bounded question",
                    "D": "not required for this bounded question",
                    "E": "not required for this bounded question",
                    "F": "not required for this bounded question",
                },
            },
        }

    def compiled(self):
        return work.compile_context(
            self.request(),
            candidates=self.candidates(),
            current_snapshot=self.SNAPSHOT,
        )

    def test_P1_closed_universe_exact_output_is_non_trivial(self):
        execution, provenance = self.compiled()
        self.assertEqual(list(execution), ["A", "B"])
        self.assertEqual(set(execution), {"A", "B"})
        self.assertEqual(
            provenance["selection_basis"]["candidate_refs"],
            ["A", "B", "C", "D", "E", "F"],
        )
        self.assertEqual(
            provenance["selection_basis"]["irrelevant_refs"],
            ["C", "D", "E", "F"],
        )
        self.assertTrue(provenance["fidelity_checks"]["closed_partition"])
        self.assertTrue(provenance["fidelity_checks"]["execution_refs_equal_required_refs"])
        self.assertTrue(provenance["fidelity_checks"]["selected_payloads_unchanged"])
        self.assertNotIn("C", execution)
        self.assertTrue(all("payload" not in item for item in provenance["omitted"]))

    def test_F1_missing_material_unresolved_alternative_fails(self):
        execution, _ = self.compiled()
        execution.pop("B")
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("missing required refs: B" in error for error in errors))

    def test_F2_uncertainty_strengthening_fails(self):
        execution, _ = self.compiled()
        execution["A"]["status"] = "resolved"
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("changed source payload semantics for A" in error for error in errors))

    def test_F3_authority_strengthening_fails(self):
        execution, _ = self.compiled()
        execution["A"]["authority"] = "Authorized"
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("changed source payload semantics for A" in error for error in errors))

    def test_F4_readiness_strengthening_fails(self):
        execution, _ = self.compiled()
        execution["A"]["readiness"] = "Inspected"
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("changed source payload semantics for A" in error for error in errors))

    def test_F5_resource_does_not_become_priority(self):
        execution, _ = self.compiled()
        execution["A"]["priority"] = "next"
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("changed source payload semantics for A" in error for error in errors))

    def test_F6_none_does_not_generate_next_action(self):
        execution, _ = self.compiled()
        execution["A"]["next_action"] = "generated-work"
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("changed source payload semantics for A" in error for error in errors))

    def test_F7_missing_purpose_is_not_substituted(self):
        execution, _ = self.compiled()
        execution["A"]["purpose"] = "richest available context"
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("changed source payload semantics for A" in error for error in errors))

    def test_F8_stale_snapshot_fails_closed(self):
        request = self.request()
        request["source_snapshot"] = "git:stale"
        with self.assertRaisesRegex(ValueError, "source_snapshot is stale"):
            work.compile_context(
                request,
                candidates=self.candidates(),
                current_snapshot=self.SNAPSHOT,
            )

    def test_F9_shared_premise_is_not_laundered_into_independence(self):
        execution, _ = self.compiled()
        execution["A"]["independent_evidence_count"] = 2
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("changed source payload semantics for A" in error for error in errors))

    def test_F10_support_repair_does_not_change_cursor(self):
        execution, _ = self.compiled()
        execution["B"]["support_repair"]["returns_to"] = "new-support-programme"
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("changed source payload semantics for B" in error for error in errors))

    def test_F11_symptom_feedback_does_not_become_architecture_authority(self):
        execution, _ = self.compiled()
        execution["A"]["human_feedback"]["architecture_authority"] = True
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("changed source payload semantics for A" in error for error in errors))

    def test_P2_explicit_none_remains_none(self):
        execution, _ = self.compiled()
        self.assertEqual(execution["A"]["next_action"], "NONE")

    def test_P3_bounded_repair_returns_to_same_cursor(self):
        execution, _ = self.compiled()
        self.assertEqual(
            execution["B"]["support_repair"]["returns_to"],
            execution["B"]["cursor"],
        )

    def test_closed_universe_requires_complete_partition(self):
        request = self.request()
        request["selection_basis"]["irrelevant_refs"].remove("F")
        with self.assertRaisesRegex(ValueError, "completely partition"):
            work.compile_context(
                request,
                candidates=self.candidates(),
                current_snapshot=self.SNAPSHOT,
            )

    def test_over_inclusive_output_fails_exact_R_contract(self):
        execution, _ = self.compiled()
        execution["C"] = copy.deepcopy(self.candidates()["C"])
        errors = work.context_fidelity_errors(
            self.request(), self.candidates(), execution, self.SNAPSHOT
        )
        self.assertTrue(any("contains refs outside R: C" in error for error in errors))

    def test_selection_without_judgement_provenance_fails(self):
        request = self.request()
        request["selection_basis"].pop("provenance_ref")
        with self.assertRaisesRegex(ValueError, "selection basis missing provenance_ref"):
            work.compile_context(
                request,
                candidates=self.candidates(),
                current_snapshot=self.SNAPSHOT,
            )

    def test_cli_bounded_context_separates_execution_payload_and_provenance(self):
        candidate_refs = [
            "governing_objective",
            "requirements",
            "authority",
            "risks",
            "material_state",
            "reconciliation",
        ]
        request = {
            "work_ref": "test:cli-p2-context",
            "question_ref": "test:bounded-cli",
            "source_snapshot": work.repository_snapshot(),
            "authority_ref": "system/authority.json",
            "selection_basis": {
                "candidate_refs": candidate_refs,
                "required_refs": ["governing_objective", "authority"],
                "irrelevant_refs": [
                    "requirements",
                    "risks",
                    "material_state",
                    "reconciliation",
                ],
                "provenance_ref": "test:explicit-selection-judgement",
                "provenance_role": "judgement",
                "rationale": {
                    ref: (
                        "required for this bounded fixture"
                        if ref in {"governing_objective", "authority"}
                        else "explicitly irrelevant to this bounded fixture"
                    )
                    for ref in candidate_refs
                },
            },
        }
        with tempfile.TemporaryDirectory() as td:
            request_path = Path(td) / "request.json"
            provenance_path = Path(td) / "provenance.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools" / "work.py"),
                    "context",
                    "--request",
                    str(request_path),
                    "--provenance-out",
                    str(provenance_path),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            execution = json.loads(proc.stdout)
            provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
        self.assertEqual(set(execution), {"governing_objective", "authority"})
        self.assertEqual(
            set(provenance["selection_basis"]["irrelevant_refs"]),
            {"requirements", "risks", "material_state", "reconciliation"},
        )
        self.assertTrue(all("payload" not in item for item in provenance["omitted"]))
        self.assertNotIn("requirements", execution)
        self.assertNotIn("reconciliation", execution)


if __name__ == "__main__":
    unittest.main()
