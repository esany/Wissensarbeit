# System Analysis + Finding-Driven Deep Research — Skill Contract

**Status:** contract candidate for Issue #44 pre-implementation review  
**Parent:** Issue #43 — System Analysis + Finding-Driven Deep Research  
**Development baseline:** PR #47 — `DEVELOPMENT_PLAN.md` at accepted head `d97043d736bd03386667e107358194a521030266`  
**Method provenance:** `esany/pflege-arnshaugk-historie` PR #123 at reviewed head `e112a8985e8c5149b6f84fb3ae8174a6202a40a2`

Reviewed provenance artifacts:

- `generic-system-analysis-deep-research-prompt-v3-20260922.md`
- `generic-system-analysis-deep-research-v3-refactoring-20260922.md`
- `generic-system-analysis-deep-research-v3-appendices-20260922.md`
- `execution-profile-chatgpt-deep-research-v3-20260922.md`

This contract defines required Skill behavior. It does **not** define runtime architecture, package layout, persistence schemas, vendor-specific execution, evaluation fixtures, or implementation design.

The terms **MUST**, **MUST NOT**, **SHOULD**, and **MAY** are normative.

---

## 1. Purpose

The Skill is a vendor-neutral epistemic method for deeply analysing an existing project or system and deriving external research from the material findings of that analysis.

Its required knowledge path is:

```text
empirical project/system analysis
→ material findings / problem clusters
→ competing explanations
→ Research Agenda derived from findings
→ finding-driven external research
→ theory + investigation methodology + empirical evidence
→ Related Work + Best-Practice evidence + counterevidence
→ analytical reconnection to original findings
→ cross-finding tensions + Research Gaps / unresolved
→ STOP before solution development
```

The Skill produces an evidence-grounded understanding of:

- what is happening in the investigated system;
- what is sufficiently supported versus uncertain;
- which mechanisms may explain material findings;
- what external knowledge is needed to discriminate between explanations;
- how external evidence strengthens, weakens, reframes, contradicts, conditions, or fails to resolve the original findings.

The Skill is **not** a long-report generator. Report length, section count, source count, or use of a particular research product do not constitute successful execution.

The Skill differs from ordinary literature research because its external Research Agenda MUST arise from empirical findings in the investigated project/system.

The Skill differs from architecture, design, planning, and implementation work because it MUST stop before choosing solutions, target states, technologies, delivery priorities, or implementation actions.

---

## 2. Core Epistemic Invariants

Every conforming implementation MUST preserve the following invariants.

1. **Empirical reconstruction precedes diagnosis.**
2. **Leading bias is minimized.** The normal path MUST NOT begin from a catalogue of expected diagnoses or failure patterns.
3. **Current evidence outranks inherited interpretation.** Earlier audits, reports, diagnoses, and labels are inputs or hypotheses, not current truth.
4. **System analysis generates the Research Agenda.**
5. **External research is finding-driven.**
6. **Competing explanations and counterevidence are constitutive, not optional polish.**
7. **Theory, investigation methodology, and empirical evidence remain distinguishable.**
8. **Best Practice is examined as conditional evidence, not converted into adoption advice.**
9. **Research depth is proportional to materiality and uncertainty.**
10. **A largely healthy system is a valid result.**
11. **Insufficient formalization or a need for more structure is a valid result.**
12. **Domain, data, technical, organizational, interface, user-work, or other explanations remain possible unless evidence rules them out.**
13. **Findings that contradict earlier diagnoses are valid.**
14. **`unresolved` is a valid result.**
15. **The Core is vendor-neutral.**
16. **Product- or platform-specific execution belongs outside the Core.**
17. **The Skill stops before solution development.**
18. **Skill output does not automatically become host-project truth.**

An implementation MUST NOT weaken these invariants merely because doing so simplifies execution.

---

## 3. Trigger Contract

The Skill SHOULD be used when the task requires an integrated empirical system analysis followed by research derived from what that analysis finds.

Appropriate triggers include cases where:

