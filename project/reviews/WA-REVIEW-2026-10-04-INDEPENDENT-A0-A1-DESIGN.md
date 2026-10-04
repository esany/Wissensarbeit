# Independent Design Review — PR #85 A0/A1

Status: **independent review evidence; no implementation admission; no Requirement promotion**

Review object: `102cc0804233d00c02f9ed856631f7538a8cc1e9`  
Repository authority checked against current `main@b448915cf774c573dbf82cf2e17bcb03c10a9ed8` and current GitHub owner state on 2026-10-04.

## Verdict

### `SHRINK A1 to derived-view-only`

The review confirms one material A0 failure: existing persistence, reconciliation and the small execution cursor do not yet provide a bounded, human-legible current problem/programme surface. A fresh worker can reconstruct the formal cursor and provenance, but the remaining active, unresolved, candidate, completed and historical landscape still requires cross-owner synthesis and Issue/audit archaeology.

The review does **not** confirm the proposed Method-Sufficiency disposition as necessary. The repository shows a plausible and important methodological pain, but not yet a sufficiently discriminating observed failure proving that an explicit new judgement record is the smallest required correction rather than correct composition of existing Competence, Research, Requirements, Design, Assurance, Integration and Learn owners. P-D is likewise not promoted: current evidence supports a clarification/design candidate, not a generic requirement or new adoption contract.

No new Building Block, Skill, Planner, Orchestrator, Bridge, Registry, parallel state store, automatic synchronization or lifecycle stage is supported.

## Fresh authority and state check

- Current `main`: `b448915...`, merge of PR #84.
- Frozen PR-85 head: `102cc080...`; current PR #85 is open, non-draft, unmerged, head unchanged, base `main@b448915...`.
- Planning source: `github:esany/Wissensarbeit#7`.
- Focus: `github:esany/Wissensarbeit#46`.
- Current step: `t5-case-c-trial`, no next action, `follow_up=not-derived`.
- `implementation_allowed=false`; allowed actions do not include implementation, design or merge.
- Current reconciliation is systemically integrated with no unresolved blockers.
- Open candidate owners #52, #53, #55, #86 and #87 remain candidates; none changes Authority, priority or implementation permission.

The later current-main state is not silently mixed into the frozen candidate: it is used only for authority/conflict checking. The frozen review object remains the reviewed design candidate.

## Independent reconstruction

`problem -> evidence -> requirement/quality/risk -> existing owner -> observed failure -> smallest sufficient correction`

The governing objective and existing contracts already strongly cover persistence, provenance, authority boundaries, systemic reconciliation, learning, restart foundations and reversible Git-native work. The decisive residual problem is narrower: the repository can externalize and validate state without yet projecting a bounded active problem surface that lets a Human Owner orient without reconstructing the programme from multiple historical owners.

The method question is different. The lifecycle and Building Blocks name the relevant capabilities and permit re-entry. Issue #86 and the design audit provide a credible hypothesis of premature solution-shaping, but the reviewed evidence does not isolate a failure that existing-owner composition cannot already express. A candidate pattern is not itself failure evidence.

## Case review

