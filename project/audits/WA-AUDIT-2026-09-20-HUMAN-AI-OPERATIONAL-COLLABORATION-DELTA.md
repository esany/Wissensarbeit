# WA-AUDIT-2026-09-20 — Human–AI operational collaboration and function-allocation delta

Status: **material audit evidence / Human-Owner intent capture / operationalization-gap synthesis / no Requirement, Building-Block, lifecycle, priority, cursor or implementation promotion**

## 0. Fresh baseline and authority boundary

Fresh repository baseline before this audit branch:

- canonical `main`: `b590523d31db5f82628d6e0d5182821501729906`
- planning owner/focus: `github:esany/Wissensarbeit#7`
- current canonical step: `p2-fidelity-manifest-preflight`
- P2 preflight: canonically completed and independently qualitatively `CONFIRM`ed
- next P2 candidate: `p2-implementation-admission`, still blocked on explicit Human admission
- `implementation_allowed=false`
- no P2 implementation is authorized by this audit.

This audit is based on direct Human-Owner evidence from the current 2026-09-20 ChatGPT conversation plus fresh repository inspection. The current chat does not expose a stable repository-addressable turn ID in this work context. Therefore the exact owner wording is preserved here by detailed semantic capture rather than by inventing a false durable chat reference.

Owner utterances are treated as primary evidence of need, pain, intent, role expectation and observed failure. They are **not** automatically promoted to Requirement, architecture, priority or implementation authority.

This audit does not change the current execution cursor. It does not decide whether a new Building Block is needed. It does not admit P2 implementation.

---

## 1. Audit question

The immediate trigger was a sequence in which the Human Owner repeatedly had to correct the assistant's framing of the same family of problems.

The audit asks:

> Does the current `Wissensarbeit` system adequately operationalize the end-to-end collaboration between a non-specialist Human Owner and an AI system, including intent reconstruction, competence acquisition, context/work instruction compilation, partial automation, Human review/decision context, uncertainty, iterative learning and cumulative correction fidelity?

A second question is methodological:

> Has the project been too willing to count a declared contract, Building Block or validated schema as evidence that a Human-facing capability is operational, even when real use still forces the Human Owner to perform the missing work?

---

## 2. Executive finding

**Finding: MATERIAL SYSTEMIC GAP / existing semantics are broad, operational collaboration is not yet end-to-end adequate.**

The current repository already contains many of the right normative ideas:

- autonomous routine work and explicit Human material authority;
- bounded context compilation;
- competence discovery;
- SOTA / best-practice research;
- Human explainability;
- automatic decision-brief semantics;
- Assurance / Trace / Integration / Learn owners;
- uncertainty and provenance preservation;
- Conversation Harvest;
- a now-canonical P2 Context-Fidelity preflight.

However, the current conversation supplies direct real-use counterevidence that these parts do not yet compose into a sufficiently operational Human–AI working system.

The Human Owner repeatedly had to do work that the system's own objective says should be absorbed by the system:

- correct the assistant's problem framing;
- restore previously stated constraints that had fallen out of focus;
- distinguish a workflow transition from a real work iteration;
- insist that review context be decision-ready rather than merely concise;
- explain that the Human is not a prompt engineer;
- explain that the Human is not the assistant's domain or technology expert;
- insist that vague, terse input is legitimate;
- remind the assistant to research when uncertain;
- remind the assistant that uncertainty and open-endedness are allowed;
- restore partial automation as a first-class problem after it was dropped;
- correct the assistant for making equal system problems subordinate to the review example;
- correct a surface audit that treated "already declared in the repo" as if it meant adequately operationalized;
- request this new audit because the prior synthesis still omitted material inputs.

The system is therefore currently stronger at **describing desired collaboration and governing changes** than at **executing that collaboration reliably with low Human meta-work**.

The central gap is not "the review problem", "the prompt problem" or "the XAI problem". Those are separate, equal system-level manifestations of an incomplete operational collaboration model.

---

## 3. Human-Owner intent — detailed preservation

The following intent must be retained together. Removing one part changes the meaning of the whole.

### 3.1 Human role

The Human Owner is **not** the AI's assistant.

The Human Owner should not be expected to:

- construct expert prompts;
- enumerate the repository files the AI should inspect;
- specify technical workflow steps the AI already knows are necessary;
- provide correct domain terminology;
- provide correct software/architecture terminology;
- know which competence discipline is missing;
- decide whether a problem belongs to UX, requirements, research, architecture, assurance or operations;
- reconstruct project state for the AI;
- manually carry context between work phases;
- manually orchestrate repeatable multi-step procedures;
- read raw complexity without orientation merely because the final decision remains Human.

The intended Human contribution is purpose, observations, experience, constraints, values, feedback, questions and material decisions.

### 3.2 Minimal and imperfect Human input is legitimate input

The Human explicitly states that they are neither the relevant domain expert nor the relevant technology expert and will normally provide:

- short;
- incomplete;
- colloquial;
- terminologically imprecise;
- potentially technically incorrect;
- symptom-level

instructions.

This is not an input defect to be repaired by demanding a better prompt.

Expected system behavior:

1. reconstruct as much as safely possible from current canonical context;
2. identify what competence is needed;
3. research current best practice / SOTA when uncertainty warrants it;
4. make assumptions and uncertainty visible;
5. ask the Human only when materially different interpretations remain and Human meaning/authority is required.

The desired pattern is **not clarification-first** and also **not silent inference**.

### 3.3 Human review and decision context

When Human review or a material decision is required, the Human needs:

- orientation: where are we and why am I being asked now?
- context: what came before and what remains unchanged?
- the concrete change;
- why it matters;
- what evidence supports it;
- what deterministic checks passed or failed;
- what qualitative judgement occurred;
- what uncertainty remains;
- alternatives and relevant counterarguments;
- consequences and reversibility;
- the exact scope of the requested decision;
- explicit non-decisions;
- traceability to underlying evidence and diffs.

The Human should not have to assemble this from multiple repository surfaces.

### 3.4 Explainability is not destructive abstraction

The Human explicitly rejects the equation:

`readability = shorter summary`

and the related equation:

`XAI = abstraction away from complexity`.

The need is to make complexity **navigable and understandable without deleting material structure**.

A suitable direction is layered/progressive disclosure:

- immediate orientation;
- structured reasoning and uncertainty;
- detailed evidence;
- underlying source / diff / provenance.

The top layer may be concise, but the system must preserve accessible depth.

### 3.5 Good prompts are an operational bottleneck

A central pain is that high-quality work currently depends on carefully crafted prompts describing:

- which repository state to read;
- which authority boundaries matter;
- which evidence to compare;
- what not to infer;
- which checks to run;
- how to stop;
- how to treat uncertainty;
- which previous review findings remain relevant.

The Human Owner cannot and does not want to construct these prompts.

The AI/system generally already knows what it needs to do. Therefore repeated prompt construction is system work and should be compiled from intent + state + authority + evidence.

### 3.6 Partial automation is a first-class problem

The Human highlighted the PR #35 review/correction/re-review sequence as a concrete example of a **partially automatable process**.

The problem is not merely to automate the final review judgement.

The system should decompose a workflow into functions and allocate them appropriately:

- deterministic / routine steps;
- AI judgement;
- specialist judgement when necessary;
- Human material authority.

For the PR #35 example, many steps were repeatable and derivable:

- fresh state acquisition;
- base/head binding;
- relevant owner/evidence compilation;
- prior finding reconstruction;
- assurance binding;
- correction-scope checking;
- focused re-review instruction generation;
- review evidence persistence;
- state/reconciliation hygiene;
- preparation of a Human promotion decision.

Those steps were largely orchestrated by long prompts. The Human regards that prompt-level orchestration burden itself as a gap.

This example must not become the parent category for all other problems. Partial automation/function allocation is one **equal system-level problem axis**.

### 3.7 Uncertainty and open-endedness are valid states

The project is explicitly outcome-open.

The system must permit:

- uncertainty;
- unknowns;
- multiple hypotheses;
- failure to confirm an assumption;
- `no change`;
- `defer`;
- `reject`;
- reframe/refine;
- iteration and reversal.

The system should not manufacture certainty, force a solution, or close a question merely to make the workflow look complete.

### 3.8 Error culture and transparent iteration

Errors are expected in complex work.

The desired response is not to hide or rewrite them into an idealized linear process.

The system should preserve:

- what was believed before;
- what failed;
- the correction;
- why the correction was necessary;
- what was learned;
- what future behavior changes because of the learning.

Iteration history is therefore part of explainability and system learning.

### 3.9 Learning must be operationalized

A "learning" is not sufficiently captured merely by recording prose.

A mature learning loop should be able to connect:

`observation/failure → interpretation/hypothesis → validated learning → affected owner → operational change or explicit no-change/defer → regression/check/workflow change where appropriate → later effectiveness evidence`.

A learning that changes no future behavior and has no explicit disposition remains weakly operationalized.

### 3.10 Real-use pain is counterevidence to an operationalization claim

The Human provided an explicit diagnostic rule:

> If the Human has to raise the problem in chat, the system should not treat the existence of a Requirement, Building Block or contract about that problem as evidence that it is adequately operationalized.

This does **not** mean every complaint proves the canonical design wrong.

It means real-use friction must downgrade unsupported claims of operational adequacy and trigger a deeper check of the actual path:

- is the feature only declared?
- is it wired to a real trigger?
- is it executable?
- is it regression-protected?
- has it been exercised in a real workflow?
- does it actually reduce the Human burden it promised to reduce?

### 3.11 Existing promised capabilities gain priority evidence when they fail in real use

The Human explicitly asked that already-created mechanisms receive **more**, not less, attention when current real-use evidence shows that the promise is not fulfilled.

The incorrect reasoning is:

> "This is already in REQ-X / BB-Y, therefore it is not a major new concern."

The stronger reasoning is:

> "This behavior was already promised, and the Human still encounters the failure; therefore the implementation/evidence gap is more strongly demonstrated."

This is prioritization evidence, not automatic execution-cursor authority.

### 3.12 Equal system-level problems must remain equal

The Human corrected the assistant after it made the review loop the conceptual center and placed other concerns underneath it.

The intended structure is:

- multiple equal overarching operational collaboration problems;
- shared root causes and interfaces;
- specific workflows, such as PR review, are evidence/examples that cross several axes;
- no one example should collapse the whole system finding into its own local vocabulary.

---

## 4. Conversation audit — chronology and observed assistant failures

This section audits the interaction itself because it is evidence.

### C1 — Transition mistaken for iteration

After the P2 preflight review was complete, the Human asked for a prompt.

The assistant produced a large promotion/post-merge gate prompt and called it the next workflow. The Human corrected:

> this is not an iteration.

Failure:

- process-state distinction was not preserved;
- a transition/gate was confused with substantive work iteration;
- the Human had to restore lifecycle semantics.

### C2 — Partial automation correctly identified, but initially review-centered

The Human asked whether the review process could become a generic partially automated capability.

The assistant correctly mapped it to existing owners and avoided immediately inventing a new top-level Building Block.

Useful learning:

- review workflow is strong real evidence for partial automation/function allocation;
- judgement and Human authority must remain distinguishable.

Incomplete aspect:

- this began a tendency to use "review" as the organizing center.

### C3 — Human decision context and prompt burden introduced

The Human then added two major equal concerns:

1. Human review requires context, orientation, clarity and transparency despite complexity;
2. "good prompts" are themselves a bottleneck because the Human is not the AI's assistant.

The assistant derived useful concepts such as decision-ready review packets and work-instruction compilation.

However, the conversation had now established at least three separate top-level concerns:

- partial automation;
- Human decision context/XAI;
- work instruction/prompt autonomy.

### C4 — Human role and uncertainty model clarified

The Human explicitly clarified:

- they are not the domain expert;
- they are not the technology expert;
- they will provide vague minimal instructions;
- the system must infer from context or ask;
- uncertainty is allowed;
- the project is outcome-open;
- error culture, iteration and transparency are central;
- research best practice/SOTA when unsure;
- document learnings operationally.