- an existing project, repository, product, research system, organization, workflow, or other socio-technical system requires deep analysis;
- symptoms, frictions, failures, trade-offs, or unexplained outcomes are visible but their explanation remains open;
- existing diagnoses need independent empirical revalidation;
- the relationship between user/domain needs and system representation or operation is unclear;
- material project findings need to generate an external Research Agenda;
- competing explanations must be discriminated using theory, empirical methods, external evidence, Related Work, or counterevidence;
- the current project may be healthy, over-structured, under-structured, differently impaired than previously assumed, or mixed;
- research findings need to be reconnected analytically to specific project evidence;
- deep understanding is required while solution selection is intentionally out of scope.

The presence of the word “research”, “audit”, “analysis”, “architecture”, or “repository” alone is not sufficient to trigger this Skill.

The distinguishing trigger is the need for the chain:

```text
project/system evidence
→ empirical findings
→ research needs
→ external research
→ analytical reconnection
```

---

## 4. Non-Trigger Contract

The Skill SHOULD NOT be used where the task can be adequately completed without empirical reconstruction of a project/system and finding-driven research.

Typical non-triggers include:

- a simple literature or factual question;
- an already isolated and sufficiently precise research question that does not require project/system reconstruction;
- ordinary web research;
- source discovery only;
- summarization or synthesis of already supplied material;
- ordinary code review;
- review of a single implementation defect where broader system reconstruction is unnecessary;
- a bounded debugging task;
- architecture or target-state selection;
- tool, vendor, framework, or product selection;
- solution design;
- roadmap creation;
- implementation planning;
- implementation execution;
- optimization of an already selected solution;
- tasks whose required evidence is entirely external and has no material project/system anchor.

If a task begins with system analysis but subsequently asks for solutions, the Skill MAY perform the analysis portion but MUST stop or hand off at the solution-development boundary rather than silently expanding its authority.

---

## 5. Required Inputs

The Skill requires enough information to identify the investigation and judge its evidence and capability boundaries.

At minimum it MUST establish:

### 5.1 Investigation object

What project, product, repository, process, research system, organization, or other system is being investigated.

GitHub or any particular storage system MUST NOT be assumed.

### 5.2 Investigation scope

The relevant boundaries, which may include:

- time period;
- components or workstreams;
- relevant actors or user groups;
- domain boundaries;
- excluded areas;
- the question or concern motivating investigation.

The scope MAY evolve when empirical evidence reveals that the initial boundary hides a material interface or dependency. Such expansion MUST be visible rather than silently assumed.

### 5.3 Current project/system evidence

Evidence reasonably capable of supporting reconstruction of the present or relevant historical state.

Examples may include project artifacts, records, source material, user/owner evidence, system outputs, operational evidence, correspondence, decisions, code, data, documentation, or other case-appropriate sources.

No particular evidence format is mandatory.

### 5.4 Known constraints

Relevant access, time, confidentiality, source, tool, research, or execution limitations.

### 5.5 Prior interpretations, when available

Earlier audits, diagnoses, reviews, research reports, or explanatory narratives MAY be provided.

Their presence is not required.

When present, they MUST be treated as prior interpretation or research leads until revalidated.

### 5.6 External research access

The execution must establish what external research capability and source classes are actually available.

### 5.7 Source and tool boundaries

Material limitations on source access, inspection depth, retrieval, citation, provenance, or preservation MUST be known or discovered during admission.

Inputs need not be complete before work begins. Missing inputs MUST remain visible and MUST affect claim strength, research scope, or completion status where material.

---

## 6. Source and Evidence Admission

Source admission determines what the available evidence permits the Skill to claim.

It does not decide whether a particular tool is powerful enough; that is Capability Admission.

### 6.1 General rule

The Skill MUST distinguish:

```text
what is directly supported
what is inferred
what is historical
what is externally researched
what remains hypothetical
what cannot currently be established
```

Missing project evidence MUST NOT be replaced by theory, generic best practice, plausible reconstruction, or prior audits.

### 6.2 Incomplete current evidence

When current evidence is incomplete, the Skill MAY continue where useful, but MUST:

- state the material gap;
- restrict claims to what the accessible evidence supports;
- preserve hypotheses as hypotheses;
- reduce confidence where appropriate;
- identify what further evidence would discriminate important explanations;
- use `unresolved` where the missing evidence prevents a justified conclusion.

It MUST NOT fabricate a coherent current state merely to complete the analysis.

### 6.3 Inaccessible sources

