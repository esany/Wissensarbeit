# Core Method — System Analysis + Finding-Driven Deep Research

This file is the mandatory detailed execution method for the Skill.

It assumes that `../skill.md` has already established trigger, evidence admission, capability admission, authority, and completion boundaries.

Do not skip this file for substantive executions.

---

## 1. Execution sequence

Preserve every epistemic function in this order, even if some steps are operationally combined:

```text
Current-State / Evidence Reconstruction
→ Empirical System Analysis
→ Need → System / Interface Analysis
→ Material Findings / Problem or Mechanism Clusters
→ Competing Explanations
→ Research Agenda Gate
→ Finding-Driven External Research
→ Theory / Investigation Methodology / Empirical Evidence
→ Related Work / Best-Practice Evidence / Counterevidence
→ Analytical Reconnection
→ Cross-Finding Tensions / Counterfindings
→ Research Gaps / unresolved
→ Coverage Check
→ STOP
```

The sequence is not a report template. It is the required logic of inquiry.

---

## 2. Current-State and Evidence Reconstruction

Reconstruct the investigated system sufficiently to understand both its relevant present condition and the history needed to interpret that condition.

Address, as applicable:

- investigation intent and owner/user goals;
- actual user or professional work;
- relevant domain logic and quality criteria;
- requirements or product logic;
- technical structures and actual use;
- organization, roles, handoffs, and decisions;
- treatment of evidence, interpretation, uncertainty, and authority;
- relevant development, usage, failure, recovery, and correction episodes;
- evidence boundaries.

### 2.1 Current evidence before inherited interpretation

Keep current project/system evidence distinct from:

- prior audits;
- earlier diagnoses;
- historical reports;
- inherited labels;
- secondary summaries;
- generic theories or Best Practice.

Earlier interpretations may be useful hypotheses or leads. They are not current truth merely because they are confident, detailed, or previously accepted.

### 2.2 Evidence-role discipline

Where material to the interpretation, distinguish:

- directly observed project/system evidence;
- inferred project/system interpretation;
- historical evidence;
- external research evidence;
- hypothesis;
- inaccessible or unavailable evidence;
- unresolved contradiction.

Do not fill missing project evidence with plausible theory.

### 2.3 Temporal reconstruction

Do not collapse materially different time horizons.

When useful, reconstruct important episodes as:

```text
initial state / trigger
→ evidence available at the time
→ interpretation at the time
→ intervention or behavior
→ observed effect
→ side effect / correction / recovery
→ current status
```

A previously real problem can now be resolved. A historically successful mechanism can now be degraded. A one-off incident is not automatically a recurring condition.

### 2.4 Source authority and inspection depth

For material claims, note when:

- source authority or provenance is unclear;
- only a secondary summary is available;
- the primary source cannot be inspected;
- access is partial;
- retrieval or citation limits constrain verification.

Do not silently strengthen a source because it is the only source available.

### 2.5 Contradictions

Preserve contradictory project evidence.

Try to explain contradictions only with evidence, for example through:

- source authority;
- chronology;
- context;
- scope;
- reliability;
- intervention or state change.

If the contradiction cannot be resolved, keep it unresolved.

---

## 3. Empirical System Analysis

Analyse what the system actually does and what effects are visible before assigning known diagnostic labels.

Look for evidence about:

- structures;
- behavior;
- transitions;
- outcomes;
- frictions;
- trade-offs;
- protections;
- recoveries;
- failure or correction episodes;
- local versus end-to-end effects.

Treat the system socio-technically. Do not assume in advance that the decisive mechanism is:

- technical;
- organizational;
- governance/control;
- domain-specific;
- data-related;
- interface-related;
- user-work related.

All remain possibilities until evidence discriminates among them.

### 3.1 Low-leading-bias rule

Do not begin from a catalogue of expected pathologies.

A phenomenon becomes a finding because project/system evidence supports it, not because it resembles a familiar anti-pattern.

### 3.2 Opposite outcomes remain valid

The evidence may support:

- a material problem;
- excessive structure;
- insufficient structure/formalization;
- a domain/data/technical-quality issue;
- an organizational or interface issue;
- a protective or recovery mechanism;
- a mixed result;
- a largely healthy system;
- no support for an inherited diagnosis;
- unresolved interpretation.

Do not force the case toward one expected diagnosis.

---

## 4. Need → System / Interface Analysis

Examine whether and how the system translates:

- needs;
- uncertainty;
- non-knowledge;
- evidence;
- constraints;
- requirements

through project interpretation, organizational processes, technical representation, and actual use.

For material signals, reconstruct as far as the evidence permits:

```text
observable need / pain / uncertainty / mental model
→ domain meaning
→ project interpretation
→ requirement / process / technical representation
→ actual effect
→ current fit
```

### 4.1 Do not presume mismatch

A Need → System chain may be:

- well-fitting;
- partially fitting;
- misfitting;
- positively protective;
- materially irrelevant to the case;
- unresolved.

If the evidence supports a well-fitting translation/interface chain, preserve that result.

Do not manufacture a need/representation mismatch merely because this analysis is mandatory.

### 4.2 Interface mechanisms are independent candidates

Do not automatically assign blame to either side of an interface.

A material effect may arise from:

- the need itself;
- its interpretation;
- representation;
- handoff;
- control structure;
- actual use;
- feedback;
- the interaction among these.

Keep the mechanism open until evidence supports a narrower account.

---

## 5. Material Findings and Problem/Mechanism Clusters

Derive material findings from project/system evidence before constructing the Research Agenda.

Possible finding types include:

- current problems;
- recurring problems;
- resolved historical problems;
- latent risks;
- effective mechanisms;
- protective/recovery mechanisms;
- one-off/tool-specific effects;
- insufficient structure/formalization;
- excessive or misplaced structure;
- domain-quality issues;
- data-quality issues;
- technical-quality issues;
- organizational/coordination issues;
- interface issues;
- evidence that the system is substantially healthy;
- unresolved phenomena.

### 5.1 Minimum information for central findings

Retain enough information for a reviewer to distinguish:

- **Observed phenomenon** — what happened or exists.
- **Evidence** — what supports it and with what source/access limits.
- **Temporal status** — current, recurring, historical, latent, one-off, protective, or unresolved as materially relevant.
- **Materiality** — why it matters for understanding the system.
- **Possible mechanism** — what may explain it.
- **Uncertainty** — what is not yet established.

Known labels or anti-pattern names may be attached only after the empirical phenomenon exists and only when they improve explanation.

### 5.2 Finding-status semantics

Where currentness or temporal status materially affects interpretation, preserve distinctions equivalent to:

- `current-active`;
- `recurring`;
- `historical-resolved`;
- `historical-with-latent-risk`;
- `protective/recovery-mechanism`;
- `one-off/tool-specific`;
- `unresolved`.

These are reporting semantics, not a required persistent enum or state machine.

---

## 6. Competing Explanations

For every central finding, consider materially plausible alternatives before explanatory closure.

Possible discriminators include:

- alternative causal mechanisms;
- confounders;
- opposite interpretations;
- historical explanations;
- local-versus-system effects;
- missing-evidence explanations;
- measurement/observation artifacts;
- positive or contradictory evidence.

A coherent story is not evidence of monocausality.

When available evidence cannot discriminate between plausible explanations, keep the uncertainty explicit.

### 6.1 Counterfactual challenge

For important findings, ask at least:

- What evidence would make this interpretation weaker?
- What alternative explanation fits the same observations?
- Is the apparent problem possibly a protective response to another condition?
- Is a locally beneficial mechanism creating a wider cost?
- Could the observed effect be historical, temporary, or measurement-driven?
- Could the opposite structural problem also explain the evidence?

These questions are challenge logic, not a diagnostic catalogue.

---

## 7. Research Agenda Gate

Do not begin substantial external research for a finding until a research need has been derived from that finding.

For each material research need establish enough of:

- **Project/System Finding** — the observed project phenomenon;
- **Unknown** — what remains unexplained;
- **Competing Explanations** — interpretations needing discrimination;
- **Research Question(s)** — what external research must answer;
- **Relevant fields / terminology** — only where needed for discovery;
- **Theory Need** — explanatory mechanisms to examine;
- **Method Need** — how the field determines whether the phenomenon is present;
- **Evidence Need** — relevant empirical evidence classes;
- **Related Work Need** — comparable systems/cases that may inform mechanism or conditions;
- **Counterevidence Target** — what would weaken the current interpretation;
- **Research Depth** — Tier A, B, or C responsibility.

The representation may be prose, table, linked notes, or another reviewable form.

### 7.1 Anchor rule

A substantial research block must identify a material project/system finding as its anchor.

If it cannot, either:

- omit the topic;
- keep it explicitly peripheral; or
- first establish a project finding that justifies it.

Otherwise the block is **Unanchored Research**.

### 7.2 Agenda revision

The Research Agenda is revisable.

External research may reveal:

- better terminology;
- another discipline;
- a different mechanism;
- a missing evidence class;
- a stronger counterposition;
- a misleading initial framing.

Revise the agenda when evidence warrants it, but preserve traceability back to the originating project finding.

---

## 8. Research Depth

Depth is an evidence responsibility, not a source-count target, prestige label, product mode, or report-length target.

Allocate depth primarily by:

- centrality of the finding to system understanding;
- uncertainty in its explanation;
- importance of discriminating competing explanations;
- consequence of getting the interpretation wrong.

Depth may change during research.

### 8.1 Tier A — central explanatory or materially uncertain finding

Tier A requires deep external challenge proportionate to the field and question.

Where available and relevant, examine:

- foundational or authoritative work;
- current empirical research;
- explanatory theory;
- competing theory or criticism;
- investigation-method literature;
- empirical evidence;
- counterevidence;
- Related Work or cases;
- Best-Practice evidence under conditions;
- backward/forward citation chaining where useful;
- source quality and inspection depth;
- transferability;
- Search Boundaries for relevant negative/completeness claims;
- saturation/stop judgement.

Tier A is not complete merely because several credible sources were found.

A Tier-A search may stop when additional high-quality searching mainly repeats established evidence, material counterpositions have been examined, and remaining uncertainty can be characterized explicitly.

### 8.2 Tier B — important supporting finding

Use multiple strong relevant sources or equivalent evidence coverage, plus:

- deliberate countercheck;
- transferability consideration.

It need not approximate an exhaustive review.

### 8.3 Tier C — contextual or bounded verification

Use targeted authoritative verification proportionate to the claim.

### 8.4 No fixed source counts

Never substitute source quantity for:

- relevance;
- quality;
- diversity of evidence;
- inspection depth;
- counterevidence;
- saturation;
- analytical reconnection.

---

## 9. Finding-Driven External Research

Organize research around the Research Agenda and its material findings, not around a predetermined catalogue of disciplines.

Research may discover new fields, terminology, mechanisms, evidence classes, or relevant cases.

Keep the link from each substantial research block to its originating finding visible.

### 9.1 Source quality and scope

For each material research claim, consider as appropriate:

- authority;
- publication type;
- population/context;
- recency;
- directness;
- primary versus secondary status;
- methodological quality;
- transferability to the investigated system.

Do not use a source simply because it supports the current interpretation.

### 9.2 External evidence does not replace project evidence

External theory or empirical research can explain or contextualize a project finding.

It cannot by itself establish that the phenomenon exists in the investigated project.

---

## 10. Theory, Investigation Methodology, and Empirical Evidence

For central research questions, keep these three functions materially distinct.

### 10.1 Theory

Ask:

- What mechanism or conceptual model could explain the phenomenon?
- Which competing theories, criticisms, or alternative mechanisms matter?

Theory explains.

### 10.2 Investigation methodology

Ask:

- How does the relevant field empirically determine whether the phenomenon is present?
- What study designs, measurements, operationalizations, data, validity risks, confounders, diagnostic methods, or observational methods are relevant?

Method investigates.

### 10.3 Empirical evidence

Ask:

- What reviews, studies, standards, technical evidence, or credible cases support, bound, or contradict the explanation?

Evidence observes or tests.

