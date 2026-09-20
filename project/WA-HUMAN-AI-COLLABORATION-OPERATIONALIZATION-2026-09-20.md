# WA-HUMAN-AI-COLLABORATION-OPERATIONALIZATION-2026-09-20

Status: **review correction applied / focused re-review pending / no roadmap promotion / no implementation admission**

This document operationalizes the material Human–AI collaboration findings captured in:

- `project/audits/WA-AUDIT-2026-09-20-HUMAN-AI-OPERATIONAL-COLLABORATION-DELTA.md`

It does **not** implement the seven capabilities. It defines how they remain complete, peer-level, restartable and activatable later without silently becoming current priority, Requirements, architecture or implementation authority.

The machine-readable companion is:

- `project/WA-HUMAN-AI-COLLABORATION-CANDIDATE-SNAPSHOT-2026-09-20.json`

That JSON is an **immutable evidence/planning snapshot**, not a mutable registry or current-state clock.

## Independent review correction — signal-first late activation

Independent qualitative review of PR #37 on head `b71e2f7527092cf1f63014160fe36c7cf8416fb3` returned **NEEDS CORRECTION** for one narrow continuity gap:

> The package described candidate triggers and what to do after a candidate had already been selected, but it did not bind a new material/failure/learning signal back to persistent known candidates. A competent worker could therefore still require Human/AI meta-orchestration to remember which OC candidate to inspect.

The corrected chain is:

`recognized material/failure/learning signal → known-candidate routing → match | no-match | uncertain-match → current trigger evaluation → at most activation candidate → problem validation/preflight → admission if authorized → implementation if authorized`

The routing obligation is owned by the **existing** Material State / `BB-INTEGRATE` / current Planning Owner path. It does not create a registry, matcher service, new Building Block or roadmap.

Deterministic enforcement is intentionally narrow but now includes referential truth: `tools/work.py integrate` checks that the routing disposition is present, the declared planning source equals the current execution cursor, candidate-evidence files exist, matched candidate IDs exist in that evidence, required fresh-state refs exist, and authority remains unchanged. The semantic match itself and completeness of the candidate search space remain AI judgement with explicit uncertainty.

Authority boundaries:

- `match` ≠ activation;
- `uncertain-match` must not activate automatically;
- `no-match` is a valid explicit result;
- matched candidate + unsatisfied/uncertain trigger remains inactive;
- matched candidate + satisfied trigger creates **at most an activation candidate**;
- activation candidate ≠ priority ≠ promotion ≠ admission ≠ implementation authority.

### Concrete next steps after the focused re-review residual findings

The original signal→known-candidate finding is considered qualitatively closed on the prior corrected head, but PR #37 is **not yet a Promotion Candidate** because referential routing truth and the clarified Human-Owner/system-orchestration hypothesis require one small follow-up slice.

1. Deterministically bind routing evidence to the current `project/execution_state.json` planning source.
2. Require repository candidate-evidence refs and reject matched candidate IDs that are not present in those persisted evidence files.
3. Require current execution/reconciliation files in `fresh_state_refs`; keep semantic overlap and search-space completeness explicitly as judgement.
4. Persist the third open Owner-model hypothesis: Human Problem Owner authority is distinct from the system's competence/orchestration function; no new Building Block or canonical role name is promoted.
5. Run formal repository assurance on the resulting exact PR head.
6. Perform focused independent qualitative re-review of the residual provenance/Owner-model corrections.
7. Treat `WA-EVAL-031..033` as **visible regression cases only**, not as blind-evidence cases: their expectations are repository-visible in `tests/fixtures/eval_cases.json`.
8. For blind evidence, use the separate two-phase protocol in `tests/probes/routing_fresh_context_stimuli_v1.json` and `tests/probes/fresh_context_trial_contract.json`: render an isolated exact-revision operational bundle with `tools/eval_integrity.py`, provide no full-repository/eval/prior-trial/oracle access, and persist the raw response before any oracle is revealed.
9. Do not count a same-chat execution, a full-repository execution with repository-visible oracle material, or an execution after oracle persistence as blind fresh-context evidence. Until valid independent probe evidence exists, routing behavior is not `real-use-demonstrated`.
10. Treat capture metadata as integrity evidence only: exact revision, stimulus identity, allowed context and access declarations do not themselves prove semantic correctness, true freshness or Human effectiveness.
11. Only if the focused re-review confirms the residual corrections and the two-phase blind probe produces valid independent evidence should PR #37 be treated as a **Promotion Candidate**.
12. Human Promotion Decision remains required before merge where the existing authority boundary requires it; after any merge, reconcile the promoted contract change.
13. P2 remains independent: its implementation still requires its own explicit Human admission and does not wait for PR #37 promotion or a future matcher/trigger engine.

---

## 1. Fresh baseline

Fresh state immediately before this operationalization write:

- canonical `main`: `b590523d31db5f82628d6e0d5182821501729906`
- planning source/focus: `github:esany/Wissensarbeit#7`
- canonical current step: `p2-fidelity-manifest-preflight`
- P2 preflight: complete and canonically promoted
- next P2 material gate: `p2-implementation-admission`, blocked on explicit Human admission
- `implementation_allowed=false`
- P2 implementation: not started
- Human–AI collaboration audit: draft PR #37, therefore not canonical on `main`
- PR #37 pre-operationalization head: `25aa7f09ace4f2f68539f1e3e5ceecdfb6559947`
- assurance on that head: Run #114, SUCCESS

This plan does not change those execution/authority facts.

---

## 2. Development-state reconstruction

`Wissensarbeit` is beyond initial Foundation work and has a functioning repository-native operational/governance core, but several promised Human–AI capabilities remain stronger as contracts than as demonstrated Human-effective runtime behavior.

Current development boundary:

1. P1 Harvest/Restart work is materially complete.
2. P2 Context-Fidelity preflight is complete and independently qualitatively confirmed.
3. P2 implementation is not admitted.
4. The current Human–AI collaboration audit identifies broader system-level operationalization gaps but does not displace the P2 gate.
5. PR #37 remains a candidate persistence/review surface until independently qualitatively reviewed and promoted.

The current programme therefore has two distinct facts that must not be collapsed:

- **current execution gate:** P2 implementation admission;
- **new material evidence:** broader Human–AI collaboration operationalization gaps.

The second does not automatically reprioritize the first.

---

## 3. Fresh staleness / authority findings

### 3.1 Current-state authority

The authoritative current P2 state is reconstructed from:

- `project/execution_state.json`
- `project/reconciliation.json`
- current Git/GitHub state.

Historical review/preflight artifacts remain valid evidence for their reviewed state but are not current-state clocks.

### 3.2 Known stale wording

`project/WA-P2-IMPLEMENTATION-ADMISSION-PROPOSAL-2026-09-19-01.md` still contains historical assurance wording stating that the P2 preflight is not yet canonical until PR #35 is promoted.

That wording is stale after PR #35 promotion.

This persistence/operationalization slice does not edit the P2 admission proposal because doing so would mix this Human–AI planning persistence slice with the separate P2 admission surface. Current authority is not ambiguous because the execution/reconciliation owners explicitly record the promoted preflight and blocked admission.

### 3.3 Derived-state limitation

`project/CURRENT_STATE.md` is reproducible from the reconciliation packet but its generic “Next operational proof” does not itself provide the decision-ready Human context for the current P2 admission gate.

This is evidence relevant to OC-05, not a reason to expand P2 in this slice.

### 3.4 Historical roadmap text

Issue #7 contains historical candidate roadmap language. Current execution priority must be derived from the persisted execution cursor, not inferred from old P0/P1/P2/P3 prose.

The OC identifiers introduced here are stable identities only and must not be interpreted as replacement roadmap phases.

---

## 4. Plan-Fidelity Gate result

The full planning model reconstructed from current audit evidence contains all of the following and they must remain jointly valid:

1. Human Owner is not Prompt Engineer, repository orchestrator, context courier or substitute specialist.
2. Short, vague, symptom-level and terminologically imperfect Human input is legitimate.
3. System reconstructs context first, detects competence gaps, researches where warranted, preserves uncertainty and asks only on residual material ambiguity.
4. Human decision/review requires orientation, context, evidence, uncertainty, consequences, reversibility, exact decision scope and drill-down trace.
5. Readability/XAI means structured access to complexity, not destructive shortening.
6. Work instruction / prompt compilation is system work where derivable.
7. Partial automation/function allocation is a peer system concern, not a review subtopic.
8. PR #35 is strong real evidence for manual orchestration burden but is only one use case.
9. Competence/research/uncertainty routing is a separate peer concern.
10. The project is outcome-open; uncertainty, reject, defer, no-change and reframing are valid.
11. Errors and iteration history are useful evidence and should not be rewritten into an idealized linear story.
12. Learnings should be operationalized into future behavior or explicitly dispositioned.
13. Material Human corrections must accumulate; later correction must not erase still-valid earlier constraints.
14. Real-use pain is counterevidence to unqualified “operationalized” claims.
15. An already-promised capability that still fails in real use gains stronger implementation/evidence relevance; this does not automatically create execution priority.
16. Capability evidence maturity and project priority are separate dimensions.
17. No new Building Block is promoted; equally, “no new Building Block ever” is not treated as an already proven architecture conclusion.
18. The current P2 scope remains bounded; broader collaboration capabilities must not be opportunistically pulled into it.
19. The current Governing Objective wording about a “fachlich bzw. konzeptionell kompetent” owner has a visible interpretive tension with the newly clarified non-specialist input model and must not be silently rewritten.
20. The persistence mechanism itself must reduce future Human meta-work rather than creating a new planning bureaucracy.

**Plan-Fidelity Gate: PASS for candidate persistence.**

PASS here means the plan is sufficiently reconstructed to choose a persistence shape. It does not mean the Human–AI collaboration audit or this plan has independent qualitative acceptance.

---

## 5. Operationalization evidence discipline

For each target capability, report only the highest demonstrated level:

1. `declared`
2. `wired`
3. `executable`
4. `regression-protected`
5. `real-use demonstrated`
6. `human-effective`
7. `robust/restartable`

Important:

- the scale describes **positive capability evidence**, not severity or priority;
- negative real-use evidence may coexist with a low positive maturity level;
- partial components can have stronger evidence than the peer-axis target as a whole;
- CI/formal PASS never upgrades semantic/Human effectiveness by itself;
- a later activated work item must reassess maturity freshly rather than copy this snapshot blindly.

---

## 6. Persistence-options evaluation

### Option A — Audit + Issue #7 only

**Strengths**

- smallest artifact count;
- no new state shape;
- #7 is already the planning owner.

**Weaknesses**

- seven peer problems remain embedded in long audit prose;
- later activation risks re-summarizing and losing detailed constraints;
- stable candidate identity and activation semantics are not explicit enough;
- machine inspection of coverage, evidence maturity and per-axis refs is weak.

**Disposition: insufficient alone.**

### Option B — one Issue per axis now

**Strengths**

- strong discoverability;
- independent discussion/work surfaces;
- straightforward linking.

**Weaknesses**

- creates seven new persistent work surfaces before any axis is activated;
- visually resembles a roadmap even when no priority exists;
- increases metadata/maintenance burden;
- encourages each issue to drift away from the common Human-intent evidence;
- violates the goal of late activation.

**Disposition: reject for current stage.**

Later activation may legitimately create a focused issue for exactly one axis.

### Option C — mutable Operationalization / Capability Registry

**Strengths**

- strong machine readability;
- easy status/maturity reporting;
- could support future automation.

**Weaknesses**

- creates a new mutable state clock;
- risks duplicating #7, execution state and canonical contracts;
- creates ongoing synchronization burden before proven need;
- invites “registry says X” to become unintended authority.

**Disposition: reject for current stage.**

A mutable registry may be reconsidered only after repeated real friction shows that issue/evidence references cannot support restartability or automation.

### Option D — immediately sharpen Requirements / Criteria / Verification

**Strengths**

- strong normative force;
- makes gaps visible to acceptance/verification.

**Weaknesses**

- converts current Human feedback/audit evidence into normative authority too early;
- several target semantics and architecture boundaries remain genuinely open;
- risks overfitting Requirements to one conversation before activated problem validation.