The assistant captured many of these, but initially converted them into a small capability list. That abstraction was useful but already risked losing the detailed behavioral requirements.

### C5 — Requested whole-system repo validation

The Human asked to structure **all ideas, requirements and underlying needs**, validate them against a fresh repository audit, and increase priority when already present.

The assistant did a fresh repository check but over-weighted the existence of canonical semantics.

It concluded that "almost everything is already laid out" and framed the main gap as operationalization.

The second half was useful; the first half was too surface-level.

### C6 — Human corrects the surface-audit error

The Human stated:

> If I write it here in chat as a problem, it means it is not well operationalized. Do not look only at the surface.

This is a material methodological correction.

The assistant then inspected runtime paths and found:

- `decision_brief.json automatic=true` has no demonstrated automatic generator in `work.py`;
- `context()` remains a near-full dump;
- current Human gate information is not surfaced well;
- competence and research are largely declarative in the operational core;
- current tests validate contracts more than Human-effective behavior.

This deeper method is closer to the required audit standard.

### C7 — Partial automation was lost from focus

Despite the deeper runtime audit, the assistant again omitted the original partial-automation problem from the center of its synthesis.

The Human had to explicitly say that the "actual problem case of partial automations" had been forgotten.

This is important evidence of **cumulative intent loss**:

- the assistant could improve locally after correction;
- but new framing displaced prior material findings;
- corrections were not being accumulated into one stable model.

### C8 — Partial automation restored, but then over-centralized

The assistant restored the PR #35 partial-automation case in detail and described the potential generic review workflow.

This was substantively useful.

But it then made that workflow the conceptual center again.

### C9 — Human corrects hierarchy

The Human clarified that the supposed partial problems are **not subtopics of review**, but equal overarching problems.

This establishes a structural constraint on the system finding:

- no review-centric hierarchy;
- no prompt-centric hierarchy;
- no XAI-centric hierarchy;
- equal axes with shared systemic roots.

### C10 — First whole-system synthesis remained incomplete

The assistant proposed a "Human–AI Operational Collaboration Gap" and six equal axes.

That was directionally correct, but still omitted two material aspects:

1. **cumulative correction / semantic continuity inside the interaction itself**;
2. a strong **operationalization-evidence discipline** distinguishing declared contracts from Human-effective capability.

The current Human request for another detailed audit is itself evidence that the previous synthesis was still too lossy.

---

## 5. Whole-system model: equal overarching problem axes

These axes are **peer problems**. Their order below is not a priority ranking.

### AXIS-A — Human role, minimal input and intent reconstruction

**Need**

The Human can provide terse, imperfect, symptom-level input without becoming a domain analyst, requirements engineer or prompt engineer.

**Expected behavior**

- bind the current project/objective/cursor;
- interpret the utterance as evidence, not automatic authority;
- distinguish request / observation / symptom / constraint / hypothesis / decision;
- reconstruct plausible meaning from context;
- preserve alternatives when materially different interpretations remain;
- ask one focused Human question only when Human meaning is actually needed.

**Existing owners**

`BB-BOOTSTRAP`, `BB-INTEGRATE`, `BB-REQUIREMENTS`, `BB-LEARN`, REQ-003/004, Human-intent audit.

**Current operational gap**

Terse free-text intent reconstruction remains explicitly open in `FF-EXECUTION-PROGRESS`. No strong real runtime/eval proves the desired behavior end-to-end.

### AXIS-B — Context and work-instruction compilation

**Need**

The Human should not courier derivable context or construct expert execution prompts.

**Expected behavior**

`minimal owner intent + canonical state + current work + authority + relevant evidence → bounded executable work packet`.

The work packet should determine, where derivable:

- sources to inspect;
- freshness requirements;
- relevant owners;
- known constraints;
- previous findings;
- required checks;
- uncertainty;
- allowed/non-allowed actions;
- stop conditions;
- expected evidence.

**Existing owners**

`BB-CONTEXT`, `BB-TRACE`, REQ-001/002/004/008/012, P2 Context-Fidelity preflight.

**Current operational gap**

The current operational `context()` is still a coarse near-full repository dump and does not take a Human work intent as input. P2 has a confirmed preflight but is not implemented.

### AXIS-C — Competence acquisition, research and uncertainty routing

**Need**

The Human should not supply missing domain, method or technology expertise.

**Expected behavior**

- detect needed competencies;
- know what is not covered;
- research current SOTA/best practice/standards where freshness or uncertainty matters;
- assess project fit rather than copy generic best practice;
- escalate to specialist where critical;
- communicate limitations;
- ask the Human only for Human-owned meaning/value/authority.

**Existing owners**

REQ-005/006, `BB-COMPETENCE`, `BB-RESEARCH`, `system/competence.json`.

**Current operational gap**

The repository contains a competence taxonomy and review questions, but the current operational core does not demonstrate a robust task-triggered competence/research route.

### AXIS-D — Partial automation, function allocation and work orchestration

**Need**

Multi-step work should not be manually orchestrated by Human-written meta-prompts.

**Expected behavior**

For each real workflow, determine which functions belong to:

- deterministic software;
- routine automation;
- AI judgement;
- specialist judgement;
- explicit Human material decision.

Automation should be **per function/task**, not a binary "automated vs manual" label for the whole workflow.

The system should preserve state across steps and compile its next operational instruction from the previous result.

**Real evidence**

The PR #35 sequence required repeated fresh-state checks, review-packet construction, correction scopes, re-review prompts, assurance checks and status hygiene. Much of this was predictable and derivable but manually orchestrated through prompts.

**Existing owners**

Authority rule classes; automation declarations on Building Blocks; `BB-ASSURE`, `BB-INTEGRATE`, `BB-TRACE`, `BB-OPERATE`, `BB-CONTEXT`.

**Current operational gap**

The repo declares automation expectations but lacks a general demonstrated function-allocation/orchestration mechanism that turns them into end-to-end partially automated workflows.

### AXIS-E — Human decision context, review experience and XAI

**Need**

