# WA-P2-FIDELITY-MANIFEST-PREFLIGHT-2026-09-19-01

Status: **P2 preflight evidence / revised PASS candidate after NEEDS CORRECTION / independent re-review required / no implementation authority**

## 1. Exact current baseline

Repository: `esany/Wissensarbeit`

Freshly resolved baseline before this preflight branch was created:

- `main@63883532af7834b5e46a84cef665ef4cfaa25a98`
- latest material commits after the 2026-09-17 baseline reconciliation:
  - `8b349ffac3c467fc2a4d580396bc179caebcc9e1` — Human-intent/symptom audit delta
  - `63883532af7834b5e46a84cef665ef4cfaa25a98` — Design/project-development-method audit delta
- no open pull request was returned by the fresh repository query
- persisted focus/planning source: `github:esany/Wissensarbeit#7`
- persisted current step: `p2-post-pr33-baseline-reconciliation`
- exactly one ready next step: `p2-fidelity-manifest-preflight`
- `implementation_allowed=false`

The accepted prior transition is `p2/post-pr33-baseline-reconciliation-2026-09-17`. This preflight does not treat the historical prompt, roadmap prose, an earlier failed preflight, CI status, or chat momentum as authority.

## 2. Freshness delta since the prior P2 baseline

The diff from the merged post-PR-33 reconciliation commit `4f27d2e9938c193d9a19eba00f9cdca452e18e14` to current `main@6388353` contains exactly two new repository files and no execution/reconciliation/authority-code change:

1. `project/audits/WA-AUDIT-2026-09-18-HUMAN-INTENT-SYMPTOM-DELTA.md`
2. `project/audits/WA-AUDIT-2026-09-19-DESIGN-PROJECT-DEVELOPMENT-METHOD-DELTA.md`

Disposition:

| Evidence | Cursor | P2 semantic effect | Disposition |
|---|---|---|---|
| 2026-09-18 Human-intent/symptom delta | unchanged | material | **integrate into P2 fidelity semantics**: Human feedback is evidence of need/constraint/failure/intent, not automatic solution, Requirement, scope, priority, architecture or programme authority |
| 2026-09-19 design/project-development delta | unchanged | bounded material effect | **preserve only the fidelity boundary in P2**: Context reduction must not collapse observation→need→problem hypothesis→solution candidate→selected design or feedback→authorization; the broader discovery/design methodology gap remains separate future candidate work |
| later/current `paleo-type` learning/repair work inspected for cross-repo freshness | no Wissensarbeit authority | candidate/case evidence only | **no promotion** into current Requirements, priority or P2 implementation authority |

Neither new Wissensarbeit audit establishes a new Requirement family, a fifteenth Building Block, a new lifecycle stage, or implementation admission. Their own “no cursor change” statements were not relied on as authority; the current execution owner and unchanged diff establish the cursor result.

## 3. Current P2 problem statement

**Problem statement**

The repository already promises a task-relevant, bounded execution context through `BB-CONTEXT`, but the current executable `tools/work.py::context()` emits nearly the complete canonical model and the existing Context-Fidelity/Token-Efficiency pilot checks establish mainly reference-set equality. Real failure evidence shows that a smaller context can remain syntactically coherent while silently strengthening or erasing meaning: uncertainty can disappear, Evidence/Candidate state can look accepted, readiness can look higher, available resources can become priority, absence can generate replacement work, stale snapshots can look current, shared premises can look independent, and Human symptom feedback can look like change authority.

Therefore P2 is not primarily a “manifest file” problem. The capability gap is:

> **Compile less context while preserving the strongest source-supported epistemic, authority, readiness, purpose, priority, uncertainty and currentness boundaries, and make material selection/omission/transformation reconstructable without creating a new truth owner.**

Equivalent core invariant:

> **Context compilation may reduce volume, but must not silently increase certainty, authority, scope, readiness, completion status or priority.**

