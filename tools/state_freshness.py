#!/usr/bin/env python3
"""Cross-clock freshness gate for current reconciliation and execution state.

This is deliberately not a new state store. It checks that the existing
reconciliation packet, execution cursor and derived CURRENT_STATE view describe
one reconstructable current transition.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECONCILIATION = ROOT / "project" / "reconciliation.json"
EXECUTION_STATE = ROOT / "project" / "execution_state.json"
CURRENT_STATE = ROOT / "project" / "CURRENT_STATE.md"


def load(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def ready_next(state: dict) -> str:
    ready = [item.get("id") for item in state.get("current_step", {}).get("next", []) if item.get("status") == "ready"]
    if len(ready) == 1:
        return ready[0]
    if not ready:
        return "none"
    return "ambiguous"


def _extract(text: str, label: str) -> str | None:
    match = re.search(rf"^- {re.escape(label)}: `([^`]+)`$", text, re.MULTILINE)
    return match.group(1) if match else None


def validate_freshness(
    reconciliation_path: Path = RECONCILIATION,
    execution_path: Path = EXECUTION_STATE,
    current_path: Path = CURRENT_STATE,
) -> list[str]:
    errors: list[str] = []
    try:
        reconciliation = load(reconciliation_path)
        execution = load(execution_path)
        current = current_path.read_text(encoding="utf-8")
    except Exception as exc:
        return [f"cannot load current-state clocks: {exc}"]

    planning = reconciliation.get("surfaces", {}).get("planning_execution_cursor")
    if not isinstance(planning, dict):
        errors.append("reconciliation is missing planning_execution_cursor disposition")
    else:
        if "project/execution_state.json" not in planning.get("objects", []):
            errors.append("planning_execution_cursor must disposition project/execution_state.json")
        if not planning.get("rationale"):
            errors.append("planning_execution_cursor requires rationale")

    expected = {
        "Reconciliation change": reconciliation.get("change_id"),
        "Execution focus": execution.get("focus"),
        "Execution current step": execution.get("current_step", {}).get("id"),
        "Execution next": ready_next(execution),
        "Implementation allowed": str(bool(execution.get("implementation_allowed"))).lower(),
    }
    for label, value in expected.items():
        actual = _extract(current, label)
        if actual is None:
            errors.append(f"CURRENT_STATE is missing {label}")
        elif actual != value:
            errors.append(f"CURRENT_STATE stale for {label}: {actual!r} != {value!r}")

    if ready_next(execution) == "ambiguous":
        errors.append("execution cursor has multiple ready next actions")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate reconciliation/execution/current-state freshness")
    parser.parse_args()
    errors = validate_freshness()
    if errors:
        print("STATE FRESHNESS FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("STATE FRESHNESS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