**Disposition: reject as a blanket action.**

Future activated slices may discover that existing Requirements need refinement; that decision must be made then with current evidence and Human authority.

### Option E — Audit + mutable candidate inventory at Planning Owner

**Strengths**

- keeps one planning owner;
- stable candidate IDs support later activation;
- better than seven premature issues.

**Weaknesses**

- if the inventory carries mutable “current status” it can become a second planning/state clock beside execution state and issue #7;
- maintaining maturity/current state in two places would recreate the synchronization problem this work is trying to solve.

**Disposition: useful direction, but needs a stronger anti-state-clock boundary.**

### Option F — selected candidate, corrected: immutable snapshot + existing Planning Owner + signal-first late activation

Structure:

1. **Detailed audit** preserves full Human intent, evidence, failures and uncertainties.
2. **This human-readable operationalization snapshot** records why and how later activation works.
3. **Immutable machine-readable companion snapshot** records stable OC identities, refs, snapshot maturity, activation conditions and routing falsification cases.
4. **Issue #7 remains the only mutable planning owner.**
5. **Execution state remains the only small current execution cursor.**
6. No per-axis Issue exists until that axis is actually activated.
7. Every newly recognized material-state/failure/learning signal entering the existing integration/planning path must produce an explicit **known-candidate routing** result: `match`, `no-match` or `uncertain-match`.
8. Routing resolves the fresh current planning source and persistent unresolved/activation-ready candidate evidence; it does not rely on chat memory or require the Human to name an OC candidate.
9. A `match` re-binds original candidate evidence to fresh repository state and then evaluates the **current** activation trigger.
10. Only `match + trigger satisfied` may produce an **activation candidate**. That candidate has no priority, promotion, admission or implementation authority.
11. A later focused work/preflight item references the OC ID, original audit, this plan, the machine snapshot, routing evidence and fresh repository state.
12. The snapshot is not mutated to track later work state. If the underlying model materially changes, a new superseding versioned snapshot is created with provenance.

**Why this is preferable now**

- closes the passive-archive gap identified by independent review;
- preserves stable, machine-readable candidate identity;
- avoids a mutable capability registry or technical matcher service;
- avoids seven premature work items;
- keeps #7 and execution state authoritative for current planning/execution;
- allows each topic to be activated independently from real signals;
- makes original Human intent and omissions reconstructable by reference;
- makes `no-match` and uncertainty explicit instead of forcing false candidate matches;
- minimizes new meta-work.

**Disposition: selected corrected candidate persistence/routing model.**

This correction is subject to focused independent qualitative re-review in PR #37.

---

## 7. Stable peer-axis identities

The identifiers below are **stable identity only**.

> **OC number = identity, not rank, phase, priority or sequence.**

### OC-01 — Human Role / Minimal Input / Intent Reconstruction

**Need**

Human can communicate tersely, colloquially, symptom-first and with imperfect terminology without becoming the system’s domain analyst or prompt engineer.

**Primary existing-owner fit**

- BB-BOOTSTRAP
- BB-INTEGRATE
- BB-REQUIREMENTS
- BB-LEARN

**Current target maturity**

`declared`

There are stronger component controls around material-state classification and Harvest provenance, but no end-to-end executable terse-intent reconstruction capability is demonstrated.

**Negative real-use evidence**

- current Human–AI collaboration audit;
- FF-EXECUTION-PROGRESS open gap;
- repeated same-chat correction/reframing.

**Activation candidates**

- a real admitted work item again requires the Human to provide derivable problem/context structure;
- terse Human input is materially misread after current-context reconstruction;
- an admitted slice explicitly depends on intent reconstruction;
- Human Owner explicitly prioritizes the capability.

**Non-activation conditions**

- mere existence of a vague Human message;
- low maturity by itself;
- completion of unrelated work.

### OC-02 — Context & Work Instruction Compilation

**Need**

Human need not courier relevant context or write expert execution prompts.

**Primary existing-owner fit**

- BB-CONTEXT
- BB-TRACE
- BB-ASSURE
- current P2 Context-Fidelity work

**Current target maturity**

`declared` for the full intent-bound Work Instruction capability.

Components are stronger:

- current `work.py context` is executable but coarse/near-full;
- existing pilot checks are regression-protected for simpler fidelity/token cases;
- P2 bounded-context contract is preflight-confirmed but not implemented.

**Current work overlap**

P2 directly addresses a bounded Context Compiler subset. It does not implement a full Work Packet compiler.

**Activation candidates for the broader axis**

- after P2, significant Human-authored meta-prompting remains necessary;
- a later admitted workflow needs derivable work instructions/stop conditions;
- repeated work shows the same context/instruction compilation burden.

### OC-03 — Competence / Research / Uncertainty Routing

**Need**

System identifies and obtains missing domain/method/technical competence rather than using the Human as substitute specialist.

**Primary existing-owner fit**

- BB-COMPETENCE
- BB-RESEARCH
- specialist authority

**Current target maturity**

`declared`

Taxonomy/contracts exist, but task-triggered end-to-end competence/research routing is not demonstrated in the current operational core.

**Activation candidates**

- material work depends on expertise not covered by current task context;
- current workflow cannot determine fit without external/SOTA evidence;
- a repeated Human burden shows the owner being asked to supply specialist knowledge.

### OC-04 — Partial Automation / Function Allocation / Orchestration

**Need**

Real workflows are decomposed into the correct functions for deterministic software, routine automation, AI judgement, specialist judgement and Human material authority.

**Primary existing-owner fit**

- Authority rule classes
- BB-CONTEXT
- BB-INTEGRATE
- BB-ASSURE
- BB-TRACE
- BB-OPERATE

**Current target maturity**

`declared`

There are executable component mechanisms such as the execution guard and CI assurance, but no generic demonstrated function-allocation/orchestration capability.

**Strong real-use evidence**

PR #35 review/correction/re-review required substantial derivable meta-orchestration through prompts.

**Activation candidates**

- a current material workflow repeatedly needs manual coordination of deterministic/judgement/Human steps;
- a second real workflow demonstrates the same generic burden;
- Human Owner explicitly prioritizes automation of an already evidenced workflow;
- an admitted capability requires coordinated multi-step execution.

