# ChatGPT Deep Research Execution Profile

**Status:** environment-specific execution profile; non-Core  
**Environment:** ChatGPT  
**Checked against current official OpenAI product documentation:** 2026-09-23

This file maps the vendor-neutral Skill requirements to ChatGPT research capabilities.

It does not redefine the Skill's trigger, evidence standards, Research Agenda Gate, research depth, counterevidence requirement, authority, completion semantics, or STOP boundary.

For those semantics, follow:

```text
../../skill.md
→ ../core-method.md
```

## 1. Current capability surface

Current official OpenAI documentation describes ChatGPT Deep Research as a multi-step research workflow that can reason over, research, and synthesize complex questions into a documented report.

Depending on account, permissions, workspace configuration, and available connections, it may be able to work with:

- uploaded files;
- the public web;
- specified or prioritized websites;
- enabled ChatGPT apps / connected sources.

The workflow may present a proposed research plan before execution and may allow the user to inspect or refine the source scope. Completed research is expected to provide citations or source links.

Availability, limits, connected sources, and UI details may change. Where activation or entitlement matters, consult current official OpenAI product documentation rather than treating this profile as a frozen product manual.

Official reference checked for this profile:

- OpenAI Help Center: “Deep research in ChatGPT” — https://help.openai.com/en/articles/10500283-deep-research

## 2. Capability Admission

Before relying on Deep Research for this Skill, establish what the current ChatGPT environment actually provides for this case.

Check, as applicable:

- whether Deep Research is available in the current account/workspace;
- whether the relevant uploaded/project files are accessible;
- whether required websites can be searched;
- whether specific-site restrictions or priorities are needed;
- whether enabled apps/connected sources needed by the investigation are available;
- whether primary sources can be inspected deeply enough;
- whether citation/source links are preserved;
- whether access restrictions, authentication, workspace policy, or quotas materially limit the work;
- whether the expected research depth is realistically achievable.

Do not infer capability from the product label alone.

If material capability is unavailable, use the generic bounded-completion behavior from the Skill rather than silently downgrading the work.

## 3. Activation rule

Use Deep Research only when the Research Agenda requires multi-step, multi-source evidence acquisition or synthesis that ordinary Chat/search cannot provide at equivalent quality.

Do not activate it merely because:

- the task contains the word “research”;
- a long report is desired;
- the capability is available;
- Tier A is named.

The Skill's epistemic sequence remains:

```text
project/system reconstruction
→ initial findings
→ competing explanations
→ Research Agenda
→ Deep Research where justified
→ analytical reconnection
→ coverage / STOP
```

Do not send the whole project history into Deep Research merely to make it rediscover findings that should already have been established from project evidence.

## 4. Research packet for ChatGPT Deep Research

Before starting a substantial Deep Research run, provide a bounded packet derived from the Research Agenda.

For each material research block, include only what is needed to perform the evidence work:

- originating Project/System Finding;
- evidence-supported description of the phenomenon;
- key unknown;
- competing explanations;
- precise research question(s);
- theory need;
- investigation-method need;
- empirical-evidence need;
- Related Work need where relevant;
- counterevidence target;
- required depth (Tier A/B/C);
- important source/access boundaries;
- required analytical return to the project finding.

Do not disclose hidden grader expectations or expected verdicts.

Do not front-load optional diagnostic catalogues.

## 5. Source control

When source scope matters:

- use uploaded material only as project evidence if its role and authority are understood;
- use specific/prioritized websites where authoritative or bounded source sets are important;
- use connected sources only when their permissions and source identity are clear;
- preserve distinctions between primary and secondary evidence;
- record material access failures;
- preserve the relevant Search Boundary for negative/completeness claims.

A source being reachable through ChatGPT does not make it authoritative.

## 6. Research depth

Deep Research is an execution capability, not a depth grade.

A run using Deep Research may still fail Tier A if it does not adequately cover the obligations in the Core method.

Conversely, a case may satisfy a research obligation without Deep Research if another available route provides equivalent evidence quality and traceability.

For Tier A, verify actual coverage of the material responsibilities rather than counting returned sources.

## 7. Counterevidence and competing explanations

The research packet should explicitly ask for evidence capable of weakening the current interpretation.

Where relevant, require attention to:

- competing theories;
- criticisms;
- failed applications;
- boundary conditions;
- contrary empirical results;
- alternative terminology;
- comparable cases with different outcomes.

Do not ask ChatGPT merely to “support” the current finding.

## 8. Citations and inspection

Use citations/source links as verification handles, not as proof of correctness by themselves.

For central claims:

- inspect the strongest or most consequential sources where possible;
- distinguish what the source directly supports from the synthesis built on top of it;
- note inaccessible primary evidence;
- reduce confidence when a central claim depends on unverified secondary material;
- preserve contradictory source evidence.

A well-cited report can still be epistemically weak if the sources do not support the claims made.

## 9. Plan review

If ChatGPT presents a proposed Deep Research plan, review it for conformity before execution.

Check that the plan:

- starts from the supplied project finding rather than a generic topic;
- addresses the competing explanations;
- includes relevant theory, investigation methodology, empirical evidence, and counterevidence where required;
- does not drift into solution selection;
- does not replace project evidence with generic literature;
- respects the requested source boundaries.

Modify or reject the plan if it would violate those constraints.

Plan approval does not constitute Owner acceptance of any later research conclusion.

## 10. Execution monitoring and interruption

If the current product allows progress inspection or interruption, use those controls only to preserve research quality or scope.

Examples:

- correct obvious topic drift;
- narrow or expand source scope;
- add a missing counterevidence direction;
- stop solution-design drift;
- add a newly discovered search term that remains anchored to the Research Agenda.

Do not interactively steer the run toward a preferred conclusion.

Any material change to the research framing should remain traceable to the originating finding.

## 11. Return contract

A Deep Research result is input to the Skill's analytical reconnection step.

Do not treat the generated research report as the final Skill result.

For each central finding, extract and reconnect:

```text
External Evidence
+ Counterevidence
+ Theory
+ Investigation Methodology
+ Empirical Evidence
+ Related Work / conditional Best-Practice evidence
→ strengthened | weakened | reframed | contradicted | partial | conditional | unresolved
→ Remaining Uncertainty
```

If the report does not support this reconnection, the research obligation remains incomplete.

## 12. Capability failure and bounded completion

Examples of material limitations include:

- required connected source unavailable;
- inaccessible primary source;
- source restriction prevents adequate countercheck;
- quota/entitlement prevents required multi-step research;
- returned source inspection is too shallow for a central claim;
- citations/source links are insufficient for verification;
- the run stops before the required depth is achieved.

When such a limitation affects the case:

- state it;
- preserve useful partial evidence;
- mark the affected research obligation unsatisfied;
- propagate the limitation into analytical reconnection and final completion;
- do not claim Tier-A or full completion merely because Deep Research was invoked.

## 13. Authority

Using ChatGPT, Deep Research, a stronger model, an app/connector, or broader source access does not grant:

- Requirement authority;
- Owner acceptance;
- architecture authority;
- implementation authority;
- canonical host-project truth/state;
- permission to select solutions.

The output remains an analysis/research artifact until the host project separately promotes it under its own rules.

## 14. STOP

Deep Research must not turn the Skill into solution development.

Stop before:

- target architecture;
- tool/framework/vendor selection;
- adoption recommendation;
- roadmap;
- implementation priority;
- implementation plan;
- implementation execution;
- governance redesign.

Return to the Core method for analytical reconnection, coverage, Research Gaps, uncertainty, and final STOP.
