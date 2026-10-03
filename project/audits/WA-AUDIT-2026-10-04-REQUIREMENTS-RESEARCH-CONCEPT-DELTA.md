# WA-AUDIT-2026-10-04 — Requirements / Research / Concept Delta

Status: **candidate/design evidence; A1 supported as existing-owner and derived-view sharpening only; independent design review required; no implementation admission**

## 1. Scope and authority

This audit performs the bounded comparison requested after the systemic design baseline:

- **A0 — Existing mechanisms sufficient**: existing owners, contracts and composition are sufficient when correctly applied; no additional contract sharpening or derived-view semantics is needed.
- **A1 — Minimal sharpening**: no new structural capability is needed, but a small sharpening of existing contracts and/or derived views is required to make current state reliably reconstructable, human-legible and restartable in the intended working mode.

This is candidate/design evidence. It does not change the Governing Objective, Requirements, priority, execution cursor, Authority, Building Blocks, lifecycle, Generic-Fit status or implementation permission.

The repository and current GitHub state remain authoritative. This audit is not a replacement truth source and does not select work after the current cursor.

## 2. Fresh baseline

Repository: `esany/Wissensarbeit`

- fresh `main`: `b448915cf774c573dbf82cf2e17bcb03c10a9ed8` (`Merge PR #84: close T5 Case C evaluation cursor`);
- current `project/execution_state.json`: focus `github:esany/Wissensarbeit#46`, planning source `#7`, current step `t5-case-c-trial`, no next action, `implementation_allowed=false`;
- current `project/reconciliation.json`: T5 Case-C evaluation closure, systemically integrated, no unresolved blockers;
- `project/CURRENT_STATE.md`: generated derived view bound to that reconciliation;
- PR #85: open, not merged, non-draft, head `07e099720673da1b278f3da4510d9f122e0c27c3`, base `main@b448915...`;
- PR #85 persists the systemic baseline and DEV-ready handoff as candidate/recovery evidence only;
- Issues #52, #53, #55, #86 and #87 remain open candidates; #76 is closed historical bounded Track-B work; none grants implementation or new-priority authority.

The continuity artifact named by the restart request, `WA-AUDIT-2026-10-04-REQUIREMENTS-RESEARCH-CONCEPT-DELTA.md`, was not present in the local repository, PR-85 branch, or fetched remote refs at restart. It is therefore not treated as evidence. This file is the fresh replacement evidence packet, based on the repository, the current GitHub owner state and the persisted PR-85 baseline.

The required existing-owner countercheck was performed against:

- `system/lifecycle.json` and `system/building_blocks.json`;
- `system/authority.json`, `system/material_state.json` and `system/reconciliation.json`;
- `project/requirements.json`, `project/risks.json`, `project/execution_state.json`, `project/reconciliation.json` and `project/CURRENT_STATE.md`;
- `tools/reconcile.py`, `tools/state_freshness.py`, `tools/work.py` and the repository tests;
- PR-85 baseline and handoff;
- #52, #53, #55, #76, #86 and #87.

## 3. Evidence basis

The comparison uses real repository history and current owners, not invented project scenarios.