A second workflow is useful generic-fit evidence but is not an absolute prerequisite if existing evidence plus current need already justifies activation.

### OC-05 — Human Decision Context / Review Experience / XAI

**Need**

Human receives decision-ready orientation and full drill-down without doing repository integration manually.

**Primary existing-owner fit**

- BB-TRACE
- BB-ASSURE
- BB-DERIVE
- BB-INTEGRATE
- Decision Brief
- Q-XAI
- Issue #6

**Current target maturity**

`wired`

The Decision Brief contract is connected to Authority/Building Blocks and structurally validated, but automatic end-to-end generation/delivery at a real material Human gate is not demonstrated.

**Negative real-use evidence**

- current Human repeatedly requested context/orientation;
- current P2 gate is not exposed by `CURRENT_STATE` as a complete decision-ready brief.

**Activation candidates**

- a material Human gate again requires manual reconstruction;
- P2/result-review or later work needs an automatic Human decision packet;
- Issue #6 is explicitly activated by current planning.

### OC-06 — Iterative Discovery / Error Culture / Operational Learning

**Need**

Failure and feedback change future behavior transparently, without erasing uncertainty or promoting unvalidated solutions.

**Primary existing-owner fit**

- BB-LEARN
- BB-DESIGN
- BB-RESEARCH
- BB-INTEGRATE
- Failure Corpus

**Current target maturity**

`wired`

Material-state persistence, audit deltas and regression candidates exist, but the full learning closure from observation through later effectiveness evidence is not demonstrated generically.

**Activation candidates**

- repeated feedback is persisted but does not alter future checks/workflow or receive explicit no-change disposition;
- a real implementation result generates learning that needs operational closure;
- the design-method audit gap becomes necessary for current product/problem work.

### OC-07 — Cumulative Correction Fidelity / Interaction Continuity

**Need**

Multiple Human corrections accumulate into one still-valid working model; “latest correction wins” must not silently erase earlier constraints.

**Primary existing-owner fit**

- BB-CONTEXT
- BB-STATE
- BB-INTEGRATE
- BB-TRACE
- BB-LEARN
- Material State / Conversation Harvest

**Current target maturity**

`declared`

Cross-session continuity has controls, but no dedicated demonstrated same-interaction cumulative correction mechanism/regression exists.

**Strong real-use evidence**

The current conversation repeatedly lost earlier peer concerns while locally incorporating later corrections.

**Activation candidates**

- the failure recurs in another representative task;
- an admitted Work Packet/Harvest/Context change requires correction-chain semantics;
- current work cannot remain faithful without explicit correction/supersession handling;
- Human Owner explicitly prioritizes the capability.

Current evidence is already sufficient to establish the gap; additional recurrence is not required to “prove” it exists.

---

## 8. Activation semantics

Candidate registration is not activation, and a trigger description is not a trigger detector.

The process starts from the **new signal**, not from an already remembered OC ID:

`recognized material/failure/learning signal → resolve current planning source → inspect persistent known candidates → match | no-match | uncertain-match`

Routing consequences:

- **no-match:** persist the rationale; do not invent a candidate merely to avoid no-match;
- **uncertain-match:** preserve uncertainty; no automatic activation;
- **match:** bind the earlier candidate evidence to fresh repository state, then evaluate the current trigger;
- **match + trigger not satisfied/uncertain:** candidate remains inactive;
- **match + trigger satisfied:** create at most an **activation candidate**.

Activation may be justified by one or more of:

- a real workflow encounters the gap again;
- an admitted/current slice depends on the capability;
- an existing promised Requirement cannot be credibly met without it;
- negative Real-Use evidence makes continued deferral materially costly;
- new SOTA/regulatory/safety evidence changes the risk;
- Human Owner makes an explicit priority decision.

An activation candidate is **not** Priority, Promotion, Implementation Admission or Implementation Authority.

After an activation candidate, the default process is:

`confirm current problem → fresh state → competence/research → existing-owner fit → options → falsification → smallest adequate slice → acceptance/admission boundary → implementation if authorized`

A future activation must re-read current repository state. This snapshot is evidence, not current-state substitution.

---

## 9. P2 impact classification

The seven axes do not become P2 scope.

| Axis | P2 classification | Current consequence |
|---|---|---|
| OC-01 | compatibility / semantic constraint | Preserve Human-feedback/authority distinctions; do not build an intent classifier. |
| OC-02 | **direct subset now** | P2 implements bounded context/provenance only; broader Work Instruction Compilation remains later. |
| OC-03 | compatibility / later | Do not erase competence/method/source refs when material; no competence-routing engine in P2. |
| OC-04 | later / enabler relationship | P2 may become a bounded-context primitive for future orchestration; no workflow engine now. |
| OC-05 | compatibility + result-review relevance | P2 provenance/omission explanation should remain inspectable; no automatic Decision Brief implementation inside P2. |
| OC-06 | result-review relevance + later | P2 result review should record validated learning/no-change; no general learning methodology implementation inside P2. |
| OC-07 | compatibility + later | P2 must not strengthen/silently erase selected provenance/authority/uncertainty; no cumulative correction engine now. |

### P2 result-review criteria strengthened by this evidence

Without changing P2 functional scope, later result review should explicitly distinguish:

- structural/deterministic PASS;
- real boundedness judgement;
- Human usefulness;
- provenance usefulness;
- process/token overhead;
- demonstrated operationalization level.

These concerns are already substantially compatible with the confirmed P2 preflight’s residual uncertainty and result-review boundary.

---

## 10. Governing Objective tension and role-function separation

Current wording:

> “fachlich bzw. konzeptionell kompetenten, technisch nicht spezialisierten Problem Owner”

Current Human clarification:

- no assumption of correct domain terminology;
- no assumption of technically correct solution language;
- no assumption that the Human can perform specialist domain/method/engineering analysis;
- Human contributes purpose, experience, observations, constraints, values and material decisions;
- the system is expected to identify, obtain and compose missing specialist competence where this is operationally necessary.

Current disposition:

**unresolved semantic interpretation / no silent edit**

