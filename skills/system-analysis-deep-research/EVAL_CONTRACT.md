# System Analysis + Finding-Driven Deep Research — Eval Contract

**Status:** semantic evaluation contract candidate for Issue #44 pre-implementation review  
**Parent:** Issue #43 — System Analysis + Finding-Driven Deep Research  
**Work Owner:** Issue #44 — Contract, package spec and eval contract  
**Skill Contract:** `SKILL_CONTRACT.md` on the same #44 specification branch  
**Package Specification:** `PACKAGE_SPEC.md` on the same #44 specification branch  
**Development baseline:** PR #47 — `DEVELOPMENT_PLAN.md` at accepted head `d97043d736bd03386667e107358194a521030266`  
**Method provenance:** `esany/pflege-arnshaugk-historie` PR #123 at reviewed head `e112a8985e8c5149b6f84fb3ae8174a6202a40a2`

This document defines how the Skill must be challenged and evaluated.

It does **not** implement eval fixtures, graders, runtime harnesses, or trial runs.

The purpose of the Eval Contract is falsification:

> Evaluation must be capable of showing that the Skill is wrong, leading, shallow, incomplete, capability-blind, or solutionist even when its output is fluent, long, well-structured, and heavily cited.

A structurally complete report is not evidence of semantic success.

---

## 1. Evaluation Objective

The evaluation system MUST determine whether an implementation of the Skill reliably performs the contractually required epistemic work across materially different projects.

It must test whether the Skill can:

- reconstruct current project/system state before diagnosing;
- distinguish current evidence from inherited interpretation;
- derive materially different findings from materially different projects;
- preserve healthy, under-formalized, over-structured, domain/data/technical, mixed, and unresolved outcomes when supported;
- derive external research from project findings rather than from a generic literature template;
- consider competing explanations;
- seek and react to counterevidence;
- keep theory, investigation methodology, and empirical evidence distinct;
- allocate research depth proportionally;
- expose source/capability limits;
- preserve current/historical distinctions;
- reconnect external research to originating findings;
- stop before solution development.

The eval MUST NOT merely test whether expected headings, keywords, tables, or source counts appear.

---

## 2. Evaluation Authority and Boundary

Evaluation MAY determine whether an observed execution conforms to the Skill Contract.

Evaluation MUST NOT:

- decide host-project truth;
- promote findings into requirements;
- choose target architecture;
- recommend tools/frameworks;
- infer owner acceptance;
- treat grader preference as scientific truth;
- silently convert ambiguous case evidence into a forced expected diagnosis;
- use implementation convenience as a reason to weaken the Contract.

A failed eval means the tested behavior is not adequately supported by the observed evidence.

It does not by itself determine whether the root cause is:

- Skill-method design;
- implementation defect;
- model behavior;
- execution/capability limitation;
- eval/grader defect;
- test-case/source ambiguity.

That causal classification belongs to review/reconciliation.

---

## 3. Evaluation Layers

The evaluation strategy MUST use three distinct layers.

### 3.1 Structural / deterministic evaluation

Suitable for properties that can be checked without interpreting the substantive analysis.

Examples:

- required package files exist;
- default Core reference is present;
- optional helpers remain separately identifiable;
- vendor-specific instructions are outside the generic Core;
- frozen artifact/version identity is recorded;
- required case evidence packets are complete;
- raw first outputs are preserved;
- forbidden package-level dependencies are absent;
- expected source/capability metadata is recorded.

Structural checks MUST NOT claim that the Skill is epistemically correct.

### 3.2 Semantic evaluation

Required for behavior whose correctness depends on evidence interpretation.

Examples:

- leading diagnosis;
- prior-audit laundering;
- evidence admission;
- materiality of findings;
- competing explanations;
- Research Agenda quality;
- research depth;
- theory/method/evidence distinction;
- counterevidence response;
- analytical reconnection;
- historical/current status;
- uncertainty;
- solutionism.

Semantic evaluation MUST cite the case evidence and the observed output behavior supporting its judgement.

### 3.3 Fresh independent review

Required at the review gates defined by the Development Plan.

Independence is not “another model agrees”.

At minimum:

- reviewer is not the same authoring context that produced the artifact/result being reviewed;
- reviewed artifacts/results are frozen;
- source and capability boundaries are explicit;
- originating reasoning narrative and expected verdict are withheld;
- raw first-run output is provided where a run is under review;
- divergent reviewer findings remain visible and are dispositioned;
- if independence cannot be achieved, the limitation is recorded and the evidence strength is downgraded.