1. **Longitudinal design-method evidence.** `WA-AUDIT-2026-09-19-DESIGN-PROJECT-DEVELOPMENT-METHOD-DELTA.md` records a real asymmetry: governance, traceability, reconciliation and assurance were stronger than problem discovery, design-space exploration and iterative development method. It explicitly maps the gap to existing Building Blocks and rejects a new fifteenth Building Block.
2. **Systemic baseline evidence.** PR #85 records repeated reconstruction of the programme/problem landscape after locally well-controlled work, and the asymmetry `Externalization Lifecycle >> Active-Knowledge Lifecycle`. It also records that implementation-shaped work can be formed before problem/design sufficiency is established.
3. **Repeated closure history.** The planning-integrity, Track-B, owner-burden and T5 closures on current `main` show strong local execution, reconciliation and fail-closed cursor behavior. Their deliberate `next = none` / `not-derived` boundaries preserve Human priority authority, but they also leave programme navigation to a later fresh reconstruction.
4. **Current derived view.** `CURRENT_STATE.md` is reproducible and fresh, but contains counts, lifecycle, canonical sources, reconciliation status and one operational proof. It does not expose a bounded current problem surface with current/candidate/historical disposition.
5. **Formal executable evidence.** The current `main` test suite runs 107 tests successfully when discovered under `tests/`. It protects state freshness, reconciliation completeness, provenance, authority boundaries, restart behavior and cursor semantics. It does not test human-legible current-vs-history discrimination or a proportionate method-sufficiency judgement.
6. **Generic-anchor question.** Git history, diffs, compare and selective commit application provide artifact-level selection and reversibility. They do not by themselves establish whether a generic improvement fits a consuming project's local purpose, requirements, decisions, risks or acceptance conditions. Existing reconciliation, requirements, decision and assurance owners can carry that judgement, but the adoption boundary is not explicit.

## 4. Eval Contract (defined before case evaluation)

### 4.1 Common procedure

For each case, evaluate the same evidence under:

- **A0**: use existing files, owners, contracts, Git/GitHub history and current derived views without adding semantics;
- **A1**: apply only the candidate minimal sharpenings described in section 8, while keeping the same canonical owners and storage.

The comparison is successful only if A1 fixes an observed material failure and does not merely produce a nicer presentation. A0 does not pass merely because the required information exists somewhere in History; it must be reliably reconstructable in the intended bounded working mode.

### 4.2 Pass criteria

| Criterion | Pass condition |
|---|---|
| Current-state reconstructability | A fresh worker can identify current focus, unresolved material problems, completed/superseded work, relevant candidates and the next authority boundary from bounded current sources. |
| Restartability | The result is reconstructable without the prior chat; historical detail remains addressable but is not required for the first correct orientation. |
| Human legibility | A non-technical Owner can answer “where are we and what remains materially open?” without Issue archaeology. |
| Current-vs-history discrimination | Current, candidate/relevant, unresolved, completed/superseded and evidence/history are not silently collapsed. |
| Method/capability sufficiency | For material work, the record shows what is understood, what remains uncertain, which capability/method work is needed or intentionally omitted, and whether implementation is admissible. |
| Project-specific fit | Generic improvements are evaluated against the local objective, needs, requirements, decisions, risks and state before adoption. |
| Authority clarity | Derived views and method judgements do not select priority, establish meaning, accept requirements or authorize implementation. |
| Learning/reconciliation closure | Results have an explicit impact/no-change disposition across required reconciliation surfaces. |
| Traceability | Current claims point to canonical owners, Git/GitHub evidence and the applicable authority; no copied status becomes a second owner. |
| No duplicate truth | A view is rebuildable and references canonical state; it is not a manually synchronized registry. |
| Proportional complexity | Clear local work can remain small; only material systemic or adoption decisions require the extra disposition. |
| Meta-work burden | The sharpening reduces archaeology and Human method-courier burden rather than creating a new planning ceremony. |

### 4.3 Failure conditions

A0 fails when any of these occurs in a material case:

- current status can only be reconstructed by reading chronological Issue/audit history;
- a completed or superseded item remains indistinguishable from active work;
- implementation-shaped work proceeds without an explicit problem/uncertainty/capability sufficiency judgement;
- generic artifact selection is mistaken for project-specific adoption fit;
- a view is current only because a human manually synchronized a second clock;
- a fresh context can repeat a plausible summary but cannot identify the evidence and authority boundary supporting it.

A1 fails if it introduces a planner, mandatory linear stages, new authority, a new store, a graph/ontology/registry, automatic synchronization, or more Human sequencing work than it removes.

## 5. Real bounded cases and observations

### Case C1 — Current programme/problem state after long development