Do not treat theory as evidence that the project phenomenon is present.

Do not misrepresent a commonly used empirical method as an explanatory theory.

---

## 11. Related Work

Use Related Work to compare mechanisms and conditions, not merely feature similarity.

Where relevant ask:

- What comparable systems/cases show the same or an opposite mechanism?
- Under what conditions did the mechanism appear?
- What important contextual differences affect transfer?
- Did superficially similar systems produce different outcomes?
- Which cases expose boundary conditions?

A related system is useful because it sharpens explanation or transferability, not because it looks similar.

---

## 12. Best-Practice Evidence

Treat Best Practice as an evidence object, never as an adoption decision.

For material use, examine proportionally:

```text
evidence base
population / context
observed benefit
costs
preconditions
failure modes
countercases
maturity / controversy
transferability
```

Do not turn a supported practice into:

- “therefore adopt”;
- tool selection;
- target architecture;
- roadmap;
- implementation priority.

Those belong to later work under separate authority.

---

## 13. Counterevidence

Actively search for evidence capable of weakening the current interpretation.

Seek as relevant:

- counterfindings;
- competing schools;
- alternative terminology;
- failed applications;
- context dependence;
- cases where the proposed mechanism did not occur under apparently similar conditions;
- evidence that the system is healthier than the hypothesis implied;
- evidence of a different dominant mechanism.

Counterevidence must be capable of changing the analysis. Do not list it ceremonially and then preserve the original conclusion unchanged without explanation.

---

## 14. Search Boundaries

For material negative or completeness claims, expose the relevant Search Boundary sufficiently for a reviewer to interpret the claim.

A Search Boundary may include:

- repositories or databases searched;
- websites/domains;
- source classes;
- time window;
- languages;
- terms/concepts;
- citation-chain depth;
- access restrictions;
- excluded areas.

If no defensible boundary can be stated, downgrade the claim to “not established” or equivalent.

Do not treat incomplete search as evidence of absence or completeness.

---

## 15. Analytical Reconnection

External research must return to the originating project/system finding.

For every central researched finding, determine whether external evidence leaves it:

- `strengthened`;
- `weakened`;
- `reframed`;
- `contradicted`;
- `partial`;
- `conditional`;
- `unresolved`;

or equivalent semantics.

Explain why.

Where useful, state:

- what external evidence explains better than the initial project analysis;
- which project assumption was weakened or falsified;
- which transfer boundary limits application;
- what additional project evidence would discriminate remaining explanations.

Research is incomplete if it merely accumulates literature and never changes or tests understanding of the finding.

---

## 16. Finding → Research Traceability

Preserve the logical chain:

```text
Project/System Finding
→ Research Need
→ Research Question
→ External Evidence
→ Counterevidence
→ Analytical Reconnection
→ Remaining Uncertainty
```

A reviewer must be able to determine:

1. which project evidence produced the finding;
2. why external research was needed;
3. what was researched;
4. what evidence and counterevidence were found;
5. how the research changed or failed to change the finding;
6. what uncertainty remains.

The representation need not be a schema.

---

## 17. Cross-Finding Tensions and Counterfindings

After individual reconnection, examine important interactions across findings.

Ask whether:

- findings contradict one another;
- multiple mechanisms are simultaneously active;
- an apparently harmful mechanism is protective under some conditions;
- a recovery mechanism also creates costs;
- local success creates wider friction;
- an apparent problem is partly a response to another failure;
- external research makes the project look healthier than the initial hypothesis implied;
- current evidence indicates a material issue overlooked by earlier audits.

Do not force all findings into a single unified causal story.

---

## 18. Research Gaps and unresolved

Preserve material uncertainty.

Research Gaps may include:

- insufficient project evidence;
- competing explanations that remain indistinguishable;
- weak, contradictory, or inaccessible external evidence;
- missing empirical data;
- uncertain transferability;
- questions where further literature search is unlikely to help without new project evidence;
- capability limits preventing required depth.

No closed synthesis is required where evidence does not support one.

Use `unresolved` only when the evidence genuinely fails to discriminate, not to avoid difficult analysis.

