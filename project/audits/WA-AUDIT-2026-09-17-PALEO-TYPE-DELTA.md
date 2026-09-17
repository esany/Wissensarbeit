# WA-AUDIT-2026-09-17 — paleo-type current-state delta and Wissensarbeit operational consequences

Status: `audit evidence / Generic-Fit + plan reconciliation / no P2 implementation authority`

## Purpose and authority boundary

This dated delta extends the 2026-09-13 and 2026-09-14 snapshots without rewriting them. It records material movement in `esany/paleo-type` through current `main` and derives the smallest justified changes to the existing `Wissensarbeit` planning/reconciliation structures.

Human-Owner instruction on 2026-09-17 explicitly authorized repository persistence and operationalization of the audit consequences. That authority covers the plan/reconciliation/assurance changes in PR #33. It does **not** authorize P2 implementation, merge of PR #33, a new Requirement family, a fifteenth Building Block, a new state store, a roadmap engine or a research-framing architecture.

`CI/formal validation != Domain Truth / Owner Acceptance`.

## Fresh checkpoints

### Wissensarbeit

- `main`: `a43e4b8fca96757191167bf54c980fcac3e361a2`
- current review branch/PR: `audit/paleo-type-2026-09-13` / PR #33
- persisted focus: Issue #7
- P1 harvest and independent restart: complete
- P2 implementation: not authorized

### paleo-type

- current `main`: `81a9be5ac37c47830c2bb1a53025197a18096c17`
- PR #224: open, not part of current `main`; treated only as open falsification evidence

Since the prior `3df61570…` checkpoint, the repository has materially advanced through:

- #203 Requirements resolution: `existing-owner refinement warranted` for plural evidence-grounded pre-priority direction formation;
- #204 Human-Owner `REFINE → ACCEPT` of a narrow existing-METHOD refinement;
- #205 explicit post-hoc reconciliation of a process-order defect: Concept/loss/result-review functions occurred after the METHOD write, and history was not rewritten to pretend ideal order;
- #208 programme-continuity analysis: local arc completion/restartability/Requirement presence do not establish programme completion, programme-cursor restartability or operative efficacy;
- #207 whole-map programme synthesis;
- #200 Requirements resolution for programme/phase/result-transition continuity;
- #211 smallest-response Concept: thin refinement of existing maintenance/workflow owners, not a registry/state machine;
- #212 bounded implementation + loss/regression review PASS;
- #206 / programme completion review: current research-system programme STOP, deferred risks remain deferred rather than becoming current work;
- #223 project-local L026–L029 learning capture;
- open PR #224: smallest falsifiable test of `active_scope = unset` as non-generative state.

## Executive finding

The current `paleo-type` evidence confirms the direction of P2 but changes the immediate sequencing and strengthens several invariants.

The most important new cross-project result is:

> A locally valid state can remain internally consistent while the programme/execution cursor, derived current-state view and later evidence evolve on different clocks. Material phase/result transitions therefore require an explicit disposition against the existing planning/execution owner; silence is not reconciliation.

`paleo-type` explicitly used `Wissensarbeit` as counterevidence against copying a separate execution-state/reconciliation architecture: multiple legitimate state clocks can drift even when each representation is individually well-formed.

Therefore P2 must not add another truth store on top of an unreconciled baseline.

## 1. Programme-transition continuity is Generic-Fit evidence

`paleo-type` #208 established:

```text
local arc completion != programme completion
local restartability != programme-cursor restartability
Requirement present != demonstrated operative capability
local Result Review PASS != whole-programme adequacy
```

The subsequent #200/#211/#212 path selected and validated the smallest response: an existing semantic owner for material programme/phase/result-transition reconciliation plus a thin execution hook; no registry, state machine, dashboard, new Requirement family or standing bureaucracy.

### Wissensarbeit consequence

The existing reconciliation contract already says material changes require whole-project reconciliation and that unchanged is valid while silence is not. The missing operational surface is the planning/execution cursor itself.

This PR therefore refines the **existing reconciliation contract** by adding `planning_execution_cursor` as a required impact surface. It does not create a second planning model.

For a material transition the packet must now explicitly say whether the planning/execution cursor is `unchanged`, `refined`, `stale`, `needs-decision`, etc., with rationale. A local PASS/closeout cannot silently imply that a later roadmap step is current.

## 2. Current-state multi-clock drift must be closed before P2

Current `Wissensarbeit/main` has:

- `project/execution_state.json`: post-P1 cursor with P2 preflight as the ready next step;
- `project/reconciliation.json`: older `evals/round-2-robustness` material clock;
- `project/CURRENT_STATE.md`: derived from that older reconciliation clock;
- PR #33: newer Generic-Fit and P2-plan evidence.

Each surface is reconstructable, but they do not describe one jointly reconciled material transition.

### Plan change

P2 Fidelity Manifest preflight is **not** the immediate next executable step anymore.

The next step becomes:

`p2-post-pr33-baseline-reconciliation`

Its purpose is narrow:

1. PR #33 must first be reviewed and merged; this audit branch itself is not `main` authority.
2. On the resulting actual `main`, reconcile execution cursor, current reconciliation packet and derived current-state surface as one baseline.
3. Persist completion evidence for that baseline transition.
4. Only then make `p2-fidelity-manifest-preflight` the next ready step.

This is a P2 prerequisite/substep, not a new roadmap phase.

## 3. No new state store; fidelity records are compile provenance

The earlier Fidelity Manifest hypothesis remains useful only if it does not become another current-state owner.

P2 should therefore prefer references to existing canonical owners plus compile-time provenance:

- exact input/snapshot identity;
- bounded work/question and authority;
- included references;
- deliberately omitted references with claim-specific rationale;
- unresolved/deferred alternatives;
- uncertainty;
- source/claim role and authority boundary;
- evidence/readiness state without task-authority promotion;
- refresh/invalidation condition;
- already-established completion/evidence-ceiling/blocker state.

A fidelity record explains what was compiled and why. It must not independently own Project truth, priority or current programme state.

## 4. Absence of authority/state must be non-generative

The newest `paleo-type` pilot finding is that `active_scope = unset` and `NEXT ACTION = NONE` can be semantically correct yet still tempt a capable context to fill the vacuum from the richest available evidence.

Open PR #224 freezes this regression before testing. It is not current `paleo-type/main` truth, but it is strong candidate evidence for P2 assurance.

### New P2 negative invariant

```text
known current scope/next action = none
+ rich available unresolved work
→ generated replacement priority/scope
= FAIL
```

Absence of current authority is a state to preserve, not a request to synthesize authority.

## 5. Missing purpose must not be replaced by richest context

`paleo-type` L026 distinguishes Project identity/boundary from the richer purpose information needed for broad direction formation. A context can know which Project exists and still lack enough owner-grounded purpose to rank the scientifically relevant next-direction space.

### New P2 negative invariant

```text
operation requires purpose/scope discriminator
+ canonical owner does not provide it
+ compiler substitutes richest/easiest/current fixture
= FAIL
```

The valid output is an explicit unresolved authority/purpose gap. This is a consequence of existing authority/context semantics, not a new scientific-priority engine.

## 6. Resource state and support recovery remain bounded

The earlier `resource unavailable → blocker → STOP/roadmap` failure remains a core P2 regression.

The newer L028 finding sharpens the recovery path:

```text
bounded execution/support failure
→ smallest authorized repair
→ return to the same still-valid scholarly/work cursor
```

Support success must not create a new support programme or replacement objective. If the original cursor is no longer authorized, surface that authority/state fact rather than manufacturing another one.

## 7. Positive capability must be measured separately from safety

L029 identifies a pilot-quality risk: a system may improve epistemic reliability, auditability and restartability while reducing timely substantive knowledge-work progress.

This is not sufficient evidence for a new P2 requirement or benchmark. It is a later assurance/learning candidate:

- scientific/source-understanding capability;
- epistemic reliability;
- human auditability/restartability;
- research overhead/recovery cost.

Do not interpret process maturity alone as overall Wissensarbeit success.

## Refined P2 preflight candidate failure classes

After the post-PR-#33 baseline reconciliation is complete, the P2 preflight should test at least:

1. silent producer-known material omission → FAIL;
2. material omission without explicit rationale/materiality disposition → FAIL;
3. justified claim-specific omission with preserved reference/reactivation condition → MAY PASS;
4. unresolved/alternative state silently resolved → FAIL;
5. uncertainty strengthened/lost → FAIL;
6. output authority stronger than source/owner basis → FAIL;
7. resource/readiness state promoted to task/roadmap authority → FAIL;
8. fresh context treats a shared derived premise as independent evidence → FAIL;
9. older snapshot presented as current after material transition → FAIL;
10. `NONE`/unset scope or next action generates replacement priority → FAIL;
11. missing purpose/scope discriminator is substituted from richest available context → FAIL;
12. bounded support repair fails to return to the still-authorized cursor and instead creates new meta-work → FAIL.

Existing P1/Foundation/Restart/Authority regressions must remain green.

## Reconciliation disposition for Wissensarbeit

### requirements

**confirmed / no new Requirement family.** Existing continuity, authority, evidence and systemic-integration requirements cover the higher-order need.

### issues/findings

**refined.** Issue #7 remains the planning source, but the immediate sequence changes: PR #33 completion + post-merge baseline reconciliation precede P2 Fidelity Manifest preflight.

### risks

**confirmed/refined.** Existing R-004/R-005/R-008/R-009 and R-003/R-007 cover semantic/authority/freshness/over-modeling risks; no new risk family is required.

### decisions/concepts

**unchanged at architecture level.** No Research-Framing layer, Candidate-Question schema, scoring model, programme state machine, agent topology or new state store is admitted.

### derived views

**refined.** `CURRENT_STATE.md` must expose both the current reconciliation change and the execution cursor so a fresh context cannot mistake one clock for the whole current state.

### planning/execution cursor

**refined.** Immediate next step becomes `p2-post-pr33-baseline-reconciliation`; P2 Fidelity Manifest preflight is a follow-up only after that step is completed on actual post-merge `main`.

### active work

**refined.** PR #33 is the current bounded evidence/plan package. P2 implementation remains unauthorized.

## Explicit non-promotions

This delta does not create:

- a new Requirement family;
- a fifteenth Building Block;
- a Research-Framing layer;
- a Candidate-Question object/schema;
- scoring/ranking;
- a generic purpose inference engine;
- a new programme registry/state machine/dashboard;
- a third current-state store;
- permanent agent/competence topology;
- P2 implementation authority;
- P3/P4/P5 activation.

## Operational next sequence

```text
PR #33 review / merge
→ p2-post-pr33-baseline-reconciliation on actual main
   - execution_state
   - project/reconciliation
   - CURRENT_STATE
   - exact merged audit evidence
→ completion evidence persisted
→ only then expose p2-fidelity-manifest-preflight as ready
→ valid P2 preflight PASS required
→ separate P2 implementation admission
→ implementation
→ systemic transition reconciliation
→ only then select any later roadmap slice
```

This sequence deliberately blocks roadmap momentum and prevents a fidelity layer from being built on an unreconciled baseline.