When a material source or source class cannot be accessed, the Skill MUST make the access boundary visible.

If the inaccessible evidence is necessary to support a central current-state claim or a required Tier-A research obligation, the execution MUST NOT present that obligation as fully satisfied.

### 6.4 Contradictory project evidence

Contradictory evidence MUST be preserved and analysed.

The Skill MUST NOT resolve a contradiction merely by choosing the source that best supports an emerging narrative.

Where authority, temporal ordering, context, or reliability can explain the contradiction, that explanation MAY be evaluated.

Where it cannot, the relevant issue remains `unresolved`.

### 6.5 Historical evidence only

Historical evidence MAY support historical reconstruction.

It MUST NOT by itself establish that the same condition is current.

A historical finding can only be treated as current when fresh evidence supports that interpretation.

### 6.6 Prior audits and strong inherited diagnoses

Prior audits, reports, and diagnoses MUST be treated as:

- prior hypotheses;
- prior interpretations;
- possible research leads;
- possible evidence about historical understanding.

Their authority or apparent confidence MUST NOT substitute for current revalidation.

A prior diagnosis MAY ultimately be strengthened, weakened, reframed, contradicted, or remain unresolved.

### 6.7 Unclear source authority

When the authority or provenance of a source is unclear, the Skill MUST qualify its use accordingly.

A secondary summary MUST NOT silently become equivalent to the primary evidence it summarizes.

### 6.8 Different time horizons

Evidence from materially different time periods MUST be kept temporally distinguishable.

The Skill MUST NOT collapse:

- historical and current conditions;
- pre-intervention and post-intervention evidence;
- temporary incidents and recurring patterns;
- resolved problems and latent risks.

### 6.9 Secondary evidence without primary access

Secondary evidence MAY be used when primary evidence is inaccessible, but the inspection limitation MUST be visible for claims where it matters.

For central claims, lack of primary access SHOULD reduce confidence or create an explicit evidence gap unless the secondary source itself is sufficiently authoritative for the claim.

---

## 7. Capability Admission

Before claiming full execution, the Skill MUST determine whether the available execution environment can perform the epistemic work required by the case.

Capability Admission MUST consider at least:

- whether the investigation object can be inspected adequately;
- whether relevant current project/system sources can be accessed;
- whether external research is available;
- whether sources can be inspected deeply enough for the claims required;
- whether relevant counterevidence can be sought;
- whether citation/provenance or equivalent evidence traceability can be maintained;
- whether necessary working state or evidence references can be retained sufficiently for coherent execution;
- whether the required research depth is realistically achievable.

Capability is evaluated against the demands of the actual case, not against a fixed product checklist.

### 7.1 No silent downgrade

An execution MUST NOT silently perform shallower work than the contract requires and then present the result as complete.

Examples include:

- claiming current-state reconstruction without access to material current evidence;
- claiming Tier-A research after only superficial search;
- claiming counterevidence review when the relevant source space could not be examined;
- claiming full Deep Research simply because a report is long or many sources were returned.

### 7.2 Tier-A capability shortfall

When a material finding requires Tier-A depth but the available execution capability cannot provide it, the Skill MUST:

- state the limitation;
- preserve any useful partial research;
- mark the unsatisfied research obligation;
- propagate the limitation into reconnection and completion;
- refrain from claiming full completion of that research need.

A vendor-specific “Deep Research” mode is neither necessary nor sufficient by itself. What matters is whether the required evidence work can actually be performed.

---

## 8. Authority Boundary

### 8.1 Permitted authority

Within the investigation scope, the Skill MAY:

- observe;
- reconstruct;
- compare;
- analyse;
- problematize;
- identify material findings;
- identify positive or protective mechanisms;
- form problem or mechanism clusters;
- generate competing explanations;
- formulate hypotheses;
- derive a Research Agenda;
- perform or route external research;
- seek counterevidence;
- challenge inherited interpretations;
- falsify or weaken hypotheses;
- strengthen hypotheses;
- reframe findings;
- preserve uncertainty;
- identify Research Gaps;
- conclude that a suspected problem is unsupported;
- conclude that more formalization or structure may be needed;
- conclude that the system is largely healthy;
- leave matters unresolved.

### 8.2 Prohibited authority

