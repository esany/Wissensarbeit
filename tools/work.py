#!/usr/bin/env python3
"""Minimal, dependency-free operational core for Wissensarbeit."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "project" / "requirements.json"
QUALITY = ROOT / "project" / "quality.json"
CRITERIA = ROOT / "project" / "criteria.json"
VERIFICATION = ROOT / "project" / "verification.json"
RISKS = ROOT / "project" / "risks.json"
LIFECYCLE = ROOT / "system" / "lifecycle.json"
AUTHORITY = ROOT / "system" / "authority.json"
COMPETENCE = ROOT / "system" / "competence.json"
FITNESS = ROOT / "system" / "architecture_fitness.json"
BUILDING_BLOCKS = ROOT / "system" / "building_blocks.json"
OBJECTIVE = ROOT / "project" / "GOVERNING_OBJECTIVE.md"
CURRENT = ROOT / "project" / "CURRENT_STATE.md"
FOUNDATION_HARVEST = ROOT / "project" / "conversation_harvest_foundation_v1.json"
P1_HARVEST = ROOT / "project" / "conversation_harvest_p1_v1.json"
DECISION_BRIEF = ROOT / "system" / "decision_brief.json"
MATERIAL_STATE = ROOT / "system" / "material_state.json"
RECONCILIATION = ROOT / "system" / "reconciliation.json"
RECONCILIATION_PACKET = ROOT / "project" / "reconciliation.json"
EXECUTION_STATE = ROOT / "project" / "execution_state.json"

REQUIRED_FILES = [
    REQ, QUALITY, CRITERIA, VERIFICATION, RISKS, LIFECYCLE, AUTHORITY, COMPETENCE,
    FITNESS, BUILDING_BLOCKS, OBJECTIVE, FOUNDATION_HARVEST, DECISION_BRIEF,
    MATERIAL_STATE, RECONCILIATION, RECONCILIATION_PACKET, P1_HARVEST,
]


def load(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def execution_errors(state: dict) -> list[str]:
    """Validate the small cursor; planning remains in the referenced source."""
    required = {"focus", "planning_source", "current_step", "dependencies", "allowed_actions", "implementation_allowed", "completion_evidence"}
    errors = [f"execution state missing {field}" for field in sorted(required - set(state))]
    planning_source = state.get("planning_source", "__missing__")
    github_source = isinstance(planning_source, str) and re.fullmatch(r"github:[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+#\d+", planning_source)
    if not github_source and not (ROOT / planning_source).is_file():
        errors.append("planning source is not reconstructable")
    if not isinstance(state.get("dependencies"), list):
        errors.append("dependencies must be a list")
    else:
        for dep in state["dependencies"]:
            if not isinstance(dep, dict) or not dep.get("id") or dep.get("status") not in {"open", "resolved"}:
                errors.append("dependency entries must have id and open/resolved status")
    if not isinstance(state.get("allowed_actions"), list) or not all(isinstance(a, str) for a in state.get("allowed_actions", [])):
        errors.append("allowed_actions must be a list of action names")
    if not isinstance(state.get("completion_evidence"), dict):
        errors.append("completion_evidence must be an object")
    return errors


def execution_status(path: Path = EXECUTION_STATE) -> dict:
    try:
        state = load(path)
    except Exception as exc:
        return {"status": "FAIL CLOSED", "errors": [f"cannot load execution state: {exc}"]}
    errors = execution_errors(state)
    if errors:
        return {"status": "FAIL CLOSED", "errors": errors, "state": state}
    return {"status": "PASS", "state": state}


def execution_preflight(action: str, path: Path = EXECUTION_STATE) -> list[str]:
    result = execution_status(path)
    if result["status"] != "PASS":
        return result["errors"]
    state = result["state"]
    if action not in state["allowed_actions"]:
        return [f"action not allowed by persisted cursor: {action}"]
    if any(dep["status"] == "open" for dep in state["dependencies"]):
        return ["open dependency blocks execution"]
    if action in {"implement", "merge"} and not state["implementation_allowed"]:
        return ["implementation authority is not persisted"]
    if action in {"work", "codex", "handoff"} and state.get("route") == "unnecessary-escalation":
        return ["stronger execution environment is not justified by the persisted route"]
    return []


def execution_next(path: Path = EXECUTION_STATE) -> tuple[bool, str]:
    result = execution_status(path)
    if result["status"] != "PASS":
        return False, "FAIL CLOSED: " + "; ".join(result["errors"])
    state = result["state"]
    candidates = [step for step in state.get("current_step", {}).get("next", []) if step.get("status") == "ready"]
    candidates = [step for step in candidates if not any(dep["status"] == "open" and dep["id"] in step.get("depends_on", []) for dep in state["dependencies"])]
    if len(candidates) != 1:
        return True, "no deterministic next action"
    return True, candidates[0]["id"]


def execution_complete(step: str, evidence: str, path: Path = EXECUTION_STATE) -> list[str]:
    errors = execution_preflight("complete", path)
    if errors:
        return errors
    state = load(path)
    known = {item.get("id") for item in state.get("current_step", {}).get("next", [])} | {state.get("current_step", {}).get("id")}
    if step not in known:
        return ["step is not present in persisted cursor"]
    evidence_path = ROOT / evidence
    if not evidence_path.is_file():
        return ["completion evidence is not present in repository"]
    try:
        evidence_path.relative_to(ROOT)
    except ValueError:
        return ["completion evidence must be inside repository"]
    tracked = subprocess.run(
        ["git", "ls-files", "--error-unmatch", "--", evidence],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if tracked.returncode != 0 or tracked.stdout.strip() != evidence:
        return ["completion evidence is not Git-persisted (tracked file required)"]
    state["completion_evidence"][step] = evidence
    state["current_step"]["id"] = step
    state["current_step"]["next"] = [item for item in state["current_step"].get("next", []) if item.get("id") != step]
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return []


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def validate_decision_brief_contract(brief: dict, authority: dict, building_blocks: dict) -> list[str]:
    errors: list[str] = []
    required = {"decision", "scope", "recommendation", "recommendation_rationale", "alternatives", "material_consequences", "reversibility", "assurance_status", "explicit_non_decisions", "response_requested"}
    if not required.issubset(set(brief.get("required_fields", []))):
        errors.append("decision brief contract is missing required decision fields")
    rules = brief.get("rules", {})
    for rule in ("automatic", "recommendation_required", "best_supported_option_first", "exact_response_required"):
        if rules.get(rule) is not True:
            errors.append(f"decision brief must enforce {rule}")
    if rules.get("routine_work_requires_brief") is not False:
        errors.append("decision brief must not burden routine work")
    consultation = authority.get("consultation_contract", {})
    if consultation.get("decision_brief_contract") != "system/decision_brief.json":
        errors.append("authority contract must reference the decision brief")
    if consultation.get("decision_brief_required_before_material_request") is not True:
        errors.append("authority contract must require a brief before material requests")
    blocks = {item.get("id"): item for item in building_blocks.get("building_blocks", [])}
    if "decision brief when material human consultation is required" not in blocks.get("BB-INTEGRATE", {}).get("outputs", []):
        errors.append("BB-INTEGRATE must output a decision brief for material consultation")
    if "complete decision brief" not in blocks.get("BB-TRACE", {}).get("outputs", []):
        errors.append("BB-TRACE must expose the complete decision brief")
    return errors


def validate_foundation_harvest(harvest: dict, requirements: list[dict]) -> list[str]:
    errors: list[str] = []
    expected_chat_id = "6a97167d-70fc-83eb-8b97-3ae4f5d7f0cf"
    allowed_classes = {"direct-owner-supported", "composite-owner-intent", "later-operationalization", "indirectly-supported", "provenance-gap"}
    allowed_roles = {"owner_primary", "owner_primary_with_embedded_ai_context", "ai_interpretation", "ai_interpretation_from_owner_intent", "ai_interpretation_from_owner_review_context", "ai_interpretation_from_owner_implementation_request"}
    required_fields = {"id", "requirement_id", "classification", "current_main_requirement_text", "source_type", "source_scope", "source_ref", "source_role", "uncertainty", "authority", "affected_canonical_ids", "disposition", "rationale", "persistent_action"}
    records = harvest.get("records", [])
    req_map = {item.get("id"): item for item in requirements}
    record_ids = [item.get("requirement_id") for item in records]
    if set(record_ids) != set(req_map) or len(record_ids) != len(set(record_ids)):
        errors.append("foundation harvest must contain exactly one record for every canonical requirement")
    for record in records:
        rid = record.get("requirement_id", "<unknown>")
        missing = sorted(required_fields - set(record))
        if missing:
            errors.append(f"{rid}: harvest record missing fields {missing}")
            continue
        if record["classification"] not in allowed_classes:
            errors.append(f"{rid}: invalid provenance classification {record['classification']}")
        if record["source_role"] not in allowed_roles:
            errors.append(f"{rid}: invalid source role {record['source_role']}")
        if record["source_scope"] not in {"project-primary", "external-historical-evidence"}:
            errors.append(f"{rid}: invalid source scope {record['source_scope']}")
        source_ref = record["source_ref"]
        if record["source_scope"] == "project-primary" and source_ref.get("chat_id") not in {None, expected_chat_id}:
            errors.append(f"{rid}: external historical evidence cannot be project-primary")
        canonical = req_map.get(rid)
        if canonical and record["current_main_requirement_text"] != canonical.get("statement"):
            errors.append(f"{rid}: harvested main requirement text is stale")
        if rid not in record["affected_canonical_ids"]:
            errors.append(f"{rid}: affected canonical IDs must include the requirement")
        action = record["persistent_action"]
        if not isinstance(action, dict) or action.get("type") not in {"no_change", "issue-update", "pr-candidate", "file-update"}:
            errors.append(f"{rid}: invalid persistent action")
        if record["classification"] == "provenance-gap":
            if record["uncertainty"] != "high" or record["disposition"] != "provenance-gap":
                errors.append(f"{rid}: provenance gap must remain explicit with high uncertainty")
            if source_ref.get("turn_ids"):
                errors.append(f"{rid}: provenance gap must not claim an owner-primary turn")
    return errors


def validate_p1_harvest(harvest: dict) -> list[str]:
    errors = []
    if harvest.get("harvest_id") != "WA-HARVEST-P1-001":
        errors.append("P1 harvest has unexpected identity")
    source = harvest.get("source_session", {})
    if source.get("seed_id") != "WA-HARVEST-SEED-003" or source.get("chat_id") != "6a97167d-70fc-83eb-8b97-3ae4f5d7f0cf":
        errors.append("P1 harvest must use the persisted real seed source")
    if not source.get("provenance_gap"):
        errors.append("P1 provenance gap must remain explicit")
    restart = harvest.get("processing", {}).get("restart_status")
    if not isinstance(restart, dict):
        errors.append("P1 harvest must contain an explicit restart assurance state")
    else:
        expected_restart = {
            "status": "passed",
            "assurance": "independently-assured",
            "run_id": "WA-RESTART-2026-09-11-02",
            "issue": "https://github.com/esany/Wissensarbeit/issues/11",
            "tested_sha": "caed6ec7c100d56813569aa13884a446cbffb82b",
            "gate_a": "pass",
            "gate_b": "pass",
            "terminal_evidence": "https://github.com/esany/Wissensarbeit/issues/11#issuecomment-5632821967",
        }
        for field, expected in expected_restart.items():
            if restart.get(field) != expected:
                errors.append(f"P1 restart assurance has unexpected {field}")
    ids = []
    source_ids = set()
    for record in harvest.get("records", []):
        ids.append(record.get("id"))
        record_source = record.get("source", {})
        source_id = (record_source.get("chat_id"), record_source.get("turn_id"))
        if all(part is not None for part in source_id):
            if source_id in source_ids:
                errors.append("P1 harvest contains semantic duplicate source identity (chat_id, turn_id)")
            source_ids.add(source_id)
        for field in ("source", "materiality", "authority", "uncertainty", "canonical_state", "scope", "disposition", "rationale", "persistent_action"):
            if field not in record:
                errors.append(f"{record.get('id', '<unknown>')}: missing {field}")
        if record.get("source", {}).get("role") == "owner-primary" and record.get("authority", {}).get("promotion") != "not-authorized":
            errors.append(f"{record.get('id')}: owner source must not imply promotion")
        if record.get("scope") not in {"generic", "project-specific"}:
            errors.append(f"{record.get('id')}: invalid scope")
        action = record.get("persistent_action", {})
        if action.get("type") not in {"no_change", "issue-update", "file-update", "pr-candidate"}:
            errors.append(f"{record.get('id')}: material item lacks valid action/no-change")
        if not record.get("canonical_state"):
            errors.append(f"{record.get('id')}: canonical state is required")
    if len(ids) != len(set(ids)):
        errors.append("P1 harvest contains semantic duplicate IDs")
    if not ids:
        errors.append("P1 harvest must contain material records")
    return errors


def validate_reconciliation_contract(contract: dict, packet: dict, authority: dict, building_blocks: dict) -> list[str]:
    errors: list[str] = []
    required_surfaces = {"requirements", "issues_findings", "risks", "decisions_concepts", "derived_views", "active_work"}
    if not required_surfaces.issubset(set(contract.get("required_impact_surfaces", []))):
        errors.append("reconciliation contract is missing required whole-project impact surfaces")
    gate = contract.get("gate", {})
    for rule in ("material_change_requires_reconciliation", "every_required_surface_must_be_present", "every_impacted_object_requires_disposition_and_rationale", "unresolved_conflict_or_needs_decision_blocks_systemically_integrated_status", "reconciliation_does_not_grant_material_authority"):
        if gate.get(rule) is not True:
            errors.append(f"reconciliation contract must enforce {rule}")
    if authority.get("consultation_contract", {}).get("reconciliation_contract") != "system/reconciliation.json":
        errors.append("authority contract must reference systemic reconciliation")
    blocks = {item.get("id"): item for item in building_blocks.get("building_blocks", [])}
    for bid in ("BB-INTEGRATE", "BB-ASSURE", "BB-TRACE", "BB-DERIVE"):
        if "systemic reconciliation" not in " ".join(blocks.get(bid, {}).get("outputs", [])).lower() + " " + blocks.get(bid, {}).get("purpose", "").lower():
            errors.append(f"{bid} must participate in systemic reconciliation")
    try:
        from reconcile import validate_packet
        errors.extend(validate_packet(packet, contract))
    except Exception as exc:
        errors.append(f"cannot validate reconciliation packet: {exc}")
    return errors


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
        foundation_harvest = load(FOUNDATION_HARVEST)
        decision_brief = load(DECISION_BRIEF)
        reconciliation = load(RECONCILIATION)
        reconciliation_packet = load(RECONCILIATION_PACKET)
        p1_harvest = load(P1_HARVEST)
    except (json.JSONDecodeError, OSError) as exc:
        return [f"cannot load contract data: {exc}"]

    req_ids = [item.get("id") for item in reqs]
    if None in req_ids or len(req_ids) != len(set(req_ids)):
        errors.append("requirement IDs must be present and unique")
    q_ids = [item.get("id") for item in qualities]
    if None in q_ids or len(q_ids) != len(set(q_ids)):
        errors.append("quality IDs must be present and unique")
    criterion_ids = [item.get("id") for item in criteria]
    if None in criterion_ids or len(criterion_ids) != len(set(criterion_ids)):
        errors.append("criterion IDs must be present and unique")
    verification_ids = [item.get("id") for item in verification]
    if None in verification_ids or len(verification_ids) != len(set(verification_ids)):
        errors.append("verification IDs must be present and unique")

    known_req, known_q, known_v = set(req_ids), set(q_ids), set(verification_ids)
    criteria_by_req: dict[str, list[dict]] = {}
    for criterion in criteria:
        cid, rid = criterion.get("id", "<unknown>"), criterion.get("requirement")
        if rid not in known_req:
            errors.append(f"{cid}: unknown requirement ref {rid}")
        else:
            criteria_by_req.setdefault(rid, []).append(criterion)
        if not criterion.get("statement"):
            errors.append(f"{cid}: missing statement")
        unknown_v = set(criterion.get("verification", [])) - known_v
        if unknown_v:
            errors.append(f"{cid}: unknown verification refs {sorted(unknown_v)}")

    allowed_classes = {"deterministic", "procedural", "judgement"}
    for method in verification:
        vid = method.get("id", "<unknown>")
        if method.get("class") not in allowed_classes:
            errors.append(f"{vid}: invalid verification class {method.get('class')}")
        if not method.get("method"):
            errors.append(f"{vid}: missing method")

    for requirement in reqs:
        rid = requirement.get("id", "<unknown>")
        for field in ("statement", "criticality", "origin", "verification"):
            if not requirement.get(field):
                errors.append(f"{rid}: missing {field}")
        unknown_q = set(requirement.get("quality", [])) - known_q
        if unknown_q:
            errors.append(f"{rid}: unknown quality refs {sorted(unknown_q)}")
        unknown_v = set(requirement.get("verification", [])) - known_v
        if unknown_v:
            errors.append(f"{rid}: unknown verification refs {sorted(unknown_v)}")
        if requirement.get("criticality") == "must" and not criteria_by_req.get(rid):
            errors.append(f"{rid}: must requirement without acceptance criterion")

    stages = lifecycle.get("stages", [])
    transitions = lifecycle.get("allowed_transitions", {})
    if set(stages) != set(transitions):
        errors.append("lifecycle stages and transition keys differ")
    for source, targets in transitions.items():
        for target in targets:
            if target not in stages:
                errors.append(f"invalid lifecycle transition {source} -> {target}")
    expected_dispositions = {"fuse", "refine", "reframe", "supersede", "conflict", "reject", "defer"}
    if not expected_dispositions.issubset(set(lifecycle.get("integration_dispositions", []))):
        errors.append("integration disposition contract is incomplete")

    if not authority.get("rule_classes") or not authority.get("authorities") or not authority.get("consultation_contract"):
        errors.append("authority contract is incomplete")
    if not competence.get("competence_domains") or not competence.get("material_review_questions"):
        errors.append("competence contract is incomplete")
    if not fitness.get("concerns") or not fitness.get("decision_order"):
        errors.append("architecture fitness contract is incomplete")

    blocks = building_blocks.get("building_blocks", [])
    block_ids = [item.get("id") for item in blocks]
    if not blocks or None in block_ids or len(block_ids) != len(set(block_ids)):
        errors.append("building-block IDs must be present and unique")
    for block in blocks:
        bid = block.get("id", "<unknown>")
        for field in ("name", "purpose", "inputs", "outputs", "automation"):
            if block.get(field) in (None, "", []):
                errors.append(f"{bid}: missing {field}")
    if not building_blocks.get("composition_principles"):
        errors.append("building-block composition principles are missing")

    errors.extend(validate_foundation_harvest(foundation_harvest, reqs))
    errors.extend(validate_p1_harvest(p1_harvest))
    errors.extend(validate_decision_brief_contract(decision_brief, authority, building_blocks))
    errors.extend(validate_reconciliation_contract(reconciliation, reconciliation_packet, authority, building_blocks))
    if EXECUTION_STATE.exists():
        errors.extend(execution_errors(load(EXECUTION_STATE)))
    return errors


def inspect_state() -> dict:
    reqs = load(REQ)["requirements"]
    qualities = load(QUALITY)["qualities"]
    criteria = load(CRITERIA)["criteria"]
    verification = load(VERIFICATION)["verification"]
    blocks = load(BUILDING_BLOCKS)["building_blocks"]
    packet = load(RECONCILIATION_PACKET)
    return {
        "objective": rel(OBJECTIVE),
        "requirements": len(reqs),
        "must_requirements": sum(item.get("criticality") == "must" for item in reqs),
        "criteria": len(criteria),
        "verification_methods": len(verification),
        "quality_dimensions": len(qualities),
        "building_blocks": len(blocks),
        "building_block_names": [item["name"] for item in blocks],
        "lifecycle_stages": load(LIFECYCLE)["stages"],
        "integration_dispositions": load(LIFECYCLE)["integration_dispositions"],
        "competence_domains": list(load(COMPETENCE)["competence_domains"]),
        "architecture_concerns": list(load(FITNESS)["concerns"]),
        "canonical_sources": [rel(path) for path in REQUIRED_FILES],
        "reconciliation": {"change_id": packet.get("change_id"), "systemically_integrated": packet.get("systemically_integrated"), "unresolved": packet.get("unresolved", [])},
    }


def context() -> dict:
    return {
        "governing_objective": OBJECTIVE.read_text(encoding="utf-8"),
        "requirements": load(REQ)["requirements"],
        "quality_model": load(QUALITY)["qualities"],
        "criteria": load(CRITERIA)["criteria"],
        "verification": load(VERIFICATION)["verification"],
        "risks": load(RISKS),
        "lifecycle": load(LIFECYCLE),
        "authority": load(AUTHORITY),
        "competence": load(COMPETENCE),
        "architecture_fitness": load(FITNESS),
        "building_blocks": load(BUILDING_BLOCKS),
        "material_state": load(MATERIAL_STATE),
        "reconciliation": load(RECONCILIATION_PACKET),
        "instruction": "Treat compiled repository state as authoritative over chat memory. Material changes must be reconciled against the whole project state before being described as systemically integrated. Automate routine work; retain existing material authority gates.",
    }


def trace(object_id: str) -> dict | None:
    reqs = load(REQ)["requirements"]
    criteria = load(CRITERIA)["criteria"]
    vmap = {item["id"]: item for item in load(VERIFICATION)["verification"]}
    qmap = {item["id"]: item for item in load(QUALITY)["qualities"]}
    for requirement in reqs:
        if requirement.get("id") == object_id:
            related = [item for item in criteria if item.get("requirement") == object_id]
            vids = set(requirement.get("verification", []))
            for criterion in related:
                vids.update(criterion.get("verification", []))
            return {
                "object": requirement,
                "qualities": [qmap[q] for q in requirement.get("quality", []) if q in qmap],
                "criteria": related,
                "origin": requirement.get("origin"),
                "verification": [vmap[v] for v in sorted(vids) if v in vmap],
                "reconciliation": load(RECONCILIATION_PACKET),
                "note": "Trace includes the current whole-system reconciliation packet; object-specific decision/implementation links remain limited where they have not been formalized.",
            }
    return None


def validate_integration_packet(path: Path) -> list[str]:
    try:
        packet = load(path)
    except Exception as exc:
        return [f"cannot load integration packet: {exc}"]
    errors: list[str] = []
    required = ["aspect", "origin", "affects", "supports", "conflicts_with", "disposition", "rationale", "required_changes", "non_changes"]
    for field in required:
        if field not in packet:
            errors.append(f"integration packet missing {field}")
    if packet.get("disposition") not in set(load(LIFECYCLE)["integration_dispositions"]):
        errors.append(f"invalid disposition: {packet.get('disposition')}")
    if packet.get("affects") is not None and not isinstance(packet.get("affects"), dict):
        errors.append("affects must be an object keyed by impacted system dimensions")
    return errors


def current_state_freshness(current: Path = CURRENT, packet: Path = RECONCILIATION_PACKET) -> list[str]:
    """Ensure the derived view is provenance-bound to the current reconciliation packet."""
    if not current.exists() or not packet.exists():
        return []
    expected = load(packet).get("change_id")
    match = re.search(r"^- Current change: `([^`]+)`$", current.read_text(encoding="utf-8"), re.MULTILINE)
    if not match:
        return ["CURRENT_STATE is missing its reconciliation change provenance"]
    if match.group(1) != expected:
        return [f"CURRENT_STATE is stale: derived change {match.group(1)!r} != current reconciliation {expected!r}"]
    return []


def audit() -> list[str]:
    findings = validate()
    if REQ.exists():
        for requirement in load(REQ)["requirements"]:
            if requirement.get("origin") == "chat-only":
                findings.append(f"{requirement.get('id')}: accepted requirement has chat-only origin")
    if RECONCILIATION_PACKET.exists():
        packet = load(RECONCILIATION_PACKET)
        if packet.get("materiality") == "material" and packet.get("systemically_integrated") is not True:
            findings.append("current material change is not systemically integrated")
    findings.extend(current_state_freshness())
    return findings


def derive() -> str:
    state = inspect_state()
    errors = validate()
    reconciliation = state["reconciliation"]
    lines = [
        "# Current State", "",
        "> Generated by `python tools/work.py derive`. Do not maintain parallel truth here.", "",
        "## Baseline",
        f"- Requirements: {state['requirements']} ({state['must_requirements']} must)",
        f"- Acceptance criteria: {state['criteria']}",
        f"- Verification methods: {state['verification_methods']}",
        f"- Quality dimensions: {state['quality_dimensions']}",
        f"- Generic building blocks: {state['building_blocks']}",
        f"- Validation: {'PASS' if not errors else 'FAIL'}", "",
        "## Lifecycle", "`" + " -> ".join(state["lifecycle_stages"]) + "`", "",
        "## Generic building blocks", ", ".join(state["building_block_names"]), "",
        "## Competence domains", ", ".join(state["competence_domains"]), "",
        "## Architecture fitness concerns", ", ".join(state["architecture_concerns"]), "",
        "## Reconciliation",
        f"- Current change: `{reconciliation['change_id']}`",
        f"- Systemically integrated: `{str(reconciliation['systemically_integrated']).lower()}`",
        f"- Unresolved reconciliation blockers: {len(reconciliation['unresolved'])}", "",
        "## Canonical sources",
        *[f"- `{path}`" for path in state["canonical_sources"]], "",
        "## Next operational proof",
        "Run the next real material change through the systemic reconciliation gate, then perform a fresh Git/GitHub-only restart and verify that affected older state is identified without chat reconstruction.",
    ]
    text = "\n".join(lines) + "\n"
    CURRENT.write_text(text, encoding="utf-8")
    return text


def main() -> int:
    parser = argparse.ArgumentParser(prog="work", description="Wissensarbeit operational core")
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "inspect", "context", "derive", "audit"):
        sub.add_parser(command)
    sub.add_parser("status")
    sub.add_parser("next")
    preflight_parser = sub.add_parser("preflight")
    preflight_parser.add_argument("--action", required=True)
    complete_parser = sub.add_parser("complete")
    complete_parser.add_argument("step")
    complete_parser.add_argument("--evidence", required=True)
    trace_parser = sub.add_parser("trace")
    trace_parser.add_argument("object_id")
    integrate_parser = sub.add_parser("integrate")
    integrate_parser.add_argument("packet", type=Path)
    args = parser.parse_args()

    if args.command == "status":
        print(json.dumps(execution_status(), indent=2, ensure_ascii=False))
        return 0 if execution_status()["status"] == "PASS" else 1
    elif args.command == "next":
        ok, message = execution_next()
        print(message)
        return 0 if ok and message != "no deterministic next action" else 1
    elif args.command == "preflight":
        errors = execution_preflight(args.action)
        if errors:
            print("PREFLIGHT FAIL")
            print("\n".join(f"- {error}" for error in errors))
            return 1
        print("PREFLIGHT PASS")
    elif args.command == "complete":
        errors = execution_complete(args.step, args.evidence)
        if errors:
            print("COMPLETION FAIL")
            print("\n".join(f"- {error}" for error in errors))
            return 1
        print("COMPLETION PASS")
    elif args.command == "validate":
        errors = validate()
        if errors:
            print("VALIDATION FAILED")
            print("\n".join(f"- {error}" for error in errors))
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
            print("\n".join(f"- {error}" for error in errors))
            return 1
        print("INTEGRATION PACKET VALID")
    elif args.command == "derive":
        print(derive(), end="")
    elif args.command == "audit":
        findings = audit()
        if findings:
            print("AUDIT FINDINGS")
            print("\n".join(f"- {finding}" for finding in findings))
            return 1
        print("AUDIT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())