| Case | Decisive evidence | A0 | A1 | Existing owner | Observed gap | Smallest sufficient correction | Counterargument | Remaining uncertainty |
|---|---|---|---|---|---|---|---|---|
| C1 Long-running programme/problem state | `CURRENT_STATE.md` is reproducible and fresh, but exposes mainly counts, lifecycle, sources, reconciliation and one next operational proof. PR-85 baseline records repeated reconstruction from #7/history after local closures. | **Fail** for intended Human-legible orientation; formal cursor/provenance pass is not enough. | **Pass only for its view portion** if the surface is a projection, not a new owner. | BB-STATE, BB-CONTEXT, BB-DERIVE, BB-TRACE, Planning/Execution Cursor, #7. | No bounded active problem surface with explicit unresolved/candidate/completed/history distinctions. | Extend the rebuildable derived current surface with owner-linked dispositions and an explicit no-next-action boundary. | A competent worker can read the handoff and current owners; this may be sufficient for a narrow restart. | Need a simple-repository counterexample to calibrate when ordinary closure is enough.
| C2 Fresh restart | Restart evidence, material-state fail-closed rules, cursor freshness tests and PR-85 handoff. | **Pass** for restartability foundations; convenience alone does not justify A1. | **Partial**: lower orientation burden through the derived view, but no new restart contract is needed. | BB-CONTEXT, BB-STATE, Material State, Reconciliation, Derived Views, #7/#46. | The first orientation still depends on manually synthesizing the active landscape; this is residual burden, not absent persistence. | Rebuildable current surface; retain existing restart contracts. | A0 already meets REQ-001 if “restart” means reconstructing from bounded canonical state and handoff. | Human-legibility threshold and burden reduction need a bounded trial.
| C3 Current vs history | T5 and prior closures preserve local provenance and reconciliation; `follow_up=not-derived` correctly avoids inventing priority, but current/candidate/completed/superseded evidence is not co-projected. | **Fail** for cross-owner discrimination; **pass** for local transition correctness. | **Pass for view-only sharpening** if status is referenced, not copied. | BB-INTEGRATE, Reconciliation, BB-DERIVE, BB-TRACE, Git/GitHub owners. | Manual classification across owners; risk of history/current collapse in the default working surface. | Derived projection with explicit evidence-bound categories and historical pointers; no recency-based inference. | Labels/statuses can be added to existing Issues without a new view. | It is not yet shown which minimum metadata is stable across materially different repos.
| C4 Method / capability sufficiency | 2026-09-19 audit and #86 describe premature solution-shaping and candidate failure classes; lifecycle/BBs already support re-entry, research, requirements, design and assurance. | **Not proven fail**. Existing owners can express the judgement when correctly composed; evidence does not yet establish a missing contract. | **Fail as a necessary correction**; at most retain as a test hypothesis or compact optional explanation. | BB-COMPETENCE, BB-RESEARCH, BB-REQUIREMENTS, BB-DESIGN, BB-ASSURE, BB-INTEGRATE, BB-LEARN, lifecycle. | Plausible method-selection friction, but no isolated repeated failure requiring a new explicit disposition. | Run a bounded discrimination trial: existing composition vs optional compact method note, including trivial fix, uncertainty, re-entry and no-change cases. | Making the judgement explicit may prevent solutionism and human method-courier burden. | Cross-project evidence and a simple-repo negative control are missing.
| C5 Learning to current state | Reconciliation requires all affected surfaces and supports unchanged; BB-LEARN externalizes learning; T5 closure demonstrates strong local closure. | **Pass** for material-change closure; **partial** for programme navigation. | **Pass only as view binding**: expose the reconciliation/learning delta in the current surface. | BB-LEARN, BB-INTEGRATE, Reconciliation, BB-DERIVE. | Closure does not automatically shrink/re-project the active programme surface. | Derived view consumes canonical reconciliation outcome; no new learning owner. | A reconciliation packet already is the correct current state, and navigation is a planning concern. | Need a case showing materially less active burden after closure, not just a nicer summary.
| C6 Generic anchor to local adoption | Git diff/compare/selective application gives artifact choice/reversibility; Integration, Requirements, Design, Assurance and Reconciliation can judge local fit. No materially different consumer-project adoption trial is present. | **Pass** for mechanics and existing semantic authority; **not yet demonstrated** as a reusable adoption workflow. | **Not established beyond clarification candidate**; an explicit disposition could be useful, but is not yet evidenced as a required contract. | BB-INTEGRATE, BB-REQUIREMENTS, BB-DESIGN, BB-ASSURE, Reconciliation, Architecture Fitness, Git. | The generic/local boundary is implicit; Git selection alone does not establish fit. | For a later adoption trial, record local fit and authority in the existing integration/reconciliation evidence; do not create synchronization infrastructure. | The proposed fields may merely restate ordinary project decision records and add meta-work. | No materially different consumer project and no repeated cross-project failure.

