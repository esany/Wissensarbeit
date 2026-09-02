#!/usr/bin/env python3
"""Deterministic completeness gate for systemic reconciliation packets.

The tool does not decide semantic impact. It verifies that a material change has
explicitly considered every required project-state surface and that unresolved
conflicts are not mislabeled as systemically integrated.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "system" / "reconciliation.json"


def load(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_packet(packet: dict, contract: dict | None = None) -> list[str]:
    contract = contract or load(CONTRACT)
    errors: list[str] = []
    for field in ("change_id", "materiality", "summary", "source_refs", "surfaces", "unresolved", "systemically_integrated"):
        if field not in packet:
            errors.append(f"reconciliation packet missing {field}")
    if errors:
        return errors

    if packet["materiality"] not in {"material", "non-material"}:
        errors.append("materiality must be material or non-material")
        return errors

    if packet["materiality"] == "non-material":
        if not packet.get("bypass_rationale"):
            errors.append("non-material reconciliation bypass requires rationale")
        return errors

    required_surfaces = set(contract.get("required_impact_surfaces", []))
    surfaces = packet.get("surfaces", {})
    missing = sorted(required_surfaces - set(surfaces))
    extra = sorted(set(surfaces) - required_surfaces)
    if missing:
        errors.append(f"material reconciliation missing impact surfaces {missing}")
    if extra:
        errors.append(f"unknown reconciliation impact surfaces {extra}")

    allowed = set(contract.get("allowed_dispositions", []))
    blocking = False
    for name in sorted(required_surfaces & set(surfaces)):
        entry = surfaces[name]
        if not isinstance(entry, dict):
            errors.append(f"{name}: surface entry must be an object")
            continue
        disposition = entry.get("disposition")
        if disposition not in allowed:
            errors.append(f"{name}: invalid disposition {disposition}")
        if not entry.get("rationale"):
            errors.append(f"{name}: reconciliation rationale is required")
        if "objects" not in entry or not isinstance(entry.get("objects"), list):
            errors.append(f"{name}: objects list is required (may be empty for unchanged surface)")
        if disposition in {"conflict", "needs-decision"}:
            blocking = True

    unresolved = packet.get("unresolved", [])
    if not isinstance(unresolved, list):
        errors.append("unresolved must be a list")
    else:
        for item in unresolved:
            if not isinstance(item, dict) or not item.get("id") or item.get("status") not in {"conflict", "needs-decision"} or not item.get("reason"):
                errors.append("each unresolved item requires id, conflict|needs-decision status and reason")
            else:
                blocking = True

    if packet.get("systemically_integrated") is True and blocking:
        errors.append("systemically_integrated cannot be true while conflict or needs-decision remains")
    if packet.get("systemically_integrated") is not True and not blocking:
        errors.append("complete non-blocking reconciliation must declare systemically_integrated=true")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate systemic reconciliation completeness")
    parser.add_argument("packet", type=Path)
    args = parser.parse_args()
    errors = validate_packet(load(args.packet))
    if errors:
        print("RECONCILIATION GATE FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("RECONCILIATION GATE PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