---

## 4. Falsifiability Rule

Each semantic requirement MUST have at least one evaluation condition under which a plausible but incorrect execution can fail.

The eval design MUST avoid tautologies such as:

- “counterevidence passed because a Counterevidence section exists”;
- “Research Agenda passed because a Research Agenda heading exists”;
- “Deep Research passed because many sources were cited”;
- “healthy-project behavior passed because the output says the project is healthy”;
- “STOP passed because the word STOP appears”.

Evaluation asks whether behavior is supported by the evidence and changes appropriately when the case changes.

---

## 5. Case Construction Principles

Eval cases MUST be constructed to discriminate behavior, not merely provide topics.

Each case packet MUST define, as applicable:

- investigation object;
- scope and exclusions;
- frozen project/system evidence;
- time boundary;
- source authority/provenance information;
- accessible versus intentionally inaccessible evidence;
- prior audits/diagnoses, when part of the case;
- external research capability boundary;
- known execution limitations;
- material ambiguity in the case itself;
- case-specific semantic traps;
- evaluation questions;
- evidence sufficient to judge those questions.

### 5.1 Do not disclose the expected diagnosis

The executor MUST NOT receive:

- the grader’s preferred diagnosis;
- hidden case labels such as “healthy case” or “under-formalization case”;
- the expected failure mode;
- a list of facts selected solely to steer the desired conclusion.

Case-class identity belongs to eval metadata, not the execution prompt.

### 5.2 Ground truth is bounded

The eval MUST distinguish:

- directly established case facts;
- deliberately planted prior interpretations;
- evaluator inference;
- genuine ambiguity.

When the case does not support a unique conclusion, the grader MUST allow `unresolved`, conditional, or competing interpretations.

### 5.3 No case explosion

Add a new case only when an existing case cannot expose a material contract failure.

Cross-cutting adversarial conditions SHOULD be embedded into the required five case classes where possible.

---

## 6. Required Cross-Project Case Classes

The eventual fresh trial suite MUST contain at least five materially different case classes.

### Case Class A — Over-structuring / integration-friction candidate

The project evidence must contain enough material to make excessive, misplaced, or coordination-producing structure plausible.

However, the case MUST also contain alternative explanations or protective value so that the executor cannot pass by simply labelling “too much governance”.

The eval checks whether the Skill:

- reconstructs the evidence first;
- distinguishes protective from costly structure;
- considers alternative mechanisms;
- does not generalize the diagnosis beyond evidence;
- derives research needs from the actual findings.

### Case Class B — Under-structuring / insufficient-formalization candidate

The evidence must support the possibility that more explicit structure, control, traceability, specification, or formalization is needed.

The eval checks whether the Skill can reach that direction without treating formalization itself as pathology.

A Skill that systematically reframes every need for structure as over-governance or bureaucracy fails this case.

### Case Class C — Largely healthy project

The evidence must contain normal imperfections but no supported major systemic pathology.

The eval checks whether the Skill:

- can preserve positive mechanisms;
- avoids manufacturing a major diagnosis;
- still identifies bounded uncertainties or local issues when supported;
- does not interpret absence of pathology as analytical failure.

### Case Class D — Strong prior-diagnosis contamination

The case includes a confident prior audit, diagnosis, or explanatory narrative.

Current evidence must materially weaken, change, complicate, or contradict at least part of it.

The eval checks whether the Skill:

- treats the prior audit as prior interpretation;
- freshly reconstructs current state;
- preserves useful historical information from the audit;
- changes the finding when current evidence requires it;
- does not launder inherited language into current truth.

### Case Class E — Domain / data / technical-quality dominant

The decisive evidence points primarily to a domain, data, technical-quality, reliability, or similar mechanism rather than the governance/integration patterns prominent in the method’s provenance.

The eval checks whether the Skill can follow that evidence and avoid Histo-Orla-shaped explanatory gravity.

---

## 7. Required Cross-Cutting Adversarial Conditions

The five case classes MUST collectively include the following conditions.

They do not require separate cases unless embedding them would make the case ambiguous or unreviewable.

### 7.1 Incomplete current evidence

At least one case MUST omit material current evidence while still permitting useful partial analysis.

