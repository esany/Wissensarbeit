# System Analysis + Finding-Driven Deep Research

## Purpose

Use this Skill to deeply analyse an existing project or system from its own evidence and then derive external research from the material findings of that analysis.

The required path is:

```text
project/system evidence
→ empirical reconstruction
→ material findings
→ competing explanations
→ finding-derived Research Agenda
→ finding-driven external research
→ analytical reconnection
→ tensions / Research Gaps / unresolved
→ STOP before solution development
```

This Skill is not a generic report generator, literature-review template, architecture method, solution-selection method, roadmap method, or implementation method.

## Trigger

Use this Skill when the task requires the integrated chain:

```text
project/system evidence
→ empirical findings
→ research needs
→ external research
→ analytical reconnection
```

Typical triggers include:

- an existing project, repository, product, research system, organization, workflow, or other socio-technical system needs deep analysis;
- visible symptoms, frictions, trade-offs, protective mechanisms, or unexplained outcomes need empirical explanation;
- inherited diagnoses or prior audits need fresh revalidation;
- the relationship between user/domain needs and system representation or actual use is unclear;
- project findings must generate a Research Agenda;
- competing explanations need to be challenged with theory, investigation methodology, empirical evidence, Related Work, Best-Practice evidence, or counterevidence;
- the system may be healthy, over-structured, under-structured, differently impaired than previously assumed, mixed, or unresolved;
- deep understanding is required while solution selection remains out of scope.

The words “research”, “audit”, “analysis”, “architecture”, or “repository” alone do not trigger this Skill.

## Non-trigger

Do not use this Skill for work that does not require both empirical system reconstruction and finding-driven research, including:

- simple factual or literature questions;
- ordinary web research or source discovery;
- summarization of supplied material;
- ordinary code review or a bounded implementation defect;
- bounded debugging;
- architecture or target-state selection;
- tool, framework, vendor, or product selection;
- solution design;
- roadmap or implementation planning;
- implementation execution;
- optimization of an already selected solution;
- external-only research with no material project/system anchor.

If a mixed request begins with analysis and then asks for solutions, perform only the analysis/research portion under this Skill and stop at the solution boundary.

## Required inputs

Establish enough information to identify and bound:

1. **Investigation object** — what system is being investigated.
2. **Scope** — relevant time period, components/workstreams, actors/user groups, domain boundaries, exclusions, and motivating concern.
3. **Current project/system evidence** — sources capable of supporting present or relevant historical reconstruction.
4. **Known constraints** — access, confidentiality, time, tooling, research, source, or execution limits.
5. **Prior interpretations** — earlier audits/diagnoses/reviews when available; treat them as prior interpretation, not current truth.
6. **External research access** — what external source classes and research capability are actually available.
7. **Source/tool boundaries** — material limits on access, inspection depth, retrieval, citation, provenance, or preservation.

Inputs need not be complete before work begins. Missing material inputs must remain visible and affect claim strength, research scope, or completion status.

## Source / Evidence Admission

Before diagnosis or external research, determine what the available project/system evidence permits you to claim.

Always distinguish, where material:

- directly supported;
- inferred;
- historical;
- externally researched;
- hypothetical;
- not currently established.

Rules:

- Do not replace missing project evidence with theory, generic best practice, plausible reconstruction, or inherited audit claims.
- If current evidence is incomplete, continue only where useful; expose the gap, restrict claims, preserve hypotheses, reduce confidence where appropriate, and use `unresolved` when necessary.
- Make inaccessible material sources visible. Do not present an obligation as fully satisfied when inaccessible evidence is necessary to support it.
- Preserve contradictory evidence. Do not resolve contradictions merely by choosing the source that fits the emerging narrative.
- Historical evidence does not establish current conditions without fresh support.
- Treat prior audits and strong inherited diagnoses as hypotheses, interpretations, historical evidence, or research leads until revalidated.
- Qualify unclear source authority or provenance.
- Do not silently treat a secondary summary as equivalent to inaccessible primary evidence.
- Keep materially different time horizons distinct.

## Capability Admission

Before claiming full execution, determine whether the available environment can actually perform the epistemic work required by this case.

Check at least:

- adequate inspection of the investigation object;
- access to relevant current project/system evidence;
- external research capability;
- source-inspection depth;
- ability to seek counterevidence;
- citation/provenance or equivalent traceability;
- ability to retain enough working state/evidence references for coherent execution;
- realistic ability to achieve the required research depth.

### No silent downgrade

Never perform shallower work than required and present it as complete.

If a central finding requires Tier-A depth that the available environment cannot provide:

- state the limitation;
- preserve useful partial work;
- mark the unsatisfied research obligation;
- propagate the limitation into reconnection and completion;
- do not claim full completion of that research need.

A product feature named “Deep Research” is neither necessary nor sufficient by itself.

## Core epistemic invariants

Every execution must preserve:

1. empirical reconstruction before diagnosis;
2. minimized leading bias;
3. current evidence before inherited interpretation;
4. system analysis generates the Research Agenda;
5. substantial external research remains finding-driven;
6. competing explanations and counterevidence are constitutive;
7. theory, investigation methodology, and empirical evidence remain distinguishable;
8. Best Practice remains conditional evidence, not adoption advice;
9. research depth follows materiality and uncertainty;
10. a largely healthy system is a valid result;
11. insufficient formalization or a need for more structure is a valid result;
12. domain, data, technical, organizational, interface, user-work, or other explanations remain possible unless evidence rules them out;
13. findings may contradict earlier diagnoses;
14. `unresolved` is a valid result;
15. the Core is vendor-neutral;
16. execution-vendor details remain outside the Core;
17. the Skill stops before solution development;
18. Skill output does not automatically become host-project truth.

## Authority boundary

Within the investigation, you may observe, reconstruct, compare, analyse, identify findings and protective mechanisms, form clusters and competing explanations, derive a Research Agenda, perform or route research, seek counterevidence, strengthen/weaken/reframe/contradict hypotheses, preserve uncertainty, identify Research Gaps, conclude that a suspected problem is unsupported, conclude that more structure may be needed, conclude that a system is largely healthy, or leave matters unresolved.

You must not, by virtue of this Skill:

- select a target architecture or system redesign;
- choose tools, frameworks, products, or vendors;
- create a roadmap or implementation priority;
- authorize implementation;
- create or promote requirements;
- alter host-project priorities;
- infer owner acceptance;
- convert Best Practice into an adoption decision;
- redesign governance;
- promote findings automatically into canonical host-project truth/state;
- acquire additional project/decision authority merely because a stronger model, tool, research mode, or execution environment is used.

Any downstream solution work requires separate authority after this Skill stops.

## Mandatory Core method

For every substantive execution, load and follow:

`references/core-method.md`

The Core method is mandatory. Do not treat it as an optional reference.

## Late-helper admission

Optional challenge/completeness or disciplinary/search helpers may be used only under these conditions:

- **Challenge/completeness aid:** only after empirical reconstruction and initial findings/clusters have been formed independently of the aid. Its role is omission challenge, not diagnosis generation.
- **Disciplinary/search aid:** only when a concrete finding or Research Agenda item needs help locating relevant fields, concepts, terminology, methods, or search vocabulary.

If such references are not present, proceed without them. Do not recreate a diagnostic catalogue from development history.

If an early helper is materially necessary in an exceptional case, make that intervention visible, treat its framing as potentially leading, test plausible opposite/alternative interpretations, and do not present helper-derived categories as findings without project evidence.

## Execution profiles

An environment-specific execution profile may be loaded during Capability Admission or before a capability-dependent phase.

If present and relevant, use it only to map generic capability needs to the current environment.

Execution profiles must not redefine:

- trigger;
- evidence standards;
- Research Agenda Gate;
- research-depth responsibility;
- counterevidence;
- authority;
- completion;
- STOP.

For ChatGPT, the initial package includes:

`references/execution-profiles/chatgpt-deep-research.md`

## Completion / bounded completion

Full completion is substantive. A long report, many citations, filled headings, a research feature, or a completed matrix do not establish completion.

Full completion requires, within scope and available evidence:

- sufficient current-state reconstruction;
- temporal separation of current and historical conditions;
- evidence-grounded central findings;
- attention to positive/protective mechanisms and material counterexamples;
- competing explanations;
- finding-derived Research Agenda;
- finding-anchored external research;
- proportional depth for central research needs;
- counterevidence;
- separation of theory / investigation methodology / empirical evidence;
- analytical reconnection;
- cross-finding tension review;
- coverage check;
- visible Research Gaps and unresolved questions;
- visible material source/capability limits;
- no silent depth downgrade;
- compliance with the STOP boundary.

If material source or capability limits prevent full execution, end with **bounded completion** rather than false completeness. State the limiting condition, affected obligations, supported partial work, reduced claim strength, unanswered questions, and the distinction between an evidence gap and evidence against a hypothesis.

`unresolved` is correct when available evidence cannot justify a conclusion in either direction. It is not a shortcut around difficult analysis.

## Output

No fixed report template is required.

The result must make reviewably available:

- scope and material source boundaries;
- relevant capability limitations;
- sufficient current/historical reconstruction;
- material findings/clusters with evidence and status;
- competing explanations;
- finding-derived Research Agenda and depth responsibilities;
- external evidence;
- theory / investigation methodology / empirical evidence distinctions;
- relevant Related Work and Best-Practice evidence;
- counterevidence;
- analytical reconnection;
- cross-finding tensions/counterfindings;
- Research Gaps / unresolved;
- coverage status;
- major remaining uncertainty;
- explicit observance of the STOP boundary.

## Final STOP

Stop before:

- target architecture;
- solution selection;
- tool or framework choice;
- adoption recommendation;
- roadmap creation;
- delivery prioritization;
- implementation plan;
- implementation execution;
- governance redesign.

The terminal output is:

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

It is not a solution package.

**STOP before solution development.**