---

## 19. Coverage Check

Before completion check at least:

### 19.1 Unresearched Major Finding

Is a central finding missing external challenge proportional to its importance or uncertainty?

If yes and the gap can still be corrected within scope/capability, correct it.

Otherwise expose the gap and do not claim that obligation complete.

### 19.2 Unanchored Research

Does any substantial research block lack a material project/system finding as its origin?

If yes, remove, bound, or re-anchor it.

### 19.3 Counterevidence

Was material counterevidence actively examined and allowed to affect conclusions?

### 19.4 Unsupported causal interpretation

Did a plausible mechanism become a causal conclusion without sufficient project or external evidence?

### 19.5 Current / historical collapse

Did a historical condition become “current” without fresh evidence?

### 19.6 Capability-limited research

Is any shallow or access-limited research being presented as fully complete?

### 19.7 Positive/protective mechanisms

Did the analysis systematically ignore functioning, protective, recovery, or healthy mechanisms because the task was framed as an audit?

### 19.8 Need → System distortion

Did the analysis either omit a material translation/interface mechanism or manufacture a mismatch where evidence supports fit?

---

## 20. Bounded completion

If full execution is impossible because of source, access, provenance, contradiction, or capability limits:

1. identify the limiting condition;
2. state which obligations or findings it affects;
3. preserve supported findings and useful partial work;
4. reduce or qualify claim strength;
5. identify material unanswered questions;
6. distinguish evidence gaps from evidence against a hypothesis;
7. avoid claiming full completion for unsatisfied obligations.

A bounded result can be epistemically correct.

A fluent but falsely complete result is not.

---

## 21. Optional helper admission

This Core does not require optional helper files.

If a host package later includes them:

- a challenge/completeness helper may be loaded only after empirical reconstruction and initial findings/clusters exist;
- a disciplinary-discovery helper may be loaded only when a concrete Research Agenda item needs field/term/method discovery.

Their content must not retroactively become project evidence.

Do not infer their contents from the existence of this section.

---

## 22. Result composition

No fixed final report template is required.

Choose a reviewable form suited to the case, but make available:

- investigation scope and material source boundaries;
- capability limitations;
- current/historical reconstruction;
- central findings/clusters;
- evidence and temporal status;
- competing explanations;
- Research Agenda and depth;
- external evidence;
- theory / investigation-method / empirical-evidence distinction;
- Related Work and Best-Practice evidence where relevant;
- counterevidence;
- analytical reconnection;
- cross-finding tensions/counterfindings;
- Research Gaps / unresolved;
- coverage status;
- major remaining uncertainty;
- explicit STOP boundary.

A useful final synthesis should foreground:

1. strongest supported findings;
2. most important counterfindings, weakening evidence, and reframings;
3. material tensions or conditional mechanisms;
4. largest remaining uncertainties;
5. open Research Gaps.

Do not append solution recommendations merely to make the report appear actionable.

---

## 23. Host-project authority and persistence

The output of this Skill is an analysis/research artifact.

It is not automatically:

- a Requirement;
- an accepted decision;
- architecture;
- priority;
- implementation authority;
- canonical project truth/state.

The host project retains authority over promotion and persistence.

The Skill may persist evidence, outputs, references, or provenance only when host-project rules permit or require it.

Do not create a new permanent registry, ontology, truth store, or state mechanism merely to preserve working analysis.

A downstream owner/process may later promote findings. That promotion is outside this Skill.

Changing model, tool, research mode, or execution environment does not change this authority boundary.

---

## 24. Final STOP

Stop before:

- target architecture;
- solution selection;
- tool/framework/vendor choice;
- adoption recommendation;
- roadmap creation;
- delivery prioritization;
- implementation plan;
- implementation execution;
- governance redesign.

You may identify conditions, evidence needs, or unanswered questions relevant to later solution work.

Do not perform that downstream work under this Skill.

Terminal epistemic output:

```text
supported findings
+ counterfindings
+ competing explanations
+ external evidence
+ analytical reconnection
+ tensions
+ Research Gaps
+ explicit uncertainty
```

**STOP before solution development.**
