# System Analysis + Finding-Driven Deep Research Skill — Development & Assurance Plan

**Status:** planning candidate / pre-implementation  
**Parent Work Owner:** #43  
**Work packages:** #44 → #45 → #46  
**Method provenance:** Histo-Orla PR #123 and its v3 method/refactoring artifacts  
**Execution constraint for this development:** web-only; no local checkout/shell  
**Planning principle:** Chat first; Work/Codex only for prepared bounded execution tasks

---

## 1. Goal

Develop a reusable Skill that reliably executes this knowledge process:

```text
empirical project/system analysis
→ material findings / problem clusters
→ competing explanations
→ Research Agenda derived from findings
→ finding-driven Deep Research
→ theory + investigation method + empirical evidence
→ Related Work + Best-Practice evidence + counterevidence
→ analytical reconnection to the original findings
→ Research Gaps / unresolved
→ STOP before solution development
```

The target is **fit-for-purpose completeness**, not minimum functionality.

Lean means:
- remove waste, duplication, speculative infrastructure and unnecessary coordination;
- keep every capability required for reliable end-to-end execution;
- prefer the simplest sufficient implementation;
- never relabel a partial/demo capability as lean completeness.

A successful first release is therefore the first **functionally complete and testable** version, not merely the smallest package that can be installed.

---

## 2. Authority and scope boundary

This Skill may:
- reconstruct and analyse project/system evidence;
- form and challenge problem hypotheses;
- derive a Research Agenda;
- perform or route proportionate external research;
- compare theories, methods, empirical evidence, related work and best-practice evidence;
- strengthen, weaken, reframe or contradict project findings;
- preserve uncertainty and `unresolved`.

It must not:
- select a target architecture;
- recommend tool/framework adoption;
- create a roadmap or implementation priority;
- promote requirements or project truth;
- infer owner acceptance;
- turn best practice into an adoption decision;
- make a host repository's existing framework vocabulary the Skill's explanatory model.

The host project remains authoritative for its own state and persistence rules.

---

## 3. Canonical development principles

The detailed method lives in the Histo-Orla v3 provenance. Development must preserve these invariants:

1. **Empirical reconstruction before diagnosis.**
2. **Low leading bias:** no expected Histo-Orla failure pattern in the normal path.
3. **Current evidence before inherited audit claims:** prior reports are hypotheses/leads.
4. **System analysis generates the Research Agenda.**
5. **Research is finding-driven:** substantial research must have a material project anchor.
6. **Competing explanations and counterevidence are constitutive.**
7. **Theory ≠ investigation methodology ≠ empirical evidence.**
8. **Best Practice = evidence under conditions, not recommendation.**
9. **Research depth is proportional to finding centrality and uncertainty.**
10. **Healthy-project, under-formalization and opposite findings are valid.**
11. **`unresolved` is valid.**
12. **Core method is vendor-neutral; execution profiles are separate.**
13. **STOP before solution development.**
14. **Lean = complete fit-for-purpose capability without unnecessary structure.**
15. **No new workflow engine, ontology, truth store or framework coupling without observed need.**

When a later implementation choice conflicts with these principles, the implementation changes; the principle is not silently weakened for convenience.

---

## 4. Work allocation

### 4.1 Chat — primary steering and reasoning context

Use Chat for:
- owner dialogue and problem clarification;
- conceptual development;
- interpretation of trial/review evidence;
- material scope and quality decisions;
- deciding whether a proposed Work/Codex task is ready;
- reviewing returned work before it changes the next step;
- deciding whether a failed run is method, model, execution or eval failure.

Chat should **not** manually perform repetitive repository production work when a prepared Work task can do it more efficiently.

### 4.2 Work — prepared web/repository execution

Use Work when the task is already bounded and benefits from multi-step web/repository/artifact execution, for example:
- create/update the Skill package from an accepted contract;
- persist a reviewed specification;
- prepare trial fixtures/evidence packages;
- execute a bounded repository-wide check;
- run a prepared Deep Research task with specified sources and outputs.

Work receives no open-ended “figure out the architecture” assignment for this Skill.

Every material Work task must be prepared in Chat/repo first using the task packet in §5.

Current development constraint: **web-only**. Use web/cloud/connector capabilities; no local checkout, local shell or local-only workflow.

### 4.3 Deep Research — evidence-intensive research execution

Use dedicated Deep Research when a research question is genuinely multi-step and source-intensive, especially Tier-A finding research.

It is an execution mode, not an epistemic authority and not part of the vendor-neutral Core.

A task may only claim Deep Research-level execution when the actual environment provided an appropriate research workflow. No silent downgrade to a few searches.

### 4.4 Codex — targeted implementation only when appropriate

