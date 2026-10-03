# System Analysis + Finding-Driven Deep Research Skill — Development & Assurance Plan

**Status:** planning candidate / pre-implementation  
**Parent Work Owner:** #43  
**Work packages:** #44 → #45 → #46  
**Method provenance:** Histo-Orla PR #123 at reviewed head `e112a8985e8c5149b6f84fb3ae8174a6202a40a2`  
**Execution constraint for this development:** web-only; no local checkout/shell  
**Planning principle:** Chat first and quota-aware; Work/Codex only when they add non-substitutable quality/capability value, then only for the smallest quality-preserving bounded slice

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

## 3.1 Reviewed v3 provenance lock

This development plan was reviewed against these Histo-Orla v3 artifacts at PR #123 head `e112a8985e8c5149b6f84fb3ae8174a6202a40a2`:

- `docs/architecture/assurance/generic-system-analysis-deep-research-prompt-v3-20260922.md` — blob `368a14eea3dcabae3f828b29a6a96b9dd5b23c0b`;
- `docs/architecture/assurance/generic-system-analysis-deep-research-v3-refactoring-20260922.md` — blob `07abe77a99787bd716270b3037331cb6ce2ac379`;
- `docs/architecture/assurance/generic-system-analysis-deep-research-v3-appendices-20260922.md` — blob `677e69a31768d0b3ce149cf59a1b558b5e9ba769`;
- `docs/architecture/assurance/execution-profile-chatgpt-deep-research-v3-20260922.md` — blob `ad15c8eed8fdd5a602d473948c94e1383dcba659`.

These SHAs identify the provenance reviewed for this planning baseline. If the source method changes materially, R1 must explicitly inspect the delta rather than silently treating a newer PR head as equivalent.

---

## 4. Work allocation and scarce-execution budget

### 4.1 Governing rule: quality first, scarce modes only when justified

For this development, Chat is the default because it is the abundant execution context; Work and Codex are quota-constrained resources.

Routing order:

```text
Can Chat + currently available web/GitHub capabilities produce
an equally reliable, reviewable and restartable result?
        │
        ├─ yes → stay in Chat
        │        even if Work/Codex would be more convenient
        │
        └─ no  → identify the exact qualitative/capability gap
                 ↓
                 prepare everything substitutable in Chat
                 ↓
                 hand off only the non-substitutable slice
                 ↓
                 return concise evidence/delta to Chat
```

A handoff is justified by **quality or capability necessity**, not by convenience, task category, or elegance of workflow.

If a Chat-based workaround is less direct but yields an equivalent-quality canonical handoff/foundation for later work, prefer it.

If avoiding Work/Codex would cause a material quality loss, do **not** accept the loss merely to save quota. Instead:
- state the quality/capability gap;
- decompose the task;
- perform analysis, source selection, semantic decisions, acceptance design and review preparation in Chat;
- send only the irreducible execution slice to the scarce mode;
- make the expected quality gain and token/quota cost visible.

### 4.2 Chat — default steering, reasoning and execution context

Use Chat for:
- owner dialogue and problem clarification;
- conceptual development;
- repository reading/writing when current web/GitHub capabilities are sufficient;
- preparation of canonical inputs and exact change sets;
- interpretation of trial/review evidence;
- material scope and quality decisions;
- semantic review;
- task decomposition before any scarce-mode handoff;
- reviewing returned work before it changes the next step;
- deciding whether a failed run is method, model, execution or eval failure.

Do not hand off repository production merely because another mode can perform it more conveniently.

### 4.3 Work — scarce multi-step web execution

Use Work only when:
1. the task is already bounded and prepared; **and**
2. Chat cannot achieve equivalent quality/restartability with available web capabilities without a material loss; **and**
3. Work's multi-step execution materially improves the result.

Potential examples:
- a long multi-step browser/repository process that Chat cannot reliably complete end-to-end;
- a bounded artifact operation whose correctness depends on Work-only capabilities;
- an execution task that would otherwise lose material evidence or consistency.

Work receives no open-ended “figure out the architecture” assignment.

Every Work task must be prepared in Chat/repo first using §5 and should contain no history or reasoning that can be replaced by canonical references.

Current development constraint: **web-only**. No local checkout, local shell or local-only workflow.

### 4.4 Deep Research — quality-driven research escalation

Use dedicated Deep Research when the Research Agenda requires source depth, breadth, citation chaining or multi-step evidence work that ordinary Chat/web research cannot provide at equivalent quality.

Do not invoke it just because a topic is “research”.

Before escalation, Chat should already provide:
- project finding / research anchor;
- precise research questions;
- scope and exclusions;
- known competing explanations;
- evidence classes sought;
- counterevidence target;
- required output/reconnection fields.

Thus scarce research execution spends its budget on evidence acquisition and synthesis, not rediscovering project context.

A task may only claim Deep Research-level execution when the actual environment provided an appropriate research workflow. No silent downgrade.

### 4.5 Codex — scarce targeted implementation/test execution

Codex is reserved for well-specified repository/code/test work where its execution capability materially improves quality or enables work Chat cannot equivalently perform.

Before Codex:
- semantics, contract, affected paths, acceptance and must-not rules are fixed in Chat/repo;
- expected tests/checks are named;
- unresolved design choices are removed from the task;
- the task is sliced to the smallest **quality-preserving** executable unit.