**Evidence:** PR-85 baseline, current `main`, `project/execution_state.json`, `project/reconciliation.json`, `CURRENT_STATE.md`, and current issue/PR statuses.

**A0 result:** local execution state is reconstructable and formally fresh. The remaining problem portfolio, current-vs-historical boundary and unresolved design questions are not present in the derived current view. A worker must read PR-85 and several owner histories to build the active surface. This is a material human-legibility and current/history failure, not a cosmetic preference.

**A1 result:** a rebuildable current-surface view can expose the bounded active problem/work surface and references to candidate/history evidence without becoming a planning owner. The observed failure is addressed with no new capability.

### Case C2 — Fresh restart without the previous chat

**Evidence:** the PR-85 handoff, canonical state files, current cursor and current GitHub owner state.

**A0 result:** restartability is substantially supported. The handoff can answer the baseline questions, and the current cursor is protected by executable freshness tests. A0 passes the narrow restart criterion.

**Residual A1 value:** the restart packet still requires a long handoff plus manual synthesis to make the active problem surface human-legible. A1 is therefore a reduction of restart reconstruction burden, not a claim that A0 lacks provenance or restart evidence.

### Case C3 — Determine relevant, open, completed and overholt material

**Evidence:** current T5 closure, prior owner-burden/Track-B/planning-integrity closures, Issue #11 completion evidence and the current `follow_up = not-derived` boundary.

**A0 result:** each local transition has an owner, Git provenance and reconciliation disposition. But “historically complete”, “currently active”, “candidate but not prioritized” and “unresolved systemic problem” are not projected together. The Human must perform the classification across owners. A0 fails current-vs-history discrimination.

**A1 result:** the derived current surface can reference the authoritative status of each class and preserve the historical pointer. It does not infer priority from relevance.

### Case C4 — Select the needed analysis/research/design/assurance work

**Evidence:** the 2026-09-19 method audit, PR-85 P-B, #86's candidate failure classes, `BB-COMPETENCE`, `BB-RESEARCH`, `BB-REQUIREMENTS`, `BB-DESIGN`, `BB-ASSURE`, `BB-LEARN` and the lifecycle transitions.

**A0 result:** the capabilities exist and may be composed, but current contracts do not require a compact material judgement that binds problem/evidence, remaining uncertainty, required/omitted capability work, re-entry conditions and implementation sufficiency. The audit sequence documents that work could become solution-shaped before that judgement. This is observed methodological friction, not a request for a fixed pipeline.

**A1 result:** an existing-owner method-sufficiency disposition makes the missing judgement explicit while allowing proportional omission and re-entry. It does not choose a priority or implement a planner.

### Case C5 — Return new evidence/learning to current state

**Evidence:** current `system/reconciliation.json`, `project/reconciliation.json`, `BB-INTEGRATE`, `BB-LEARN`, and the T5/owner-burden closure history.

**A0 result:** material change reconciliation is strong and passes deterministically; explicit `unchanged` is supported. A0 passes local learning/reconciliation closure.

**Residual A1 value:** reconciliation closes a change but does not by itself shrink or re-project the active programme/problem surface. A1 connects the existing reconciliation outcome to the derived current surface without copying its truth.

### Case C6 — Generic tooling anchor evolves; project decides whether to adopt

**Evidence:** `system/architecture_fitness.json` (avoid/reuse/configure/integrate/thin custom layer/build custom), `BB-INTEGRATE`, `BB-REQUIREMENTS`, `BB-DESIGN`, Authority, Git history/diff/compare/cherry-pick semantics, and the generic-pilot learning rule that case evidence must not silently promote framework truth.

**A0 result:** Git already supports selective artifact adoption, reversibility and review. Existing project owners can assess fit if deliberately invoked. Git alone does not express the semantic adoption question: which local need/requirement/decision is served, what must be adapted, what is rejected, and what evidence establishes local acceptance. A0 therefore covers mechanics but leaves an explicit semantic boundary implicit.

