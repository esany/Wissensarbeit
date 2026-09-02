import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots" / "arnshaugk-u2-moxa" / "acceptance-scenarios.json"


class ArnshaugkPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.blocks = json.loads(
            (ROOT / "system" / "building_blocks.json").read_text(encoding="utf-8")
        )["building_blocks"]
        cls.authority = json.loads(
            (ROOT / "system" / "authority.json").read_text(encoding="utf-8")
        )

    def test_pilot_keeps_source_repository_read_only(self):
        self.assertEqual(self.fixture["source_mode"], "read-only")
        self.assertEqual(
            self.fixture["source_repository"], "esany/pflege-arnshaugk-historie"
        )

    def test_pilot_maps_every_existing_block_once_without_new_block(self):
        canonical_ids = [block["id"] for block in self.blocks]
        mapped_ids = self.fixture["building_block_refs"]
        self.assertEqual(len(mapped_ids), len(set(mapped_ids)))
        self.assertEqual(set(mapped_ids), set(canonical_ids))
        self.assertEqual(len(canonical_ids), 14)

    def test_slice_keeps_all_required_value_chain_stages_visible(self):
        required = {
            "goal_pain",
            "domain_method",
            "requirement",
            "decision",
            "delivery_verification",
            "owner_feedback",
        }
        self.assertEqual(set(self.fixture["slice_stages"]), required)

    def test_scenarios_use_declared_authority_classes(self):
        declared = {rule["id"] for rule in self.authority["rule_classes"]}
        self.assertEqual(set(self.fixture["authority_classes"]), declared)
        for scenario in self.fixture["scenarios"]:
            self.assertIn(scenario["review_class"], declared)

    def test_missing_owner_acceptance_remains_an_explicit_gap(self):
        self.assertIn(
            "slice_specific_owner_acceptance_missing",
            self.fixture["observed_gaps"],
        )
        scenario = next(
            item
            for item in self.fixture["scenarios"]
            if item["id"] == "REG-ARN-005"
        )
        self.assertEqual(scenario["expected"], "owner_acceptance_open")

    def test_pilot_does_not_claim_a_new_framework_layer(self):
        scenario = next(
            item
            for item in self.fixture["scenarios"]
            if item["id"] == "ACC-ARN-002"
        )
        self.assertEqual(scenario["expected"], "fourteen_existing_blocks_only")


if __name__ == "__main__":
    unittest.main()
