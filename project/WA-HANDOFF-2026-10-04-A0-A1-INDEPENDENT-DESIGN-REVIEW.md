# Independent Design Review Handoff — A0/A1 Current Surface and Method Sufficiency

Status: **review-ready; not implementation-ready**

## Review target

Independently test whether the smallest supported correction to the PR-85 systemic baseline is:

- `A0 SUPPORTED`: existing mechanisms are sufficient as-is; or
- `A1 SUPPORTED`: existing owners need only a minimal contract/derived-view sharpening; or
- `A0/A1 NOT YET DISTINGUISHABLE`.

Primary evidence packet: `project/audits/WA-AUDIT-2026-10-04-REQUIREMENTS-RESEARCH-CONCEPT-DELTA.md`.

Current authority remains `main@b448915cf774c573dbf82cf2e17bcb03c10a9ed8`, `project/execution_state.json`, `project/reconciliation.json`, `system/authority.json`, and the current GitHub owner state. The evidence packet is not authority and does not change `implementation_allowed=false`.

## What must be checked

Use the same real cases from the packet:

1. long-running current programme/problem state;
2. fresh restart without the old chat;
3. current/open/completed/superseded discrimination;
4. proportionate analysis/research/design/assurance sufficiency;
5. learning returned through reconciliation;
6. selective adoption of a generic-tooling improvement by a project with local autonomy.

For each case, test existing mechanisms first. A1 is valid only where A0 fails on a material reconstructability, decisionability, authority, traceability or restartability criterion and the proposed sharpening fixes that failure without a new structural capability.

## Required reviewer output

Return one verdict from:

- `CONFIRM A1 / existing-owner sharpening only`;
- `SHRINK A1 to derived-view-only`;
- `REJECT A1 / A0 SUPPORTED`;
- `A0/A1 NOT YET DISTINGUISHABLE`;
- `MATERIAL DESIGN CORRECTION REQUIRED`.

The review must state:

- the decisive evidence for each case;
- which existing owner is sufficient or needs sharpening;
- whether the current-surface view is a projection or an accidental second truth;
- whether method sufficiency remains proportional and re-entry-capable;
- whether P-D is only a clarification/gap candidate or has repeated cross-project evidence;
- which alternatives were rejected and why;
- what remains before a development package could be considered.

Do not implement, promote a Requirement, activate a candidate, create a planner/bridge/graph/registry, or infer a new priority from this handoff.

