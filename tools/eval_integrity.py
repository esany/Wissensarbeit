"""Deterministic integrity checks for recorded eval trial evidence."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "tests" / "fixtures" / "eval_cases.json"
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