When Human authority is required, the system must make the decision understandable without transferring repository-integration work to the Human.

**Expected behavior**

Provide:

- situation/orientation;
- decision requested;
- recommendation when appropriate;
- rationale;
- alternatives;
- relevant evidence;
- uncertainty;
- assurance state;
- consequences;
- reversibility;
- explicit non-decisions;
- drill-down trace.

Complexity should be structured, not deleted.

**Existing owners**

Q-XAI, `system/decision_brief.json`, `BB-TRACE`, `BB-ASSURE`, `BB-DERIVE`, Issue #6.

**Current operational gap**

The Decision Brief contract declares `automatic=true`, but current `work.py` primarily validates the contract; a real automatic generator/trigger path is not demonstrated. Current derived state also does not automatically present the blocked P2 Human-admission gate as a complete decision-ready packet.

### AXIS-F — Iterative discovery, error culture and operational learning

**Need**

The project is outcome-open. Errors and user feedback should improve the system without silently rewriting history or converting every symptom into a new direction.

**Expected behavior**

- preserve hypotheses and uncertainty;
- distinguish symptom/cause/need/solution;
- test high-value uncertainty;
- record before/intervention/effect/learning;
- keep corrections visible;
- promote only validated learning;
- convert repeated learning into executable safeguards where semantics are stable;
- preserve explicit no-change/defer/reject outcomes.

**Existing owners**

`BB-LEARN`, `BB-DESIGN`, `BB-RESEARCH`, `BB-INTEGRATE`, lifecycle feedback transitions, Failure Corpus, 2026-09-19 design-method audit.

**Current operational gap**

The design-method audit already found a real methodological gap in user/problem discovery, concept exploration, iteration semantics, feedback interpretation and learning-to-requirement promotion. Current dialogue again demonstrates the cost: local corrections repeatedly caused a new framing rather than cumulative improvement.

### AXIS-G — Cumulative correction fidelity and interaction continuity

**Need**

A material correction must refine the working model without causing earlier material constraints to disappear.

**Expected behavior**

Within one ongoing interaction as well as across sessions:

- retain all still-valid material owner constraints;
- track which statement corrected/superseded which interpretation;
- do not treat the latest correction as a replacement for the rest of the intent;
- surface contradictions instead of silently resolving them;
- preserve the correction chain as evidence of learning;
- keep the active work model cumulative and restartable.

**Real evidence from this conversation**

The assistant repeatedly:
- incorporated the latest correction;
- improved one local dimension;
- then dropped a previously established equal concern.

The most obvious example was losing partial automation after the deeper operationalization audit.

**Existing-owner fit**

Strongest current fit is across `BB-CONTEXT`, `BB-LEARN`, `BB-INTEGRATE`, `BB-STATE`, `BB-TRACE`, Material State and Conversation Harvest.

**Current operational gap**

Cross-chat persistence is partially addressed, but this conversation demonstrates that **same-interaction semantic accumulation** can still fail even when all information is technically present in the chat context.

---

## 6. Cross-cutting evidence discipline: what counts as operationalized?

This audit adds a needed assessment discipline. It is not a new canonical Requirement yet.

A capability should be described at the highest **demonstrated** level, not the highest intended level.

Proposed audit maturity language:

1. **declared** — requirement, principle, schema or Building Block says the behavior should exist;
2. **wired** — a real trigger/input path is connected to an implementation;
3. **executable** — the behavior can actually run;
4. **regression-protected** — relevant failure modes have executable checks/evals;
5. **real-use demonstrated** — the capability has succeeded in a representative real workflow;
6. **human-effective** — observed use shows it actually reduces the intended Human burden / improves the intended decision or work quality;
7. **robust/restartable** — the behavior survives relevant perturbation, fresh context, correction and continuity boundaries.

Rules:

- levels must not be silently skipped;
- deterministic tests cannot establish semantic/Human effectiveness by themselves;
- a declared `automatic=true` is not evidence of runtime automation;
- a Building Block catalog entry is not evidence that routing exists;
- a synthetic fixture is not automatically real-use proof;
- a successful local workflow is not automatically robust/restartable;
- repeated Human pain is counterevidence to an unqualified "operationalized" claim.

This directly addresses the failure in the assistant's earlier surface audit.

---

## 7. Fresh repository mapping against the seven axes

| Axis | Declared | Wired/executable evidence | Regression evidence | Real-use / Human evidence | Current judgement |
|---|---|---|---|---|---|
| A Intent reconstruction | strong | partial via Harvest/Integration semantics | failure corpus names open terse-intent gap | current chat shows repeated reframing/correction | **not adequately operationalized** |
| B Context/work instruction | strong BB-CONTEXT | `context()` exists but is near-full and not intent-bound | old context/token fixtures; P2 preflight stronger but not implemented | Human still needed long meta-prompts | **not adequately operationalized** |
| C Competence/research | strong | taxonomy/review questions; no strong task-trigger route shown in operational core | no strong end-to-end runtime regression found in current audit | Human explicitly reports they cannot supply this expertise | **declared more strongly than demonstrated** |
| D Partial automation/orchestration | automation policy strong | individual guards/checks exist; no generic workflow orchestration proven | local tests / workflow assurance, not general function allocation | PR #35 required Human/meta-prompt orchestration | **material operational gap** |
| E Human decision/XAI | strong | Decision Brief contract validator exists | contract test exists | Human repeatedly asks for context/orientation and rejects compression-as-XAI | **contract stronger than Human-effective runtime** |
| F Iteration/learning | strong BB-LEARN/failure corpus | partial persistence/eval infrastructure | failure corpus and prior audit evidence | repeated corrections not yet converted into a stable cumulative working model | **real methodological/operational gap** |
| G Correction fidelity | implicit across Context/Learn/Integrate/State | no dedicated demonstrated same-interaction accumulation path | no direct regression established here | current conversation is direct FAIL evidence | **newly sharpened real-use gap** |

---

## 8. Audit of the assistant's current approach

The assistant's own method in this conversation is part of the problem evidence.

### 8.1 Too much architecture closure before full problem capture

The assistant repeatedly concluded:

> no fifteenth Building Block is needed.

That may remain a plausible outcome, but it was stated too confidently before the whole problem had been reconstructed.

Correct status:

- existing-owner refinement has strong evidence;
- a new top-level block is **not currently justified**;
- but the repeated real friction means the question should remain falsifiable rather than being treated as already settled.

### 8.2 Conflating repository presence with operational adequacy

The first whole-system repo audit over-weighted that many user needs mapped to existing Requirements and Building Blocks.

This under-weighted the critical question:

> does the real path actually perform the behavior?

The deeper inspection showed concrete contract/runtime asymmetries.

### 8.3 Local correction without cumulative integration

The assistant often responded correctly to the latest Human correction, then lost an earlier peer concern.

That interaction pattern is exactly what the system should learn to prevent.

### 8.4 Premature hierarchy

The assistant used the review workflow as an organizing frame because it was concrete.

The Human clarified that review, prompt/work-packet autonomy, competence, Human XAI, partial automation and learning are not subordinate to one another.

Future synthesis must preserve peer-level structure unless evidence establishes dependency or hierarchy.

### 8.5 Insufficient persistence of current material Human feedback

The conversation generated repeated material findings. Until this audit branch, they remained only in chat.

That is itself inconsistent with the project principle that recognized material state should leave chat before a continuity boundary.

### 8.6 Insufficient external method check before proposing mechanisms

The Human explicitly asked to research best practice/SOTA when uncertain.

Earlier responses proposed concepts such as progressive disclosure, work packets and review loops mostly from internal synthesis.

This audit corrects that by checking current Human-AI / Human-Factors guidance before claiming a design direction.

---

## 9. External best-practice / SOTA cross-check

External sources support treating these findings as a **function-allocation and Human-AI collaboration problem**, not merely a prompt-design issue.

### NIST AI RMF

NIST AI RMF Appendix C says Human and AI roles/responsibilities should be clearly differentiated, and explicitly notes configurations ranging from full automation through Human decision support. It also warns that converting complex Human phenomena into system representations can remove necessary context.

NIST AI RMF Core further calls for documented knowledge limits, Human oversight processes, application scope and regular integration of external feedback.

Project implication:

- Human/AI responsibility allocation should be explicit at the function level;
- system limitations/uncertainty and oversight conditions must be visible;
- context loss is itself a risk.

Sources:
- https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/
- https://airc.nist.gov/airmf-resources/airmf/5-sec-core/

### Microsoft Guidelines for Human-AI Interaction / HAX

The evidence-based Human-AI guidelines include:

- show contextually relevant information;
- support efficient invocation;
- support efficient correction;
- scope services when uncertain;
- explain why the system acted;
- remember recent interactions;
- learn from user behavior.

Project implication:

- terse Human invocation must work;
- correction must be cheap and cumulative;
- uncertainty should lead to bounded clarification rather than overconfident inference;
- explanation should expose rationale and context;
- recent corrections should not fall out of the working model.

Sources:
- https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/
- https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/

### NASA Human Factors / automation function allocation

NASA Human Factors guidance treats the level of automation as a function/task allocation question rather than a whole-system binary. It recommends task analysis/function-allocation evaluation, clear information about automation state/mode, and decision aids that expose rationale and consequences so the Human can maintain situation awareness and make informed decisions.

Project implication:

- partial automation should be designed per workflow function;
- the Human must know what is automated, what remains Human, and why;
- automation should reduce workload without creating new monitoring/meta-work burdens;
- decision context and partial automation are related but distinct peer concerns.

Sources:
- https://www.nasa.gov/reference/10-0-crew-interfaces-vol-2/
- https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-017-automated-and-robotic-systems.pdf

These sources validate the direction of the audit. They do **not** prescribe a specific Wissensarbeit implementation.

---

## 10. Root-cause hypotheses

These are hypotheses to test, not accepted architecture.

1. **Capability catalog > orchestration fidelity**  
   The repository defines good capabilities but has fewer executable compositions that carry work from terse Human intent through context, competence, execution, review and learning.

2. **Contract validation > outcome validation**  
   Several tests establish that contracts contain the expected fields/rules, not that the promised Human-facing behavior actually occurs.

3. **Object-state maturity > interaction-state maturity**  
   Canonical files and reconciliation are increasingly strong, while the live cumulative Human–AI interaction model can still lose prior corrections.

4. **Automation declared per Building Block, not yet allocated per real workflow function**  
   A label such as `automation: high` does not itself determine which concrete workflow steps software, AI, specialist or Human should own.

5. **Context compilation lacks a full intent-bound runtime**  
   The confirmed P2 preflight is an important enabler, but current context runtime remains coarse.

6. **Human gate contracts lack complete automatic delivery paths**  
   The Decision Brief contract is stronger than the demonstrated generator/trigger path.

7. **Learning persistence is stronger than learning closure**  
   Findings can be persisted, but the chain to an operational behavior change and later effectiveness evidence is not consistently closed.

8. **Synthesis pressure can cause semantic loss**  
   The assistant repeatedly compressed a growing set of peer concerns into a smaller conceptual model and lost details that the Human considered material.

---

## 11. Candidate acceptance directions — no implementation admission

The following are candidate future tests, not current implementation scope.

### A — Minimal-input reconstruction

Input:
- terse, colloquial Human instruction with imperfect terminology;
- sufficient relevant canonical context exists.

Expected:
- system reconstructs the likely work intent;
- explicitly marks assumptions;
- does not demand a repository/file list from the Human;
- does not silently invent material meaning;
- asks only if a material ambiguity remains.

### B — Work-packet compilation

Input:
- short work request + canonical state.

Expected:
- system compiles relevant state/evidence/authority/checks/stop conditions;
- irrelevant context is omitted with fidelity provenance;
- no Human-written mega-prompt required.

### C — Competence/research routing

Input:
- task needing a competence absent from the Human instruction.

Expected:
- system detects competence need;
- researches current authoritative/SOTA sources when warranted;
- records fit and limitations;
- escalates only the residual Human/specialist decision.

### D — Partial-automation review workflow

Input:
- Human says only: "Review this PR."

