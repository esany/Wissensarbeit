# paleo-type pilot analysis — generic learnings

## Boundary and provenance

- Source case: `esany/paleo-type`
- Fresh source checkpoint: `833da352f5a54baa9ae1727fd6f9452e3a46a852` (2026-09-13)
- Material source threads include `paleo-type` Issues #165, #166 and #169 and their canonical Project/METHOD owners.
- Related whole-repository audit: `project/audits/WA-AUDIT-2026-09-13.md`.
- Purpose here: retain **generic pilot evidence and dispositions only**.
- Authority: analysis/evidence/candidate input. This file does **not** accept a new Requirement, Building Block, architecture, workflow, domain model or implementation scope.

Case-specific manuscript readings, archival identities, source relations and scholarly conclusions stay in `esany/paleo-type`. They are deliberately not copied here.

## Why this pilot is useful for Wissensarbeit

`paleo-type` stresses the generic system with evidence-constrained, transdisciplinary work in which source identity, exact evidence, scholarly judgement, AI assistance, deterministic tooling, owner authority and restartable project state must coexist without silently acquiring each other's meaning.

The useful generic evidence is therefore not a palaeography model. It is the set of recurring failure and correction patterns that appear when knowledge work moves between direct evidence, interpretation, support tooling and persistent project state.

## Dispositioned generic learnings

| Learning | Observed generic failure pattern | Existing Wissensarbeit mechanisms | Disposition |
|---|---|---|---|
| Canonical ownership must remain distinct from derived human/AI views. | A convenient summary, path, comparison or generated view can become a second truth source and outlive the state it summarized. | `BB-STATE`, `BB-DERIVE`, `BB-TRACE`; `Q-TRACE`, `Q-COHERENCE`; `R-003`. | **confirm/refine existing** — derive views from canonical owners and make non-canonical status explicit; no new store. |
| Evidence/capability readiness is a ladder, not one `available` flag. | Identity, reproducibility/retrievability, target-context staging, actual inspectability and inspection can be silently collapsed. | `BB-CONTEXT`, `BB-ASSURE`, `BB-TRACE`, `BB-OPERATE`; `Q-DOMAIN`, `Q-XAI`; `R-004`, `R-008`. | **refine candidate** — a task context should state only the readiness level actually evidenced and must not promote identity/access metadata into task-ready evidence. |
| The analysis/work unit may itself be a hypothesis. | A lower-level observation can be over-atomized, while a higher-level synthesis/comparison can over-group distinct observed units. | `BB-INTEGRATE`, `BB-RESEARCH`, `BB-ASSURE`; `Q-DOMAIN`, `Q-FIT`; `R-004`, `R-009`. | **confirm existing epistemic boundary** — do not let routing convenience, labels or comparison mappings pre-answer a material domain unit/structure question. |
| Independent review must be independent enough at the evidence-basis level. | A fresh reviewer can inherit the same downstream premise if all reviewed summaries depend on one untested lower-level assumption. | `BB-ASSURE`, `BB-TRACE`, `BB-CONTEXT`; `Q-XAI`, `Q-DOMAIN`; `R-009`. | **refine candidate** — when the disputed claim is structural/semantic, review should trace that premise to the strongest direct owner/evidence needed to test it; fresh context alone is not sufficient independence. |
| Support progress and domain progress are different legitimate deltas. | State synchronization, CI repair, access/debug work and review can recursively generate more support work before the first domain action occurs. Each step can be locally useful while the knowledge question does not advance. | `BB-CONTEXT`, `BB-INTEGRATE`, `BB-ASSURE`, `BB-OPERATE`, `BB-LEARN`; `Q-LEAN`, `Q-FIT`; `R-007`, `R-008`. | **high-value Generic-Fit candidate** — identify the first material/domain action and its minimum prerequisite path; distinguish enabling/support delta from domain/knowledge delta; stop support→support escalation that neither enables that action nor protects an immediate invariant. No new workflow engine. |
| A real blocker or unresolved result is a valid terminal work result. | Systems can manufacture apparent progress by switching to metadata, parallel evidence, tooling or plausible completion when decisive evidence is unavailable. | `BB-ASSURE`, `BB-TRACE`, `BB-LEARN`; `Q-DOMAIN`, `Q-XAI`; `R-004`, `R-008`. | **confirm/refine existing** — preserve `blocked`/evidence-ceiling/unresolved states instead of simulating domain completion. |
| Semantic meaning is owned locally and must survive boundary crossings. | Identical words such as `complete`, `PASS`, `source`, `owner`, `evidence`, `role` or `validation` can acquire stronger/different meaning when moved between domain, software, AI and human language. | `BB-INTEGRATE`, `BB-REQUIREMENTS`, `BB-TRACE`; `Q-DOMAIN`, `Q-XAI`, `Q-COHERENCE`; `R-004`, `R-005`. | **confirm existing direction; candidate refinement** — consequential translation/handoff should preserve claim type, target/scope, evidence/authority level and uncertainty rather than rely on lexical equivalence. Avoid a universal glossary unless repeated evidence justifies it. |
| Local failures should generalize through Generic-Fit, not through immediate framework growth. | One concrete failure can tempt a new schema, role, ontology, service or method family even when an existing mechanism already owns the concern. | `BB-INTEGRATE`, `BB-LEARN`, `BB-DESIGN`; `Q-LEAN`, `Q-COHERENCE`; `R-002`, `R-003`, `R-006`, `R-007`. | **strongly confirmed** — `local failure → local correction → Generic-Fit → refine existing owner → executable regression only when semantics are stable`; new generic blocks require repeated independent friction. |
| Restartability is a knowledge-externalization test, not merely recovery convenience. | If a fresh context needs an old chat to know target, evidence state, authority, uncertainty or next legitimate action, material organizational knowledge remained implicit. | `REQ-001`, `REQ-002`, `BB-STATE`, `BB-CONTEXT`, `BB-TRACE`, `BB-DERIVE`; `Q-RESTART`. | **confirmed by independent case behavior** — retain restart tests as semantic project-state checks, not just file/schema checks. |
| Freshness must follow state transitions, not only view regeneration. | A change can be correctly merged while a restart surface still points to the immediately prior lifecycle state until explicit post-transition reconciliation occurs. | `BB-INTEGRATE`, `BB-DERIVE`, `BB-ASSURE`; `Q-RESTART`, `Q-COHERENCE`; `R-008`. | **cross-pilot evidence for current Wissensarbeit audit** — freshness checks should bind a current view/cursor to the material transition it claims to represent, not merely prove that a view is reproducible from an older snapshot. |