Expected behavior:

- gap is visible;
- claims are bounded;
- hypotheses remain hypotheses;
- missing evidence is not replaced by theory or generic Best Practice;
- completion is bounded where necessary.

### 7.2 Inaccessible material source

At least one case MUST make a material source or source class inaccessible.

Expected behavior:

- access limit is stated;
- central claims depending on it are qualified;
- required research depth is not falsely claimed complete.

### 7.3 Contradictory evidence

At least one case MUST contain materially conflicting evidence.

Expected behavior:

- contradiction remains visible;
- source authority/time/context may be analysed;
- evidence is not cherry-picked merely to preserve one narrative;
- `unresolved` remains available.

### 7.4 Historical/current trap

At least one case MUST contain a historically real but currently resolved or changed problem.

Expected behavior:

- historical evidence is preserved;
- the historical finding is not reported as current-active without fresh evidence.

### 7.5 Negative/completeness claim trap

At least one case MUST tempt a claim such as:

- “no evidence exists”;
- “no countercases exist”;
- “the project never did X”;
- “all relevant approaches do Y”.

Expected behavior:

- material negative/completeness claims expose a defensible Search Boundary;
- otherwise the claim is qualified as not established.

### 7.6 Capability shortfall

At least one execution condition MUST make required Tier-A depth unavailable.

Expected behavior:

- no silent downgrade;
- useful partial research may be preserved;
- the unsatisfied obligation remains visible;
- output does not claim full Deep Research completion.

---

## 8. Mandatory Anti-Regression Evaluations

The implementation/trial suite MUST be able to falsify at least the following failure modes.

### AR-01 — Leading Diagnosis

**Failure:** Initial analysis is materially shaped by expected failure categories before project evidence establishes them.

**Challenge:** Case evidence contradicts a familiar or provenance-shaped diagnosis.

**Pass condition:** Findings arise from evidence; opposite explanations remain available.

### AR-02 — Prior-Audit Laundering

**Failure:** A strong prior audit is restated as current truth without revalidation.

**Challenge:** Current evidence has changed.

**Pass condition:** Prior interpretation is separated from fresh current evidence and may be weakened/reframed/contradicted.

### AR-03 — Healthy-Project Pathology

**Failure:** The Skill manufactures a major failure because the task is framed as an audit.

**Challenge:** Largely healthy project with bounded imperfections.

**Pass condition:** Analysis can conclude that no major systemic pathology is supported.

### AR-04 — Under-Formalization Blindness

**Failure:** Evidence supporting more structure/formalization is systematically reframed as excessive governance.

**Challenge:** Under-structured case.

**Pass condition:** The Skill can identify insufficient structure without solution-design leakage.

### AR-05 — Project-Evidence Admission Failure

**Failure:** Missing, inaccessible, or contradictory project evidence is hidden or filled in.

**Challenge:** Evidence-admission stress.

**Pass condition:** Limits, hypotheses, reduced confidence, bounded completion, or `unresolved` appear where warranted.

### AR-06 — Unanchored Research

**Failure:** A substantial literature/research block has no material project finding as its origin.

**Challenge:** Tempting adjacent research topic with no case anchor.

**Pass condition:** The topic is omitted, bounded as peripheral, or explicitly linked to a material finding before substantial research.

### AR-07 — Unresearched Major Finding

**Failure:** A central explanatory finding receives insufficient external challenge.

**Challenge:** Case contains one highly material uncertain finding plus several easier peripheral findings.

**Pass condition:** Research depth follows centrality/uncertainty rather than convenience.

### AR-08 — Theory / Method Collapse

**Failure:** An explanatory theory is treated as the empirical method for detecting the phenomenon, or vice versa.

**Challenge:** Research domain where theory and operationalization are distinct.

**Pass condition:** Theory, investigation methodology, and empirical evidence remain materially distinguishable.

### AR-09 — Counterevidence Ignored

**Failure:** Counterevidence is listed but does not affect the interpretation.

**Challenge:** External evidence materially weakens or conditions the initial finding.

**Pass condition:** Reconnection visibly changes to weakened/reframed/conditional/contradicted/unresolved as justified.

### AR-10 — Silent Research-Depth Downgrade

**Failure:** The execution claims Tier-A/deep completion despite shallow or capability-limited research.

**Challenge:** Restricted research capability.

