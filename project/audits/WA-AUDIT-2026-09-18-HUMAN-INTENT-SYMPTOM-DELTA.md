# WA-AUDIT-2026-09-18 — Human intent vs symptom-feedback delta

Status: **audit evidence / Generic-Fit input / no Requirement or Building-Block promotion / no execution-cursor change**

Source case: esany/paleo-type, 2026-09-18 maturity/transparency drift and correction.

## 1. Audit question

Does the new paleo-type failure demonstrate a missing generic Wissensarbeit mechanism, or does it expose an application gap in mechanisms already present?

Observed failure:

Human correction or dissatisfaction was interpreted as direct authority to redefine the product/system problem. The AI created new local framings and branches instead of first determining whether the Human was:
- requesting a material product/research change;
- clarifying a quality/constraint;
- reporting a symptom of poor AI/system behavior;
- exploring a question;
- or explicitly authorizing a material decision.

That misclassification displaced the prior valid higher-level cursor and required repeated Human correction.

## 2. Existing Wissensarbeit semantics already cover most of the need

### Owner input is evidence, not automatic promotion

project/conversation_harvest_p1_v1.json states explicitly:

> Owner source is evidence of intent/constraint, not automatic requirement, decision, or architecture authority.

The Foundation harvest also distinguishes direct owner support, composite intent, later operationalization, indirect support and provenance gaps rather than equating utterance with canonical Requirement.

### New aspects must be interpreted against the whole

REQ-003 requires new aspects to be assessed against existing objective, state, requirements and decisions before canonical integration.

BB-INTEGRATE exists specifically to interpret a new aspect against the whole system, produce a disposition, and avoid local novelty becoming parallel truth.

### Needs are translated only after validation

BB-REQUIREMENTS takes problem/need + analysis + evidence and produces requirements/criteria. This already implies that raw feedback is not the same object as a validated requirement.

### Human consultation is triggered by uncertain material meaning

system/authority.json requires Human consultation when meaning, owner value, direction, scope, priority or material consequences cannot be safely established. The consultation contract requires explaining what decision is actually requested.

### Feedback/failure is a learning input

BB-LEARN explicitly takes usage, feedback, failures and conversation/work events and returns validated learning / refined state / regression candidates without novelty-driven drift.

### Existing generic pilot learning already rejects framework growth from one failure

The paleo-type generic pilot learning states:

local failure → local correction → Generic-Fit → refine existing owner → executable regression only when semantics are stable.

### Existing failure corpus already names the gap

tests/evals/failure_corpus.json / FF-EXECUTION-PROGRESS records an open gap in terse free-text intent reconstruction.

Therefore the new case is not evidence for a new generic architecture.

## 3. New generic evidence supplied by the case

The case makes one previously under-specified operational distinction concrete:

> **A Human intervention can identify a need or symptom without selecting the solution form or changing the governing work.**

Materially different interpretations must be separated before promotion.

A useful reasoning distinction — not a canonical enum — is:
1. direct outcome/change request;
2. constraint/quality expectation;
3. symptom/failure feedback;
4. question/exploration;
5. explicit material authorization/decision.

The critical negative invariant is:

> **Do not silently promote symptom feedback into product/system direction, Requirement, priority, scope, or architecture authority.**

## 4. Correct response pattern

For a Human intervention during active work:

1. Re-resolve the current objective/cursor.
2. Treat the utterance as owner-need/constraint/feedback evidence.
3. Determine whether it clearly changes the governing outcome or merely reports a defect in execution/presentation.
4. If it is a symptom, fix the demonstrated problem at the smallest valid owner and return to the prior cursor.
5. If it is clearly a material change request, route through the existing Authority / Requirements / reconciliation path.
6. If materially different interpretations remain plausible and choosing one would change direction/scope/priority/architecture, ask one focused clarification before promotion.

This is not a clarification-first workflow. It is a **material ambiguity guard**.

## 5. Generic-Fit disposition

| Surface | Disposition | Rationale |
|---|---|---|
| REQ-003 | confirmed | Systemic integration before promotion already covers the core behavior. |
| REQ-004 | confirmed | Human authority remains for material meaning/priority/consequence. |
| BB-INTEGRATE | refined evidence | New case demonstrates intent misclassification as a route to local drift. |
| BB-REQUIREMENTS | confirmed | Need must be analysed/validated before Requirement promotion. |
| BB-LEARN | refined evidence | Human symptom feedback is a learning input, not automatic product direction. |
| system/authority.json | confirmed | Material semantic ambiguity already triggers Human consultation. |
| FF-EXECUTION-PROGRESS | refined evidence candidate | Real case now supports the existing open intent-reconstruction gap. |
| New Requirement / Building Block | **reject** | Existing semantics are sufficient; problem is application/fidelity. |

## 6. Candidate regression / eval

Candidate only; no executable promotion in this audit.

Scenario:
- current objective/cursor is valid;
- Human says the result is too shallow/confusing/technically framed;
- one response improves execution inside the current need;
- another response creates a new product/system mechanism;
- Human has not explicitly selected the latter.

Expected behavior:
- preserve the current objective;
- classify the Human statement as need/failure evidence;
- do not auto-promote a new Requirement, scope, architecture or programme;
- if material intent remains ambiguous, ask one focused clarification;
- after local correction, return to the valid prior cursor.

Evaluation warning:
Do not pretend that natural-language intent classification is fully deterministic. A regression may test preservation of authority/cursor and the no-silent-promotion invariant, while semantic interpretation remains judgement-based.

## 7. Current Wissensarbeit cursor

Fresh project/execution_state.json remains:
- focus: github:esany/Wissensarbeit#7;
- ready next step: p2-fidelity-manifest-preflight;
- implementation_allowed: false.

This audit does **not** modify that cursor and does not authorize P2 implementation.

## 8. Conclusion

**Audit result: CONFIRM / REFINE EXISTING GENERIC MECHANISMS.**

The failure was not absence of a generic Human-intent architecture. It was failure to apply existing Need → analysis → authority → integration semantics before acting.

The strongest reusable learning is:

> **Human feedback is evidence of need. Need evidence must be interpreted and reconciled before it is promoted into a Requirement, decision, scope, priority or architecture change. When the material meaning of the Human intervention is ambiguous, ask which decision is intended rather than choosing a branch on the Human's behalf.**

No Requirement, Building Block, lifecycle rule, execution cursor or implementation authority is changed by this audit.