The open question must be split into two different questions rather than treating all hypotheses as alternative definitions of one Owner role.

### A. Human Problem Owner semantics

Question:

> Which competence must the Human actually possess for the Governing Objective to remain valid?

Two live hypotheses remain:

- **OH-01:** “fachlich bzw. konzeptionell kompetent” can be read as competence in purpose, lived/problem experience, constraints and material meaning rather than specialist analytical terminology.
- **OH-02:** the wording materially overstates expected Human competence and may require later Human-authorized refinement.

No normative choice between OH-01 and OH-02 is made here.

### B. Systemic competence/orchestration function

Separate question:

> Which domain, method, research, logical, technical, contextual and transdisciplinary competence must the system situationally detect, obtain, synthesize and orchestrate so the Human does not become the substitute specialist?

**OH-03:** Human Problem Ownership and systemic competence/reasoning orchestration are distinct functions.

Under this hypothesis:

- the Human retains purpose, meaning, constraints, values, priorities, risk/acceptance and material-decision authority;
- the system reconstructs context, detects required competence, researches when needed, composes specialist/method/technical perspectives, checks project fit and supports execution;
- system competence does not inherit Human Authority merely because it supplies reasoning or specialist capability.

OH-03 is **compatible with** the already-canonical combination of the Governing Objective, `system/competence.json` and `system/authority.json`. Its comparative explanatory adequacy relative to other interpretations remains to be tested; it is an **open interpretation**, not a preferred or normative rewrite.

Working terminology for the system-side function should avoid “Owner” because that could imply material meaning or decision authority. Candidate descriptive terms include **competence orchestration**, **reasoning/competence orchestration** or **systemic competence/orchestration function**. No canonical role name is selected here.

No new Building Block follows from OH-03. The current composition hypothesis is:

`BB-BOOTSTRAP + BB-CONTEXT + BB-COMPETENCE + BB-RESEARCH + BB-INTEGRATE + BB-ASSURE + BB-TRACE`

This is a composition hypothesis to be tested through real work, not an architecture promotion.

This role-model tension does **not** block current P2 because the P2 contract already treats Human feedback as evidence rather than automatic semantic/solution authority.

A later normative Governing Objective, authority or role change requires an explicit Human decision brief.

---

## 11. SOTA / best-practice research disposition

No new external research was required to choose the persistence shape in this slice.

Reason:

- the repository already contains explicit anti-bloat, authority, candidate/promotion, material-state and execution-cursor contracts;
- the underlying Human–AI/function-allocation direction was already cross-checked in the source audit against NIST AI RMF, Microsoft Human–AI/HAX guidance and NASA Human Factors/function-allocation guidance;
- the remaining decision here is primarily repository-state architecture: how to preserve candidate evidence without creating a second state clock.

New external research should be performed when an axis is activated and its method/technical solution becomes material.

---

## 12. Operationalization-fidelity falsification

| Failure | Result | Reason |
|---|---|---|
| F1 Audit becomes roadmap | PASS | OC IDs have no order/priority semantics; execution cursor unchanged. |
| F2 Candidate becomes Requirement | PASS | no Requirement text/change; candidates remain evidence/planning only. |
| F3 Candidate becomes Implementation Authority | PASS | `implementation_allowed=false`; activation and admission explicitly separate. |
| F4 Numbering becomes priority | PASS | identity-only rule repeated in human and machine snapshot. |
| F5 Meta-state overload | PASS, residual risk | no mutable registry; only versioned snapshot evidence. |
| F6 Existing owners ignored | PASS | each OC axis maps to existing owners first. |
| F7 Existing owners dogmatically fixed | PASS | new architecture remains falsifiable if future evidence requires it. |
| F8 P2 scope creep | PASS | P2 matrix explicitly separates direct subset/constraint/result-review/later. |
| F9 Original Human intent lost | PASS subject to qualitative review | full audit remains primary evidence and each candidate links back to it. |
| F10 Latest-note wins | PASS by design, not yet runtime proof | cumulative correction requirement is explicit; no claim it is implemented. |
| F11 Declared = operationalized | PASS | maturity ladder and target-level assessment make the distinction explicit. |
| F12 Meta-work becomes product | PASS, monitor | two versioned artifacts are added; no ongoing per-axis maintenance until activation. |
| F13 Trigger exists but known candidate is never rediscovered | PASS by corrected design; runtime maturity remains bounded | Material State / BB-INTEGRATE now requires explicit match/no-match/uncertain-match routing through the existing integration path; semantic matching remains judgement, not a matcher service. |

No deterministic PASS here proves Human-intent semantic completeness. Independent qualitative review remains required.

---

## 13. Coverage / omission manifest

| Planning / Intent element | Persisted where | Status | Omitted? | Rationale |
|---|---|---|---:|---|
| Human not prompt engineer | audit §3.1/3.5; this plan §4/OC-01/02 | covered | no | core Human-role boundary |
| minimal/imprecise input | audit §3.2; OC-01 | covered | no | explicit normal input model |
| competence acquisition | audit §3.2; OC-03 | covered | no | separate peer axis |
| research when uncertain | audit §3.2; OC-03 | covered | no | kept conditional on material uncertainty |
| material clarification only | audit §3.2; OC-01/03 | covered | no | avoids clarification-first and silent inference |
| uncertainty allowed | audit §3.7; OC-03/06 | covered | no | project remains outcome-open |
| outcome-open project | audit §3.7; OC-06 | covered | no | reject/defer/no-change remain valid |
| error culture | audit §3.8; OC-06 | covered | no | failures remain visible evidence |
| transparent iteration | audit §3.8; OC-06/07 | covered | no | correction history retained |
| operationalized learning | audit §3.9; OC-06 | covered | no | prose-only learning not treated as sufficient |
| context/work-packet compilation | audit §3.5/AXIS-B; OC-02 | covered | no | explicit broader-than-P2 distinction |
| partial automation | audit §3.6/AXIS-D; OC-04 | covered | no | peer axis |
| PR #35 as evidence | audit §3.6/C2/C7/C8; OC-04/05 | covered | no | example, not parent topic |
| review not parent topic | audit §3.6/3.12; plan §4/OC-04 | covered | no | peer-axis rule explicit |
| Human decision context | audit §3.3; OC-05 | covered | no | separate peer axis |
| XAI ≠ shortening | audit §3.4; OC-05 | covered | no | complexity remains navigable |
| progressive disclosure candidate | audit §3.4; OC-05 | covered as candidate | no | not promoted as implementation |
| cumulative correction fidelity | audit AXIS-G; OC-07 | covered | no | same-chat failure retained |
| real-use pain as counterevidence | audit §3.10; plan §5 | covered | no | maturity claims evidence-calibrated |
| existing promise + failure = stronger evidence | audit §3.11 | covered | no | explicitly not automatic priority |
| evidence maturity ladder | audit §6; plan §5; machine snapshot | covered | no | separate from priority |
| no silent roadmap | audit boundaries; plan option F/activation | covered | no | #7 + cursor remain authority |
| late activation | plan §8; machine snapshot | covered | no | no premature work items |
| P2 boundary | audit + plan §9 | covered | no | scope separated from later axes |
| open Building-Block question | audit §12/15; plan §4 | covered | no | no 15th block promoted or permanently excluded |
| Governing Objective tension | audit §13; plan §10 | covered, unresolved | no | requires later Human semantic decision if material |
| no Human-as-repository-orchestrator | audit §3.1; OC-01/02/05 | covered | no | core intended burden reduction |