Codex is reserved for well-specified repository/code/test work, not conceptual exploration.

For this web-only development:
- do not require local Codex workflows;
- use a web/cloud Codex path only if available and materially better for an already frozen coding/test task;
- otherwise use Work/GitHub-capable execution.

Codex never receives unresolved semantic design questions that should first be decided in Chat.

---

## 5. Token-efficient execution packet

Before handing work to Work/Codex, prepare this compact packet:

```text
TASK
Exact action and intended outcome.

CANONICAL INPUTS
Only the required repo paths / issues / commits / accepted review findings.

SCOPE
What may change.

MUST NOT
Semantic/authority/non-goal boundaries.

ACCEPTANCE
Observable conditions that make the task complete.

REQUIRED CHECKS
Exact validation/tests/review evidence.

OUTPUT / PERSISTENCE
Exact files/issues/PR/evidence to produce.

STOP / RETURN
When to stop rather than improvise, and what short summary to return.
```

Rules:
- do not paste broad history when stable repo references suffice;
- do not ask execution models to rediscover decisions already made;
- do not send unresolved conceptual alternatives into implementation tasks;
- return deltas/evidence, not long narrative repeats;
- if a task cannot be specified this way, it is not ready for bounded Work/Codex execution.

---

## 6. Model / reasoning routing

Model choice follows **semantic risk and verifiability**, not a blanket “cheapest model” rule.

### High reasoning / strongest available model
Use for:
- Skill Contract;
- eval semantics;
- leading-bias review;
- interpretation of counterevidence;
- cross-project reconciliation;
- changes that could alter the method;
- independent qualitative review.

For ChatGPT, GPT-5.6 Sol with high reasoning is an appropriate current default where available for this class of complex knowledge work.

### Lower-cost/faster model
May be used for:
- exact mechanical transformations;
- formatting;
- bounded metadata updates;
- deterministic fixture rendering;
- repetitive checks with unambiguous acceptance;
- tasks whose semantic output is independently verified.

Do not use a cheaper/faster model merely to save tokens when an error could change the Skill's meaning or the interpretation of trial evidence.

### Deep Research
Research depth is routed by the Research Agenda and evidence need, not by model prestige. Dedicated Deep Research is preferred for genuine multi-source Tier-A work.

### Independent review diversity
Where practical, use a fresh context and avoid giving the reviewer the originating chat's reasoning narrative. Provide canonical artifacts, review question and acceptance criteria. Independence is about evidence and context separation, not pretending prior work does not exist.

Product/model details are execution-profile information and should be rechecked against current official documentation when used; they are not frozen Skill semantics.

---

## 7. Development sequence

### Phase P0 — Planning freeze
**Owner:** #43  
**This plan:** current phase.

Outputs:
- one canonical development plan;
- child Work Packages #44–#46;
- explicit Chat/Work/Deep-Research/Codex division;
- explicit review/test gates.

Exit:
- owner/review confirms the plan is sufficient and not itself an unnecessary framework.

### Phase P1 — Contract + Eval Design
**Owner:** #44

Produce together, before implementation:
- functionally complete Skill Contract;
- trigger/non-trigger contract;
- capability/source admission;
- output and failure/stop behavior;
- package/reference specification;
- semantic Eval Contract;
- cross-project test-case requirements.

Reason to combine:
The eval must be capable of falsifying the exact behavior the contract claims. Designing them separately risks a self-confirming test suite.

#### Gate R1 — independent pre-implementation review
Fresh review asks:
- Does the contract preserve v3 without importing Histo-Orla diagnoses?
- Can the Skill conclude healthy / under-formalized / differently broken?
- Can counterevidence change the diagnosis?
- Are failure/capability states complete?
- Does the eval actually challenge the contract?
- Is any proposed runtime/package structure speculative?
- Is anything required for full functionality missing?

No implementation starts until material R1 findings are dispositioned.

### Phase P2 — Fit-for-purpose implementation
**Owner:** #45  
**Depends on:** accepted/dispositioned R1.

Implement exactly the reviewed contract:
- `skill.md`;
- required reference modules;
- separate execution profiles;
- only sufficient runtime scaffolding demonstrated necessary by the contract.

Implementation should be a bounded execution task, not an architecture exploration.

#### Gate R2 — contract-conformance review
Before generic trials:
- every required behavior traced to package content;
- no hidden framework coupling;
- no early loading of leading checklists;
- no vendor detail in the generic Core;
- no missing failure/STOP behavior;
- package can execute the full method end-to-end.

### Phase P3 — Fresh cross-project trials
**Owner:** #46  
**Depends on:** reviewed P2.

Freeze Skill version first. Run fresh contexts across materially different cases.

