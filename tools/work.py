#!/usr/bin/env python3
"""Minimal, dependency-free operational core for Wissensarbeit v0.1."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "project" / "requirements.json"
QUALITY = ROOT / "project" / "quality.json"
LIFECYCLE = ROOT / "system" / "lifecycle.json"
AUTHORITY = ROOT / "system" / "authority.json"
COMPETENCE = ROOT / "system" / "competence.json"
OBJECTIVE = ROOT / "project" / "GOVERNING_OBJECTIVE.md"
CURRENT = ROOT / "project" / "CURRENT_STATE.md"

REQUIRED_FILES = [REQ, QUALITY, LIFECYCLE, AUTHORITY, COMPETENCE, OBJECTIVE]


def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def validate() -> list[str]:
    errors: list[str] = []
    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing required file: {rel(path)}")
    if errors:
        return errors

    try:
        reqs = load(REQ).get("requirements", [])
        qualities = load(QUALITY).get("qualities", [])
        lifecycle = load(LIFECYCLE)
        authority = load(AUTHORITY)
        competence = load(COMPETENCE)
    except (json.JSONDecodeError, OSError) as exc:
        return [f"cannot load contract data: {exc}"]

    req_ids = [r.get("id") for r in reqs]
    if None in req_ids or len(req_ids) != len(set(req_ids)):
        errors.append("requirement IDs must be present and unique")
    q_ids = [q.get("id") for q in qualities]
    if None in q_ids or len(q_ids) != len(set(q_ids)):
        errors.append("quality IDs must be present and unique")
    known_q = set(q_ids)

    for r in reqs:
        rid = r.get("id", "<unknown>")
        for field in ("statement", "criticality", "origin", "verification"):
            if not r.get(field):
                errors.append(f"{rid}: missing {field}")
        unknown = set(r.get("quality", [])) - known_q
        if unknown:
            errors.append(f"{rid}: unknown quality refs {sorted(unknown)}")

    stages = lifecycle.get("stages", [])
    transitions = lifecycle.get("allowed_transitions", {})
    if set(stages) != set(transitions):
        errors.append("lifecycle stages and transition keys differ")
    for source, targets in transitions.items():
        for target in targets:
            if target not in stages:
                errors.append(f"invalid lifecycle transition {source} -> {target}")

    dispositions = set(lifecycle.get("integration_dispositions", []))
    expected = {"fuse", "refine", "reframe", "supersede", "conflict", "reject", "defer"}
    if not expected.issubset(dispositions):
        errors.append("integration disposition contract is incomplete")

    if not authority.get("rule_classes") or not authority.get("authorities"):
        errors.append("authority contract is incomplete")
    if not competence.get("competence_domains") or not competence.get("material_review_questions"):
        errors.append("competence contract is incomplete")
    return errors


def inspect_state() -> dict:
    reqs = load(REQ)["requirements"]
    qualities = load(QUALITY)["qualities"]
    return {
        "objective": rel(OBJECTIVE),
        "requirements": len(reqs),
        "must_requirements": sum(r.get("criticality") == "must" for r in reqs),
        "quality_dimensions": len(qualities),
        "lifecycle_stages": load(LIFECYCLE)["stages"],
        "integration_dispositions": load(LIFECYCLE)["integration_dispositions"],
        "competence_domains": list(load(COMPETENCE)["competence_domains"]),
        "canonical_sources": [rel(p) for p in REQUIRED_FILES],
    }


def context() -> dict:
    return {
        "governing_objective": OBJECTIVE.read_text(encoding="utf-8"),
        "requirements": load(REQ)["requirements"],
        "quality_model": load(QUALITY)["qualities"],
        "lifecycle": load(LIFECYCLE),
        "authority": load(AUTHORITY),
        "competence": load(COMPETENCE),
        "instruction": "Treat this compiled repository state as authoritative over chat memory. Produce candidates; do not silently promote judgement-heavy changes.",
    }


def trace(object_id: str) -> dict | None:
    reqs = load(REQ)["requirements"]
    for r in reqs:
        if r.get("id") == object_id:
            qmap = {q["id"]: q for q in load(QUALITY)["qualities"]}
            return {
                "object": r,
                "qualities": [qmap[q] for q in r.get("quality", []) if q in qmap],
                "origin": r.get("origin"),
                "verification": r.get("verification", []),
                "note": "v0.1 traces baseline requirements; decisions, implementation and test refs are extended as they materialize.",
            }
    return None


def validate_integration_packet(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        packet = load(path)
    except Exception as exc:
        return [f"cannot load integration packet: {exc}"]
    required = ["aspect", "origin", "affects", "supports", "conflicts_with", "disposition", "rationale", "required_changes", "non_changes"]
    for field in required:
        if field not in packet:
            errors.append(f"integration packet missing {field}")
    allowed = set(load(LIFECYCLE)["integration_dispositions"])
    if packet.get("disposition") not in allowed:
        errors.append(f"invalid disposition: {packet.get('disposition')}")
    affects = packet.get("affects")
    if affects is not None and not isinstance(affects, dict):
        errors.append("affects must be an object keyed by impacted system dimensions")
    return errors


def audit() -> list[str]:
    findings = validate()
    reqs = load(REQ)["requirements"] if REQ.exists() else []
    for r in reqs:
        if r.get("criticality") == "must" and not r.get("verification"):
            findings.append(f"{r.get('id')}: critical requirement without verification")
        if r.get("origin") == "chat-only":
            findings.append(f"{r.get('id')}: accepted requirement has chat-only origin")
    return findings


def derive() -> str:
    state = inspect_state()
    errors = validate()
    lines = [
        "# Current State",
        "",
        "> Generated by `python tools/work.py derive`. Do not maintain parallel truth here.",
        "",
        "## Baseline",
        f"- Requirements: {state['requirements']} ({state['must_requirements']} must)",
        f"- Quality dimensions: {state['quality_dimensions']}",
        f"- Validation: {'PASS' if not errors else 'FAIL'}",
        "",
        "## Lifecycle",
        "`" + " -> ".join(state["lifecycle_stages"]) + "`",
        "",
        "## Competence domains",
        ", ".join(state["competence_domains"]),
        "",
        "## Canonical sources",
        *[f"- `{p}`" for p in state["canonical_sources"]],
        "",
        "## Next operational proof",
        "Run one real Issue -> candidate -> requirement/criterion -> implementation -> verification -> PR -> merge -> derive/restart cycle and record failures as regressions.",
    ]
    text = "\n".join(lines) + "\n"
    CURRENT.write_text(text, encoding="utf-8")
    return text


def main() -> int:
    parser = argparse.ArgumentParser(prog="work", description="Wissensarbeit operational core")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    sub.add_parser("inspect")
    sub.add_parser("context")
    trace_p = sub.add_parser("trace")
    trace_p.add_argument("object_id")
    int_p = sub.add_parser("integrate")
    int_p.add_argument("packet", type=Path)
    sub.add_parser("derive")
    sub.add_parser("audit")
    args = parser.parse_args()

    if args.command == "validate":
        errors = validate()
        if errors:
            print("VALIDATION FAILED")
            print("\n".join(f"- {e}" for e in errors))
            return 1
        print("VALIDATION PASS")
    elif args.command == "inspect":
        print(json.dumps(inspect_state(), indent=2, ensure_ascii=False))
    elif args.command == "context":
        print(json.dumps(context(), indent=2, ensure_ascii=False))
    elif args.command == "trace":
        result = trace(args.object_id)
        if result is None:
            print(f"unknown object: {args.object_id}", file=sys.stderr)
            return 2
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif args.command == "integrate":
        errors = validate_integration_packet(args.packet)
        if errors:
            print("INTEGRATION PACKET INVALID")
            print("\n".join(f"- {e}" for e in errors))
            return 1
        print("INTEGRATION PACKET VALID")
    elif args.command == "derive":
        print(derive(), end="")
    elif args.command == "audit":
        findings = audit()
        if findings:
            print("AUDIT FINDINGS")
            print("\n".join(f"- {e}" for e in findings))
            return 1
        print("AUDIT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
