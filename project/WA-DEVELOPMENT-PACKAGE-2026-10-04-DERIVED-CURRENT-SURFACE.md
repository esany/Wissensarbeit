# WA Development Package 2026-10-04 — Derived Current Surface

Status: **development-package candidate / independently reviewed design boundary / no implementation admission / no Requirement or Architecture promotion**

## 1. Purpose

This package translates the independent PR-85 design verdict into an implementation-ready **bounded development specification** for the one design correction that survived review:

> **SHRINK A1 to derived-view-only.**

The package does not reopen A0/A1, does not implement Method Sufficiency, does not implement Generic Adoption, and does not introduce a new state owner.

The implementation target is only a richer rebuildable current-state projection under the existing `BB-DERIVE` / `BB-TRACE` responsibility.

## 2. Frozen evidence and authority boundary

### Reviewed design object

- PR #85 frozen review object: `102cc0804233d00c02f9ed856631f7538a8cc1e9`
- candidate audit: `project/audits/WA-AUDIT-2026-10-04-REQUIREMENTS-RESEARCH-CONCEPT-DELTA.md`
- independent review handoff: `project/WA-HANDOFF-2026-10-04-A0-A1-INDEPENDENT-DESIGN-REVIEW.md`

### Independent design verdict

Independent review evidence:

- PR #85 comment `5982891915`
- `project/reviews/WA-REVIEW-2026-10-04-INDEPENDENT-A0-A1-DESIGN.md`
- review verdict: `SHRINK A1 to derived-view-only`

The independent review rejects as current implementation requirements:

- mandatory Method-Sufficiency disposition;
- Generic-Adoption contract;
- new Building Block;
- new Skill;
- Planner / Orchestrator / Resolver / Bridge;
- graph / ontology runtime;
- Registry / parallel state store;
- automatic synchronization;
- rigid lifecycle stage or pipeline.

### Current canonical baseline at package creation

Resolve fresh before implementation. At package creation the canonical baseline remains:

- `main@b448915cf774c573dbf82cf2e17bcb03c10a9ed8`;
- Planning Source: `github:esany/Wissensarbeit#7`;
- Focus: `github:esany/Wissensarbeit#46`;
- current step: `t5-case-c-trial`;
- no ready next action;
- `follow_up.status = not-derived`;
- `implementation_allowed = false`.

This package creates no implementation authority. `project/execution_state.json` remains authoritative for that boundary.

## 3. Problem being solved

The repository already persists and reconciles material state well. It already has:

- a small execution cursor;
- deterministic cursor/reconciliation freshness checking;
- rebuildable `project/CURRENT_STATE.md`;
- traceability and completion evidence;
- fail-closed authority boundaries.

The confirmed residual failure is narrower:

> The generated current view does not expose enough of the already-persisted current work, authority, reconciliation and current-vs-history boundary for a Human Owner or fresh worker to orient without unnecessary Issue/audit archaeology.

The correction must improve orientation **without creating another current-state clock**.

## 4. Existing owners — unchanged

| Responsibility | Existing owner | Development-package rule |
|---|---|---|
| accepted/canonical project state | `BB-STATE` + canonical files | unchanged |
| planning/priority source | current Planning Source referenced by `project/execution_state.json` | view may link; never replace |
| current work / execution authority | `project/execution_state.json` | authoritative input; view cannot edit or reinterpret it |
| material change impact | `project/reconciliation.json` under `system/reconciliation.json` contract | authoritative input for current reconciliation/dispositions |
| human-readable projection | `BB-DERIVE` / `project/CURRENT_STATE.md` | **implementation target** |
| provenance/explanation | `BB-TRACE` | links and explanations only; no copied truth |
| freshness | `tools/state_freshness.py` + derived-state reproducibility | extend only as needed to bind new projected fields |
| material authority | `system/authority.json` | unchanged |

No new owner is introduced.

## 5. Implementation scope

### In scope

A bounded extension of the existing derived-view path:

1. extend `tools/work.py derive` so `project/CURRENT_STATE.md` exposes the minimum current orientation surface defined below;
2. extend `tools/state_freshness.py` so every newly rendered current-clock field that can go stale is checked against its existing authoritative input;
3. add/update deterministic regression tests;
4. regenerate `project/CURRENT_STATE.md` through the existing derive path;
5. perform the long-running and simple negative-control semantic trials defined in this package;
6. persist completion/review evidence under existing project conventions.

### Explicitly out of scope

