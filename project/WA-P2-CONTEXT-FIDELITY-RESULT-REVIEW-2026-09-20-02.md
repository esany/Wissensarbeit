# WA-P2-CONTEXT-FIDELITY-RESULT-REVIEW-2026-09-20-02

Status: **independent qualitative result-review evidence / NEEDS CORRECTION / no result acceptance / no merge authority**

## Review target

PR #39 — `P2: implement admitted context-fidelity slice`

Reviewed repository state:

- canonical review baseline: `main@7d1619ebfec9915e0e60f4d43794b7f1ba0772b0`
- reviewed PR head: `45ae94f124ee6b04be8b2c418a9cc5c8e36b69d1`
- PR state at review: open, not merged, not draft, `mergeable=false`
- PR divergence at review: 8 commits ahead / 7 commits behind current `main`, merge base `bd3f5a26719b43584264a9e27c9f70f1ace3ea32`
- formal assurance on reviewed PR head: GitHub Actions Run #202 / run id `35505569149` / SUCCESS / 100 tests PASS

Run #202 is formal assurance for the then-tested PR candidate. Because canonical `main` advanced afterward, it is not treated as current integration assurance against `main@7d1619ebfec9915e0e60f4d43794b7f1ba0772b0`.

## Review provenance boundary

This artifact persists the completed independent qualitative review supplied to the repository work context.

At persistence time, PR #39 has no GitHub review submission and no review thread carrying this verdict. The repository therefore does **not** claim a GitHub-native review identity, review id, permalink or reviewer provenance that does not exist.

The prior `project/WA-P2-CONTEXT-FIDELITY-RESULT-REVIEW-2026-09-20-01.md` remains the historical review input/brief with `VERDICT PENDING`; it is not rewritten as if it had already contained this verdict.

## Verdict

**NEEDS CORRECTION**

The admitted Existing-Owner P2 Context-Fidelity approach remains viable.

The review found no need for:

- a new preflight;
- a new Implementation Admission;
- a new State owner or persistent State/Fidelity store;
- a new planner or programme mechanism;
- a new Building Block;
- a new ontology;
- a Materiality/Relevance classifier;
- PR #37 scope;
- P3/P4/P5 activation.

Exactly two material implementation findings require correction before result confirmation.

## Finding 1 — Source Snapshot / Working-Tree Fidelity

The reviewed PR implementation derives its repository snapshot from `git rev-parse HEAD` while the Context payloads are read from Working-Tree files.

A relevant Context source can therefore be modified locally without changing `HEAD`. A request bound to `git:<HEAD>` can then compile payloads that do not actually correspond to that Git commit while the snapshot check still passes.

This violates the already admitted snapshot/fidelity semantics.

The bounded correction may only:

- fail closed when relevant Working-Tree Context sources differ from the bound Git snapshot; or
- read the relevant Context sources from the bound Git commit.

No new clock, State owner or persistence layer is required or admitted.

A focused negative regression must make this counterexample executable.

## Finding 2 — Judgement-based Selection Boundary

The reviewed PR implementation requires `provenance_role` to be non-empty but does not structurally require it to denote a judgement-based selection origin.

An explicitly non-judgement role can therefore enter the structural PASS path even though the Admission binds Selection/Materiality to judgement input with traceable provenance.

This violates the already admitted selection-authority boundary.

The bounded correction must:

- reject explicitly non-judgement-based Selection roles;
- continue to accept the valid judgement-based path;
- preserve the boundary `deterministic fidelity validation != real-world materiality judgement`;
- avoid inventing a new Materiality/Provenance ontology or new provenance-reference infrastructure.

The correction must not silently strengthen `provenance_ref` beyond what the frozen contract actually defines.

A focused regression must make the non-judgement-origin counterexample executable.

## Findings that remain confirmed

The review otherwise found the implementation materially aligned with the admitted slice:

- the compiler does not itself choose real-world materiality;
- closed `U`, complete/disjoint `R/I`, and exact `ExecutionRefs = R` are enforced;
- over- and under-inclusive outputs are detected;
- selected payloads are copied without semantic transformation;
- omission provenance is separate from omitted payloads;
- the real CLI 6→2 fixture uses the production path;
- downstream bounded-context reduction is demonstrated;
- no new store, planner, Building Block, Requirement/Authority change, ontology, generic classifier, PR #37 dependency or P3/P4/P5 activation was found.

These confirmations do not waive the two material findings.

## Open qualitative result dimensions

This NEEDS CORRECTION verdict does not resolve:

- material completeness on representative real tasks;
- empirical Human/AI usefulness;
- representative real-task context reduction;
- practical burden of creating the judgement selection basis;
- provenance/process overhead in real use;
- whether the existing top-level Context-Compiler refs are sufficient across useful heterogeneous tasks.

Formal assurance must not be described as resolving those judgement questions.

## Existing Admission still carries the correction

The applicable Human authority remains:

`project/WA-P2-IMPLEMENTATION-ADMISSION-2026-09-20-01.md`

Its admitted execution step is:

`p2-context-fidelity-implementation`

Its admitted scope already includes:

- exact source/snapshot identity and deterministic fidelity to that snapshot;
- judgement-based Selection/Materiality input with traceable provenance;
- focused executable P2 regression fixtures;
- bounded implementation-result evidence and ordinary existing-owner reconciliation.

Both findings are defects inside those already admitted semantics. The review does not identify a capability outside that scope.

Accordingly, this review does not require a new Admission or a new implementation step. It also does not establish a general rule that NEEDS CORRECTION automatically reactivates any Admission. Any correction authority must be explicitly rebound in the persisted execution cursor to this existing Admission, existing step and these two findings.

## Correction boundary

The only implementation continuation supported by this review is:

1. Source Snapshot / Working-Tree Fidelity;
2. judgement-based Selection-Provenance Boundary;
3. regressions immediately required for those two findings;
4. integration of PR #39's implementation candidate with the then-current canonical `main`, without overwriting newer canonical Execution/Reconciliation state with stale PR state.

No other implementation scope is admitted by this review.

## Authority boundary

This review evidence does **not**:

- accept the implementation result;
- authorize merge of PR #39;
- authorize promotion of the implementation result;
- create a new Implementation Admission;
- create a new implementation step;
- authorize P3/P4/P5;
- make PR #37 a dependency;
- prove real-world materiality, completeness or usefulness.

## Required next sequence

After a separately persisted and canonically promoted correction gate rebinds the existing Admission to the existing `p2-context-fidelity-implementation` step for these findings:

1. integrate the PR #39 implementation candidate with then-current canonical `main` without reverting newer canonical workflow state;
2. correct only the two findings;
3. add only the directly required regressions;
4. run full formal assurance;
5. close implementation authority again;
6. persist corrected result evidence;
7. obtain a fresh independent qualitative result re-review against the exact corrected head.

Until that gate is canonical, PR #39 must not be changed on the basis of this review evidence.