**Pass condition:** Limitation propagates into completion status.

### AR-11 — Best-Practice Solution Drift

**Failure:** Evidence about a practice becomes an adoption recommendation.

**Challenge:** Strong external practice evidence with uncertain transferability.

**Pass condition:** Benefits, costs, preconditions, failures, countercases, controversy, and transfer limits are analysed without adoption advice.

### AR-12 — Historical / Current Collapse

**Failure:** A resolved historical problem is reported as current.

**Challenge:** Clear intervention/recovery timeline.

**Pass condition:** Temporal finding status remains correct.

### AR-13 — Solutionism

**Failure:** Output crosses into target architecture, tool choice, roadmap, implementation priority, governance redesign, or adoption decision.

**Challenge:** Case where research strongly suggests an attractive solution.

**Pass condition:** The Skill stops with findings, evidence, gaps, and uncertainty.

### AR-14 — Checklist Compliance

**Failure:** Expected sections are filled without discriminating evidence or real analytical linkage.

**Challenge:** Case where superficial template completion is easy.

**Pass condition:** Evaluation follows evidence quality, causal discrimination, research anchoring, and reconnection rather than section presence.

### AR-15 — Over-Generalization

**Failure:** A case-local mechanism is presented as generic without transfer evidence.

**Challenge:** Strong single-case pattern with plausible contextual dependence.

**Pass condition:** Scope and transfer limits remain explicit.

### AR-16 — Late-Helper Leakage

**Failure:** Challenge/Completeness or disciplinary discovery content shapes initial findings before empirical reconstruction / Research Agenda admission.

**Challenge:** Optional helper contains a salient diagnosis absent from project evidence.

**Pass condition:** The diagnosis does not appear as an initial finding merely because the helper exists.

### AR-17 — Need→System Omission

**Failure:** A material translation chain from need/uncertainty/evidence/constraint to project representation and actual effect exists but is not examined.

**Challenge:** Case includes an important translation/interface mechanism.

**Pass condition:** The chain is reconstructed proportionally without assuming mismatch in advance.

### AR-18 — Negative-Claim Without Search Boundary

**Failure:** Material absence/completeness claim is made from incomplete search.

**Challenge:** Search space is explicitly bounded.

**Pass condition:** Search Boundary is visible or the claim is downgraded to not established.

---

## 9. Semantic Scoring / Judgement Model

The Eval Contract does not require a universal numeric score.

For each evaluated requirement or anti-regression, the evaluator SHOULD use:

- `PASS` — behavior is supported by the case evidence and Contract;
- `FAIL` — material non-conformance is supported;
- `INCONCLUSIVE` — case evidence, capability, or grader evidence is insufficient;
- `NOT_APPLICABLE` — the requirement genuinely does not arise in this case.

### 9.1 No averaging away material failures

A central Contract violation MUST NOT be hidden by a high aggregate score.

Examples of material failures include:

- leading diagnosis;
- fabricated current state;
- prior-audit laundering;
- silent research-depth downgrade;
- unresearched central finding;
- failure to react to material counterevidence;
- solution-development leakage.

If numeric summaries are later added, they remain secondary to explicit material failure disposition.

### 9.2 Evidence required for judgement

A semantic judgement MUST identify:

- the relevant case evidence;
- the relevant observed output behavior;
- the Contract/Eval obligation;
- why the behavior satisfies or violates it.

Grader preference alone is insufficient.

---

## 10. Evaluation of Research Depth

Research-depth evaluation MUST test responsibility, not source quantity.

### Tier A

A Tier-A finding SHOULD be judged on whether research proportionally covered:

- foundational/authoritative work;
- current empirical evidence;
- explanatory theory;
- competing theory/criticism;
- investigation methodology;
- counterevidence;
- Related Work/cases;
- Best-Practice evidence under conditions where relevant;
- citation chaining where useful;
- transferability;
- Search Boundary for material negative claims;
- saturation/stop judgement.

A fixed source minimum MUST NOT substitute for this assessment.

### Tier B

Evaluation asks whether multiple strong sources or equivalent evidence coverage, a deliberate countercheck, and transfer consideration were present.

### Tier C

Evaluation asks whether the contextual claim received proportionate authoritative verification.

### Dynamic depth

If research changes a finding’s centrality or uncertainty, evaluation MUST allow and expect depth to change accordingly.

---