- no new JSON/YAML current-state store;
- no manually maintained programme registry;
- no new Planning Source;
- no change to `project/execution_state.json` schema;
- no change to `system/reconciliation.json` or `project/reconciliation.json` schema unless a later design review separately proves it unavoidable;
- no Issue/PR label taxonomy requirement;
- no crawler that infers priority from open Issues or recency;
- no Method-Sufficiency record;
- no Generic-Adoption record;
- no new lifecycle stage;
- no Requirement, Building Block, Authority or Skill promotion;
- no automatic next-work selection;
- no change to Focus / Planning Source / `implementation_allowed`;
- no implementation of #86 or #87;
- no graph/ontology/registry/planner/orchestrator/synchronizer.

If implementation cannot satisfy acceptance without crossing one of these boundaries: **STOP and return to design**.

## 6. Canonical input contract

The richer current surface is derived from **existing inputs only**.

### I1 — execution cursor

`project/execution_state.json`

Allowed projected facts:

- `planning_source`;
- `focus`;
- `current_step.id`;
- ready-next result derived from `current_step.next` using the existing execution semantics;
- dependency status summary;
- `allowed_actions`;
- `implementation_allowed`;
- `follow_up.status`;
- `follow_up.candidate` when explicitly present;
- `follow_up.rule` as an explanatory boundary;
- completion-evidence reference for the current step when present.

### I2 — current reconciliation packet

`project/reconciliation.json`

Allowed projected facts:

- `change_id`;
- `systemically_integrated`;
- `unresolved` entries;
- current `planning_execution_cursor` disposition/binding;
- current `active_work` disposition, objects and rationale;
- current `issues_findings` disposition, objects and rationale;
- the other required reconciliation surfaces only as compact disposition summary when useful for orientation.

### I3 — canonical contracts for labels/explanation only

The generator may use stable contract metadata from existing canonical files when already part of the current derive path, but it must not synthesize new current programme facts from them.

Examples:

- Governing Objective pointer;
- Requirement/Quality counts;
- lifecycle;
- Building Block list;
- Authority boundary explanation.

### I4 — owner references

GitHub/repository owner references already present in I1/I2 may be rendered as links/pointers.

The derived view **must not** discover or classify additional active/candidate work by:

- crawling all open Issues;
- sorting by `updated_at`;
- treating `open` as `current`;
- title keyword inference;
- AI guesswork not bound to an explicit owner/disposition.

If an item is not represented by the authoritative input set, the view must not invent its current status.

## 7. Projection semantics

These are output semantics, not a new project-state ontology.

### 7.1 Current planning and work

Render from I1:

- Planning Source;
- Focus;
- current step;
- deterministic ready-next result;
- follow-up status/candidate;
- implementation permission;
- allowed actions.

Rules:

- `next=[]` or no single ready next action renders **`none / no deterministic next action`**;
- `follow_up.status=not-derived` renders **`not derived`**, never an inferred candidate;
- `follow_up.candidate=null` renders **`none selected/derived`**;
- visibility never implies priority.

### 7.2 Active-work explanation

Render the current `project/reconciliation.json -> surfaces.active_work` disposition, owner objects and rationale.

Rules:

- the reconciliation packet is the source of the explanation;
- the view does not independently rewrite active-work truth;
- if the packet and execution cursor disagree, freshness/assurance fails rather than choosing one.

### 7.3 Material unresolved state

Render exactly the current reconciliation `unresolved` set.

Rules:

- empty means **`no unresolved reconciliation blockers`**;
- it does **not** mean “the project has no open problems”;
- the view must say this distinction explicitly.

### 7.4 Completion / history boundary

The default current surface remains bounded.

Render:

- current-step completion evidence when present;
- count of resolved execution dependencies;
- a pointer that deeper completion/history evidence remains available through existing completion evidence / Git / GitHub owners.

Do **not** dump every resolved dependency or historical Issue into the default view.

A resolved dependency must never be rendered as active merely because it remains in `execution_state.json` for traceability.

### 7.5 Candidate boundary

The view may render a candidate only when I1 explicitly provides one (for example `follow_up.candidate`).

When no candidate is persisted:

> `No successor candidate is selected/derived by the execution cursor.`

The view must not convert the existence of open candidate Issues into current selection.

### 7.6 Supersession/history

The view may call an object `superseded` only when that disposition is explicit in an authoritative input reachable through I1/I2.

No `latest wins`, recency or closed/open inference.

If explicit supersession is absent, the view uses the weaker available status and source link.

### 7.7 Reconciliation/learning delta

The current `change_id` and compact disposition summary may be shown as the latest integrated delta.

This is not a learning registry and does not create a new learning owner.

## 8. Required `CURRENT_STATE.md` information architecture

Exact wording/format is an implementation detail; semantic sections are frozen.

