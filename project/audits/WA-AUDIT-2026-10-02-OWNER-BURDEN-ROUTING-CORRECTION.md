# WA-AUDIT-2026-10-02 — Owner-Burden / Execution-Routing Thin Correction

Status: **bounded candidate correction / second independent re-review incorporated / F1 executable regression correction complete / no promotion authority**

## Trigger

The Human Owner had to ask which execution environment to use and whether an unexpected browser/permission request was actually necessary during repository/GitHub work.

This is direct Owner-burden evidence. It does not by itself authorize a new Skill, planner, scheduler, workflow engine, Requirement, Building Block or product-specific routing table.

Human priority is persisted in:

- Work Package #80;
- Planning Owner #7 comment `5959986881` (`Owner-Burden-Korrektur jetzt`).

## Fresh baseline

Candidate derived from `main@1e68aee25c75f7cf2ef90642c6ab101554808bf1`.

Freshly checked owners:

- `project/GOVERNING_OBJECTIVE.md`: automation must relieve the Problem Owner; meta-work must not become the product;
- `system/authority.json`: routine operational necessity is AI-autonomous and Human consultation is for material choices/meaning/consequences;
- #48: candidate owner of capability/quality/scarcity execution routing;
- #55: candidate owner of task/instruction compilation, including derive-before-asking and workflow-dumping failure boundaries;
- #5: persistence/restartability owner for continuity across environments;
- #7: Planning Owner;
- #80: only active correction candidate after Human priority selection.

## Independent semantic review sequence

### First independent review

Fresh independent review on writer head `da7d0a9003fe199468edb617fb3df78c5c5123bf` against main `1e68aee25c75f7cf2ef90642c6ab101554808bf1`:

- `https://github.com/esany/Wissensarbeit/pull/81#issuecomment-5961073344`
- Verdict: **ACCEPT WITH BOUNDED CORRECTION**.

It rejected the no-change counterhypothesis as a complete protection, while rejecting the first writer representation as non-minimal. Required corrections were:

1. remove the standalone `operational_orchestration` routing mini-contract;
2. keep one compact canonical responsibility boundary;
3. separate technical permission necessity from security/privacy/material-risk/consequential-action authorization;
4. replace the universal one-action cap with the smallest unavoidable Human action set, preferring one bundled instruction when sufficient;
5. rework deterministic coverage around semantic positive/negative invariants;
6. preserve #48/#55/#5 boundaries, product neutrality, #80-only cursor, no successor and no merge authority.

### Corrected-head independent re-review

Fresh independent re-review on corrected head `e77e7bae65681929bb86c0aa47e188cc48d6b13a` against the same main:

- `https://github.com/esany/Wissensarbeit/pull/81#issuecomment-5965774930`
- Verdict: **NEEDS FURTHER BOUNDED CORRECTION**.

The re-review marked the Authority shape, AI-owned routine mechanics, necessity-vs-authorization boundary, smallest unavoidable Human action set, #48/#55/#5 owner separation, product neutrality, #80-only cursor and reconciliation semantics **RESOLVED**.

Its sole material blocker F1 was evidentiary: `WA-EVAL-031`–`WA-EVAL-036` existed as declarative fixture inventory, but the executable tests did not consume the scenarios and their forbidden outcomes. No further Authority change was requested.

## Disposition of stale historical branch

Historical branch:

`fix/execution-routing-owner-burden-2026-10-02`

Current disposition: **evidence / partially reusable / implementation shape rejected**.

Retained evidence:

1. the Owner-burden incident is real;
2. routine route/permission mechanics should not be shifted to the Human when derivable;
3. unexpected permission requests require concrete bounded operational guidance rather than workflow reconstruction;
4. deterministic regression coverage is useful but cannot prove product UI/model behavior.

Rejected implementation shape:

- canonical route names such as `normal-chat-first` or `work-or-codex`;
- a generic Authority rule specifically about Chrome/browser access;
- product/vendor/application names as permanent core routing semantics;
- old #73/#74 and stale-main bindings;
- validator coupling to a product-specific route model;
- any interpretation that Authority itself becomes #48's quality/cost route-selection method;
- any interpretation that Authority becomes #55's task/instruction compiler.

