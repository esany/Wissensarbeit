# WA-AUDIT-2026-10-02 — Owner-Burden / Execution-Routing Thin Correction

Status: **bounded candidate correction / fresh-main derivation / independent review required / no promotion authority**

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

## Disposition of stale branch

Historical branch:

`fix/execution-routing-owner-burden-2026-10-02`

Current disposition: **evidence / partially reusable / implementation shape rejected**.

Retained evidence:

1. the Owner-burden incident is real;
2. routine route/permission mechanics should not be shifted to the Human when derivable;
3. unexpected permission requests require a concrete operational instruction rather than workflow reconstruction;
4. deterministic regression coverage is useful but cannot prove product UI/model behavior.

Rejected implementation shape:

- canonical route names such as `normal-chat-first` or `work-or-codex`;
- a generic Authority rule specifically about Chrome/browser access;
- product/vendor/application names as permanent core routing semantics;
- any interpretation that Authority itself becomes #48's quality/cost route-selection method;
- any interpretation that Authority becomes #55's task/instruction compiler.

Reason: those details are environment-specific evidence. Encoding them in generic Authority would increase coupling, stale semantics and second-owner risk.

## Smallest candidate correction

The current branch changes only the operational responsibility boundary in canonical Authority:

1. routine execution-route choice is AI-owned when derivable;
2. capability and permission preflight is AI-owned when derivable;
3. the AI checks adequate existing capabilities before escalating;
4. operational permission is requested only when necessary for a concrete required action unavailable through an already adequate capability;
5. convenience alone does not justify escalation;
6. execution route never transfers project/semantic/acceptance/priority authority;
7. when Human action is genuinely unavoidable, expose at most one action and state:
   - what to do;
   - why it is needed;
   - the exact option;
   - what the Human is not being asked to decide;
8. core semantics remain product/vendor/model/application/interface neutral.

## Existing-owner boundaries

### #48

Retains the candidate method question:

> Which available route preserves required quality/capability under contextual scarcity?

This correction does not implement that Skill. Authority only states that routine route mechanics are not a Human meta-decision.

### #55

Retains task/instruction compilation semantics, including smallest sufficient instruction and derive-before-asking. This correction only requires a concrete Human action instruction when action is unavoidable; it does not compile general task packets.

### #5

Retains continuity/restartability semantics across environment boundaries. No new run registry or handoff store is created here.

## Falsification / independent review target

A fresh reviewer must test both directions:

1. **No-change counterhypothesis:** current Authority already says enough (`maintain_required_project_operations`, `do_not_burden_human_with`), so the new operational-orchestration wording is redundant and should be removed.
2. **Under-specification counterhypothesis:** without the explicit responsibility boundary, the observed route/permission burden can recur while still appearing consistent with current generic Authority.

Reject or shrink the Authority delta if it:

- duplicates #48/#55 method semantics;
- embeds environment/product policy;
- adds more maintenance than operational clarity;
- creates a second routing owner;
- does not materially change the expected response to the observed Owner-burden case.

## Promotion boundary

This branch is a candidate only.

Formal CI can establish syntax/contract consistency and regression behavior; it cannot establish that the Authority refinement is semantically necessary or Human-effective.

No merge/promotion before fresh independent semantic review of the exact candidate head.

No downstream priority follows from completion of #80.