## 11. Evaluation of Finding→Research Traceability

For every central research block, the evaluator MUST be able to reconstruct:

```text
Project/System Finding
→ Research Need
→ Research Question
→ External Evidence
→ Counterevidence
→ Analytical Reconnection
→ Remaining Uncertainty
```

The exact presentation format is irrelevant.

Failure occurs when the logical trace cannot be established even if the output contains all expected headings.

---

## 12. Evaluation of Analytical Reconnection

For each central researched finding, evaluation asks whether external evidence materially returned to the originating project finding.

Acceptable outcomes include:

- `strengthened`;
- `weakened`;
- `reframed`;
- `contradicted`;
- `partial`;
- `conditional`;
- `unresolved`;

or equivalent semantics.

A research block fails reconnection when it merely summarizes literature and leaves the original finding untouched without explaining why.

Counterevidence MUST be capable of changing the outcome.

---

## 13. Evaluation of Completion and Bounded Completion

### 13.1 Full completion

A run may be judged fully complete only when the material obligations relevant to the case were satisfied, including:

- sufficient current-state reconstruction;
- evidence-grounded central findings;
- competing explanations;
- finding-derived Research Agenda;
- proportional external research;
- counterevidence;
- theory/method/evidence distinction;
- analytical reconnection;
- cross-finding tension review;
- Research Gaps/unresolved;
- coverage check;
- visible material capability/access limits;
- STOP compliance.

### 13.2 Bounded completion

A run MAY correctly end bounded when source/capability limitations prevent full completion.

The evaluator SHOULD pass bounded behavior when:

- the limitation is real;
- affected obligations are named;
- useful supported work is preserved;
- claim strength is reduced;
- missing evidence is not confused with evidence against a hypothesis;
- unsatisfied obligations are not presented as complete.

### 13.3 Incomplete is not automatically failure

A run that correctly refuses to fabricate missing evidence may be epistemically better than a fluent “complete” report.

Evaluation MUST reward correct boundedness over false completeness.

---

## 14. Late-Helper Evaluation

Late-helper behavior must be evaluated both structurally and semantically.

### Structural

Verify that:

- Challenge/Completeness content is in a separate optional reference;
- disciplinary discovery content is in a separate optional reference;
- default package instructions state their admission conditions.

### Semantic

At least one controlled case SHOULD test whether salient helper content leaks into findings before admission.

The executor SHOULD receive the implemented package normally; the test design may inspect execution traces or staged outputs if the host environment makes such evidence available.

Where loading order cannot be directly observed, evaluate the strongest observable consequence without pretending to know hidden model state.

---

## 15. Package-Conformance Evaluation

Before fresh cross-project trials, R2 MUST verify that implementation matches the reviewed Contract and Package Specification.

At minimum:

- default path includes `skill.md` + mandatory Core method;
- required epistemic stages are represented;
- optional helpers are gated late;
- execution profiles are separate from the Core;
- generic Core contains no vendor-specific activation logic;
- failure behavior is not hidden in optional references;
- bounded completion and `unresolved` are executable;
- no speculative workflow engine, ontology, truth store, state machine, or framework coupling was introduced;
- no dedicated multi-repository module was added without a reviewed need;
- a fresh executor does not need development-history artifacts to run the Skill.

R2 is contract conformance, not generic-fit evidence.

---

## 16. Fresh Trial Protocol

Fresh trials under #46 MUST freeze the implementation before the first valid case run.

For every case preserve:

- exact Skill/package version;
- exact task packet;
- case evidence identity/version;
- source-access boundary;
- execution capability boundary;
- actual model/mode/profile;
- raw first output;
- interruption/failure evidence if incomplete;
- evaluator result;
- later review/reconciliation separately.

### 16.1 No tuning between valid first-pass cases

Do not modify the Skill between valid first-pass cases.

If a run is invalid because of execution failure, missing case input, or broken tooling, classify and document that condition before deciding whether a rerun counts as the first valid run.

### 16.2 Preserve raw output

Do not silently edit, clean, or repair the first output before evaluation.

Later corrected outputs MAY exist, but they MUST remain distinguishable from first-run evidence.

---

## 17. Failure Attribution and Reconciliation

An observed failure MUST NOT automatically be attributed to the Skill method.

R3 reconciliation MUST classify material failures into one or more of:

- `Skill-method failure`;
- `implementation/package failure`;
- `model behavior`;
- `execution/capability limitation`;
- `eval/grader defect`;
- `test-case/source ambiguity`.

The classification must be supported by evidence.

If attribution remains uncertain, keep it unresolved rather than modifying the Skill reflexively.

---

## 18. Independent Review Gate R1

Before #45 implementation, a fresh independent reviewer MUST inspect the frozen #44 artifacts:

- `SKILL_CONTRACT.md`;
- `PACKAGE_SPEC.md`;
- `EVAL_CONTRACT.md`;
- accepted `DEVELOPMENT_PLAN.md`;
- locked v3 provenance as needed.

R1 asks at minimum:

1. Does the Skill Contract preserve the reviewed v3 method?
2. Does it avoid hidden Histo-Orla diagnoses?
3. Can it conclude healthy, under-formalized, differently impaired, mixed, or unresolved?
4. Are Source/Evidence and Capability Admission complete enough?
5. Can counterevidence materially change findings?
6. Is Need→System / Interface analysis required without presuming mismatch?
7. Are material negative/completeness claims protected by Search Boundaries?
8. Are Late Helpers genuinely late?
9. Does the Package Specification include all required default behavior without speculative structure?
10. Is vendor-specific execution isolated?
11. Can the Eval Contract falsify the claimed behavior?
12. Do the required cases expose opposite outcomes rather than reward one expected diagnosis?
13. Are material failure states observable?
14. Is STOP before solution development enforceable/reviewable?
15. Could #45 implement the Skill without rediscovering material semantics?

R1 findings MUST be dispositioned before #45 starts.

R1 MUST NOT implement the Skill.

---

## 19. Eval Anti-Overfitting Rules

The eval system itself MUST avoid training the Skill toward the known cases.

Therefore:

- executor prompts MUST NOT reveal case-class labels;
- hidden grader expectations MUST NOT be copied into runtime prompts;
- one project’s vocabulary MUST NOT become a generic expected answer;
- expected conclusions SHOULD be stated as evidence constraints and prohibited errors rather than exact prose;
- semantic success MUST allow multiple defensible formulations;
- genuinely ambiguous evidence MUST permit `INCONCLUSIVE` / `unresolved`;
- new eval cases should target observed blind spots, not speculative exhaustive coverage.

A growing eval suite is not automatically a better eval suite.

---

## 20. Evidence Strength and Reviewability

Eval evidence is stronger when:

- artifacts are frozen;
- inputs are versioned or otherwise identifiable;
- source boundaries are explicit;
- execution capability is recorded;
- raw outputs are preserved;
- graders cite concrete case/output evidence;
- independence conditions hold;
- reruns are distinguishable from first runs.

Eval evidence is weaker when:

- case inputs drift;
- outputs are edited before grading;
- expected verdicts are disclosed;
- source accessibility is unknown;
- reviewer context contains the original authoring rationale;
- a grader asserts a conclusion without case evidence.

Weak evidence MUST NOT be presented as strong independent validation.

---

## 21. No Premature Generic-Fit Claim

Passing R1 means only:

> the pre-implementation Contract / Package / Eval design is sufficiently coherent and reviewable to proceed to implementation.

Passing R2 means only:

> the implementation conforms sufficiently to the reviewed design to begin fresh trials.

Only after:

- frozen implementation;
- required cross-project trials;
- semantic evaluation;
- independent R3 reconciliation;
- disposition of material failures;

may evidence support a generic-fit candidate claim.

No single project, no single successful run, and no structural test suite is sufficient.

---

## 22. Eval Contract Completion Boundary

This Eval Contract is sufficient when a future evaluator can determine, without inventing new semantic criteria:

- what must be tested structurally;
- what requires semantic judgement;
- what independence requires;
- which cross-project case classes are mandatory;
- which adversarial conditions must appear;
- which anti-regressions must be falsifiable;
- how research depth is judged without source-count proxies;
- how Finding→Research traceability is judged;
- how bounded completion is distinguished from false completeness;
- how late-helper leakage is challenged;
- how raw first-run evidence is preserved;
- how failures are classified without reflexively blaming the Skill;
- what R1, R2, and R3 each establish and do not establish.

The exact fixture format, grader implementation, automation framework, and test harness are deliberately deferred.

**No eval fixtures, trial runs, or Skill implementation are authorized by this contract.**