### Deliberately not adopted / omitted as current design

| Candidate idea | Disposition | Why |
|---|---|---|
| mutable operationalization registry | rejected now | would create a second state clock without proven need |
| seven immediate OC issues | rejected now | premature fragmentation/roadmap signal |
| Work Packet as persistent object | defer | desired capability is clear; storage/object form is not |
| progressive disclosure as fixed UI architecture | defer | valid design direction, not yet selected implementation |
| new Building Block | no promotion | existing-owner fit must be tested first; future evidence may re-open |
| Governing Objective rewrite | defer / Human gate | semantic interpretation unresolved |
| priority order among OC axes | omitted intentionally | no current authority/evidence for ordering |
| P2 expansion to implement OC-01/03/04/05/06/07 | rejected | violates confirmed bounded P2 scope |

---

## 14. Restart / future activation protocol

A fresh worker processing a new material-state/failure/learning signal should:

1. read current `main`, `GOVERNING_OBJECTIVE.md`, Authority, execution state and reconciliation;
2. resolve the current planning owner from repository state;
3. inspect persistent unresolved/activation-ready candidate evidence referenced by that owner or canonical state;
4. record one explicit routing result: `match`, `no-match` or `uncertain-match`;
5. for `no-match`, preserve the rationale and continue without manufacturing an OC activation;
6. for `uncertain-match`, preserve uncertainty and do not activate automatically;
7. for `match`, read the original audit, human-readable plan, machine snapshot and any later superseding evidence for the matched candidate;
8. bind that evidence to fresh current repository state;
9. evaluate whether the candidate's current activation trigger is actually satisfied now;
10. only if both match and current trigger are established, create an **activation candidate**;
11. confirm the current problem rather than assuming historical evidence is still sufficient;
12. re-evaluate current capability maturity;
13. perform current competence/SOTA research where material;
14. reassess existing-owner fit;
15. define/falsify the smallest adequate slice;
16. create a focused Work/Preflight item only when justified;
17. preserve Human priority, promotion, admission and implementation authority boundaries.

The worker must not infer priority merely because an OC candidate exists, and must not require the Human to remember or name the OC candidate for routing to occur.

---

## 15. Self-critical Plan-Fidelity review

1. **Latest Human turn over-weighted?** No. Earlier partial automation, prompt burden, XAI, competence, uncertainty, learning and correction fidelity remain peer concerns.
2. **Any axis subsumed under review?** No. Review appears only as evidence/use case.
3. **“Present” confused with “operationalized”?** No. Target maturity is explicitly conservative.
4. **Preferred solution promoted without alternatives?** No. A–F evaluated; Option F chosen as current candidate only.
5. **Uncertainty closed artificially?** No. Governing Objective meaning, future architecture, mutable registry need and Building-Block fit remain open.
6. **Priority manufactured?** No. No OC ordering and no cursor change.
7. **P2 expanded?** No. Only compatibility/result-review links recorded.
8. **Restartable without chat?** Intended yes: audit + this snapshot + machine manifest + #7 + execution/reconciliation provide the chain; independent review must verify semantic completeness.
9. **Human meta-work reduced?** The design avoids per-axis issues/status maintenance until activation and provides a future reconstruction protocol.
10. **New meta-artifacts excessive?** Residual risk exists; two versioned artifacts are justified by the need for both Human-readable planning coverage and machine-readable stable identity without a mutable registry.

**Self-review status: READY FOR INDEPENDENT QUALITATIVE REVIEW after formal assurance.**

---

## 16. Non-changes

This operationalization does not change:

- Governing Objective;
- Requirements;
- Criteria;
- Verification methods;
- Quality model;
- Risks;
- lifecycle;
- Authority contract;
- Building Blocks;
- current programme priority;
- `project/execution_state.json`;
- `implementation_allowed`;
- P2 functional scope;
- P3/P4/P5 activation;
- implementation code.

It adds candidate evidence/planning structure only.

---

## 17. Stop boundary

Stop after:

- this snapshot and its machine-readable companion are persisted;
- reconciliation references them without changing the execution cursor;
- issue #7 is given a trace reference without new priority;
- formal assurance passes on the exact head;
- status remains `READY FOR INDEPENDENT QUALITATIVE REVIEW`.

No capability implementation, P2 admission, roadmap creation or additional architecture follows automatically.


---

## 18. Work-type semantic contract — candidate operationalization

This section operationalizes a Human-corrected terminology rule that has already failed repeatedly in real use.

It is a **candidate semantic contract inside PR #37**, not yet a promoted modification of `system/lifecycle.json` or `system/authority.json`.

### Core rule

> Classify work by its actual function and consequence, not by the generic fact that “some work happened”.

A bounded unit of work is **not automatically an iteration**.

A workflow may contain several work types. For example:

`Preflight → Admission → Implementation Slice → Assurance → Review → Correction → Re-Review → Promotion → Reconciliation`

That complete sequence may contribute to a larger genuine iteration **only if** real evidence changes the hypothesis/design/implementation understanding and produces a changed next state.

### WT-01 — Iteration

**Definition**

A genuine learning/development cycle in which a hypothesis, problem framing, design or implementation is exposed to real evidence, and that evidence changes what is understood or what happens next.

Minimal semantic shape:

`starting hypothesis/state → intervention/attempt → evidence/result → learning → changed next state`

**Required evidence**

- starting hypothesis/state or explicit question;
- what was tried or observed;
- evidence/result;
- what was learned;
- what changed in the next state because of the learning.

**Allowed consequences**

- refine/reframe/supersede a hypothesis or candidate;
- change a design or implementation candidate;
- generate new uncertainty;
- justify a later planning/admission proposal;
- produce validated learning for BB-LEARN.

**Does not imply**

- Human acceptance;
- promotion;
- implementation admission;
- merge;
- successful outcome;
- requirement change.

**Misclassification failure**

Calling a gate, merge, persistence action or administrative transition an iteration hides whether actual learning occurred.

### WT-02 — Preflight

**Definition**

A bounded check of whether a later proposed slice is sufficiently specified, evidentially grounded, owner-aligned and safe enough to be considered for admission/execution.

**Required evidence**

- proposed later scope;
- relevant owners/requirements/authority;
- known risks and uncertainties;
- falsification/stop conditions;
- smallest credible candidate;
- explicit residuals.

**Allowed consequences**

- PASS / FAIL / NEEDS CORRECTION / INSUFFICIENT EVIDENCE;
- recommendation that admission may or may not be considered;
- refinement of the proposed slice.

**Does not imply**

- implementation start;
- implementation permission;
- merge;
- promotion;
- result acceptance.

**Staleness consequence**

A materially changed target/scope can invalidate the preflight and require re-evaluation.

### WT-03 — Review

**Definition**

Qualitative assessment of a concrete, identifiable state against stated semantic/quality/authority criteria.

**Required evidence**

- exact review target/revision;
- review scope;
- applicable criteria/owners;
- findings and uncertainty;
- verdict.

**Allowed consequences**

- CONFIRM;
- NEEDS CORRECTION;
- INSUFFICIENT EVIDENCE;
- block or support consideration of a later authority transition.

**Does not imply**

- promotion;
- admission;
- implementation success;
- Human acceptance unless the Human explicitly owns and performs that acceptance.

**Revision consequence**

A material change after review makes the old verdict insufficient for the changed state until the delta is assessed.

### WT-04 — Re-Review

**Definition**

A review performed after correction/change, normally focused on whether identified findings were closed and whether the correction introduced material regressions inside the agreed review boundary.

**Required evidence**

- prior review target/verdict;
- exact corrected target/revision;
- identified findings;
- correction delta;
- focused re-review scope.

**Allowed consequences**

- close or retain prior findings;
- identify correction-induced problems;
- update the qualitative verdict for the exact reviewed state.

**Does not imply**

- that unrelated parts were freshly reviewed;
- promotion/admission;
- merge authority.

**Freshness consequence**

The re-review verdict is bound to the reviewed revision. A later material delta requires another assessment.

### WT-05 — Correction

**Definition**

A targeted change made in response to an identified finding, failure or discrepancy.

**Required evidence**

- triggering finding/failure;
- intended correction boundary;
- actual delta;
- unchanged/non-target areas where relevant.

**Allowed consequences**

- modify the candidate/artifact;
- invalidate prior formal or qualitative evidence where the changed surface matters;
- trigger re-assurance and/or re-review.

**Does not imply**

- that the finding is actually closed;
- that the new state is accepted;
- that scope may expand beyond the correction boundary.

**Default consequence**

After a material correction, assurance/review evidence bound to the old revision must not be reused as if it covered the new revision.

### WT-06 — Promotion

**Definition**

An authority transition by which an already reviewed/accepted candidate state becomes canonical or accepted project state.

Typical repository example:

candidate PR → approved merge/promotion → canonical `main`.

**Required evidence**

- exact candidate state;
- required assurance/review;
- applicable Human/authority decision;
- known material consequences;
- reconciliation requirement.

**Allowed consequences**

- canonical state changes;
- prior candidate becomes accepted/promoted state;
- downstream current-state views may need refresh/reconciliation.

**Does not imply**

- implementation admission for a different/later slice;
- result acceptance beyond the promoted artifact;
- priority change unless explicitly part of the authority decision.

**Default follow-up**

Material promotion requires systemic reconciliation before the change is described as fully integrated.

### WT-07 — Admission

**Definition**

An authority transition that permits a specifically bounded next action or implementation slice that was previously not authorized.

**Required evidence**

- exact admitted scope;
- preconditions/dependencies;
- explicit authority;
- stop conditions;
- what remains excluded;
- persisted admission.

**Allowed consequences**

- the admitted action may become executable;
- `implementation_allowed` or equivalent execution permission may change **only if the canonical execution contract explicitly binds it**.

**Does not imply**

- implementation success;
- merge;
- result acceptance;
- permission for adjacent scope;
- promotion of later findings.

**Scope consequence**

Anything outside the admitted boundary remains unauthorized and requires a new decision/preflight as applicable.

### WT-08 — Reconciliation

**Definition**

Systemic alignment of the wider project state after or around a material change, ensuring all required impact surfaces are explicitly dispositioned.

**Required evidence**

- material change reference;
- required impact surfaces;
- impacted objects;
- disposition/rationale;
- cursor impact;
- unresolved conflicts.

**Allowed consequences**

- establish that the wider project state is explicitly aligned;
- expose conflicts or needed decisions;
- block a claim of systemic integration if incomplete.

**Does not imply**

- new priority;
- new scope;
- promotion;
- admission;
- semantic correctness of the underlying decision.

### WT-09 — Persistence / Operationalization Slice

**Definition**

A bounded work unit that externalizes findings, intent, planning semantics, activation rules or other material state so future work can reconstruct and use it reliably.

**Required evidence**