Required case classes:
- over-structuring / integration-friction candidate;
- under-structuring / insufficient-formalization candidate;
- largely healthy project;
- prior-diagnosis-heavy project;
- domain/data/technical-quality-dominant project.

Preserve:
- exact Skill version;
- exact task packet;
- accessible sources/capabilities;
- model/mode;
- raw first result;
- research/source boundary;
- execution failure/blocker if incomplete.

Do not tune the Skill between valid first-pass cases.

#### Gate R3 — independent evidence reconciliation
Fresh reviewer classifies observed problems as:
- Skill-method failure;
- model behavior;
- execution/capability limitation;
- eval/grader defect;
- test-case/source ambiguity.

No generic-fit claim until R3.

### Phase P4 — Evidence-driven revision or candidate acceptance

Only after R3:
- revise concrete observed defects;
- add tests tied to observed failures;
- rerun affected cases;
- decide whether evidence supports a reusable generic candidate.

Do **not** add mechanisms merely because a reviewer can imagine another possible failure.

---

## 8. Anti-regression matrix

The Eval Contract must test at least:

| Failure mode | Required challenge |
|---|---|
| Leading diagnosis | project evidence contradicts common/Histo-Orla-shaped diagnosis |
| Prior-audit laundering | strong old audit exists but current evidence changed |
| Healthy-project pathology | mostly healthy project; no major failure should be invented |
| Under-formalization blindness | evidence supports more structure/formalization |
| Unanchored Research | substantial literature block has no material finding anchor |
| Unresearched Major Finding | central finding receives insufficient external challenge |
| Theory/method collapse | explanatory theory confused with method for testing it |
| Counterevidence ignored | external evidence should weaken/reframe initial finding |
| Silent Deep-Research downgrade | capability insufficient but output claims deep research |
| Best-practice solution drift | evidence about a practice turns into adoption advice |
| Historical/current collapse | resolved historical problem reported as current-active |
| Solutionism | report crosses STOP boundary into architecture/roadmap/tool choice |
| Checklist compliance | output fills expected sections without discriminating evidence |
| Over-generalization | one case is presented as generic mechanism without transfer evidence |

Passing deterministic checks alone is not evidence that the Skill is epistemically sound.

---

## 9. Test and review strategy

Use three layers:

### A. Structural/deterministic checks
Good for:
- package completeness;
- required references;
- forbidden vendor leakage into Core;
- fixture identity/integrity;
- expected output fields if later formalized;
- version/evidence binding.

### B. Semantic evaluation
Needed for:
- leading bias;
- competing explanation quality;
- correct current/historical interpretation;
- adequacy of Research Agenda;
- meaningful reaction to counterevidence;
- preservation of uncertainty;
- solutionism.

### C. Fresh independent review
Needed before implementation and after trials because the development team can reproduce its own assumptions even when deterministic tests pass.

Independent review is not “a second model agrees”. It must inspect the evidence, contract, raw outputs and alternatives.

---

## 10. Planning and issue discipline

Canonical homes:

```text
#43
= parent / status / next gate / links

this DEVELOPMENT_PLAN.md
= full development sequence + execution/review/test policy

#44
= contract + package spec + eval contract

#45
= implementation

#46
= fresh trials + independent reconciliation
```

Do not create an issue for every finding or every test case. Add another Work Owner only when there is genuinely independent scope, dependency or DoD.

Do not duplicate the full plan into issue bodies; issues summarize and link.

---

## 11. Stop / escalation conditions

Stop and return to Chat/owner review when:
- the Skill meaning would change;
- a new persistent runtime/schema/framework is proposed;
- evaluation exposes ambiguity in desired behavior;
- execution capability is insufficient for the claimed research depth;
- test-case ground truth is itself ambiguous;
- implementation requires choosing between materially different epistemic behaviors;
- a Work/Codex task cannot be specified with the packet in §5.

Do not resolve these through implementation convenience.

---

## 12. Fit-for-purpose completion

The Skill is not “done” because `skill.md` exists.

Candidate completion requires:
- reviewed complete Skill Contract;
- reviewed falsifiable Eval Contract;
- fit-for-purpose package implementing the full contract;
- contract-conformance review;
- fresh cross-project evidence across materially different cases;
- independent reconciliation;
- no unresolved central regression falsely presented as success;
- explicit known limits;
- evidence that the Skill can produce materially different conclusions when projects differ;
- evidence that Research Agenda routing changes external research according to actual findings;
- evidence that STOP before solution development holds.

Only then may a generic-candidate status be considered.

---

## 13. Current next action

Proceed with #44 only after this planning PR is reviewed/accepted.

#44 should be prepared in Chat first, then handed to Work only as a bounded artifact task once the conceptual Contract/Eval semantics are sufficiently resolved.

No Skill implementation belongs in the planning PR.