For this web-only development:
- do not require local Codex workflows;
- use a web/cloud Codex path only if available and necessary for the bounded task;
- otherwise remain in Chat/Work/GitHub-capable execution.

### 4.6 Quality-equivalence test

Before every Work/Codex handoff ask:

1. What exact capability/quality would be lost by staying in Chat?
2. Can that loss be avoided by changing the Chat approach rather than the execution mode?
3. Which parts of the task are semantic/reasoning work that should remain in Chat?
4. What is the smallest remaining execution slice?
5. What evidence must come back so Chat can review it without replaying the work?
6. Is the expected quality gain worth the scarce-mode token/quota cost?

If question 1 has no material answer, do not hand off.

---

## 5. Token-transparent execution packet

Before handing work to Work/Codex, prepare this compact packet:

```text
WHY THIS MODE
Exact non-substitutable capability / expected quality gain versus Chat.

CHAT PREPARATION ALREADY DONE
Decisions, analysis and narrowing completed before handoff.

TASK
Exact action and intended outcome.

CANONICAL INPUTS
Only required repo paths / issues / commits / accepted review findings.

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
When to stop rather than improvise, and the shortest sufficient evidence summary.

COST / QUALITY TRADE-OFF
Why the scarce-mode budget is justified and what would be lost by a Chat-only route.
```

Rules:
- front-load all substitutable reasoning and context reduction in Chat;
- do not paste broad history when stable repo references suffice;
- do not ask execution models to rediscover decisions already made;
- do not send unresolved conceptual alternatives into implementation tasks;
- return deltas/evidence, not long narrative repeats;
- split large tasks so scarce modes receive only irreducible execution;
- never split so aggressively that cross-file/system correctness or reviewability is lost;
- if a task cannot state its non-substitutable value and quality/cost trade-off, it is not ready for Work/Codex.

---

## 6. Model / reasoning routing

Model choice follows **semantic risk, verifiability and scarce-mode economics**. Use the lowest-cost route that preserves required quality; never trade away material quality merely to reduce tokens/quota.

### High reasoning / strongest available model
Use for:
- Skill Contract;
- eval semantics;
- leading-bias review;
- interpretation of counterevidence;
- cross-project reconciliation;
- changes that could alter the method;
- independent qualitative review.

Use the strongest reasoning capability needed to preserve the required semantic quality in the current environment; do not freeze a model/version into the generic development contract.

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

### Independent review protocol
For R1 and R3, independence is a required evidence condition, not merely a preference.

Minimum conditions:
- reviewer is not the same authoring context that produced the artifact/result under review;
- review input is limited to the frozen canonical artifacts, explicit source/capability boundaries, the review question/criteria, and—where relevant—raw first-run outputs;
- do not provide the originating reasoning narrative or expected verdict;
- the reviewer may inspect referenced primary evidence as needed, but must distinguish source evidence from prior interpretation;
- materially divergent findings must be recorded and dispositioned explicitly rather than normalized away;
- if these conditions cannot be met, record the limitation and downgrade the strength of the review evidence rather than calling it independent.

Independence is about evidence/context separation and the possibility of disagreement, not pretending prior work does not exist.

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
- cross-project test-case requirements;
- explicit **late-helper admission rule**: the empirical Core runs before Challenge/Completeness checklists or disciplinary discovery/search aids are allowed to shape interpretation; such helpers load only after empirical reconstruction and, where relevant, after the Research Agenda is formed, unless a specific exception is justified and recorded.

Reason to combine:
The eval must be capable of falsifying the exact behavior the contract claims. Designing them separately risks a self-confirming test suite.

#### Gate R1 — independent pre-implementation review
Fresh review asks:
- Does the contract preserve v3 without importing Histo-Orla diagnoses?
- Can the Skill conclude healthy / under-formalized / differently broken?
- Can counterevidence change the diagnosis?
- Are failure/capability states complete, including missing, inaccessible or contradictory current project evidence?
- Does the contract keep Challenge/Completeness and disciplinary discovery aids late enough to avoid leading the empirical analysis?
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
| Project-evidence admission failure | current project evidence is incomplete, inaccessible or contradictory; Skill must expose limits/open hypotheses/`unresolved` rather than invent reconstruction or overstate diagnosis |
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

## 13. Review disposition — independent planning review

Independent review verdict: `READY WITH CORRECTIONS`.

Disposition of findings:
- **F-01 material — independent review not operationalized:** corrected in §6 and applied as a required protocol for R1/R3.
- **F-02 material — late helper admission not explicit in P1:** corrected in §7 P1/R1.
- **F-03 material — no adversarial case for incomplete/conflicting project evidence:** corrected in §8 and R1.
- **F-04 minor — mutable provenance + version-specific model default:** corrected via §3.1 provenance lock and vendor/version-neutral model routing.

No additional issue/gate/framework structure was added.

---

## 14. Current next action

Proceed with #44 only after this planning PR is reviewed/accepted.

#44 should be developed and reviewed in Chat as far as current web/GitHub capabilities allow. Hand off any remainder to Work/Codex only after the §4.6 quality-equivalence test shows a material non-substitutable benefit, and then only as the smallest quality-preserving bounded execution slice.

No Skill implementation belongs in the planning PR.