## Derived View determination

The proposed Current Surface is acceptable only as a reproducible projection of canonical owner state. It must be generated from current cursor, reconciliation, owner references and explicit dispositions, with currentness bound to evidence rather than recency. It must preserve history pointers and unresolved conflicts, and must not infer priority from visibility.

Under those constraints it is **not** a second truth or second clock. It becomes one if a human must manually maintain active/current status separately from Issues, reconciliation and execution state, or if the view can drift while still being treated as current. The existing `CURRENT_STATE.md` freshness check proves provenance binding to the reconciliation packet, but does not yet prove the richer active-surface semantics.

## Method Sufficiency determination

The proposed disposition is currently disproportionate as a required contract. It risks becoming a hidden process stage unless it is falsified against clear local fixes, material uncertainty, re-entry and explicit no-change cases. Existing owners already carry the semantic responsibilities and lifecycle permits non-linear re-entry. Keep the question as an unresolved evaluation hypothesis, not as an accepted design correction.

## P-D disposition

**Requirement clarification candidate** (with **unresolved uncertainty** about generic fit); not a genuine promoted Requirement gap.

The evidence supports clarifying that a generic change must be evaluated against local purpose, requirements, decisions, risks and acceptance before adoption. It does not support a new generic requirement, registry, updater, product-line platform or automatic Generic-to-Project synchronization. A materially different consumer-project trial is required before stronger promotion.

## Negatives architecture check

The exclusions are supported by the evidence currently available. Existing owners plus a derived view can address the observed cases. No concrete failure demonstrates the need for a new Building Block, dedicated Skill, Planner, Orchestrator, Bridge, Resolver, graph/ontology runtime, Registry, parallel state store, automatic synchronization or rigid pipeline. Plausibility or conceptual elegance is not enough to reopen any exclusion.

## Alternatives rejected

- **A0 unchanged:** rejected only for the current-surface/current-history working-mode failure, not for persistence, authority or local reconciliation.
- **Full A1:** rejected because Method Sufficiency and generic-anchor adoption are not independently demonstrated as necessary contract changes.
- **Method-Sufficiency owner/phase:** deferred because it can create ceremony and a hidden pipeline before comparative failure evidence exists.
- **New capability/Building Block/Skill:** rejected because the residual failures map to existing owners and a derived projection.
- **Registry/second state store:** rejected because it violates single-owner/reversibility principles and lacks failure evidence.
- **Automatic synchronization:** rejected because local project autonomy and human acceptance remain material.
- **No correction at all:** rejected because current-state orientation demonstrably remains archaeology-heavy in this long-running repository.

## Failure severity and return level

No blocking design correction is required for the narrowed view-only result. The rejected Method-Sufficiency and P-D claims are **non-blocking for review**, but **blocking for any development package that would implement them**. The smallest return level is a derived-view design package plus a bounded discrimination plan; Method Sufficiency and generic adoption remain evaluation candidates.

## Verification distinction

Deterministic repository checks can verify schema, freshness, reconciliation completeness, provenance and cursor boundaries. They cannot prove Human legibility, correct current/history interpretation, method sufficiency or local adoption fit. Those require semantic review and bounded human/consumer-project acceptance.

## Required next package if this verdict is accepted

Before any implementation admission, the development package must specify:

1. canonical input owners and exact projection rules;
2. currentness, unresolved, candidate, completed, superseded and history semantics;
3. stale-view detection and no-second-clock invariants;
4. owner-linked provenance and authority boundaries;
5. a simple-repository negative control and this repository's long-running case;
6. deterministic checks for rebuildability/freshness plus semantic acceptance criteria for Human legibility;
7. explicit non-goals preserving no planner, registry, synchronizer, new store or lifecycle stage;
8. separate future trials for Method Sufficiency and generic-anchor adoption, without implementation authority or Requirement promotion.

This review does not authorize implementation, merge, priority selection, Requirement promotion, or changes to Planning Source, Focus or `implementation_allowed`.
