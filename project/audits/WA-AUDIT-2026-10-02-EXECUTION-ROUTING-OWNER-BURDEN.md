# WA-AUDIT-2026-10-02 — Execution routing and Owner burden

Status: **bounded orchestration correction / existing-owner refinement / no promotion authority**

## Finding

The Human Owner had to ask whether a repository/GitHub task belonged in Work or
normal Chat, and then had to ask whether a Work request for Chrome access was
necessary. The orchestration had identified the next substantive step but had
not supplied the execution route, capability/permission preflight, and one
concrete unavoidable Owner action.

This is Owner-primary usability evidence from the 2026-10-02 task context. It
does not authorize a new project priority, architecture, tool registry,
connector, browser access or promotion decision.

## Fresh repository/GitHub boundary

- Planning Owner: `github:esany/Wissensarbeit#7`.
- Active bounded Work Package: `github:esany/Wissensarbeit#73`, selected by the
  Human Owner and persisted in `#7#issuecomment-5953726767`.
- PR #74 remains an independent-review candidate at the latest inspected exact
  head `25c81532734a899f97f9236f7feea10fcdfe8c80`; its head is not changed
  here. Earlier review notes refer to the superseded `7b98fa6` head.
- Current GitHub `main` at inspection: `0853a30e32bdf078e75d5f69414097b68cc1a59a`.
- Issue #28 already contains a bounded execution-guard concept and a
  connector-first routing regression, but neither the Authority contract nor
  the guard required AI-owned route/permission decisions and an exact
  Owner-action instruction.

## Root cause classification

Combination of:

1. **Operationalization gap:** `system/authority.json` said to automate routine
   work but did not explicitly make environment selection, capability admission
   or permission necessity AI-owned.
2. **Regression gap:** the existing `FF-EXECUTION-PROGRESS` case covered a
   connector-first route, but not the complete A–E boundary: environment choice,
   least-privilege permission choice, an unexpected prompt, missing capability,
   and convenience escalation.
3. **Product boundary:** repository contracts can specify and test the
   orchestration behavior, but cannot control a ChatGPT/Work UI permission
   prompt. The UI must still surface the prescribed allow/deny instruction.

Existing authority, execution-guard, decision-brief and reconciliation
mechanisms are sufficient owners. No new planner, orchestrator, registry,
Building Block, Requirement or runtime service is justified.

## Bounded correction

The existing Authority contract now requires the AI to:

- select `normal-chat-first` for adequate read-only connector work;
- select `work-or-codex` when local mutation, branch/commit work or checks are
  actually required;
- inspect alternatives before the smallest necessary escalation;
- reject browser/Chrome access when the connector or repository tools suffice;
- give an exact allow/deny instruction if a permission prompt still appears;
- leave the Owner at most one unavoidable action, with what/why/option and
  explicit non-decisions stated.

`tools/work.py` validates this contract. `WA-EVAL-031` through `WA-EVAL-035`
cover the five observed routing/permission boundaries as regression candidates;
they are deterministic boundary checks, not claims of model or UI proof.

## Non-changes and authority boundary

- no change to `project/GOVERNING_OBJECTIVE.md`;
- no Requirement, Building Block, risk family, priority or Planning Owner change;
- no activation of another candidate or automatic follow-up priority;
- no change to `project/execution_state.json`;
- no merge or promotion authority for PR #74 or this correction;
- no request for Chrome, Work, normal Chat or any external permission is made by
  this audit.

The correction is reversible and remains a candidate until the applicable
independent review and promotion gates are satisfied.