The Skill MUST NOT, by virtue of this contract:

- select a target architecture;
- prescribe a system redesign;
- decide tool or framework adoption;
- select vendors;
- create a delivery roadmap;
- prioritize implementation work;
- authorize implementation;
- create or promote requirements;
- alter host-project priorities;
- infer owner acceptance;
- treat external best practice as an adoption decision;
- redesign governance;
- promote its findings automatically into host-project truth;
- acquire additional decision authority merely because a stronger model, tool, research mode, or execution environment was used.

If downstream solution work is required, it MUST occur under separate authority after this Skill has stopped.

---

## 9. Late-Helper Admission

The normal execution path MUST begin without leading diagnostic catalogues.

Challenge, completeness, disciplinary-discovery, terminology, or search aids MAY support the Skill, but their admission is constrained.

### 9.1 Challenge and completeness aids

A challenge/completeness aid MAY be used only after:

1. empirical reconstruction has occurred; and
2. initial findings or problem/mechanism clusters have been formed independently of that aid.

Its role is to challenge omissions, not generate the expected result.

Candidate issues introduced solely by a checklist MUST be discarded unless project evidence supports them.

### 9.2 Disciplinary and search aids

A disciplinary discovery map, terminology map, or broad field list MAY be used only when a concrete finding or Research Agenda item requires help locating relevant conceptual, methodological, or empirical fields.

It MUST NOT become the primary report structure or force every listed discipline into the research.

### 9.3 Exceptions

If an early helper is materially necessary for a specific investigation, the execution MUST:

- state why;
- identify what was introduced before empirical reconstruction;
- treat any resulting framing as potentially leading;
- test plausible opposite or alternative interpretations;
- avoid presenting helper-derived categories as empirical findings without evidence.

An exception MUST NOT silently turn the default method into checklist-led diagnosis.

---

## 10. Required End-to-End Process

The implementation MAY combine steps operationally, but it MUST preserve every epistemic function below.

### 10.1 Current-State and Evidence Reconstruction

Reconstruct the system sufficiently to understand its relevant present condition and history.

The reconstruction MUST address, as applicable:

- investigation intent and owner/user goals;
- actual user or professional work;
- relevant domain logic and quality criteria;
- requirements or product logic;
- technical structures and actual use;
- organization, roles, handoffs, and decisions;
- treatment of evidence, interpretation, uncertainty, and authority;
- relevant development, usage, failure, recovery, and correction episodes;
- evidence boundaries.

Earlier audits and interpretations MUST remain distinguishable from primary or current evidence.

Historical reconstruction SHOULD preserve causal humility. Where useful, relevant episodes can be reconstructed as:

```text
initial state / trigger
→ evidence available at the time
→ interpretation at the time
→ intervention or behavior
→ observed effect
→ side effect / correction / recovery
→ current status
```

### 10.2 Empirical System Analysis

Analyse actual structures, behavior, transitions, outcomes, frictions, protections, and recoveries.

The analysis MUST NOT begin by assigning known diagnosis labels.

It SHOULD consider the system socio-technically rather than assuming that the decisive mechanism is technical, organizational, governance-related, or domain-specific.

Possible explanatory classes MAY include domain, technical, organizational, interface, governance/control, and user-transferred complexity, but none is presumed pathological.

### 10.3 Need → System / Interface Analysis

The Skill MUST examine whether and how:

- needs;
- uncertainty;
- non-knowledge;
- evidence;
- constraints;
- requirements

are translated through project interpretation, organizational processes, technical representation, and actual use.

The depth of this analysis MAY be proportional to the investigation. If no material translation or interface phenomenon is supported by the evidence, the Skill MUST preserve that result rather than manufacture one.

For material signals, the Skill MUST reconstruct, to the extent the available evidence permits, the chain:

```text
observable need / pain / uncertainty / mental model
→ domain meaning
→ project interpretation
→ requirement / process / technical representation
→ actual effect
→ current fit
```

Interface phenomena MUST be treated as possible independent mechanisms rather than automatically assigning blame to either side of the interface.

### 10.4 Material Findings and Problem/Mechanism Clusters

The Skill MUST derive material findings from the evidence before constructing the Research Agenda.

Findings MAY include:

- current problems;
- recurring problems;
- resolved historical problems;
- latent risks;
- effective mechanisms;
- protective or recovery mechanisms;
- one-off or tool-specific effects;
- insufficient structure or formalization;
- excessive or misplaced structure;
- domain-quality issues;
- data-quality issues;
- technical-quality issues;
- organizational or coordination issues;
- interface problems;
- conditions indicating the system is substantially healthy;
- unresolved phenomena.

For each central finding or cluster, enough information MUST be retained to distinguish:

- the observed phenomenon;
- supporting evidence and current status;
- why it is material;
- possible mechanism;
- remaining uncertainty.

Known labels or anti-pattern names MAY be attached only after the empirical phenomenon exists and only if they improve explanation.

### 10.5 Competing Explanations

For every central finding, the Skill MUST consider materially plausible alternatives before settling on an explanation.

This includes, as applicable:

- alternative causal mechanisms;
- confounders;
- opposite interpretations;
- historical explanations;
- local-versus-system effects;
- missing-evidence explanations;
- measurement or observation artifacts;
- positive or contradictory evidence.

A coherent narrative is not sufficient evidence for monocausality.

Where available evidence cannot discriminate between plausible explanations, the uncertainty MUST remain explicit.

### 10.6 Research Agenda Gate

External research for a finding begins only after a research need has been derived from that finding.

For each material research need, the execution MUST establish enough of the following to route research intelligently:

- **Project Finding** — what has actually been observed;
- **Unknown** — what remains unexplained;
- **Competing Explanations** — which interpretations need discrimination;
- **Research Question(s)** — what external research must answer;
- **Relevant fields or terminology** — when needed for discovery;
- **Theory Need** — what explanatory mechanisms need examination;
- **Method Need** — how the field establishes whether the phenomenon is present;
- **Evidence Need** — what empirical evidence classes are relevant;
- **Related Work Need** — what comparative systems or cases could inform the question;
- **Counterevidence Target** — what would weaken the current interpretation;
- **Research Depth** — Tier A, B, or C responsibility.

The exact representation is not prescribed.

Research that cannot identify a material project/system finding as its anchor MUST NOT become a substantial research block under this Skill.

### 10.7 Finding-Driven External Research

External research MUST be organized around the Research Agenda and its material findings rather than a predetermined catalogue of academic disciplines.

Research MAY discover new terminology, fields, mechanisms, or evidence classes.

The Research Agenda MUST therefore be revisable when research shows that its initial framing was incomplete or misleading.

Changing the framing does not sever traceability to the original finding.

### 10.8 Theory, Investigation Methodology, and Empirical Evidence

For central research questions the Skill MUST keep distinct:

#### Theory

What mechanism or conceptual model explains the phenomenon?

Which competing theories or criticisms matter?

#### Investigation methodology

How does the relevant field empirically determine whether the phenomenon is present?

This may include:

- study designs;
- measurements;
- data;
- operationalizations;
- validity risks;
- confounders;
- diagnostic or observational methods.

#### Empirical evidence

What actual reviews, studies, standards, technical evidence, or credible cases support, bound, or contradict the explanation?

Theory MUST NOT substitute for evidence that the phenomenon is present in the investigated project.

A commonly used empirical method MUST NOT be misrepresented as an explanatory theory.

### 10.9 Related Work, Best-Practice Evidence, and Counterevidence

Where relevant, Related Work SHOULD examine comparable real systems, infrastructures, projects, or practices for mechanisms and conditions rather than feature similarity alone.

Best-practice evidence MUST be treated as an evidence object.

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

The Skill MUST NOT convert this analysis into an adoption recommendation.

Research MUST actively seek evidence capable of weakening the current interpretation, including:

- counterfindings;
- competing schools;
- alternative terminology;
- failed applications;
- context dependence;
- cases where the proposed mechanism did not occur under apparently similar conditions.

For material negative or completeness claims, the relevant Search Boundary MUST be made visible to the extent necessary to interpret the claim.

If no defensible Search Boundary can be stated, the Skill MUST qualify the claim as not yet established rather than present incomplete searching as evidence of absence or completeness.

### 10.10 Analytical Reconnection

External research MUST return to the original project/system finding.

For every central researched finding, the result MUST state whether the external evidence leaves it:

- `strengthened`;
- `weakened`;
- `reframed`;
- `contradicted`;
- `partial`;
- `conditional`; or
- `unresolved`.

Equivalent wording MAY be used if the semantic distinction is preserved.

The reconnection MUST explain why.

Where relevant it SHOULD state:

- what external evidence explains better than the original project analysis;
- which project assumption was weakened or falsified;
- what transfer boundary limits application of external evidence;
- what additional project evidence would discriminate remaining explanations.

Research is incomplete if it merely accumulates literature without changing or testing understanding of the finding.

### 10.11 Cross-Finding Tensions and Counterfindings

After individual reconnection, the Skill MUST examine relevant interactions across findings.

This includes asking whether:

- findings contradict each other;
- multiple mechanisms are simultaneously active;
- an apparently harmful mechanism is protective under some conditions;
- a recovery mechanism also produces costs;
- local success creates system-level friction;
- an apparent problem is partly a response to another failure;
- research makes the project look healthier than the initial hypothesis implied;
- current evidence indicates a problem overlooked by earlier audits.

The Skill MUST NOT force all findings into a single unified causal narrative.

### 10.12 Research Gaps and Unresolved

The Skill MUST preserve material uncertainty.

Research Gaps MAY include:

- insufficient project evidence;
- competing explanations that remain indistinguishable;
- weak, contradictory, or inaccessible external evidence;
- missing empirical data;
- uncertain transferability;
- research questions where further literature search is unlikely to help without new project evidence.

No closed synthesis is required where the evidence does not support one.

### 10.13 Coverage Check

Before completion, the Skill MUST check for at least:

- **Unresearched Major Finding** — a central finding has not received research proportional to its importance or uncertainty;
- **Unanchored Research** — a substantial research block lacks a material project/system finding as its anchor;
- material counterevidence not examined;
- unsupported causal interpretations;
- current/historical collapse;
- capability-limited research presented as complete.

When a gap can still be corrected within available scope and capability, the Skill SHOULD correct it.

Otherwise it MUST expose the gap.

### 10.14 STOP

The Skill MUST stop before:

- target architecture;
- solution selection;
- tool or framework choice;
- adoption recommendation;
- roadmap creation;
- delivery prioritization;
- implementation plan;
- implementation execution;
- governance redesign.

Findings MAY identify conditions or unanswered questions relevant to later solution work.

They MUST NOT themselves authorize or perform that downstream work.

---

## 11. Finding-Status Semantics

Current/historical status is normative because collapsing time materially changes the meaning of a finding.

For substantive findings, the Skill MUST preserve the distinctions represented by the provenance vocabulary:

- `current-active`;
- `recurring`;
- `historical-resolved`;
- `historical-with-latent-risk`;
- `protective/recovery-mechanism`;
- `one-off/tool-specific`;
- `unresolved`.

These terms are **epistemic reporting semantics**, not a mandated persistent enum or runtime state machine.

An implementation MAY use different presentation vocabulary where it preserves an unambiguous semantic mapping.

Not every minor observation requires a status label. The obligation applies where currentness, recurrence, resolution, protection/recovery, case-specificity, or unresolved status materially affects interpretation.

---

## 12. Research Depth Contract

Research depth expresses an evidence responsibility, not prestige, source quantity, product mode, or report length.

Depth MUST depend primarily on:

- centrality of the finding to system understanding;
- uncertainty in its explanation;
- importance of discriminating competing explanations;
- evidentiary consequence of getting the interpretation wrong.

Depth MAY change during research if new evidence changes a finding's centrality or uncertainty.

### 12.1 Tier A — Central explanatory or materially uncertain finding

Tier A requires deep external challenge proportionate to the field and question.

It SHOULD normally include, where available and relevant:

- foundational literature or authoritative foundations;
- current empirical research;
- explanatory theory;
- competing theory or criticism;
- investigation-method literature;
- empirical evidence;
- counterevidence;
- Related Work or cases;
- Best-Practice evidence under conditions;
- backward and/or forward citation chaining where useful;
- source-quality and inspection-depth awareness;
- transferability analysis;
- search-boundary awareness for relevant negative claims;
- a saturation or stop judgement.

