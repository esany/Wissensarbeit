import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import state_freshness  # noqa: E402


class StateFreshnessTests(unittest.TestCase):
    def test_current_clocks_are_bound(self):
        self.assertEqual(state_freshness.validate_freshness(), [])

    def test_cli_passes(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "state_freshness.py")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("STATE FRESHNESS PASS", proc.stdout)

    def test_stale_execution_next_fails(self):
        with tempfile.TemporaryDirectory() as td:
            current = Path(td) / "CURRENT_STATE.md"
            current.write_text((ROOT / "project" / "CURRENT_STATE.md").read_text(encoding="utf-8").replace(
                "p2-post-pr33-baseline-reconciliation", "p2-fidelity-manifest-preflight"
            ), encoding="utf-8")
            errors = state_freshness.validate_freshness(current_path=current)
            self.assertTrue(any("Execution next" in error for error in errors))

    def test_stale_reconciliation_change_fails(self):
        with tempfile.TemporaryDirectory() as td:
            reconciliation = Path(td) / "reconciliation.json"
            packet = json.loads((ROOT / "project" / "reconciliation.json").read_text(encoding="utf-8"))
            packet["change_id"] = "newer-transition"
            reconciliation.write_text(json.dumps(packet), encoding="utf-8")
            errors = state_freshness.validate_freshness(reconciliation_path=reconciliation)
            self.assertTrue(any("Reconciliation change" in error for error in errors))

    def test_missing_planning_cursor_disposition_fails(self):
        with tempfile.TemporaryDirectory() as td:
            reconciliation = Path(td) / "reconciliation.json"
            packet = json.loads((ROOT / "project" / "reconciliation.json").read_text(encoding="utf-8"))
            packet["surfaces"].pop("planning_execution_cursor")
            reconciliation.write_text(json.dumps(packet), encoding="utf-8")
            errors = state_freshness.validate_freshness(reconciliation_path=reconciliation)
            self.assertTrue(any("planning_execution_cursor" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