**A1 result:** sharpen the existing integration/reconciliation decision to record generic source, local fit, affected local owners, adopt/adapt/reject disposition, and local evidence/acceptance. No automatic sync, package/update infrastructure or product-line platform is required. Because this is not yet exercised by a repeated cross-project upgrade trial, P-D remains a clarification/gap candidate rather than a promoted generic requirement.

## 6. Decision

### `A1 SUPPORTED`

The smallest supported explanation is:

> Existing mechanisms are sufficient for provenance, restart foundations, local authority protection, deterministic freshness and material reconciliation. They are not sufficient in the intended working mode for a bounded, human-legible current problem surface or for an explicit, proportionate judgement of remaining method/capability sufficiency before solution commitment. A small sharpening of existing owners and derived views is required; no new structural capability is supported.

A0 is rejected because it passes formal and local checks while failing the usability question the Eval Contract makes material: the Human/worker must be able to use current state without Issue archaeology, and must be able to distinguish missing epistemic work from already-sufficient design. “The information exists somewhere” is not enough.

A1 is bounded by observed evidence from the 2026-09-19 audit, PR-85's longitudinal synthesis and repeated closure/reconstruction behavior. It is not justified by presentation preference alone.

## 7. P-D disposition

Human primary intention:

> `Wissensarbeit` is the generic tooling anchor for the Human Owner's projects. Generic improvements should be adoptable by existing projects, but must be checked and adapted against each project's local purpose, needs, requirements, decisions and state.

Findings:

- Git history, diff/compare and selective change application already provide provenance, reversibility and artifact-level choice.
- Requirements, Decisions, Context, Architecture Fitness, Integration, Assurance and Reconciliation already provide the places where project-specific meaning and acceptance can be judged.
- None of those mechanics alone states the generic-anchor/project-truth boundary or requires an explicit local fit/adaptation/acceptance disposition.
- There is no evidence here for automatic synchronization, a registry, package infrastructure, updater or product-line platform.

Disposition: **Requirement-clarification / design-gap candidate; existing-owner sharpening only.** It is not a new requirement, priority, Building Block or capability promotion. A separate materially different consumer-project adoption trial is required before claiming repeated Generic Fit.

## 8. Frozen Design Candidate (subject to independent review)

### 8.1 Existing owners and boundaries

- `BB-STATE` remains canonical ownership of accepted project state.
- `BB-INTEGRATE` remains the owner of impact interpretation, disposition and systemic integration.
- `BB-COMPETENCE`, `BB-RESEARCH`, `BB-REQUIREMENTS`, `BB-DESIGN`, `BB-ASSURE` and `BB-LEARN` remain distinct capabilities; none becomes a planner or mandatory stage.
- `BB-DERIVE`/`BB-TRACE` remain owners of rebuildable human-readable projections and provenance.
- `project/execution_state.json` and Planning Owner #7 remain the current cursor/priority boundary until a separately authorized change.
- `system/authority.json` remains the authority contract. Method selection and view derivation do not grant meaning, priority, acceptance or implementation authority.

### 8.2 Minimal contract sharpening

For material systemic work, the existing-owner composition should make one bounded **method-sufficiency disposition** explicit:

1. problem/need/evidence currently bound;
2. material uncertainty and competing interpretations;
3. required capability/method work before solution commitment;
4. capability/method work intentionally omitted and why proportionality permits omission;
5. re-entry trigger if new evidence changes the problem or design basis;
6. current design/implementation admissibility and applicable Human gate;
7. explicit `no change` outcome where existing mechanisms already suffice.

This is a judgement record/derived explanation under existing owners, not a new canonical store, lifecycle stage, planner, resolver or work scheduler. Small local changes may use a compact form or no additional packet when the disposition is genuinely obvious and non-material.

For generic-anchor adoption, the same existing integration/reconciliation boundary should make explicit:

1. generic source/change reference;
2. local project need and affected requirements/decisions/risks;
3. adopt, adapt, defer or reject disposition;
4. project-specific adaptation and authority boundary;
5. local evidence/acceptance and rollback/reversibility.