Expected:
- system resolves current repo/PR state;
- constructs the review packet;
- runs deterministic checks;
- performs clearly labelled AI judgement;
- persists findings;
- on correction, compiles a focused re-review from prior findings;
- does not ask the Human to reproduce its own review protocol;
- stops at the correct Human authority gate.

### E — Decision-ready Human gate

Input:
- material Human decision becomes necessary.

Expected:
- complete orientation/context/uncertainty/evidence/consequence packet appears automatically;
- top layer is readable;
- full depth remains accessible;
- Human does not need to reconstruct state across files.

### F — Operational learning loop

Input:
- repeated Human correction of system behavior.

Expected:
- correction is externalized;
- root-cause hypothesis is explicit;
- existing owner is identified;
- validated learning causes a regression/workflow/contract change or explicit no-change/defer rationale;
- later evidence checks whether the correction actually worked.

### G — Cumulative correction fidelity

Input:
- sequence of multiple independent Human corrections in one conversation.

Expected:
- each correction refines the cumulative intent model;
- earlier still-valid constraints remain active;
- contradiction is surfaced;
- final work packet reflects the union of still-valid material constraints rather than only the latest correction.

### Cross-cutting operationalization gate

A capability must not be described as operational merely because it is declared or schema-valid.

A later assurance should report the demonstrated maturity level and the evidence supporting it.

---

## 12. Existing-owner / Requirement disposition

### Requirements

No new Requirement is promoted by this audit.

Strongly implicated existing Requirements:

- REQ-001 restartable context;
- REQ-002 persistent trace;
- REQ-003 system-wide interpretation before integration;
- REQ-004 autonomous routine operation + explicit Human material authority;
- REQ-005 competence detection;
- REQ-006 SOTA / best-practice research and project fit;
- REQ-007 end-to-end trace;
- REQ-008 automate recurring operational burden;
- REQ-011 distinguish deterministic checks, judgement and Human acceptance;
- REQ-012 operational core;
- REQ-013 composable generic capabilities.

Current evidence suggests that future work may need stronger acceptance/evaluation semantics under existing Requirements before a new Requirement family is considered.

### Quality dimensions

Particularly affected:

- Q-XAI;
- Q-AUTO;
- Q-FIT;
- Q-DOMAIN;
- Q-TRACE;
- Q-RESTART;
- Q-LEAN;
- Q-COHERENCE.

### Existing Building Blocks

The gap crosses multiple existing owners:

- BB-BOOTSTRAP;
- BB-CONTEXT;
- BB-COMPETENCE;
- BB-RESEARCH;
- BB-INTEGRATE;
- BB-REQUIREMENTS;
- BB-DESIGN;
- BB-ASSURE;
- BB-TRACE;
- BB-DERIVE;
- BB-LEARN;
- BB-OPERATE where workflow automation becomes operational infrastructure.

**No fifteenth Building Block is promoted.**

Equally, this audit no longer treats "no new Building Block" as a proven final architecture conclusion. Existing-owner refinement remains the default hypothesis to falsify first, consistent with the current composition principle and anti-bloat rules.

### Risks / failure families

The finding strongly intersects:

- R-001 chat knowledge monopoly;
- R-002 novelty drift;
- R-003 accretion;
- R-004 plausibility becomes truth;
- R-005 authority creep;
- R-006 solutionism;
- R-007 over-modeling;
- R-008 false completion;
- R-009 self-reinforcing error;
- R-010 technical blind spot.

Failure-corpus fit:

- FF-EXECUTION-PROGRESS;
- FF-EPISTEMIC-INTEGRITY;
- FF-SYSTEMIC-DRIFT;
- FF-AUTHORITY-PROMOTION;
- FF-FALSE-ASSURANCE;
- FF-SOLUTIONISM-BLOAT;
- FF-STATE-CONTINUITY.

The repeated same-chat loss of prior corrections may justify a later refinement/eval under existing families; this audit does not create a new failure family.

---

## 13. Governing Objective mismatch to resolve later

The current Governing Objective describes the Problem Owner as:

> "fachlich bzw. konzeptionell kompetent, technisch nicht spezialisiert"

The Human now clarified that they do **not** want the operating model to assume that they can supply correct domain terminology, domain analysis or technological competence.

This may be:

- a compatible clarification of what "fachlich bzw. konzeptionell kompetent" was intended to mean; or
- a real semantic mismatch in the current Owner model.

This audit does not silently rewrite the Governing Objective.

The discrepancy must remain visible for later Human-authorized interpretation/refinement.

---

## 14. Reconciliation direction for this audit

This audit should be integrated as a material finding without changing current programme priority.

- **requirements:** confirmed as relevant; no text promotion
- **issues/findings:** refined — previous Human-intent and design-method audits are now understood as parts of a broader peer-level operational collaboration finding
- **risks:** refined evidence against existing risk families; no new risk family
- **decisions/concepts:** no architecture decision; work-packet compiler, partial-automation protocol, progressive disclosure and similar mechanisms remain candidate design directions
- **derived views:** only change provenance if this audit is canonically promoted
- **planning/execution cursor:** unchanged; this audit does not displace the current P2 implementation-admission gate
- **active work:** no new implementation work activated

---

## 15. Explicit non-promotions

This audit does not:

- create or prioritize a new roadmap phase;
- admit P2 implementation;
- set `implementation_allowed=true`;
- change the current execution cursor;
- create a new Building Block;
- create a new Requirement;
- create a generic agent framework;
- create a workflow engine;
- create a universal intent ontology;
- prescribe a named design framework;
- assert that progressive disclosure, a Work Packet object or any particular orchestration architecture is already the correct implementation;
- treat Human feedback as automatic authority for a technical solution.

---

## 16. Audit conclusion

The main system finding is:

> **Wissensarbeit has a real end-to-end operational collaboration gap. The repository contains many of the correct semantic owners, but the Human still carries too much context reconstruction, prompt engineering, competence substitution, workflow orchestration, correction tracking and decision-context assembly.**

The problem has at least seven equal system-level axes:

1. Human role / minimal input / intent reconstruction;
2. context and work-instruction compilation;
3. competence, research and uncertainty routing;
4. partial automation / function allocation / orchestration;
5. Human decision context / review experience / XAI;
6. iterative discovery / error culture / operational learning;
7. cumulative correction fidelity / interaction continuity.

The PR #35 review sequence is valuable real evidence for axes 4 and 5, but it is not the parent category for the others.

The current conversation itself is valuable evidence for axes 1, 2, 5, 6 and 7 because the Human repeatedly had to restore information or perform meta-work that the intended system should absorb.

Finally, future audits must stop treating "present in the repository" as equivalent to "operationalized". Claims should be evidence-calibrated using the operationalization maturity ladder and real Human-use outcomes.

Uncertainty remains valid. This audit captures and structures the demonstrated problem; it deliberately does not pretend the correct implementation architecture is already known.


---

## 17. Additional real-use evidence — work-type terminology drift

After the operationalization package had been prepared, the assistant again described the completed persistence/operationalization work as an "iteration".

The Human Owner corrected this immediately because the distinction had already been established earlier: not every bounded work unit, transition, review, correction, promotion or persistence action is an iteration.

This recurrence is additional evidence for **OC-07 Cumulative Correction Fidelity / Interaction Continuity**:

- the semantic correction already existed in the same conversation;
- the assistant could reproduce the distinction when explicitly challenged;
- the correction was still not reliably applied to later work-description;
- therefore the failure is not only missing vocabulary but failure to carry a still-valid semantic rule forward.

The Human then supplied/confirmed the intended distinctions:

- **Iteration** — a genuine learning/development cycle in which a hypothesis, design or implementation is changed through real evidence and produces a changed next state;
- **Preflight** — determines whether a later slice is sufficiently specified/admissible;
- **Review / Re-Review** — qualitative assessment of a concrete state / focused reassessment after correction;
- **Correction** — targeted change in response to a finding;
- **Promotion / Admission** — authority transition, not iteration;
- **Reconciliation** — systemic state alignment, not iteration;
- **Persistence / Operationalization Slice** — makes findings/state restartable and later actionable; not automatically an iteration;
- **Implementation Slice** — executes a bounded admitted scope; may participate in an iteration but is not one merely by being implemented.

Material implication:

> Work-type names must carry operational consequences. Classification should determine what authority is created, what evidence becomes stale, what follow-up checks are required, and which transitions are explicitly **not** implied.

This audit does not promote these semantics into `system/lifecycle.json` or `system/authority.json`. They are added to the PR #37 candidate operationalization package for independent qualitative review first.



---

## 18. Independent qualitative review correction — signal to known-candidate routing

Independent qualitative review of PR #37 at exact head `b71e2f7527092cf1f63014160fe36c7cf8416fb3` returned **NEEDS CORRECTION**.

The finding was narrow but material:

> Promotion of the immutable OC snapshot would protect the candidate knowledge from loss, but would not itself guarantee that a later newly recognized signal is routed back to the relevant known candidate. The original Option F began too late: it assumed somebody already knew which candidate to activate.

The missing edge was:

`new material/failure/learning signal → known unresolved/activation-ready candidate check → match | no-match | uncertain-match → current trigger evaluation`

This correction uses existing owners rather than new architecture:

- `system/material_state.json` now defines the generic known-candidate routing contract;
- `BB-INTEGRATE` is refined as the existing procedural owner for that routing together with the current Planning Owner;
- `tools/work.py integrate` validates that routing was explicitly dispositioned and that authority boundaries were preserved;
- regression tests cover no/uncertain/matched trigger cases and prevent activation from creating priority/admission/implementation authority;
- the OC snapshot contains signal-driven falsification cases so later review can distinguish content discovery from authority transitions.

The semantic match remains judgement. This change deliberately does **not** add a matcher service, registry, new Building Block, roadmap phase or autonomous trigger engine.

P2 remains independent. Its current implementation gate remains explicit Human admission; this correction neither grants nor blocks that admission.

Required follow-up for PR #37:

1. formal assurance on the corrected exact head;
2. focused independent re-review of this former finding and regression risk;
3. only after qualitative `CONFIRM`, consider promotion/merge through the existing authority boundary;
4. reconcile any promoted contract change after merge.

This is a **Correction** under the candidate work-type semantics, not a new iteration, promotion or implementation admission.



---

## 19. Focused re-review residuals — referential routing truth and Owner-model interpretation

Focused re-review of corrected head `636713178969b594616b143937b1c5b569ab9a89` confirmed the original signal→known-candidate continuity finding as materially closed, including the authority boundary and the decision not to add a registry, matcher service or new Building Block.

Two bounded residual findings remain before PR #37 should be treated as promotion-ready.

### 19.1 Referential routing truth

The first routing validator proved that a routing disposition existed and that status/trigger/authority combinations were coherent. It did **not** yet prove that the declared references were real/current.

Residual examples included:

- a fabricated `matched_candidate_refs: ["OC-999"]` could satisfy the prior structural validator;
- `candidate_source_refs` was not bound to the current `execution_state.planning_source`;
- candidate/fresh-state file existence was not checked;
- a `no-match` could name an arbitrary candidate source set without any deterministic provenance check.

Correction:

The routing provenance is split explicitly into three deterministic properties:

- **existence** — candidate evidence and fresh-state refs must resolve to existing Git-persisted repository files;
- **binding** — `planning_source_ref` must equal the current `project/execution_state.json` planning source; candidate evidence must itself declare that same planning owner; matched candidate IDs must be addressable inside evidence bound to that owner;
- **freshness** — `repository_revision_ref` must equal the exact checked-out Git revision on which the routing decision is validated, and the required execution/reconciliation state refs must be Git-tracked at that revision.

This rejects not only fabricated `OC-999`, but also a valid-looking `OC-03` taken from candidate evidence bound to another planning owner.

Negative regression coverage therefore includes:

- wrong planning source;
- fabricated candidate ID;
- nonexistent candidate evidence;
- valid candidate ID from the wrong planning-owner evidence;
- unbound extra candidate-source claims;
- incomplete fresh-state refs;
- stale/falsely bound repository revision.