The generated file must expose, near the top and before historical/reference-heavy material:

1. **Current work and authority**
   - Planning Source
   - Focus
   - current step
   - next
   - follow-up
   - implementation allowed

2. **Current reconciliation / active-work effect**
   - current change
   - integrated state
   - unresolved reconciliation blockers
   - active-work disposition + owner links + compact rationale

3. **Current-vs-history boundary**
   - current-step completion evidence when available
   - resolved dependency count
   - explicit note that resolved/history evidence remains on demand and is not active work

4. existing baseline/lifecycle/building-block/canonical-source information may remain after the orientation surface.

5. explicit footer/note:

> This file is a rebuildable derived view. It does not select priority, replace its linked owners, authorize implementation, or prove that unlisted candidate/history objects do not exist.

The file must remain compact. It must not become a programme narrative or append-only history.

## 9. No-second-clock invariants

The implementation fails if any invariant below is violated.

### DV-INV-01 — rebuildable

`CURRENT_STATE.md` is generated from existing authoritative inputs and can be reproduced exactly by the existing derive path.

### DV-INV-02 — no manual current status

No human-authored `active/current/candidate/completed` value exists solely in the derived file.

### DV-INV-03 — source-bound currentness

Every projected current-work/status statement has a direct I1/I2 source.

### DV-INV-04 — no recency semantics

Timestamps, update order and “latest Issue” are not used to establish currentness, relevance or priority.

### DV-INV-05 — no priority inference

Being visible in the current surface does not select work or change Planning Source/Focus.

### DV-INV-06 — fail stale

If a projected execution/reconciliation field changes without re-derivation, the freshness/reproduction checks fail.

### DV-INV-07 — bounded history

Completion/history is summarized and linked, not copied into the current surface.

### DV-INV-08 — explicit absence semantics

`none`, `not-derived` and empty reconciliation blockers retain their exact weaker meanings; they are not converted to “no problems” or “complete”.

## 10. Deterministic freshness contract

`tools/state_freshness.py` currently verifies reconciliation-to-execution bindings and binds `CURRENT_STATE.md` to the reconciliation `change_id`.

The implementation should extend this existing checker only for newly projected current-clock fields.

At minimum, stale detection must cover:

- Planning Source;
- Focus;
- current step;
- ready-next result;
- follow-up status;
- follow-up candidate, including explicit null/none;
- `implementation_allowed`;
- reconciliation `change_id`;
- current unresolved reconciliation blocker count/state;
- current active-work disposition/owner set when rendered.

Preferred implementation principle:

> Compare rendered fields directly with I1/I2; do not add another manifest/store merely to check freshness.

Exact full-file reproduction by `derive` remains the strongest backstop when already supported by the test path.

## 11. Deterministic regression suite

Implementation must add tests for at least the following.

### DV-T01 — current baseline reproduces

Current repository inputs derive the committed `CURRENT_STATE.md` exactly and freshness passes.

### DV-T02 — planning-source staleness

Change fixture `planning_source` without re-deriving -> freshness fails.

### DV-T03 — focus staleness

Change fixture `focus` -> freshness fails.

### DV-T04 — current-step staleness

Change fixture `current_step.id` -> freshness fails.

### DV-T05 — no-next boundary

No single ready next action -> output says no deterministic next action; it must not select one.

### DV-T06 — follow-up not-derived

`follow_up.status=not-derived`, `candidate=null` -> output preserves both boundaries and invents no candidate.

### DV-T07 — candidate present

A fixture with an explicit persisted follow-up candidate renders that candidate and its source only.

### DV-T08 — unresolved is not project completeness

Empty `reconciliation.unresolved` renders no reconciliation blockers plus the explicit non-equivalence to “no project problems”.

### DV-T09 — resolved dependency stays history

A resolved dependency with completion evidence does not appear as active work; history count/pointer remains available.

### DV-T10 — active-work source binding

Change `surfaces.active_work` disposition/object set without re-derivation -> stale/reproduction check fails.

### DV-T11 — no hard-coded project object

Run derive against fixture inputs with different GitHub refs/step IDs; output follows fixture values. The generator must not contain project-specific #7/#46/T5 literals as current truth.

### DV-T12 — boundedness

A fixture with many resolved dependencies does not expand the default current surface linearly with full historical detail; it renders a bounded summary and on-demand pointer.

## 12. Semantic acceptance trials

Deterministic tests cannot prove Human legibility or correct semantic usefulness. Two bounded semantic trials are mandatory before Result Acceptance.

### Trial L — long-running repository case: `Wissensarbeit`

Use the implemented view on a current long-running state equivalent in complexity to this repository.