### 8.3 Derived views

`BB-DERIVE` should produce a bounded current surface from canonical sources, including:

- current cursor and active work;
- unresolved material problems and decisions;
- candidates relevant but not prioritized;
- completed/superseded items with evidence pointers;
- the current reconciliation/learning delta;
- explicit “not selected / no next action” boundaries.

The view must reference owners rather than copy their status as a second truth. Currentness must be evidence-bound, not recency-only. History remains addressable. No priority is inferred from visibility.

### 8.4 Acceptance and failure conditions

The design is acceptable only if an independent review and later bounded trials show:

- a fresh worker can answer the current-state questions without chronological archaeology;
- a material systemic case shows why a method/capability was required or omitted;
- a clear local fix remains small;
- a new result can re-enter analysis/requirements/design when required;
- a generic improvement can be selectively adopted and locally adapted without automatic synchronization;
- the current surface is reproducibly derived and does not become a second clock;
- Human meaning, priority, trade-offs and acceptance remain explicit.

Failure is declared if the design becomes a mandatory phase pipeline, increases Human method-courier work, hides unresolved conflicts, treats a view as canonical, treats generic source similarity as local fit, or claims DEV READY while an independent design review is absent.

### 8.5 Migration and explicit exclusions

Migration, if later authorized, starts by deriving the view from existing `main`, GitHub owners, reconciliation and execution state. It does not delete or rewrite History, close Issues merely to make the view smaller, or create a new canonical registry. Existing completed evidence remains addressable.

Explicitly excluded: implementation now; Requirement promotion; new Building Block; Bridge Skill; planner; orchestrator; graph/ontology infrastructure; registry; package/updater/product-line platform; automatic cross-project synchronization; new lifecycle stage; new priority; merge authorization.

## 9. DEV-READY gate

Result: **DESIGN REVIEW READY — NOT YET DEV READY**.

The concept is bounded enough for independent design review, but it is not ready for implementation because:

- the contract sharpening has not yet been independently reviewed;
- the current-surface semantics need falsification against a simple repository where ordinary Git/Issue closure may already suffice;
- P-D needs a real cross-project generic-anchor adoption case;
- no implementation admission is present, and `implementation_allowed=false` remains unchanged.

## 10. Independent review handoff

The reviewer must work from current repository/GitHub state and this evidence packet, but must not inherit its conclusion.

Review questions:

1. Are the claimed A0 failures real failures of the intended working mode, rather than a desire for a nicer summary?
2. Does the existing-owner countercheck accurately show what `BB-STATE`, `BB-CONTEXT`, `BB-INTEGRATE`, `BB-DERIVE`, `BB-TRACE`, `BB-LEARN`, Reconciliation and current Git/GitHub already provide?
3. Can A0 be made to pass by applying existing contracts correctly, without the proposed sharpening? If yes, identify the smallest counterexample and reject/shrink A1.
4. Does the method-sufficiency disposition preserve proportionality, `no change`, uncertainty, re-entry and Human authority without becoming a planner or stage gate?
5. Does the derived current surface avoid a second truth clock and preserve current-vs-history, supersession, unresolved conflict and provenance?
6. Does the generic-anchor disposition preserve local project autonomy and avoid automatic synchronization, while still making adoption/adaptation decision-ready?
7. Are the failure conditions falsifiable with real cases, including one simple repository and one materially different consumer project?
8. Is the migration path implementable without architecture invention or destructive history changes?

Independent verdict options:

- `CONFIRM A1 / existing-owner sharpening only`;
- `SHRINK A1 to derived-view-only`;
- `REJECT A1 / A0 SUPPORTED`;
- `A0/A1 NOT YET DISTINGUISHABLE`;
- `MATERIAL DESIGN CORRECTION REQUIRED`.

The reviewer must return the evidence basis, case outcomes, rejected alternatives, and any corrected design before any development package or implementation admission is considered.