Tier A MUST NOT be declared complete merely because several credible sources were found.

A Tier-A search can stop when additional high-quality searching primarily repeats already established evidence, material counterpositions have been examined, and remaining uncertainty can be explicitly characterized.

### 12.2 Tier B — Important supporting finding

Tier B requires multiple strong, relevant sources or equivalent evidence coverage plus a deliberate countercheck and transferability consideration.

It need not approximate an exhaustive review.

### 12.3 Tier C — Contextual or bounded verification

Tier C requires targeted authoritative verification proportionate to the contextual claim.

### 12.4 No fixed source count

The contract defines no universal minimum number of sources.

Source quantity MUST NOT substitute for:

- relevance;
- quality;
- diversity of evidence;
- inspection depth;
- counterevidence;
- saturation;
- analytical reconnection.

---

## 13. Traceability Contract

The Skill MUST preserve the logical chain:

```text
Project/System Finding
→ Research Need
→ Research Question
→ External Evidence
→ Counterevidence
→ Analytical Reconnection
→ Remaining Uncertainty
```

The implementation MAY represent this chain in prose, tables, linked sections, structured records, or another reviewable form.

The representation is sufficient only if a reviewer can determine:

1. which project evidence produced a material finding;
2. why external research was needed;
3. what was researched;
4. what evidence and counterevidence were found;
5. how that research changed or failed to change the original interpretation;
6. what uncertainty remains.

Two traceability failures are prohibited as silent completion:

### Unresearched Major Finding

A material finding requiring external challenge is left without proportional research and without an explicit research gap.

### Unanchored Research

A substantial external research block has no material project/system finding as its origin.

---

## 14. Required Result Content

The contract does not require one fixed report template.

A complete result MUST nevertheless make reviewably available:

- investigation scope and material source boundaries;
- relevant capability limitations;
- current-state and historical reconstruction sufficient for the analysis;
- material findings/problem or mechanism clusters;
- evidence and status for central findings;
- competing explanations;
- the finding-derived Research Agenda;
- research depth responsibilities;
- external evidence for material research questions;
- meaningful distinction between theory, investigation methodology, and empirical evidence;
- relevant Related Work and Best-Practice evidence;
- counterevidence;
- analytical reconnection to the original findings;
- cross-finding tensions and counterfindings;
- Research Gaps and unresolved questions;
- coverage status;
- the major remaining uncertainty;
- explicit observance of the STOP boundary.

A useful final synthesis SHOULD emphasize:

1. the strongest supported project/system findings;
2. the most important counterfindings, weakening evidence, and reframings;
3. material tensions or conditional mechanisms;
4. the largest remaining uncertainties;
5. open Research Gaps.

It MUST NOT append solution recommendations merely to make the report appear actionable.

---

## 15. Completion Contract

Completion is substantive, not cosmetic.

The Skill MUST NOT be considered complete merely because:

- a long report exists;
- many sources were cited;
- every expected heading contains text;
- a dedicated research mode was invoked;
- a coverage table was mechanically filled;
- one coherent explanatory story was produced.

Full completion requires that, within the agreed scope and available evidence:

- the relevant current state has been reconstructed sufficiently;
- historical and current conditions are not materially conflated;
- central findings are visible and evidence-grounded;
- positive/protective mechanisms and material counterexamples have not been systematically ignored;
- plausible competing explanations have been examined;
- the Research Agenda was derived from findings;
- substantial research blocks remain anchored to material findings;
- central research needs received proportional depth;
- relevant counterevidence was examined;
- theory, investigation methodology, and empirical evidence were not materially collapsed;
- external evidence was analytically reconnected to the originating findings;
- cross-finding tensions were considered;
- coverage was checked;
- significant Research Gaps and unresolved questions remain visible;
- material capability and access limits remain visible;
- no silent depth downgrade occurred;
- the STOP boundary was respected.

Completion does not require certainty.

A fully executed Skill may correctly end with central conclusions still marked `unresolved`.

---

## 16. Bounded Completion and Failure Behavior

The Skill MUST be able to terminate correctly when full execution is not possible.

Possible limiting conditions include:

