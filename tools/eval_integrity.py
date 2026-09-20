"""Deterministic integrity checks for recorded eval trial evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "tests" / "fixtures" / "eval_cases.json"
PROBES = ROOT / "tests" / "probes" / "routing_fresh_context_stimuli_v1.json"
PROBE_TRIAL_CONTRACT = ROOT / "tests" / "probes" / "fresh_context_trial_contract.json"
FIXTURE_IDENTITY_FIELDS = ("id", "family", "type", "source_refs", "context", "prompt", "expect")
FIXTURE_IDENTITY_PREFIX = "sha256:"


def load(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def get_case(case_id: str) -> dict | None:
    for case in load(CASES).get("cases", []):
        if case.get("id") == case_id:
            return case
    return None


def fixture_identity(case: dict) -> str:
    """Return the versioned identity of the canonical content a trial used."""
    fixture = {field: case.get(field) for field in FIXTURE_IDENTITY_FIELDS}
    encoded = json.dumps(fixture, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return FIXTURE_IDENTITY_PREFIX + hashlib.sha256(encoded).hexdigest()


def validate_fixture_identity(case: dict, recorded_identity: object) -> list[str]:
    if not isinstance(recorded_identity, str) or not recorded_identity:
        return ["trial missing fixture_identity"]
    if recorded_identity != fixture_identity(case):
        return [f"fixture_identity mismatch for {case['id']}"]
    return []


def validate_trial_record(record: dict) -> list[str]:
    """Fail closed unless trial evidence names the current canonical fixture exactly."""
    case_id = record.get("case_id")
    case = get_case(case_id) if isinstance(case_id, str) else None
    if case is None:
        return [f"trial references unknown case {case_id}"]
    errors = validate_fixture_identity(case, record.get("fixture_identity"))
    raw_response = record.get("raw_response")
    if raw_response is None:
        return [*errors, "trial missing raw_response"]
    try:
        result = json.loads(raw_response) if isinstance(raw_response, str) else raw_response
    except json.JSONDecodeError:
        return [*errors, "trial raw_response is not valid JSON"]
    if not isinstance(result, dict) or result.get("case_id") != case_id:
        errors.append(f"trial result case_id mismatch: expected {case_id}")
    return errors


PROBE_IDENTITY_PREFIX = "sha256:"


def probe_document() -> dict:
    return load(PROBES)


def get_probe(probe_id: str) -> dict | None:
    for probe in probe_document().get("probes", []):
        if probe.get("probe_id") == probe_id:
            return probe
    return None


def probe_identity(probe: dict) -> str:
    payload = {
        "probe_id": probe.get("probe_id"),
        "prompt": probe.get("prompt"),
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return PROBE_IDENTITY_PREFIX + hashlib.sha256(encoded).hexdigest()


def current_repository_revision() -> str | None:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value if re.fullmatch(r"[0-9a-f]{40}", value) else None


def _git_text_at_revision(revision: str, ref: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{revision}:{ref}"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise ValueError(f"probe context is not Git-readable at {revision}: {ref}: {detail}")
    try:
        return result.stdout.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"probe context is not UTF-8 text at {revision}: {ref}") from exc


def _sha256_text(value: str) -> str:
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def probe_bundle_identity(manifest: dict) -> str:
    encoded = json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def render_probe_bundle(probe_id: str) -> dict:
    doc = probe_document()
    probe = get_probe(probe_id)
    if probe is None:
        raise ValueError(f"unknown probe {probe_id}")
    revision = current_repository_revision()
    if revision is None:
        raise ValueError("cannot resolve exact repository revision")
    paths = doc.get("operational_context_paths", [])
    context_files = []
    for ref in paths:
        content = _git_text_at_revision(revision, ref)
        context_files.append({
            "path": ref,
            "sha256": _sha256_text(content),
            "content": content,
        })
    instructions = (
        "You are a fresh project-working instance. Use only the stimulus and repository context files "
        "contained in this bundle. Do not access the repository, eval fixtures, prior trial outputs or "
        "external oracle material. Resolve the current planning source and known candidate evidence from "
        "the supplied repository state. Return JSON with probe_id, selected_action, claims, preserved_states, "
        "authority, routing, questions, notes. Preserve uncertainty and authority boundaries."
    )
    stimulus = probe.get("prompt")
    manifest = {
        "schema_version": "1.0",
        "probe_id": probe_id,
        "probe_identity": probe_identity(probe),
        "repository_revision": revision,
        "context_mode": doc.get("execution_protocol", {}).get("context_mode"),
        "context_files": [{"path": item["path"], "sha256": item["sha256"]} for item in context_files],
        "instructions_sha256": _sha256_text(instructions),
        "stimulus_sha256": _sha256_text(stimulus),
    }
    return {
        "schema_version": "1.1",
        "probe_id": probe_id,
        "probe_identity": probe_identity(probe),
        "repository_revision": revision,
        "context_mode": doc.get("execution_protocol", {}).get("context_mode"),
        "bundle_manifest": manifest,
        "bundle_identity": probe_bundle_identity(manifest),
        "instructions": instructions,
        "stimulus": stimulus,
        "context_files": context_files,
    }


def validate_probe_definitions() -> list[str]:
    errors: list[str] = []
    doc = probe_document()
    probes = doc.get("probes", [])
    ids = [p.get("probe_id") for p in probes]
    if not probes or None in ids or len(ids) != len(set(ids)):
        errors.append("probe IDs must be present and unique")
    forbidden_keys = {"expect", "expected", "oracle", "grading", "answer"}
    for probe in probes:
        present = forbidden_keys & set(probe)
        if present:
            errors.append(f"{probe.get('probe_id')}: stimulus-only probe contains oracle-like fields {sorted(present)}")
        encoded = json.dumps(probe, ensure_ascii=False)
        if "OC-" in encoded:
            errors.append(f"{probe.get('probe_id')}: stimulus-only probe leaks an OC identifier")
        if not isinstance(probe.get("prompt"), str) or not probe.get("prompt", "").strip():
            errors.append(f"{probe.get('probe_id')}: missing prompt")
    context_paths = doc.get("operational_context_paths", [])
    if not isinstance(context_paths, list) or not context_paths:
        errors.append("probe operational_context_paths must be non-empty")
    for ref in context_paths:
        if ref.startswith(("tests/", "tools/")):
            errors.append(f"probe context must exclude eval/tool surfaces: {ref}")
    return errors


def validate_probe_bundle_manifest(manifest: object, record: dict) -> list[str]:
    if not isinstance(manifest, dict):
        return ["fresh probe trial bundle_manifest must be an object"]
    errors: list[str] = []
    for field in ("probe_id", "probe_identity", "repository_revision", "context_mode", "context_files", "instructions_sha256", "stimulus_sha256"):
        if field not in manifest:
            errors.append(f"fresh probe trial bundle_manifest missing {field}")
    if errors:
        return errors

    if manifest.get("probe_id") != record.get("probe_id"):
        errors.append("fresh probe trial bundle_manifest probe_id mismatch")
    if manifest.get("probe_identity") != record.get("probe_identity"):
        errors.append("fresh probe trial bundle_manifest probe_identity mismatch")
    if manifest.get("repository_revision") != record.get("repository_revision"):
        errors.append("fresh probe trial bundle_manifest repository_revision mismatch")
    if manifest.get("context_mode") != record.get("context_mode"):
        errors.append("fresh probe trial bundle_manifest context_mode mismatch")

    doc = probe_document()
    expected_paths = doc.get("operational_context_paths", [])
    context_files = manifest.get("context_files")
    if not isinstance(context_files, list):
        errors.append("fresh probe trial bundle_manifest context_files must be a list")
    else:
        actual_paths = [item.get("path") for item in context_files if isinstance(item, dict)]
        if actual_paths != expected_paths:
            errors.append("fresh probe trial bundle_manifest context paths must exactly match the operational allowlist")
        for item in context_files:
            if not isinstance(item, dict) or not isinstance(item.get("sha256"), str) or re.fullmatch(r"sha256:[0-9a-f]{64}", item.get("sha256", "")) is None:
                errors.append("fresh probe trial bundle_manifest context hashes must be sha256 values")

    for field in ("instructions_sha256", "stimulus_sha256"):
        if not isinstance(manifest.get(field), str) or re.fullmatch(r"sha256:[0-9a-f]{64}", manifest.get(field, "")) is None:
            errors.append(f"fresh probe trial bundle_manifest {field} must be sha256")
    return errors


def validate_fresh_probe_trial_record(record: dict) -> list[str]:
    errors: list[str] = []
    contract = load(PROBE_TRIAL_CONTRACT)
    required = set(contract.get("capture_required_fields", []))
    missing = sorted(required - set(record))
    if missing:
        return [f"fresh probe trial missing fields {missing}"]

    probe_id = record.get("probe_id")
    probe = get_probe(probe_id) if isinstance(probe_id, str) else None
    if probe is None:
        errors.append(f"fresh probe trial references unknown probe {probe_id}")
    elif record.get("probe_identity") != probe_identity(probe):
        errors.append(f"fresh probe trial probe_identity mismatch for {probe_id}")

    revision = record.get("repository_revision")
    if not isinstance(revision, str) or re.fullmatch(r"[0-9a-f]{40}", revision) is None:
        errors.append("fresh probe trial repository_revision must be an exact 40-character Git SHA")

    doc = probe_document()
    expected_paths = doc.get("operational_context_paths", [])
    if record.get("context_mode") != "isolated-repository-bundle":
        errors.append("fresh probe trial context_mode must be isolated-repository-bundle")
    if record.get("accessible_context_paths") != expected_paths:
        errors.append("fresh probe trial accessible_context_paths must exactly match the isolated operational allowlist")
    if record.get("fresh_instance") is not True:
        errors.append("fresh probe trial must declare fresh_instance=true")
    if record.get("external_repository_access") is not False:
        errors.append("fresh probe trial must declare external_repository_access=false")
    if record.get("prior_trial_access") is not False:
        errors.append("fresh probe trial must declare prior_trial_access=false")
    if record.get("oracle_access") is not False:
        errors.append("fresh probe trial must declare oracle_access=false")
    if record.get("response_captured_before_oracle_reveal") is not True:
        errors.append("fresh probe trial must capture response before oracle reveal")

    manifest = record.get("bundle_manifest")
    errors.extend(validate_probe_bundle_manifest(manifest, record))
    bundle_identity = record.get("bundle_identity")
    if not isinstance(bundle_identity, str) or re.fullmatch(r"sha256:[0-9a-f]{64}", bundle_identity) is None:
        errors.append("fresh probe trial bundle_identity must be sha256")
    elif isinstance(manifest, dict) and bundle_identity != probe_bundle_identity(manifest):
        errors.append("fresh probe trial bundle_identity mismatch")

    raw_response = record.get("raw_response")
    if not isinstance(raw_response, str) or not raw_response.strip():
        errors.append("fresh probe trial raw_response must be a non-empty unchanged string")
    else:
        try:
            parsed = json.loads(raw_response)
        except json.JSONDecodeError:
            errors.append("fresh probe trial raw_response must be valid JSON")
        else:
            if not isinstance(parsed, dict):
                errors.append("fresh probe trial raw_response must decode to an object")
            elif parsed.get("probe_id") != probe_id:
                errors.append(f"fresh probe trial response probe_id mismatch: expected {probe_id}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(prog="eval-integrity")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate-probes")
    render_p = sub.add_parser("render-probe-bundle")
    render_p.add_argument("probe_id")
    trial_p = sub.add_parser("validate-probe-trial")
    trial_p.add_argument("record", type=Path)
    args = parser.parse_args()

    if args.command == "validate-probes":
        errors = validate_probe_definitions()
        if errors:
            print("PROBE DEFINITIONS INVALID")
            print("\n".join(f"- {error}" for error in errors))
            return 1
        print("PROBE DEFINITIONS VALID")
        return 0
    if args.command == "render-probe-bundle":
        try:
            print(json.dumps(render_probe_bundle(args.probe_id), indent=2, ensure_ascii=False))
        except Exception as exc:
            print(f"cannot render probe bundle: {exc}")
            return 2
        return 0
    try:
        record = load(args.record)
    except Exception as exc:
        print(f"cannot load fresh probe trial: {exc}")
        return 2
    errors = validate_fresh_probe_trial_record(record)
    if errors:
        print("FRESH PROBE TRIAL INVALID")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("FRESH PROBE TRIAL VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
