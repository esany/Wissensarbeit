# WA-P2-CONTEXT-FIDELITY-IMPLEMENTATION-2026-09-20-01-EVIDENCE

Status: **implementation result evidence / formal assurance PASS / qualitative result review required / no merge authority**

## Canonical admission basis

Implementation started only after the Human admission was canonical and formally green:

- canonical admitted baseline: `main@bd3f5a26719b43584264a9e27c9f70f1ace3ea32`
- admission: `project/WA-P2-IMPLEMENTATION-ADMISSION-2026-09-20-01.md`
- admitted step: `p2-context-fidelity-implementation`
- admitted scope: `P2-CONTEXT-FIDELITY-SLICE`

PR #37 was not used as a dependency or scope source.

## Implementation head before result-state persistence

`961f5c61e3fa78a60b45fa0bac2fc3726b6fb51e`

At that head, the implementation diff against the admitted baseline changed exactly:

1. `tools/work.py`
2. `tests/test_context_fidelity.py`

No Requirement, Authority, Building Block, persistent State/Fidelity store, planner, ontology or P3/P4/P5 surface was changed.

## Implemented capability

The existing `work.py context` path remains backwards compatible when called without a bounded request.

The new opt-in bounded compile path:

- accepts explicit `work_ref` and `question_ref`;
- binds an exact Git `source_snapshot`;
- binds `authority_ref=system/authority.json`;
- requires an explicit judgement-provenance selection basis;
- requires a closed Candidate Universe `U`;
- requires complete `R/I` partition with `R ∩ I = ∅` and `R ∪ I = U`;
- rejects duplicate, unresolved or stale structured selection inputs;
- copies exactly the required/material `R` payloads into the execution context;
- detects missing, extra or semantically modified selected payloads;
- writes provenance separately through `--provenance-out`;
- records included/omitted refs and rationales without copying omitted source payloads into the provenance record;
- states explicitly that deterministic checks prove fidelity to the bound selection judgement, not real-world materiality or semantic completeness.

The compiler does not choose `R` or `I`.

## Executable P2 contract

`tests/test_context_fidelity.py` makes the stable structured semantics executable.

Covered cases include:

- F1 — material unresolved alternative omission fails;
- F2 — uncertainty strengthening fails;
- F3 — authority strengthening fails;
- F4 — readiness strengthening fails;
- F5 — resource availability cannot become priority;
- F6 — explicit NONE cannot generate work;
- F7 — missing Purpose cannot be substituted;
- F8 — stale snapshot fails closed;
- F9 — shared-premise evidence cannot be semantically rewritten into independence;
- F10 — bounded support repair cannot silently change its return cursor;
- F11 — symptom feedback cannot be rewritten into architecture authority;
- P1 — closed non-trivial universe with exact `ExecutionRefs = R`;
- P2 — explicit NONE remains NONE;
- P3 — bounded prerequisite repair returns to the same cursor.

The real CLI positive fixture uses six explicit candidate context refs, selects two required refs and omits four explicit irrelevant refs. The execution payload contains only the two required refs; omission provenance is written separately.

## Formal assurance

GitHub Actions assurance:

- run: **#196**
- run id: `35505439281`
- head: `961f5c61e3fa78a60b45fa0bac2fc3726b6fb51e`
- result: **SUCCESS**
- regression suite: **100 tests PASS**

Successful workflow surfaces:

- repository contract validation;
- `work.py audit`;
- material-state continuity;
- systemic reconciliation;
- AI failure-corpus validation;
- full regression tests;
- derived-state generation;
- derived-state reproducibility.

## Scope-boundary check

Observed implementation diff is inside the admitted technical boundary:

- existing Context Compiler modified;
- one focused P2 regression module added;
- no helper module was required;
- no new persistent store;
- no new service/dependency;
- no new planning engine;
- no new Building Block;
- no Requirement or Authority change;
- no generic relevance/materiality classifier;
- no global near-full threshold;
- no PR #37 scope;
- no P3/P4/P5 activation.

## Important limits / unresolved result questions

Formal PASS does **not** prove P2 effectiveness.

Still unproven and reserved for qualitative result review:

1. whether real task selections are materially complete;
2. whether real task contexts are usefully smaller;
3. whether Human/AI work improves in actual use;
4. whether selection/omission explanations are sufficient to operators;
5. whether provenance overhead is proportionate to context saved;
6. whether building the legacy full source map internally before selecting `R` creates unacceptable process overhead, even though only `R` is sent downstream;
7. whether top-level Context-Compiler refs are sufficient for useful heterogeneous real tasks without widening scope;
8. whether real source payloads preserve all relevant semantic boundaries in practice.

These are not converted into deterministic CI claims.

## Result classification

**Implementation completed inside the admitted slice and formal assurance is green.**

This classification is not:

- qualitative result acceptance;
- Human usefulness acceptance;
- merge authorization;
- canonical promotion;
- later programme priority.

The next gate is a separate qualitative P2 Context-Fidelity result review.