This is supported by REQ-001/002/003/004/007/008/011/012, Q-TRACE/Q-RESTART/Q-XAI/Q-COHERENCE/Q-FIT/Q-LEAN/Q-DOMAIN, R-002/003/004/005/006/007/008/009, the failure corpus, the P1 harvest/restart evidence, the 2026-09-17 P2 audit delta, and the two 2026-09-18/19 audit deltas.

## 4. Evidence inventory

Primary current repository evidence:

- `project/GOVERNING_OBJECTIVE.md`
- `project/requirements.json`
- `project/quality.json`
- `project/criteria.json`
- `project/verification.json`
- `project/risks.json`
- `project/execution_state.json`
- `project/reconciliation.json`
- `project/CURRENT_STATE.md`
- `system/authority.json`
- `system/material_state.json`
- `system/reconciliation.json`
- `system/building_blocks.json`
- `system/decision_brief.json`
- `tools/work.py`
- `tools/state_freshness.py`
- `tools/reconcile.py`
- `tests/test_work.py`
- `tests/test_state_freshness.py`
- `tests/evals/failure_corpus.json`
- `pilots/generic-pilot-learnings/regression-scenarios.json`
- `tools/pilot_regressions.py`
- `project/WA-HARVEST-P1-001-EVIDENCE.md`
- `project/conversation_harvest_p1_v1.json`
- `project/WA-P2-BASELINE-RECON-2026-09-17-01-EVIDENCE.md`
- `project/audits/WA-AUDIT-2026-09-17-PALEO-TYPE-DELTA.md`
- the two newer audit deltas listed above
- current planning source `github:esany/Wissensarbeit#7`, including the prior stale-baseline P2 preflight failure and the accepted post-PR-33 transition
- `project/WA-P2-PREFLIGHT-REVIEW-2026-09-19-01.md` — independent qualitative review result `NEEDS CORRECTION` that identified the full-dump and selection-provenance loophole
- `project/WA-P2-PREFLIGHT-REREVIEW-2026-09-19-02.md` — focused re-review result `NEEDS CORRECTION` that confirmed selection provenance but found the stronger generic near-full claim unsupported by the positive fixture