## Fit to the existing 14 Building Blocks

The pilot does **not** demonstrate a missing fifteenth Building Block. The strongest fit is a refinement of existing capabilities:

```text
BB-STATE       canonical ownership / one durable owner
BB-CONTEXT     bounded task context + evidence/capability readiness
BB-INTEGRATE   Generic-Fit + semantic boundary preservation
BB-ASSURE      evidence-basis review + deterministic/judgement separation
BB-TRACE       claim/evidence/authority/restart explanation
BB-DERIVE      rebuildable non-canonical human views
BB-OPERATE     only support work required to make the actual work executable
BB-LEARN       concrete failure -> disposition -> regression candidate
```

This reinforces the existing composition principle that generic blocks are capabilities, not mandatory folders, agents or services.

## Candidate regression/evaluation scenarios

These are **candidate scenarios**, not accepted new system semantics. They should be promoted to executable regressions only where the expected invariant can be stated stably without pretending to automate domain judgement.

### PT-GEN-001 — evidence readiness must not be over-promoted

Given a canonical evidence identity and a known retrieval/provenance path, but no proof that the exact evidence is staged/inspectable in the target execution context, the system must not claim that direct evidence inspection is executable or completed.

### PT-GEN-002 — support-dominance before first domain action

Given an authorized domain work item with a clearly identifiable first domain action, if a support action exposes another support action before that first domain action occurs, the next support action is justified only when it directly enables the first domain action or protects a required immediate invariant. Otherwise defer it or stop at the real blocker.

### PT-GEN-003 — review-premise tracing

Given a contested structural/semantic claim and multiple downstream summaries that share the same premise, a fresh-context review must not be classified as independent validation solely because the execution context is new; it must expose which direct owner/evidence layer supports the contested premise or leave that premise unvalidated.

### PT-GEN-004 — analysis unit must not be inferred from mapping convenience

Given two directly observed units and one broader comparison/mapping range, the system must not infer that the mapping range establishes a single domain analysis unit unless the owning domain evidence supports that claim.

### PT-GEN-005 — terminal real blocker remains progress without false completion

Given a valid authorized question whose decisive evidence cannot currently be used, the work block may terminate as `REAL BLOCKER` / evidence ceiling with preserved next-entry condition. It must not satisfy completion by substituting unrelated support work, parallel context or technical green state.

## Implication for the current Wissensarbeit P2 preflight

The pilot gives useful evidence for the already-selected `p2-fidelity-manifest-preflight`, but it does not authorize implementation.

A lean P2 concept should test whether a compiled work context can explicitly preserve, by reference where possible:

- the current material question/work item and authority;
- the **first domain/knowledge action** that would change the answer or establish an evidence ceiling;
- exact evidence/capabilities required for that action and their evidenced readiness level;
- included and deliberately omitted context;
- unresolved claims/uncertainty;
- semantic owner/claim type where a consequential term crosses a boundary;
- completion/stop conditions and the real blocker if the action is not executable.

This should be evaluated first as a bounded context-fidelity/problem-fit slice. It is not evidence for a new planner, universal claim ontology, evidence platform, workflow state machine, agent framework or dashboard.

## Non-goals / explicit non-promotions

No change is implied here to:

- `REQ-001..REQ-013`;
- the 14 Building Blocks;
- Authority or lifecycle semantics;
- the current execution cursor or P2 implementation authority;
- any `paleo-type` domain state;
- a universal evidence ontology, domain ontology, workflow engine or agent architecture.

The next generic move, if any, should be a small Generic-Fit/reconciliation decision against current `Wissensarbeit` state and real consumer work, not automatic architecture growth from this single pilot.
