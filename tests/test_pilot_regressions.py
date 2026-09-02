import json
import unittest
from pathlib import Path

from tools.pilot_regressions import evaluate


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots" / "generic-pilot-learnings" / "regression-scenarios.json"


class PilotRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenarios = json.loads(FIXTURE.read_text(encoding="utf-8"))["scenarios"]

    def test_six_unique_generic_regressions_are_executable(self):
        self.assertEqual(len(self.scenarios), 6)
        self.assertEqual(len({item["id"] for item in self.scenarios}), 6)
        for scenario in self.scenarios:
            with self.subTest(scenario=scenario["id"]):
                self.assertEqual(evaluate(scenario), scenario["expected"])

    def test_scenarios_are_domain_neutral(self):
        serialized = json.dumps(self.scenarios).lower()
        for forbidden in ("moxa", "arnshaugk", "knaus", "bernico", "dendro"):
            self.assertNotIn(forbidden, serialized)

    def test_negative_inputs_fail_closed(self):
        negative = {
            "mechanism": "conversation_harvesting",
            "input": {"material_items": [{"persisted_ref": "", "chat_only": True}]},
        }
        self.assertEqual(evaluate(negative), "material_state_only_in_chat")


if __name__ == "__main__":
    unittest.main()