- what is being persisted;
- source/intent provenance;
- why it is material;
- authority status;
- what it enables later;
- what it explicitly does not authorize;
- coverage/omission where fidelity is material.

**Allowed consequences**

- material knowledge leaves chat-only state;
- future restart/activation becomes possible;
- candidate structure may become machine-readable;
- reconciliation/traceability may improve.

**Does not imply**

- that the persisted finding is accepted as a Requirement;
- priority;
- activation;
- admission;
- implementation;
- successful operational capability.

**Key distinction**

PR #37 is currently this type: a persistence/operationalization slice prepared for qualitative review. It is not itself a genuine iteration merely because substantial work occurred.

### WT-10 — Implementation Slice

**Definition**

Concrete implementation work within an already permitted, bounded scope.

Possible outputs include code, tests, data, configuration, docs or operational mechanisms.

**Required evidence**

- admitted/authorized scope where material;
- implementation delta;
- tests/assurance evidence;
- known residuals;
- result review/reconciliation as required.

**Allowed consequences**

- executable behavior may change;
- new result evidence exists;
- later review/learning can evaluate the implementation.

**Does not imply**

- that the implementation is correct;
- Human-effective;
- accepted;
- merged;
- promoted;
- a genuine iteration.

**Iteration relationship**

An Implementation Slice becomes part of a genuine iteration only when its real result feeds evidence/learning back into a changed next state.

---

## 19. Consequence matrix

| Type | Creates new evidence? | Can change artifact/state? | Creates authority? | Typical next obligation | Explicitly not equivalent to |
|---|---|---|---|---|---|
| Iteration | yes | often | no by itself | persist learning / reconcile material change | “some work happened” |
| Preflight | yes | proposal may refine | no | admission decision or correction | admission |
| Review | yes | no, except findings | no | correction or later authority decision | promotion |
| Re-Review | yes | no, except updated findings | no | later authority decision or more correction | full fresh review of unrelated scope |
| Correction | yes | yes | no | re-assurance / re-review | finding closed |
| Promotion | yes | yes, canonical state | **yes, for canonicalization** | reconciliation | implementation admission |
| Admission | yes | changes permission state | **yes, for bounded action** | execute only admitted scope | result acceptance |
| Reconciliation | yes | project-state dispositions | no new material authority | resolve blockers / integrated-state claim | promotion or prioritization |
| Persistence / Operationalization Slice | yes | evidence/planning artifacts | no | review if material; later activation when justified | implementation |
| Implementation Slice | yes | implementation | only inherited from prior admission | assurance / result review / reconciliation | success or iteration |

### Review/Correction independence boundary from real use

A 2026-09-20 real-use incident on PR #37 showed a downstream reviewer transitioning into implementing its own material findings. Git history stayed linear, but the Review → Correction → Re-Review sequence began to recursively extend itself. This is evidence about **role/evidence independence**, not a need for a new role system.

Operational boundary:

- a reviewer may become the writer/corrector, but after a material write it cannot count its own later assessment of that correction as **independent** review evidence;
- independent confirmation after a material self-correction requires a fresh reviewer bound to the new exact revision;
- a reviewer claiming independent evidence should remain read-only for the reviewed target revision; if it materially writes, the role has changed and the prior verdict is stale for the changed revision;
- sequential use of one branch is allowed; independence is an evidence/provenance property, not a branch-topology rule;
- this refines existing WT-03 Review, WT-04 Re-Review, WT-05 Correction and OC-05/OC-07 only. It creates no new lifecycle stage, authority class, Building Block or standing reviewer role.

### Authority rule

Only a type whose purpose is itself an authority transition may create the corresponding authority, and only when the correct authority holder and persistence requirements are satisfied.

Therefore:

- Review CONFIRM ≠ Promotion.
- Promotion ≠ Implementation Admission.
- Admission ≠ Implementation Result Acceptance.
- CI PASS ≠ Review CONFIRM.
- Reconciliation PASS ≠ Domain/Human Acceptance.
- Persistence ≠ Priority.
- Implementation ≠ Iteration.
- Correction ≠ Closed Finding.

---

## 20. Classification rules for future work

A fresh worker should classify a work unit by asking, in order:

1. **Is the purpose to learn through evidence and change the next understanding/state?**  
   → Iteration candidate.

2. **Is the purpose to decide whether later work is sufficiently defined/safe to consider?**  
   → Preflight.

3. **Is the purpose to judge a concrete existing state?**  
   → Review / Re-Review.

4. **Is the purpose to change something because a finding exists?**  
   → Correction.

5. **Is the purpose to grant authority?**  
   → Promotion or Admission; distinguish canonicalization from permission-to-act.

6. **Is the purpose to align all affected project surfaces?**  
   → Reconciliation.

7. **Is the purpose to make knowledge/planning/state restartable and later actionable?**  
   → Persistence / Operationalization Slice.

8. **Is the purpose to build/change the admitted solution?**  
   → Implementation Slice.

If more than one applies, treat the workflow as a **composition of typed steps**, not as one overloaded label.

If uncertain, preserve the uncertainty and use the narrower non-authority interpretation until the actual consequence is resolved.

### Terminology-fidelity rule

Before reporting a work unit as complete, state:

- work type;
- exact target/scope;
- evidence produced;
- authority gained, if any;
- evidence invalidated/staled, if any;
- required next gate;
- explicit non-consequences.

This is intended to prevent language from silently granting process meaning that did not occur.

---

## 21. Transparent Human explanation contract

When explaining a typed work step to the Human Owner, do not merely name the type.

Explain in plain language:

1. **What kind of step was this?**
2. **Why is that the correct type?**
3. **What changed because of it?**
4. **What did not change?**
5. **Did it create any authority? If yes, exactly which authority?**
6. **Which previous evidence is still valid and which became stale?**
7. **What is the next real gate?**
8. **Is Human action required now? Why?**

Example:

> “This was a correction, not a new iteration. We changed the artifact specifically to close Finding X. That invalidates the prior assurance/review for the changed revision, so re-assurance and focused re-review are needed. It does not authorize merge or implementation.”

The explanation should remain proportional to the consequence. Routine typed steps can be concise; material authority transitions require the full decision-context contract.
