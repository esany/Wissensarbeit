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
CRITERIA = ROOT / "project" / "criteria.json"
VERIFICATION = ROOT / "project" / "verification.json"
LIFECYCLE = ROOT / "system" / "lifecycle.json"
AUTHORITY = ROOT / "system" / "authority.json"
COMPETENCE = ROOT / "system" / "competence.json"
FITNESS = ROOT / "system" / "architecture_fitness.json"
BUILDING_BLOCKS = ROOT / "system" / "building_blocks.json"
OBJECTIVE = ROOT / "project" / "GOVERNING_OBJECTIVE.md"
CURRENT = ROOT / "project" / "CURRENT_STATE.md"

REQUIRED_FILES = [REQ, QUALITY, CRITERIA, VERIFICATION, LIFECYCLE, AUTHORITY, COMPETENCE, FITNESS, BUILDING_BLOCKS, OBJECTIVE]


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
        criteria = load(CRITERIA).get("criteria", [])
        verification = load(VERIFICATION).get("verification", [])
        lifecycle = load(LIFECYCLE)
        authority = load(AUTHORITY)
        competence = load(COMPETENCE)
        fitness = load(FITNESS)
        building_blocks = load(BUILDING_BLOCKS)
    except (json.JSONDecodeError, OSError) as exc:
        return [f"cannot load contract data: {exc}"]

    req_ids = [r.get("id") for r in reqs]
    if None in req_ids or len(req_ids) != len(set(req_ids)):
        errors.append("requirement IDs must be present and unique")
    q_ids = [q.get("id") for q in qualities]
    if None in q_ids or len(q_ids) != len(set(q_ids)):
        errors.append("quality IDs must be present and unique")
    criterion_ids = [c.get("id") for c in criteria]
    if None in criterion_ids or len(criterion_ids) != len(set(criterion_ids)):
        errors.append("criterion IDs must be present and unique")
    verification_ids = [v.get("id") for v in verification]
    if None in verification_ids or len(verification_ids) != len(set(verification_ids)):
        errors.append("verification IDs must be present and unique")

    known_req = set(req_ids)
    known_q = set(q_ids)
    known_v = set(verification_ids)
    criteria_by_req: dict[str, list[dict]] = {}

    for c in criteria:
        cid = c.get("id", "<unknown>")
        rid = c.get("requirement")
        if rid not in known_req:
            errors.append(f"{cid}: unknown requirement ref {rid}")
        else:
            criteria_by_req.setdefault(rid, []).append(c)
        if not c.get("statement"):
            errors.append(f"{cid}: missing statement")
        unknown_v = set(c.get("verification", [])) - known_v
        if unknown_v:
            errors.append(f"{cid}: unknown verification refs {sorted(unknown_v)}")

    allowed_classes = {"deterministic", "procedural", "judgement"}
    for v in verification:
        vid = v.get("id", "<unknown>")
        if v.get("class") not in allowed_classes:
            errors.append(f"{vid}: invalid verification class {v.get('class')}")
        if not v.get("method"):
            errors.append(f"{vid}: missing method")

    for r in reqs:
        rid = r.get("id", "<unknown>")
        for field in ("statement", "criticality", "origin", "verification"):
            if not r.get(field):
                errors.append(f"{rid}: missing {field}")
        unknown_q = set(r.get("quality", [])) - known_q
        if unknown_q:
            errors.append(f"{rid}: unknown quality refs {sorted(unknown_q)}")
        unknown_v = set(r.get("verification", [])) - known_v
        if unknown_v:
            errors.append(f"{rid}: unknown verification refs {sorted(unknown_v)}")
        if r.get("criticality") == "must" and not criteria_by_req.get(rid):
            errors.append(f"{rid}: must requirement without acceptance criterion")

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

    if not authority.get("rule_classes") or not authority.get("authorities") or not authority.get("consultation_contract"):
        errors.append("authority contract is incomplete")
    if not competence.get("competence_domains") or not competence.get("material_review_questions"):
        errors.append("competence contract is incomplete")
    if not fitness.get("concerns") or not fitness.get("decision_order"):
        errors.append("architecture fitness contract is incomplete")

    blocks = building_blocks.get("building_blocks", [])
    block_ids = [b.get("id") for b in blocks]
    if not blocks or None in block_ids or len(block_ids) != len(set(block_ids)):
        errors.append("building-block IDs must be present and unique")
    for block in blocks:
        bid = block.get("id", "<unknown>")
        for field in ("name", "purpose", "inputs", "outputs", "automation"):
            value = block.get(field)
            if value is None or value == "" or value == []:
                errors.append(f"{bid}: missing {field}")
    if not building_blocks.get("composition_principles"):
        errors.append("building-block composition principles are missing")
    return errors


