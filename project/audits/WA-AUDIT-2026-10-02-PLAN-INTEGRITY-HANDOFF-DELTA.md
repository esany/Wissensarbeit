# WA-AUDIT-2026-10-02-PLAN-INTEGRITY-HANDOFF-DELTA

Status: **bounded continuity/planning-integrity evidence / candidate / no priority or architecture promotion**

## Purpose

This audit persists the bounded result of the 2026-10-02 review of two connected questions:

1. how project-level planning should remain navigable without creating another mega-issue, planning registry or second project-management system; and
2. whether the current long ChatGPT conversation has itself become a continuity/drift risk that justifies a semantic handoff into a fresh chat.

This artifact does **not** select the next project priority, activate a new Work Package, create a Milestone/Parent hierarchy, change Requirements/Authority/Building Blocks, or promote the earlier QP-0…QP-6 planning synthesis.

Repository/GitHub state remains authority for current project state, execution, priority, promotion and acceptance. Chat-derived planning material is used only as recovery/provenance evidence.

## Fresh repository baseline

Freshly checked before persistence:

- repository: `esany/Wissensarbeit`;
- current `main`: `0853a30e32bdf078e75d5f69414097b68cc1a59a` (PR #71 post-P2 closure);
- planning owner: `github:esany/Wissensarbeit#7`;
- `project/execution_state.json`: P2 dependencies resolved, `implementation_allowed=false`, `follow_up.status=not-derived`, `candidate=null`;
- `project/reconciliation.json`: P2 promotion closure systemically integrated, no downstream priority selected;
- `project/CURRENT_STATE.md`: derived view only; not a roadmap;
- `system/material_state.json`: `handoff`, `session_end`, `environment_switch` and `context_compaction` are continuity boundaries;
- `system/reconciliation.json`: local completion does not imply programme completion and reconciliation does not manufacture priority;
- Issue #7 currently carries long historical planning/audit context, no milestone and no sub-issues;
- PR #37 remains an unmerged candidate whose selected model is existing mutable Planning Owner #7 + versioned immutable operationalization snapshot + late focused activation; it explicitly avoids seven premature work issues, a mutable registry, a new Building Block and workflow/agent machinery;
- Issue #43 demonstrates that Parent + bounded Child Work Packages can work well for a concrete, separately bounded development programme, with the detailed plan kept outside the parent issue;
- Issue #6 defines Milestones as optional target/baseline brackets, not mandatory workflow phases.

## Historical planning intent recovered

A current-chat historical planning source supplied by the Human Owner contains an earlier candidate operating model. Source role: **owner-provided historical planning text / recovery source / not current repository authority**.

Its material intent was:

- do not build a second project-management system;
- do not turn #7 into an ever-growing chronological mega-container;
- if a parent is used, keep it small and current-facing rather than an evidence store;
- perform actual work in bounded, closable Work Packages;
- use Git/PR/closed work as history rather than keeping history active;
- allow persistent information to grow while keeping active working context bounded;
- prefer a small fresh-agent bootstrap and load deeper evidence/history on demand.

The historical suggestion `Milestone → Parent → roughly 5–7 Work Packages` was a candidate organizational model, not an accepted project requirement or architecture.

## Finding 1 — no project-wide mega-parent is justified

The project does not currently need a new project-wide Parent Issue in addition to #7.

Reasoning:

- #7 already owns project-level planning/execution continuity by current `execution_state.json`.
- Creating another mutable parent would risk a second planning clock and parallel truth.
- PR #37 already contains a better-fitting candidate pattern: keep #7 as the mutable planning owner, persist versioned bounded planning/operationalization snapshots, and activate concrete work late.
- The current problem is not absence of issue containers; it is keeping strategic target/plan/current-work roles distinct and restartable.

Therefore the strongest current minimal hypothesis is:

```text
Governing Objective / Target Image
        ↓
existing Planning Owner #7
        ↓
small versioned Planning Baseline / snapshot
        ↓
one activated bounded Work Package
        ↓
project/execution_state.json
        ↓
PR / Evidence / Review / Real Proof
        ↓
Closure + Reconciliation
        ↓
fresh derivation against Target Image + Planning Baseline
```

This is a **candidate planning-integrity finding**, not yet a promoted planning architecture.

## Finding 2 — Parent/Child remains useful locally

Parent/Child is not rejected as a pattern.

Issue #43 provides a strong local example:

- one bounded parent owns a concrete Skill-development programme;
- a separate development plan holds detail;
- #44/#45/#46 are closable work packages with explicit dependencies and review gates;
- the parent does not become the detailed evidence store.

Therefore:

- project-wide new Parent: **not currently justified**;
- bounded Parent for a real coherent development programme: **valid situational pattern**;
- Child/Sub-Issue relation: **useful when a Work Package is actually activated**, not as speculative taxonomy.

## Finding 3 — no Milestone now

A Milestone is not currently required for planning integrity.

Issue #6 correctly frames a Milestone as a verifiable target/baseline bracket rather than a workflow phase. The project does not yet have a sufficiently settled product/release/qualification target that would justify introducing a Milestone merely for structure.

Candidate later use: a real qualification/release target such as a verified template/framework baseline, once its semantics are actually established.

## Finding 4 — long-chat continuity risk is material

Verdict: **`restart-now`, after bounded persistence of this audit + semantic handoff**.

This is not because long chats are inherently invalid. It is based on repeated concrete evidence in this conversation and repository history:

- a larger quality-revision synthesis previously remained chat-/Project-Knowledge-only and required a dedicated recovery audit;
- several planning interpretations were materially corrected during the same conversation (including execution-environment escalation, P2 closure interpretation, spontaneous next-priority selection and planning-structure assumptions);
- current valid repository state now differs materially from several earlier conversational states;
- the active chat therefore contains many plausible-but-superseded planning models alongside current ones;
- context compaction is explicitly a continuity boundary under `system/material_state.json`.

Counterevidence / limiting evidence:

- P1/Restart and later state mechanisms make the repository substantially more restartable than at project start;
- current P2 closure state is reconstructable from Git/GitHub;
- therefore the full transcript is **not** required as normal working context.

The appropriate response is not to copy the whole chat into the repository, but to create a semantic handoff whose normal boot remains repository-first.

## Recommended handoff hierarchy

```text
Primary
fresh repository / GitHub canonical state

    ↓ only if strategic provenance or unresolved synthesis is needed

Secondary
persisted semantic handoff / recovery snapshot

    ↓ only if a concrete material provenance question remains unresolved

Tertiary fallback
original long chat or Human-provided export/excerpt
```

Rules:

- Repository/GitHub always wins for current state, current authority, execution, priority and promotion.
- The semantic handoff is recovery context, not a second truth store.
- The original chat is deep fallback only.
- If the original chat is not technically addressable in a fresh context, record `source unavailable`; do not reconstruct it from memory.
- Owner statements recovered from chat are historical Intent/Need/Decision evidence subject to current authority resolution; AI statements are interpretation/candidate evidence unless independently supported.

## What should be persisted vs not persisted

### Persist now

- this bounded audit finding;
- one semantic fresh-chat handoff;
- pointer from existing Planning Owner #7 to the persistence candidate.

### Do not persist as new canonical project truth

- the whole chat transcript;
- QP-0…QP-6 as an authorized roadmap;
- a new project-wide Parent;
- a Milestone merely for planning structure;
- speculative Child Issues;
- a new planning registry, workflow engine, planner or orchestrator;
- any new project priority.

## Failure-pattern check

Applied late against the current repository failure families.

- `FF-STATE-CONTINUITY`: material planning/history in a single long chat is a demonstrated risk; mitigation here is bounded externalization + fresh restart, not transcript archiving.
- `FF-SYSTEMIC-DRIFT`: the handoff must resolve current truth freshly from Git/GitHub and cannot override the execution/reconciliation state.
- `FF-SOLUTIONISM-BLOAT`: a new mega-parent, pre-created 5–7 child issues, Milestone-by-default, registry or planner would exceed demonstrated need.
- `FF-EXECUTION-PROGRESS`: keeping the entire long conversation as the normal working context would increase reconstruction/context burden; the smaller normal boot is preferred.
- `FF-FALSE-ASSURANCE`: this persistence does not prove the future fresh-chat restart until an actual fresh-context use succeeds.
- `FF-AUTHORITY-PROMOTION`: this artifact creates no priority, admission, implementation or acceptance authority.

No new failure family is proposed.

## Candidate minimal planning role

Current strongest bounded hypothesis:

- Target Image: `project/GOVERNING_OBJECTIVE.md` and accepted normative sources;
- mutable planning owner: existing Issue #7;
- strategic current snapshot/baseline: small versioned artifact, if/when separately operationalized;
- active work: at most one selected bounded Work Package unless real evidence requires concurrency;
- execution cursor: `project/execution_state.json` only;
- evidence/closure: PR/evidence/review/reconciliation/Git history;
- history: closed/superseded Git/GitHub objects, not active planning containers.

This audit does **not** itself create that planning baseline or activate work to implement it.

## Restart boundary

Once this audit and `project/WA-HANDOFF-2026-10-02-FRESH-CHAT.md` are persistently visible in GitHub, the current long conversation should cease being the normal work context.

The fresh conversation should:

1. resolve current repository/GitHub state independently;
2. use the handoff only as orientation/recovery context;
3. not select a new priority merely because this audit exists;
4. return to the Human only if a genuine material priority/meaning decision remains after fresh derivation.

## Non-decisions

This audit does not decide:

- #4 vs #5 vs #6 vs #37 vs #48 vs #52/#53/#55 or any other priority;
- whether a planning baseline should later be a specific filename or GitHub construct;
- whether PR #37 should be promoted;
- whether a future milestone is needed;
- product/template/release architecture;
- QP sequencing;
- new Requirements or Building Blocks.

## Completion boundary for this persistence packet

The persistence packet is complete when:

- this audit is stored on a reviewable Git branch/PR;
- the semantic handoff is stored beside it;
- Planning Owner #7 has a durable pointer to that candidate persistence;
- no current priority/execution authority is changed;
- the next normal interaction can begin in a fresh chat using repository-first bootstrap.