- insufficient current project/system evidence;
- inaccessible material sources;
- contradictory evidence that cannot be resolved;
- unclear source authority;
- insufficient external research capability;
- required Tier-A depth not achievable;
- inability to inspect relevant primary evidence;
- provenance or persistence limitations that materially impair traceability;
- source or test-case ambiguity.

These are behavioral conditions, not mandated runtime enums.

### 16.1 Required behavior under limitation

When a limitation materially affects the analysis, the Skill MUST:

1. identify the limiting condition;
2. state which part of the analysis or research it affects;
3. preserve supported findings and useful partial work;
4. reduce or qualify claim strength accordingly;
5. identify material unanswered questions;
6. distinguish an evidence gap from evidence against a hypothesis;
7. avoid claiming full completion for unsatisfied obligations.

### 16.2 `unresolved`

`unresolved` is appropriate where a finding or research question cannot be justified in either direction from the available evidence.

It MUST NOT be used merely to avoid difficult analysis.

It MUST also not be treated as failure when the available evidence genuinely does not discriminate between plausible explanations.

### 16.3 Overall bounded completion

An overall execution MAY end as bounded rather than fully complete when important work was possible but one or more contract obligations could not be satisfied because of source or capability limits.

The output MUST make that boundary obvious.

No formal overall state vocabulary is required by this contract.

---

## 17. Host-Project Persistence Boundary

Skill output is an analysis/research artifact.

It is not automatically canonical project truth.

The host project retains authority over:

- requirements;
- accepted decisions;
- architecture;
- priorities;
- implementation authority;
- canonical state;
- durable project records;
- promotion of findings into those records.

The Skill MAY persist its evidence, outputs, references, or provenance when the host project's rules permit or require this.

It MUST NOT bypass host governance in order to make its findings durable.

Temporary working structures MUST NOT automatically become new permanent truth stores, registries, ontologies, or project state.

A downstream owner or process MAY later promote a Skill finding into host-project truth. That promotion is outside this Skill's authority.

---

## 18. Vendor Neutrality

The Core Contract MUST NOT depend on:

- ChatGPT;
- Work;
- Codex;
- a product named “Deep Research”;
- a specific model family or version;
- GitHub;
- a local shell;
- a particular browser;
- a particular search provider;
- a particular citation manager or research database.

The Core MAY require generic capabilities such as:

- adequate project/source access;
- external research capability;
- sufficient reasoning capability;
- evidence inspection;
- counterevidence search;
- citation or evidence traceability;
- working-state or provenance preservation.

Product-specific activation, tooling, runtime behavior, source-connection instructions, and model routing belong in separate execution profiles.

Changing execution vendor or mode MUST NOT change the Skill's epistemic or decision authority.

---

## 19. Implementation Freedom and Non-Requirements

A conforming implementation MAY choose the simplest sufficient mechanism for executing this contract.

This contract intentionally does **not** require:

- a workflow engine;
- a persistent state machine;
- a new ontology;
- a new truth store;
- fixed JSON or database schemas;
- mandatory enums;
- a fixed report template;
- a fixed source count;
- a fixed number of findings;
- a fixed number of Research Questions;
- a mandatory vendor-specific research mode;
- a host-framework integration layer.

Such structures MAY be proposed later only when a separate design or implementation step demonstrates that they are necessary to satisfy the contract reliably.

Implementation convenience alone is not sufficient justification.

---

## 20. Conformance Boundary

A future implementation conforms to this Skill Contract only if a competent executor can use it to perform the complete epistemic path without inventing material Skill semantics that are absent here.

In particular, implementation MUST NOT need to invent:

- whether project evidence precedes diagnosis;
- whether prior audits are authoritative;
- when research may begin;
- what makes research finding-driven;
- whether competing explanations are required;
- whether counterevidence can change findings;
- whether theory and investigation method differ;
- how research depth is allocated;
- whether healthy or under-formalized results are allowed;
- whether `unresolved` is legitimate;
- whether capability limitations may be hidden;
- whether Best Practice implies adoption;
- whether output becomes host-project truth;
- whether solution development is permitted.

Implementation details not affecting these semantics remain outside this contract.

---

## 21. Final Boundary

The terminal epistemic output of this Skill is:

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

It is not:

```text
target architecture
+ chosen solution
+ adoption decision
+ roadmap
+ implementation plan
```

**STOP before solution development.**