def inspect_state() -> dict:
    reqs = load(REQ)["requirements"]
    qualities = load(QUALITY)["qualities"]
    criteria = load(CRITERIA)["criteria"]
    verification = load(VERIFICATION)["verification"]
    blocks = load(BUILDING_BLOCKS)["building_blocks"]
    return {
        "objective": rel(OBJECTIVE),
        "requirements": len(reqs),
        "must_requirements": sum(r.get("criticality") == "must" for r in reqs),
        "criteria": len(criteria),
        "verification_methods": len(verification),
        "quality_dimensions": len(qualities),
        "building_blocks": len(blocks),
        "building_block_names": [b["name"] for b in blocks],
        "lifecycle_stages": load(LIFECYCLE)["stages"],
        "integration_dispositions": load(LIFECYCLE)["integration_dispositions"],
        "competence_domains": list(load(COMPETENCE)["competence_domains"]),
        "architecture_concerns": list(load(FITNESS)["concerns"]),
        "canonical_sources": [rel(p) for p in REQUIRED_FILES],
    }


def context() -> dict:
    return {
        "governing_objective": OBJECTIVE.read_text(encoding="utf-8"),
        "requirements": load(REQ)["requirements"],
        "quality_model": load(QUALITY)["qualities"],
        "criteria": load(CRITERIA)["criteria"],
        "verification": load(VERIFICATION)["verification"],
        "lifecycle": load(LIFECYCLE),
        "authority": load(AUTHORITY),
        "competence": load(COMPETENCE),
        "architecture_fitness": load(FITNESS),
        "building_blocks": load(BUILDING_BLOCKS),
        "instruction": "Treat compiled repository state as authoritative over chat memory. Automate recurring routines and necessary project operations by default. Ask the human when a choice materially affects meaning, needs, direction, priorities, quality, risk acceptance or hard-to-reverse consequences; explain the consequences and the actual decision requested. Detect competence gaps and unknown unknowns. Research SOTA/best practice when material uncertainty warrants it, then assess project fit and operating burden before selecting technology.",
    }


def trace(object_id: str) -> dict | None:
    reqs = load(REQ)["requirements"]
    criteria = load(CRITERIA)["criteria"]
    vmap = {v["id"]: v for v in load(VERIFICATION)["verification"]}
    qmap = {q["id"]: q for q in load(QUALITY)["qualities"]}
    for r in reqs:
        if r.get("id") == object_id:
            related_criteria = [c for c in criteria if c.get("requirement") == object_id]
            vids = set(r.get("verification", []))
            for c in related_criteria:
                vids.update(c.get("verification", []))
            return {
                "object": r,
                "qualities": [qmap[q] for q in r.get("quality", []) if q in qmap],
                "criteria": related_criteria,
                "origin": r.get("origin"),
                "verification": [vmap[v] for v in sorted(vids) if v in vmap],
                "note": "v0.1 traces baseline requirements through criteria and verification; decisions and implementation refs are added when they materialize.",
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
        f"- Acceptance criteria: {state['criteria']}",
        f"- Verification methods: {state['verification_methods']}",
        f"- Quality dimensions: {state['quality_dimensions']}",
        f"- Generic building blocks: {state['building_blocks']}",
        f"- Validation: {'PASS' if not errors else 'FAIL'}",
        "",
        "## Lifecycle",
        "`" + " -> ".join(state["lifecycle_stages"]) + "`",
        "",
        "## Generic building blocks",
        ", ".join(state["building_block_names"]),
        "",
        "## Competence domains",
        ", ".join(state["competence_domains"]),
        "",
        "## Architecture fitness concerns",
        ", ".join(state["architecture_concerns"]),
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