Cross-repo evidence was used only as a fresh falsification/consumer check. `esany/paleo-type` was freshly read at its then-current main including `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, the active system owner #225, and relevant current learning/method evidence. Consumer-domain state remains in that repository.

## 5. Existing-owner / Requirement mapping

| Demonstrated P2 need | Existing owner | Assessment | P2 consequence |
|---|---|---|---|
| canonical truth and accepted persistence | `BB-STATE` + canonical project/system files | **fully sufficient** | compile record references owners; it does not copy/own truth |
| bounded task-relevant context | `BB-CONTEXT` | **normatively sufficient, operationally insufficient** | current `context()` is a coarse near-full dump; this is the central P2 implementation gap |
| no silent evidence/feedback promotion | `BB-INTEGRATE` + `system/material_state.json` + Authority | **normatively sufficient** | compiler preserves dispositions/authority and does not create promotion |
| provenance / explainability | `BB-TRACE` | **normatively sufficient, compile provenance not operationalized** | compile choices must be reconstructable by reference |
| negative invariants / rule-class separation | `BB-ASSURE` + verification classes | **normatively sufficient, P2 regression gap** | stable structured invariants may be deterministic; semantic judgement remains judgement |
| rebuildable noncanonical views | `BB-DERIVE` | **fully sufficient pattern** | fidelity record is rebuildable compile provenance, never a current-state owner |
| feedback/failure → validated learning | `BB-LEARN` | **fully sufficient semantics** | Human symptom/feedback role remains evidence and does not become product direction |
| need/evidence → validated requirements | `BB-REQUIREMENTS` | **fully sufficient semantics** | no Requirement promotion from raw feedback |
| problem-cleared solution exploration | `BB-DESIGN` | **sufficient owner; broader methodology gap outside P2** | P2 compares implementation options only; no design engine |
| execution/current priority | `project/execution_state.json` + reconciliation | **fully sufficient** | compile output must preserve `NONE`/blocked/unset/current cursor; it does not select replacement work |

**Genuine new top-level owner/norm gap found: none.**

The gap is an operationalization gap inside existing owners, principally `BB-CONTEXT` with `BB-TRACE`/`BB-ASSURE` support.

## 6. Human-intent and discovery/design fidelity boundary

A Human intervention may carry one or several reasoning roles:

- direct outcome/change request;
- constraint or quality expectation;
- symptom/failure feedback;
- question/exploration;
- explicit material authorization/decision.

These are **reasoning distinctions, not a required permanent enum**.

P2 must preserve the source role/authority actually established. It must not deterministically infer all Natural-Language intent. If materially different interpretations remain plausible and choosing one would change direction, scope, priority or architecture, the existing Authority contract requires focused Human clarification.

P2 also must not collapse:

- observation → inferred need;
- need → proposed solution;
- symptom → cause;
- problem hypothesis → accepted problem framing;
- solution candidate → selected design;
- feedback → authorization.

The broader need-elicitation/problem-framing/design-space/prototype/iteration methodology gap is real evidence, but **outside this P2 slice**. It remains a separately dispositionable future candidate and does not alter the P2 cursor.

## 7. Frozen P2 invariants

### Core fidelity

Context compilation may reduce volume, but must not silently increase certainty, authority, scope, readiness, completion status or priority.

### Provenance

Material selection, omission and transformation must be reconstructable against exact source/snapshot identities.

### Non-generative absence

Absence of authority is a state, not a request to manufacture authority. `scope = none`, `NEXT ACTION = NONE`, unknown, blocked, unresolved, or missing Purpose must not synthesize replacement work.

### Uncertainty preservation

Uncertainty and unresolved alternatives remain visible unless a separately authorized/evidenced source resolves them.

### Authority preservation

Candidate, Evidence, Advisory, Accepted, Selected and Authorized may not silently collapse into one another.

### Readiness preservation

Identified, retrievable, staged, inspectable and inspected may not silently collapse into one another.

### Purpose fidelity

If an operation requires a Purpose/Scope discriminator and the canonical owner does not provide it, compilation returns a visible gap; the richest available context is not a substitute.

### Recovery fidelity

A bounded Support/Execution repair returns to the still-valid cursor. Support success does not create a support programme or replacement objective.

### Freshness

A compiled context is current only relative to its bound source/snapshot baseline and explicit invalidation rule. A superseded snapshot must not be presented as current.

### Independence

Several summaries derived from the same unverified premise do not become independent evidence through repetition.

### Human-feedback fidelity

Symptom/quality feedback does not by itself grant Requirement, scope, priority, architecture or programme authority.

### Positive boundedness

A compile is not sufficient merely because it preserves every semantic boundary. The frozen positive fixture must declare a **closed candidate-ref universe** `U`, partition it completely into required/material refs `R` and non-required/irrelevant refs `I`, require `R ∩ I = ∅` and `R ∪ I = U`, and require the execution-ref set to equal `R` exactly.

At least one frozen fixture must demonstrate non-trivial reduction with a visibly bounded proper subset, for example the fixture semantics `U={A,B,C,D,E,F}`, `R={A,B}`, `I={C,D,E,F}`, expected execution refs exactly `{A,B}`. Concrete implementation fixture identifiers may differ, but weakening this partition/output relation requires re-opening the preflight.

This deterministically rejects full or over-inclusive output **for the frozen fixture**. It does not claim that arbitrary real-world "near-fullness" is globally or deterministically decidable.

### Selection provenance

Selection/materiality is not silently owned by the compiler. Deterministic validation may check a compile against an explicit structured selection basis, but the basis itself must identify its judgement/provenance source. Passing deterministic checks proves fidelity to that bound selection basis; it does not prove that real-world materiality or semantic sufficiency was correctly judged.

## 8. Frozen falsification matrix

The scenarios below are the pre-implementation contract. Implementation may refine fixtures/field names, but must not weaken their semantics without re-opening this preflight.

| ID | Scenario | Expected | Verification class |
|---|---|---|---|
| F1 | two declared material unresolved alternatives; compiled output loses one without allowed rationale | FAIL | deterministic for explicit structured material inventory; judgement for whether real-world materiality inventory is adequate |
| F2 | uncertain/unresolved input rendered certain/resolved | FAIL | deterministic where source/output state is structured; semantic-language equivalence remains judgement |
| F3 | Candidate/Advisory/Evidence becomes Accepted/Selected/Authorized | FAIL | deterministic for explicit authority states |
| F4 | Identified/Retrievable becomes Staged/Inspected | FAIL | deterministic for explicit readiness states |
| F5 | resource availability becomes next task/priority | FAIL | deterministic when resource and cursor/priority states are explicit |
| F6 | explicit NONE/unset scope/NEXT ACTION yields replacement work | FAIL | deterministic for structured absence/current-cursor states |
| F7 | required Purpose missing; richest available context substituted as Purpose | FAIL | deterministic for explicit missing discriminator + output; deciding whether operation requires Purpose can be judgement |
| F8 | bound source baseline superseded but output presented as current | FAIL | deterministic snapshot/freshness check |
| F9 | downstream summaries sharing one premise are counted as independent evidence | FAIL | deterministic for explicit provenance ancestry/duplicate premise refs; substantive independence judgement may remain judgement |
| F10 | bounded support repair changes valid cursor or creates meta-programme without authority | FAIL | deterministic where before/after cursor and admission are explicit; interpretation of support failure can be judgement |
| F11 | Human “shallow/confusing” symptom is promoted to new architecture/product direction without authority | FAIL | deterministic/procedural no-promotion check once source role/authority is established; Natural-Language role classification remains judgement |
| P1 | closed fixture universe `U` is fully partitioned into required/material `R` and non-required/irrelevant `I`; execution refs equal `R` exactly; a frozen non-trivial fixture uses a bounded proper subset (e.g. `U={A,B,C,D,E,F}`, `R={A,B}`, `I={C,D,E,F}`); uncertainty/authority/freshness and selection provenance are preserved | PASS only when output refs equal `R` exactly; missing `R` or any output ref outside `R` is FAIL | deterministic for the frozen structured fixture and fidelity to its bound selection basis; real-world boundedness/material sufficiency remains judgement |
| P2 | explicit `NEXT ACTION = NONE` remains NONE; residuals remain evidence only | PASS | deterministic |
| P3 | bounded prerequisite repair returns to unchanged valid cursor | PASS | deterministic for explicit cursor/repair fixture |

**No claim is made that Natural-Language materiality, intent, semantic equivalence or problem-fit is fully deterministically decidable.**

The positive P1 fixture is deliberately stronger than the older reference-set preservation checks: it freezes a closed universe and exact expected output set, including several explicit irrelevant/non-required refs in at least one non-trivial fixture. This prevents a semantically conservative full or over-inclusive output from masquerading as successful bounded compilation **for that fixture**. It does not create a universal near-full metric.

## 9. Solution-space comparison

### A — no implementation; keep current Context function and add regressions

Strengths: minimum code/change risk and zero new state.

Failure: regressions alone do not make `BB-CONTEXT` task-bounded. Current `context()` still returns nearly the full canonical model and has no compile provenance/omission/freshness explanation. This does not close the demonstrated capability gap.

**Disposition: insufficient.**

### B — minimally extend the existing Context Compiler with compile-provenance/fidelity output

Strengths:

- directly closes the existing-owner gap;
- no new canonical state/store/clock;
- allows bounded output while preserving exact source refs;
- supports deterministic invariant checks over explicit structured inputs;
- rebuildable/reversible;
- Human-readable explanation of inclusion/omission;
- can keep judgement outside fake deterministic classification.

Costs/risks:

- small API/output complexity;
- selection/materiality remains judgement and needs an explicit boundary;
- must avoid turning the provenance record into a state owner.

**Disposition: preferred minimal candidate.**

### C — small separate helper inside existing owners

A helper is acceptable only if implementation clarity/test isolation materially improves. It remains an implementation detail owned by `BB-CONTEXT`/`BB-ASSURE`, with no persistence/authority of its own.

Compared with B, it adds one code surface but can reduce `work.py` complexity. This choice is reversible and may be made only inside the admitted functional boundary.

**Disposition: allowed implementation shape, not a new architecture.**

### D — new persistent fidelity/state structure

This would introduce an additional state/clock and maintenance/reconciliation surface while the demonstrated need is compile provenance over existing owners. No evidence shows that A–C cannot satisfy P2.

**Disposition: reject.**

## 10. Minimal implementation candidate

The smallest adequate P2 slice is:

`existing canonical owners → bounded compile operation → rebuildable compile-provenance/fidelity record → deterministic stable-invariant checks → bounded context`

The record explains the compile; it does **not** own Project Purpose, Project Priority, NEXT ACTION, Programme State, Domain Truth, Acceptance or Evidence Truth.

Minimum record semantics:

- exact repository/source snapshot identity;
- work/question reference;
- authority reference;
- bound selection/materiality basis, including the provenance/role of the judgement that supplied or approved it;
- included refs;
- deliberately omitted refs/classes + rationale;
- retained unresolved/uncertainty;
- relevant source/claim roles where they constrain interpretation;
- actual readiness state where relevant;
- refresh/invalidation condition.

Deterministic validation is scoped to explicit structured compile inputs, the bound selection/materiality basis, and their source states. It must not claim global semantic completeness, decide real-world materiality, or infer Human intent. A caller-provided include-list without traceable selection provenance is insufficient for P1.

## 11. Loss/regression risks

1. **False safety:** passing structural checks could be overclaimed as semantic completeness.
2. **Manifest accretion:** provenance output could drift into a new truth store.
3. **Over-selection:** safety could force near-full context and destroy the intended bounded capability; the frozen positive P1 fixture therefore uses a closed universe with a non-trivial proper subset and exact expected output, while real-task over-selection remains a judgement review concern.
4. **Under-selection:** judgement may omit material context despite a structurally valid record.
5. **Status vocabulary inflation:** temporary test vocabulary could become a universal ontology.
6. **Stale compile reuse:** snapshot identity may exist without enforced invalidation.
7. **Human-feedback misclassification:** a model may still misread free text; deterministic checks cannot solve this alone.
8. **Process overhead:** per-compile metadata could cost more than the context reduction if not generated automatically or if the full provenance record is forced into the same execution payload.
9. **Shared-premise laundering:** provenance ancestry may be incomplete and require judgement.
10. **Compatibility:** existing `context` consumers must not silently receive incompatible semantics without a bounded migration decision.

Mitigation: reference existing owners; keep record derived/rebuildable; automate it; freeze negative regressions; maintain explicit judgement review; measure positive usefulness/overhead separately.

## 12. Explicit non-goals

P2 does not create:

- a new state store or programme registry;
- a roadmap/priority engine;
- a new agent architecture;
- a fifteenth Building Block;
- a universal Claim or Intent ontology;
- a universal materiality classifier;
- an automatic Human-intent classifier;
- a generic Purpose inference engine;
- a general design/discovery methodology;
- P3/P4/P5 activation;
- consumer-domain canonical state;
- automatic Requirement/Architecture promotion;
- a claim that CI/regression PASS equals Domain Truth, Human Acceptance, or complete semantic fidelity.

## 13. Residual uncertainty

- Materiality and semantic sufficiency remain judgement-heavy.
- The exact smallest code shape (inline `work.py` vs one helper) should be chosen only inside an admitted functional boundary.
- Real Human usefulness/token/process-overhead benefit is not proven by preflight; it must be reviewed after the bounded slice.
- The current repo lacks a universal object resolver across every canonical artifact; the first slice should not build one speculatively.
- Shared-premise independence is only deterministically checkable where provenance ancestry is explicit.
- The later `paleo-type` learning-integration/claim-calibration repair is current cross-repo candidate evidence, not a Wissensarbeit Requirement or P2 cursor authority.

None of these residuals requires a new top-level owner or blocks a bounded Existing-Owner slice, provided implementation admission keeps them explicit.

## 14. Verification plan

### Deterministic/procedural assurance

Before merge of any later implementation:

- repository contract validation;
- `python tools/work.py audit`;
- material-state continuity boundary;
- systemic reconciliation gate;
- state-freshness/cross-clock check;
- existing full regression suite;
- frozen P2 Fidelity scenarios F1–F11/P1–P3 translated into executable fixtures only for their stable structured invariants;
- at least one frozen positive P1 fixture with a closed universe `U`, complete partition `U=R∪I`, several explicit irrelevant refs, and exact expected execution refs `R`, so full or over-inclusive output fails for that fixture;
- selection/materiality provenance binding check: deterministic validation proves fidelity to the supplied judgement basis, not the correctness of real-world materiality itself;
- derived-state reproduction;
- explicit negative authority/uncertainty/readiness/NONE/purpose/staleness cases;
- compatibility check for existing context behavior or an explicit bounded migration.

### Judgement review kept separate

- Problem Fit;
- semantic fidelity of selected/omitted real context;
- Human usefulness;
- whether design/discovery distinctions are preserved without importing a design engine;
- maintenance burden;
- process overhead, assessed across the bounded execution context **and** its compile-provenance output rather than hiding provenance cost outside the review;
- whether context is actually smaller/useful rather than governance-heavy;
- whether a fresh worker can reconstruct Problem, Scope, Evidence, boundaries and the next permitted step from repository/GitHub.

## 15. Qualitative PASS conditions

Assessment at this preflight:

- real problem evidence: **satisfied**
- P2 separated from broad design/discovery gap: **satisfied**
- existing-owner mapping complete: **satisfied**
- no new truth layer required: **satisfied**
- negative invariants concrete/testable: **satisfied with explicit structured-input boundary**
- judgement vs deterministic checks separated: **satisfied**
- no new priority/planning mechanism: **satisfied**
- Human-feedback fidelity included: **satisfied**
- stale snapshot/invalidation included: **satisfied**
- slice can be small/reversible/existing-owner-based: **satisfied**
- positive bounded capability is falsifiable before implementation: **satisfied for the frozen structured fixture by closed-universe partitioning and exact expected output; no claim is made that arbitrary real-world near-fullness is deterministically decidable, and real-world boundedness/usefulness/material sufficiency remains judgement for result review**
- expected overhead proportional if record is automatically derived: **satisfied, to be measured after implementation**
- fresh-context reconstruction from repo/GitHub: **satisfied by this persisted preflight + existing cursor/authority/evidence package once promoted through its PR**

## 16. Preflight verdict

**REVISED PASS CANDIDATE — bounded implementation admission may be considered only after independent re-review confirms that the NEEDS CORRECTION finding is closed.**

Classification: **judgement backed by repository evidence and deterministic repository-state facts.**

This revised candidate judgement means only that the problem, scope, semantic boundaries, corrected positive boundedness contract, owner fit and smallest credible solution appear sufficiently bounded to ask for a separate implementation admission **if the corrected PR is independently re-reviewed as CONFIRM and then canonically promoted**.

It is **not**:

- implementation start;
- Human acceptance;
- architecture selection beyond the bounded candidate;
- a Requirement change;
- a claim that the future implementation will pass;
- authority to merge or activate P2 implementation.

Until a separate explicit admission is persisted, `implementation_allowed` remains **false**.