A fresh reviewer, without reading chronological Issue comments first, must be able to answer from `CURRENT_STATE.md` plus direct owner links only where needed:

1. What is the current Planning Source?
2. What is the current Focus/current step?
3. Is there a deterministic next action?
4. What is the follow-up/selection boundary?
5. Is implementation currently authorized?
6. What material change was last reconciled?
7. Are there unresolved reconciliation blockers?
8. Why is the current active work still active / what just changed?
9. Where is completion/history evidence, without treating it as active work?
10. What does the view **not** claim about unlisted project problems/candidates?

Pass condition:

- answers are correct against the owners;
- no Issue chronology is required for first orientation;
- the reviewer does not infer a priority/candidate that the cursor did not select;
- owner links make deeper verification possible.

### Trial N — simple negative control

Use a minimal fixture/repository state with:

- one focus;
- one current step;
- no ready next action or one explicit ready action;
- zero reconciliation blockers;
- few or zero resolved dependencies;
- no candidate unless explicitly persisted.

Pass condition:

- the same derive path works without adding programme ceremony;
- output remains small;
- no empty taxonomy, fake problem portfolio, candidate registry or additional state artifact is required;
- ordinary simple work remains understandable without extra maintenance.

This trial is specifically an anti-overengineering control.

## 13. Human-legibility acceptance

Human acceptance is judgement-based and separate from deterministic PASS.

The Human Owner should be able to answer, from the current view without chronological archaeology:

- “Woran arbeiten wir gerade?”
- “Warum ist das noch current?”
- “Was ist gerade abgeschlossen/reconciled?”
- “Gibt es einen bereits ausgewählten nächsten Schritt?”
- “Darf implementiert werden?”
- “Wo prüfe ich die zugrunde liegende Evidence?”

The package intentionally does **not** set an arbitrary time/word-count threshold because the review found that threshold unmeasured. The result review must record observed burden and any remaining archaeology explicitly.

## 14. Work breakdown

### WP-DV1 — Projection implementation

Scope:

- modify `tools/work.py derive`;
- regenerate `project/CURRENT_STATE.md`;
- add/update derive regressions.

Exit:

- semantic sections in section 8 are produced from I1/I2 only;
- no new persistent state source.

### WP-DV2 — Freshness and anti-second-clock regressions

Scope:

- extend `tools/state_freshness.py` for newly rendered clock fields;
- add/update `tests/test_state_freshness.py` and directly related tests;
- add bounded fixture(s) only where required for tests.

Exit:

- DV-T01..DV-T12 deterministic obligations pass;
- stale projected status fails closed.

### WP-DV3 — Semantic proof

Scope:

- run Trial L;
- run Trial N;
- perform independent result review against the frozen package and design verdict;
- record Human-legibility judgement separately from deterministic assurance.

Exit:

- both trials pass or findings return to the smallest applicable level;
- no claim stronger than evidence.

The implementation may combine WP-DV1 and WP-DV2 in one reversible PR when technically coherent. WP-DV3 remains evidence/review, not a reason to expand implementation automatically.

## 15. Expected changed-file envelope

The intended implementation should normally be bounded to:

- `tools/work.py`;
- `tools/state_freshness.py`;
- `project/CURRENT_STATE.md` (generated);
- `tests/test_work.py` and/or the existing direct derive tests;
- `tests/test_state_freshness.py`;
- optional bounded test fixture(s);
- one result-evidence/review artifact after execution.

A material need to change any of the following is a **STOP / design return**:

- `project/requirements.json`;
- `system/building_blocks.json`;
- `system/authority.json`;
- `system/lifecycle.json`;
- `project/execution_state.json` schema or meaning;
- `system/reconciliation.json` contract;
- a new current-state registry/store;
- GitHub issue taxonomy as a required runtime dependency.

## 16. Migration and rollout

There is no canonical-state migration.

Implementation migration is:

1. update derivation logic;
2. update freshness/regression logic;
3. regenerate the derived `CURRENT_STATE.md`;
4. run full repository assurance;
5. run semantic trials;
6. independent result review;
7. only after accepted proof, promote/merge under existing Authority.

Existing Issue/PR history remains untouched.

No backfill of historical objects is required.

## 17. Rollback

Rollback must be trivial and Git-native:

- revert the implementation commit(s);
- regenerate `CURRENT_STATE.md` with the prior derive implementation;
- run existing assurance/freshness checks.

Because no canonical source/schema is migrated, rollback does not require state conversion.

If rollback would require reconstructing a new store or manually restoring status metadata, the implementation violated this package.

## 18. Failure / STOP conditions

STOP implementation and return to design if any of these occurs:

1. required orientation information cannot be projected from existing authoritative I1/I2 sources without inventing a manually maintained status source;
2. a new Registry, current-state store, planner or synchronization mechanism appears necessary;
3. the implementation needs to infer currentness from recency/open status/title keywords;
4. the view needs to change Planning Source, Focus, priority or implementation authority;
5. Method Sufficiency or Generic Adoption is pulled into the implementation to make the view work;
6. a Requirement, Building Block, lifecycle or Authority change becomes necessary;
7. deterministic PASS requires masking a semantic ambiguity;
8. Trial L still requires chronological Issue archaeology for first orientation;
9. Trial N shows disproportionate process/meta-work for a simple project;
10. the view can remain “fresh” while one of its rendered authoritative source fields has changed;
11. the output suggests that `unresolved=[]` means “no open project problems”;
12. any candidate/priority is inferred rather than explicitly persisted by an owner.

## 19. Assurance plan

### Deterministic

Run at least the repository's existing full assurance path, including:

- contract validation;
- audit;
- unit/regression suite;
- derive/reproduction;
- state freshness;
- reconciliation gate;
- any existing derived-state checks.

Green CI means only deterministic/formal conformance.

### Semantic

Independent result review verifies:

- faithful implementation of this package;
- no second truth/clock;
- no priority inference;
- current/history semantics are not overclaimed;
- Trial L correctness;
- Trial N proportionality;
- owner-link/provenance usability;
- Human-legibility evidence.

### Human

Human acceptance is limited to whether the resulting surface actually reduces orientation/archaeology burden while preserving understandable authority and evidence links.

## 20. Result-disposition matrix

| Result | Required response |
|---|---|
| deterministic tests fail | correct implementation; no semantic claim |
| deterministic pass, Trial L fail | return to derived-view design; do not add structure automatically |
| Trial N fail | shrink implementation |
| semantic review finds copied/parallel truth | reject/correct implementation |
| view works but Human burden unchanged | no Result Acceptance; reassess value |
| all deterministic + semantic + Human acceptance pass | eligible for existing promotion/merge process; no broader A1 claims |

## 21. Deferred questions — explicitly outside this package

These remain separate evidence questions:

### Method Sufficiency / #86

Not an implementation requirement. Future comparison may test existing-owner composition vs optional compact explanation using trivial fix, uncertainty, re-entry and `no change` cases.

### Generic/local adoption / P-D

Requirement-clarification candidate only. Requires a materially different consumer-project trial before stronger claims.

### Active Knowledge Lifecycle / #87

This package may provide evidence relevant to #87, but it does not promote #87 or implement a generic Active-Knowledge capability. If the derived-view correction is sufficient, #87 may shrink/merge/reject accordingly.

## 22. Development-readiness assessment

### Design readiness

**PASS for the narrowed derived-view design.** The independent design review has already rejected the broader A1 claims and confirmed the smallest surviving correction.

### Development-package completeness

This package freezes:

- exact existing owners;
- input boundary;
- projection semantics;
- no-second-clock invariants;
- freshness obligations;
- implementation envelope;
- deterministic tests;
- semantic long-running and negative-control trials;
- rollback;
- STOP conditions;
- explicit deferred questions.

### Remaining gate

Because this package was authored after the independent design review, a fresh **package-conformance review** should verify that it has not silently reintroduced rejected A1 semantics or a second clock.

Therefore current status after this package is:

> **DEVELOPMENT PACKAGE PREPARED — DEV-READY CANDIDATE — PACKAGE CONFORMANCE REVIEW NEXT — NO IMPLEMENTATION ADMISSION**

A package-conformance `CONFIRM` may establish `DEV READY` for this bounded derived-view implementation. It still does not itself set `project/execution_state.json -> implementation_allowed=true`; implementation admission remains a separate Authority transition.

## 23. Package-conformance review checklist

A fresh reviewer should answer only:

1. Does every projected current claim derive from I1/I2 or an already-existing canonical contract?
2. Does the package preserve `BB-DERIVE` as a projection rather than create a new owner/store?
3. Are Method Sufficiency, Generic Adoption and broader A1 claims truly excluded?
4. Are `none`, `not-derived`, empty blockers and resolved history kept semantically weak?
5. Can stale rendered fields fail closed without another manifest/store?
6. Does the simple negative control prevent overengineering?
7. Is the changed-file envelope proportional?
8. Are rollback and STOP conditions sufficient?
9. Is any material design choice still left for the implementer to invent?
10. If `CONFIRM`, is the package sufficient to call the bounded derived-view work `DEV READY` while keeping implementation authority separate?

STOP after this review. Do not implement in the review run.