## Corrected smallest candidate

Canonical Authority adds one compact `operational_responsibility_boundary` only.

It states that, when derivable from task/current state/available capabilities:

- AI carries routine execution-route choice, available-capability inspection, least-privilege technical preflight and technical permission-necessity mechanics;
- an already adequate capability is checked before stronger escalation;
- convenience alone does not justify escalation;
- technical necessity does not itself authorize security/privacy-sensitive permission, accept material risk or decide consequential external effects;
- route choice does not transfer project, semantic, acceptance or priority authority;
- if Human/specialist action remains unavoidable, only the smallest unavoidable action set is exposed;
- one bundled instruction is preferred when sufficient, but independent unavoidable decisions are not hidden to satisfy a numeric cap;
- each unavoidable action states `what_to_do`, `why_needed`, `exact_option`, `what_not_to_decide`.

There is no canonical product/vendor/model/application route table and no standalone routing mini-contract. The corrected-head independent re-review found no remaining Authority change necessary.

## Existing-owner boundaries

### #48

Retains the candidate method question:

> Which available route preserves required quality/capability under contextual scarcity?

This correction does not implement that Skill. Authority only assigns routine operational responsibility and preserves material authority boundaries.

### #55

Retains task/instruction compilation semantics, including smallest sufficient instruction and derive-before-asking. This correction constrains unavoidable Human burden but does not compile general task packets.

### #5

Retains continuity/restartability semantics across environment boundaries. No new run registry or handoff store is created here.

## Executable regression coverage — F1 correction

`tests/fixtures/owner_burden_cases.json` now uses schema `1.1` and retains the six bounded cases with structured scenario facts plus required `expected` and `forbidden` outcomes:

- `WA-EVAL-031`: existing adequate capability → no Human route decision;
- `WA-EVAL-032`: technically unnecessary stronger capability → no convenience escalation;
- `WA-EVAL-033`: technical permission necessity ≠ security/privacy/material-risk authorization;
- `WA-EVAL-034`: independent unavoidable Human actions remain explicit rather than artificially collapsed;
- `WA-EVAL-035`: operational route choice preserves project/semantic/acceptance/priority authority;
- `WA-EVAL-036`: product-specific incident evidence remains outside canonical Authority.

`tests/test_owner_burden.py` now:

1. deterministically interprets the canonical responsibility boundary into bounded policy predicates;
2. executes all six structured scenarios;
3. requires every declared `expected` outcome;
4. requires every declared `forbidden` outcome to remain absent on the canonical contract;
5. applies targeted negative contract mutations and verifies that the intended forbidden outcomes or missing expected outcomes are detected;
6. proves that every declared forbidden token is actually consumed by a negative probe.

Assurance #278 on intermediate head `7a7781db852bc0328d287b303c9783b6e5910238` correctly failed because one declared forbidden outcome (`escalate-for-convenience`) lacked a dedicated negative probe. That formal failure was corrected rather than waived.

Assurance #279 on F1-corrected code head `805a7e7dd8597fae42de656bce5ac0c8068f3888` is **SUCCESS**. The remaining audit persistence in this file changes evidence description only; fresh assurance is still required on the final exact PR head before independent confirmation.

These deterministic tests establish repository contract-regression behavior only. They do not establish model behavior, UI behavior, domain truth, Human effectiveness or owner acceptance.

## Cursor / reconciliation boundary

- Planning Owner remains #7.
- #80 remains the only active bounded Work Package.
- reversible design/implementation/check/evidence work remains admitted on the candidate branch.
- merge is not an allowed cursor action.
- no successor or downstream priority is selected.
- internal `systemically_integrated=true` does not grant promotion or merge authority.

## Promotion boundary

The latest independent re-review is correction evidence for head `e77e7bae...`, not acceptance evidence for the final F1-corrected head.

After this evidence update, the final exact PR head requires:

1. fresh formal assurance; and
2. a narrow independent confirmation that F1 is resolved without regression of the already-confirmed Authority/owner/cursor boundaries.

Only after that may the Human Owner receive the separate material promotion decision.

No merge/promotion is authorized by the Human priority selection, writer correction, internal reconciliation, CI or earlier reviews.

No downstream priority follows from completion of #80.
