# Scoped-authority resolution audit — implementation blockade and system-wide return path

Status: CURRENT SYSTEM AUDIT / bounded implementation evidence
Date: 2026-10-09
Repository: esany/Wissensarbeit
Related concrete case: esany/paleo-type PR #327
Online source: GitHub connector only

## Problem

A Human Owner can authorize a bounded implementation, but the execution cursor exposes only a global boolean:

`implementation_allowed: false`

A safe connector therefore blocks the requested mutation even when the requested target is narrow, reversible and explicitly bounded. The system has no canonical way to represent:

- which repository is admitted;
- which PR or branch is admitted;
- which files may change;
- which actions are allowed;
- which owner accepts the result;
- which DOR/DOD applies;
- what remains explicitly unauthorized.

## Root cause

The current system conflates two different questions:

1. Is material implementation generally enabled for the current programme cursor?
2. Is this exact implementation, on this exact target and within this exact scope, admitted?

The global flag is a legitimate safety default, but it is too coarse to resolve a scoped Human decision. Treating it as the only gate creates a mechanical blocker. Treating a user message as permission to overwrite it would create authority laundering.

## Manifestations

- a safe bounded implementation is blocked despite explicit Human direction;
- the assistant asks the Human to repeat or broaden a permission that was already specific;
- a D-016 record risks being rewritten by the implementation agent itself;
- the Human must carry repository/governance vocabulary that the system should resolve;
- work remains in comments and Draft PRs rather than reaching the correct owner boundary;
- local fallback becomes tempting, even though it is prohibited;
- a technical status can be mistaken for an acceptance decision.

## Systemic network

```
Human outcome
→ bounded implementation request
→ global Boolean gate
→ safe stop without scoped resolution path
→ extra approval/meta-work
→ stale or partial context
→ pressure for local workaround or authority overreach
→ recurring false-learn/local-PASS/closure spiral
```

This is an owner-burden and authority-resolution defect, not a GitHub transport defect.

## Implemented target

The bounded mechanism adds scoped admissions to the existing execution cursor without changing the global default:

- global `implementation_allowed: false` remains unchanged;
- a scoped admission is bound to repository and target branch/PR;
- allowed actions and paths are explicit;
- merge requires a separate admission;
- scope overflow fails closed;
- admission does not establish implementation completion, scholarly truth or Human acceptance;
- exactly one admitted scope must match a requested target.

The mechanism is implemented by extending the existing decision-brief contract, `tools/work.py`, and the existing test owner. It does not create a second state store or autonomous planner.

## Enforcement status

The scoped check is now connected to the existing `preflight` execution path, not only exposed as a helper:

- scoped preflight requires repository, target type, exact working branch and changed paths;
- mismatched targets, branches, actions and paths fail closed;
- the CLI path has both an allowed-case and a blocked-case regression;
- remote assurance run 299 passed at commit `2dcc664c6529c44e7f5bb9ac3f75875c8c084d08`;
- this proves the tested execution path only, not enforcement by untested external connectors or scholarly acceptance.

## Work split

- Wissensarbeit owns the generic scoped-authority contract and preflight semantics.
- paleo-type owns the concrete Outcome-Preserving Return Gate and failure-family fixtures.
- Each repository remains authoritative for its own truth.
- Cross-repository references identify PR, branch and commit; one repository's PASS does not close the other.

## Definition of Done

- malformed scoped admissions fail validation;
- missing, duplicate or mismatched admissions fail preflight;
- actions outside the admission fail;
- merge is rejected without a separate admission;
- allowed paths are enforced;
- the global implementation flag remains false;
- a valid scoped admission permits only the listed action/target;
- a fresh context can reconstruct the admission, evidence, residual and return condition;
- the paleo-type PR exercises the concrete return-gate failure families;
- no Issue closure, merge or scholarly acceptance is inferred.

## Assurance ceiling

Repository tests establish only the deterministic contract. They do not prove Human acceptance, scholarly truth, connector implementation details outside the tested boundary, or universal future model behavior.
