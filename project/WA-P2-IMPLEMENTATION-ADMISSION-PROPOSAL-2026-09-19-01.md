# WA-P2-IMPLEMENTATION-ADMISSION-PROPOSAL-2026-09-19-01

Status: **implementation-admission proposal / NOT ADMITTED / `implementation_allowed=false`**

Preflight basis: `project/WA-P2-FIDELITY-MANIFEST-PREFLIGHT-2026-09-19-01-EVIDENCE.md`

This document is a decision brief and bounded proposal. It is not an implementation admission. A valid admission requires explicit Human-Owner acceptance of this exact slice **and** a separate persisted admission artifact after the P2 preflight is canonical.

## Decision

Whether to admit the smallest P2 Context-Fidelity implementation slice described below.

## Scope

Admit only an Existing-Owner refinement that makes the current `BB-CONTEXT` executable path capable of producing a **positively bounded** context with rebuildable compile provenance, explicit selection/materiality provenance, stable negative-invariant validation, and a positive fixture that rejects safe full/near-full dumps.

### Allowed functional boundary

1. **Existing Context Compiler path**
   - extend `tools/work.py` context compilation rather than creating a parallel context/state service;
   - accept/bind an explicit work/question reference, source/snapshot identity, authority reference, and a traceable selection/materiality basis sufficient for the bounded compile;
   - the selection/materiality basis is judgement input/provenance, not a deterministic truth claim by the compiler;
   - produce a bounded execution context plus a noncanonical compile-provenance/fidelity record;
   - for an explicit structured fixture, retain all declared required/material refs and exclude declared non-required/irrelevant refs; a full/near-full dump must fail.

2. **At most one small internal helper if needed for clarity/test isolation**
   - helper remains owned by `BB-CONTEXT`/`BB-ASSURE`;
   - no persistence, authority, planning or canonical-state ownership.

3. **P2 regression fixtures/tests**
   - executable coverage for the stable structured semantics of F1–F11/P1–P3;
   - at least one positive P1 fixture binds required/material refs, explicit irrelevant refs and the provenance/role of the selection judgement; inclusion of those explicit irrelevant refs fails the boundedness contract;
   - deterministic validation checks fidelity relative to the bound selection basis, not whether real-world materiality was correctly judged;
   - Natural-Language Human-intent/materiality/semantic-equivalence judgement is not converted into fake deterministic classification.

4. **Result evidence and ordinary existing-owner reconciliation**
   - after implementation assurance, persist the bounded result review;
   - update only existing execution/reconciliation/derived-state owners as required by their contracts.

### Expected touched implementation/test surfaces

Expected, not permission to expand beyond the functional boundary:

- `tools/work.py`
- optionally one small helper under `tools/` dedicated to context fidelity validation
- one focused P2 regression test module and/or fixture under `tests/`
- existing state/reconciliation/result-evidence files only for the post-implementation transition

If the slice requires changes to Requirements, `system/authority.json`, `system/building_blocks.json`, a new persistent schema/store, a new programme owner, or a generic Intent/Claim ontology, the admission is exceeded and implementation must stop.

The admission also excludes three degenerate implementation shapes:
- a hidden deterministic relevance/materiality classifier that silently owns selection judgement;
- a caller-provided include-list with no traceable selection/materiality provenance;
- a safe full/near-full context dump that preserves fidelity boundaries but does not perform the required positive reduction.

## Recommendation

**Admit this bounded Existing-Owner slice only after the preflight evidence is promoted to canonical `main`.**

The recommendation is not an implementation action. It is the smallest solution that closes the demonstrated `BB-CONTEXT` operational gap without creating a new truth layer.

## Recommendation rationale

- Option A (tests only) leaves the current near-full-dump Context Compiler unchanged and therefore does not provide the promised bounded capability.
- Option B (minimal extension of existing Context Compiler) directly closes the gap with the least new ownership.
- Option C is permitted only as a small internal code-organization detail inside Option B.
- Option D (new persistent structure/state layer) is unsupported and rejected by the preflight.

## Alternatives

### Do not implement P2 now

Keep the current full context output and frozen preflight as evidence only.

Consequence: no architectural risk or maintenance cost, but the demonstrated bounded Context-Fidelity capability remains unimplemented.

### Re-open preflight

Use this if review finds a material problem in the owner mapping, deterministic/judgement boundary, falsification matrix, or assumed ability to remain within existing owners.

Consequence: implementation remains blocked and no compensating architecture is built.

## Material consequences

If admitted and successfully implemented:

- Context compilation must demonstrably become task-bounded on the explicit positive fixture while preserving provenance and semantic boundaries; real-task usefulness and sufficiency remain later judgement.
- The compile output gains a derived fidelity/provenance explanation; this adds some generated metadata and maintenance/test surface.
- Stable authority/readiness/NONE/freshness invariants gain deterministic regression coverage.
- Semantic materiality, Human intent, problem-fit and real-world usefulness remain judgement dimensions, not CI truth.

If implemented poorly:

- the fidelity record could become another state clock;
- safety metadata or an in-band full provenance payload could negate boundedness;
- selection judgement could be hidden inside the compiler or an unproven caller include-list;
- structural PASS could be overstated as semantic completeness;
- Human-intent judgement could be encoded as a brittle classifier.

These are explicit stop/review risks.

## Reversibility

High.

The slice must remain confined to the existing Context Compiler and tests, preserve canonical owners by reference, create no required migration of project truth, and avoid persistent new state. It can therefore be reverted without rewriting canonical Requirements/Authority/Programme state.

## Tests / regressions required

Before implementation result review:

- repository contract validation;
- `work.py audit`;
- material-state continuity check;
- systemic reconciliation gate;
- state-freshness/cross-clock check;
- all existing tests/regressions unchanged green;
- new P2 stable-invariant fixtures for F1–F11/P1–P3;
- explicit positive bounded-selection fixture: required/material refs retained, explicit irrelevant refs excluded, full/near-full dump fails;
- selection/materiality provenance binding: validator proves fidelity to the judgement basis, not correctness of materiality itself;
- stale snapshot and explicit NONE/purpose-gap negative cases;
- authority and readiness strengthening negative cases;
- derived-state reproduction.

Judgement review remains separate for Problem Fit, semantic fidelity, Human usefulness, design/discovery boundary, maintenance burden and overhead.

## Maintenance / process-overhead expectation

Expected incremental burden is low only if the fidelity record is generated from the compile request/source refs and bound selection provenance rather than manually maintained. Manual per-compile governance bookkeeping is outside the admitted design.

The fidelity/provenance record must not be required to travel wholesale inside the same bounded execution payload. It may be separately inspectable/rebuildable. Result review must assess the combined cost of execution context plus provenance output and explicitly check that context reduction provides useful knowledge-work value rather than merely shifting tokens into governance metadata.

## Stop condition

Stop implementation and re-open the preflight if any of the following becomes necessary:

- new canonical state/truth owner;
- new programme/priority mechanism;
- changes to Governing Objective or material Requirement semantics;
- universal object/claim/intent ontology;
- deterministic Natural-Language intent/materiality classifier;
- hidden deterministic relevance/materiality selection;
- caller include-set without selection provenance;
- persistent fidelity registry;
- inability to enforce the frozen negative invariants without substantially widening scope;
- evidence that the bounded compile cannot remain useful without effectively loading the whole canonical state into the downstream execution context;
- inability to bind a reviewable judgement basis for selection without creating a new persistent truth owner.

Do not compensate for a failed preflight assumption by adding architecture.

## Merge / result-review conditions

Implementation PR is not merge-ready merely because CI is green.

Required before merge:

1. deterministic assurance stack passes;
2. frozen P2 semantics have not been weakened;
3. explicit result review finds no authority strengthening, new state clock, accidental normative Candidate semantics, or disproportionate overhead;
4. a fresh-context review can reconstruct the implemented capability, limits and current cursor;
5. systemic reconciliation dispositions cover every required surface;
6. `implementation_allowed` is handled according to the admitted execution state and is not inferred from tests/PR status.

## Assurance status

- P2 preflight on the branch: **revised PASS candidate after NEEDS CORRECTION; independent re-review pending**
- implementation admission: **not granted**
- implementation: **not started**
- deterministic P2 implementation tests: **not yet applicable**
- Human acceptance of this proposal: **pending**
- current canonical `main` `implementation_allowed`: **false**

## Explicit non-decisions

This proposal does not decide or authorize:

- a new Requirement;
- a new Building Block;
- a new Context/Fidelity store;
- P3/P4/P5;
- broad discovery/design-methodology work;
- a universal Human-intent taxonomy;
- consumer-domain changes;
- merge of any future implementation;
- Domain Truth or general semantic-completeness claims.

## Response requested

Only after the corrected P2 preflight receives an independent `CONFIRM` and is canonically promoted, the only material decision requested is:

> **Admit the exact bounded P2 Context-Fidelity slice above, or do not admit it.**

Exact affirmative response for later persistence:

`ADMIT P2-CONTEXT-FIDELITY-SLICE`

An affirmative chat response alone is still not the persisted admission; it must be externalized as a separate repository admission record before `implementation_allowed` can become true and before implementation starts.
