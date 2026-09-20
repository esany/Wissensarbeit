# WA-P2-IMPLEMENTATION-ADMISSION-2026-09-20-01

Status: **HUMAN IMPLEMENTATION ADMISSION / P2-CONTEXT-FIDELITY-SLICE / no result acceptance / no merge authority**

## Canonical basis

Fresh canonical baseline at admission persistence:

- `main@b590523d31db5f82628d6e0d5182821501729906`
- canonical preflight: `project/WA-P2-FIDELITY-MANIFEST-PREFLIGHT-2026-09-19-01-EVIDENCE.md`
- final qualitative CONFIRM: `project/WA-P2-PREFLIGHT-REREVIEW-2026-09-20-03.md`
- canonical post-promotion reconciliation: `project/WA-P2-POST-PR35-PROMOTION-RECON-2026-09-20-01.md`
- canonical admission proposal: `project/WA-P2-IMPLEMENTATION-ADMISSION-PROPOSAL-2026-09-19-01.md`

At this baseline, `p2-implementation-admission` is blocked by explicit Human admission and `implementation_allowed=false`.

## Human decision

The Human Owner explicitly authorized the exact proposal-bound slice with:

> `ADMIT P2-CONTEXT-FIDELITY-SLICE`

This admission is the material Human decision requested by the canonical proposal.

## Admitted implementation slice

Admission id:

`WA-P2-IMPLEMENTATION-ADMISSION-2026-09-20-01`

Admitted execution step:

`p2-context-fidelity-implementation`

The admitted scope is only the Existing-Owner P2 Context-Fidelity slice already reviewed and confirmed:

1. extend the existing `tools/work.py` Context Compiler path;
2. accept an explicit task/work reference, source/snapshot identity, authority reference and traceable judgement-based selection/materiality basis;
3. operate over a closed Candidate Universe `U` supplied by that selection basis;
4. require a complete partition into required/material `R` and non-required/irrelevant `I` with `R ∩ I = ∅` and `R ∪ I = U`;
5. output exactly the selected `R` payloads as the bounded execution context for the frozen structured capability contract;
6. retain separately inspectable/rebuildable compile provenance for inclusion and omission;
7. preserve selected payload semantics rather than rewriting uncertainty, alternatives, authority, readiness, purpose, priority or evidence state;
8. add focused executable P2 regression fixtures for the stable structured semantics of F1–F11/P1–P3;
9. persist bounded implementation-result evidence and ordinary existing-owner reconciliation after assurance.

At most one small internal helper is permitted if needed for clarity/test isolation. It must own no persistence, authority, planning or canonical truth.

## Selection authority boundary

The compiler is **not** admitted to decide real-world materiality.

Selection/materiality remains judgement input with traceable provenance. Deterministic validation may prove only that the compiled output is faithful to the bound `U/R/I` basis and source snapshot.

This admission does not authorize:

- a hidden deterministic relevance/materiality classifier;
- an unproven caller include-list without selection provenance;
- a global deterministic near-full ratio/threshold;
- a universal Human-intent/materiality classifier.

## Explicit exclusions

This admission does **not** authorize:

- a new canonical State or Fidelity store;
- a new planning engine or programme owner;
- a new Building Block;
- a new Requirement family or material Requirement change;
- changes to `system/authority.json` or `system/building_blocks.json`;
- a universal Claim/Intent/Object/Materiality ontology;
- P3/P4/P5;
- scope transfer from PR #37;
- consumer-domain canonical changes;
- automatic promotion, merge or result acceptance.

PR #37 is not a dependency of this slice.

If implementation requires any excluded capability or materially wider owner/scope, work must stop fail-closed and return a Decision Brief to the Human Owner.

## Authority separation

This admission means only:

> the exact bounded implementation experiment may begin after this admission is canonically persisted and formally validated.

It does not mean:

`Implementation Admission = Implementation Result Acceptance`

It does not mean:

`Implementation Admission = Merge Authorization`

It does not mean:

`Implementation Admission = later programme priority`

Any implementation result requires separate assurance and qualitative result review. Any later merge/promotion remains a separate decision under the existing repository contracts.

## Execution-state consequence

Once this admission record and its reconciliation are canonical and assurance passes:

- `implementation_allowed=true` may be set only while the persisted cursor names `p2-context-fidelity-implementation` as the sole ready implementation step bound to this admission;
- `implement` may become allowed;
- `merge` remains not allowed by the persisted execution cursor;
- no other implementation scope is authorized.

## Result-review dimensions retained

Green CI will not establish P2 effectiveness.

The later result review must still judge:

- actual context reduction;
- material completeness;
- preservation of uncertainty and authority boundaries;
- reconstructability of inclusion/omission;
- Human/AI usefulness in real use;
- provenance overhead relative to context saved;
- compliance with this exact admitted scope.