Boundary retained:

> These checks establish source existence, Git persistence, planning-owner binding, candidate addressability and exact-revision freshness. They do not prove semantic overlap or completeness of the candidate search space. Those remain judgement and require independent fresh-context/real-use evidence.

### 19.2 Human Problem Owner versus system competence/orchestration function

The current Governing Objective already combines two ideas:

- a Human Problem Owner with purpose/problem competence and material authority;
- system compensation for missing specialist domain/method/technical/project competence.

The prior operationalization plan represented only two interpretations of the phrase “fachlich bzw. konzeptionell kompetent”. A third open interpretation is now persisted:

> Human Problem Owner and system competence/orchestration function are distinct roles. The Human retains purpose, meaning, constraints, priorities, risk/acceptance and material-decision authority. The system reconstructs and operationalizes situationally required domain, method, research, logical, technical and contextual competence.

This is an interpretation hypothesis, not a Governing Objective rewrite or new authority class.

The system-side function is currently modeled as composition across existing owners:

`BB-BOOTSTRAP + BB-CONTEXT + BB-COMPETENCE + BB-RESEARCH + BB-INTEGRATE + BB-ASSURE + BB-TRACE`

No canonical name such as “Logic Owner” is introduced because “Owner” could imply material meaning/decision authority.

### 19.3 Fresh-context evidence gate — oracle visibility correction

The first routing probe design used `WA-EVAL-031..033` from `tests/fixtures/eval_cases.json`.

Their rendered prompt omitted `expect`, and regression tests correctly proved **prompt-level** non-disclosure. Focused review identified a stronger evidence problem:

> prompt-blind ≠ repository-blind.

A tested instance with repository access could search the case ID or fixture and read the repository-visible `expect` fields. Therefore `WA-EVAL-031..033` remain useful **oracle-visible regression cases**, but they are not valid independent blind/fresh-context evidence.

Correction:

- the visible cases are explicitly marked `regression-only-oracle-visible`;
- the normal renderer labels them as regression cases rather than independent blind evidence;
- independent routing evidence uses a separate stimulus-only set in `tests/probes/routing_fresh_context_stimuli_v1.json`;
- the new probe definitions contain no `expect`, expected routing result or OC identifier;
- the tested instance receives an **isolated exact-revision operational bundle** rendered by `tools/eval_integrity.py`, not full repository/eval access;
- the allowlisted bundle contains only the operational repository state needed to resolve planning source, candidate evidence, routing contract, competence and authority;
- a minimal capture record binds probe identity, exact repository revision, accessible context, fresh-instance declaration, external-repository access=false, prior-trial access=false, oracle access=false and the unchanged raw response;
- raw response must be persisted before any separately held oracle is revealed or persisted.

The capture validator improves evidence integrity but does not prove semantic correctness, actual psychological freshness or Human effectiveness. Those remain grading/review claims.

No independent trial is claimed by this repository change.

Required remaining evidence before promotion-candidate status:

1. green formal assurance on the exact oracle-visibility correction head;
2. focused qualitative re-review of the evidence-design correction;
3. independent fresh-instance execution using the isolated bundle protocol;
4. persist raw response/capture first;
5. only then disclose/persist the separately held oracle and grade/review the result.

The original signal→candidate mechanism and referential routing fidelity remain separately CONFIRMED by the prior focused review; this finding concerns the validity of the planned behavioral evidence, not a new routing-mechanism defect.

P2 remains independently gated by explicit Human implementation admission.



---

## 20. Focused evidence-integrity correction — strict blind bundle binding

A later focused review of the exact PR #37 state confirmed:

- the original signal→known-candidate routing finding is closed;
- referential routing fidelity is closed for the current architecture boundary;
- OH-03 is structurally persisted as an open, non-authority composition hypothesis;
- `WA-EVAL-031..033` cannot be used as strict blind evidence because their expected outcomes are repository-visible.

Fresh repository inspection also found that PR #37 already contained a **separate stimulus-only probe path**:

- `tests/probes/routing_fresh_context_stimuli_v1.json`;
- `tests/probes/fresh_context_trial_contract.json`;
- `tools/eval_integrity.py render-probe-bundle`;
- `tools/eval_integrity.py validate-probe-trial`.

That path correctly separates stimulus-only `RP-*` probes from the visible `WA-EVAL-031..033` fixtures and requires a fresh instance with no external repository, prior-trial or oracle access.

Two remaining integrity weaknesses were identified in the implementation of that otherwise appropriate path:

1. the renderer recorded an exact Git revision but read accessible context from the mutable working tree rather than from Git at that revision;
2. the trial capture recorded revision/path metadata but did not bind the response to an identity of the concrete rendered bundle.

Correction:

- accessible context is now read with Git object access at the exact recorded revision;
- every accessible context file is SHA-256 hashed;
- instructions and stimulus are SHA-256 hashed;
- a deterministic `bundle_manifest` records probe identity, revision, context mode, exact allowlist and hashes;
- `bundle_identity` hashes that manifest and is mandatory in the trial record;
- trial validation rejects manifest/record mismatches and invalid bundle identities;
- probe-definition validation fails if an opaque probe ID or the exact probe stimulus appears in any accessible context file;
- the Human-readable plan and machine snapshot explicitly classify `WA-EVAL-031..033` as visible regression cases, not strict blind evidence;
- `project/WA-PR37-BLIND-ROUTING-PROBE-PROTOCOL-2026-09-20.md` documents the two-phase evidence sequence.

Evidence boundary retained:

> Bundle/capture validation proves exact-revision context binding and the encoded access conditions. It does not grade semantic correctness, prove psychological freshness, or establish Human effectiveness.

No independent `RP-*` trial is claimed by this correction. The oracle for those stimulus-only probes must remain unpersisted until the raw responses are captured and persisted.

PR #37 therefore remains **not yet promotion-ready on blind behavior evidence** until independent pre-oracle trials are executed, captured, later graded against a separately revealed oracle, and qualitatively reviewed.

P2 remains independent and unchanged.
