#!/usr/bin/env python3
"""Fail-closed continuity-boundary checker for recognized material project state."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "system" / "material_state.json"


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate_packet(packet: dict, contract: dict | None = None) -> list[str]:
    contract = contract or load(CONTRACT)
    errors: list[str] = []
    boundary = packet.get("boundary")
    if boundary not in set(contract.get("continuity_boundaries", [])):
        errors.append(f"invalid or missing continuity boundary: {boundary}")

    items = packet.get("items")
    if not isinstance(items, list):
        return errors + ["items must be a list"]

    required = set(contract["externalization"]["required_fields"])
    actions = set(contract["externalization"]["persistent_action_types"])
    dispositions = set(contract["externalization"]["allowed_dispositions"])
    blocking = set(contract["fail_closed"]["blocking_statuses"])

    seen: set[str] = set()
    for index, item in enumerate(items):
        prefix = item.get("id") or f"item[{index}]"
        missing = sorted(required - set(item))
        if missing:
            errors.append(f"{prefix}: missing fields {missing}")
            continue
        if item["id"] in seen:
            errors.append(f"{prefix}: duplicate id")
        seen.add(item["id"])
        if item["disposition"] not in dispositions:
            errors.append(f"{prefix}: invalid disposition {item['disposition']}")

        status = item.get("persistence_status", "unknown")
        action = item.get("persistent_action")
        if not isinstance(action, dict) or action.get("type") not in actions:
            errors.append(f"{prefix}: invalid persistent_action")

        if item.get("materiality") == "material":
            if status in blocking or status != "persisted":
                errors.append(f"{prefix}: material state is not persistently externalized at boundary ({status})")
            if isinstance(action, dict) and action.get("type") != "no_change" and not action.get("ref"):
                errors.append(f"{prefix}: persisted action requires a durable ref")
            if isinstance(action, dict) and action.get("type") == "no_change" and not action.get("reason"):
                errors.append(f"{prefix}: no_change requires a reason")
        elif item.get("materiality") != "non-material":
            errors.append(f"{prefix}: materiality must be material or non-material")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check", help="check a continuity-boundary packet")
    check.add_argument("packet", type=Path)
    args = parser.parse_args()

    if args.command == "check":
        errors = validate_packet(load(args.packet))
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("MATERIAL STATE BOUNDARY PASS")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
