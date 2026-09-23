# WA-AUDIT-2026-09-23 — Learning assurance overclaim delta

Status: **audit evidence / Generic-Fit input / no Requirement, Building Block, lifecycle, P2 correction scope or execution-cursor change**

Source case: `esany/paleo-type`, learning-integration claim repair, 2026-09-23.

## 1. Audit question

Does the paleo-type Failure B — a persisted learning was described to the Human as if it had already created reliable future operational behavior — demonstrate a missing generic `Wissensarbeit` mechanism?

## 2. Observed failure

The source case had these states:

1. a real Human-feedback failure was observed;
2. the learning was persisted as non-normative failure/audit evidence;
3. no new METHOD/Requirement had been promoted;
4. no executable behavioral regression had been added;
5. no independent fresh-context fixture had demonstrated changed future behavior;
6. nevertheless the assistant described the behavior as if it would apply “going forward”.

The error is therefore not loss of persistence. It is **assurance inflation**:

```text
persisted learning evidence
≠ normative integration
≠ executable enforcement
≠ regression-tested behavior
≠ real-world future-behavior proof
```

## 3. Existing generic owners already cover the semantics

### FF-FALSE-ASSURANCE — direct fit

The existing failure family states:

> Evidence is described more strongly than it supports.

Its existing open gap states:

> Natural-language claims need evidence-calibrated regression grading.

The paleo-type case is direct real-world evidence for this already-defined gap.

### REQ-007 / REQ-011

- REQ-007 requires end-to-end linkage among requirements, decisions, implementation and verification.
- REQ-011 requires deterministic checks, judgement-based reviews and Human acceptance to remain distinguishable.

The source failure collapsed precisely those distinctions in Human-facing language.

### BB-LEARN

BB-LEARN outputs validated learning / regression candidates. Its semantics do not imply automatic normative or executable promotion.

### BB-ASSURE

BB-ASSURE exists to keep validation, review and acceptance classes separate. A persisted learning is not by itself tested behavior.

### BB-TRACE

BB-TRACE must explain what actually changed, with what authority and consequence. Claiming future operational behavior without an actual mechanism/test violates this explanatory boundary.

### BB-INTEGRATE / reconciliation

The reconciliation contract already states that a material change must not be described as systemically integrated before the required reconciliation is complete, and reconciliation itself does not grant material authority.

The same general assurance principle supports the source-case correction.

## 4. Generic-Fit disposition

| Surface | Disposition | Rationale |
|---|---|---|
| FF-FALSE-ASSURANCE | **confirmed with new real-world evidence** | Exact demonstrated failure family. |
| FF-AUTHORITY-PROMOTION | secondary confirmation | Non-normative evidence was implicitly presented as a stronger state. |
| FF-EXECUTION-PROGRESS | unchanged for Failure B | Human-intent reconstruction remains relevant to the separate Failure A. |
| REQ-007 | confirmed | Trace must extend through actual verification, not rhetorical implication. |
| REQ-011 | confirmed | Evidence/review/test/acceptance classes must remain distinct. |
| BB-LEARN | confirmed | Learning output is not automatic enforcement. |
| BB-ASSURE | confirmed | Assurance classes already separate. |
| BB-TRACE | confirmed | Human explanation must not overstate effect. |
| BB-INTEGRATE | confirmed | Integration claims require actual integration evidence. |
| New Requirement | **reject** | Existing Requirements already own the distinction. |
| New Building Block | **reject** | Existing blocks already cover it. |
| Lifecycle change | **reject** | No missing lifecycle stage demonstrated. |

## 5. Regression disposition

The case strengthens the need for an **evidence-calibrated natural-language eval**, but does not justify pretending the whole problem is deterministic.

A future eval should discriminate among statements such as:

- “the failure is documented”;
- “the learning is reconciled”;
- “the rule already exists normatively”;
- “an executable mechanism was added”;
- “a regression passed”;
- “future behavior is guaranteed”.

The expected answer must be bounded by the strongest actual evidence.

Do not implement a lexical check that merely looks for words like `FAILURE EVIDENCE ONLY`; that would not test the semantic claim-calibration failure.

## 6. Current programme boundary

Fresh `project/execution_state.json` on 2026-09-23 shows:

- focus remains `github:esany/Wissensarbeit#7`;
- current work is the separately admitted P2 Context-Fidelity correction;
- `implementation_allowed=true` only inside that explicit correction scope;
- this audit does not consume or expand that scope.

This file is evidence persistence only.

## 7. Generic conclusion

**CONFIRM EXISTING GENERIC MECHANISMS / ADD REAL-WORLD EVIDENCE.**

The new case does not show that `Wissensarbeit` lacks a conceptual owner for the problem. It shows that its already-known false-assurance gap has another concrete manifestation:

> **Persisting a learning is not evidence that the system has operationally integrated, enforced, tested or real-world-proven the corresponding future behavior. Human-facing claims must remain calibrated to the strongest actual assurance state.**

No Requirement, Building Block, lifecycle rule, implementation admission or execution cursor changes through this audit.
