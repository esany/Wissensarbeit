# WA-AUDIT-2026-09-19 — Design / project-development methodology delta

Status: **audit evidence / Generic-Fit input / no Requirement, Building Block, lifecycle or execution-cursor change**

Source evidence:
- current `project/GOVERNING_OBJECTIVE.md`
- `project/requirements.json`
- `project/quality.json`
- `system/lifecycle.json`
- `system/competence.json`
- `system/building_blocks.json`
- `system/authority.json`
- `system/decision_brief.json`
- current repository inventory/search
- recent real failure evidence from `esany/paleo-type`

## 1. Audit question

Is `Wissensarbeit` as strong in **user/problem discovery, design methodology and iterative project/product development** as it is in governance, authority, traceability, assurance and restartability?

## 2. Finding

**No. The current repository is materially stronger at controlling, tracing, reconciling and assuring change than at methodically discovering and shaping the right change.**

The gap is not total absence. The repository already names relevant capabilities:

- lifecycle stages: `discover → understand → research → model → decide → build → verify → use → learn`;
- project competence: `problem_framing`, requirements, prioritization, acceptance, change management;
- research competence: literature search, source evaluation, experiment design, evaluation;
- `BB-REQUIREMENTS`: translate validated needs into requirements/criteria;
- `BB-DESIGN`: develop/compare solution concepts;
- `BB-LEARN`: use real feedback/failures to refine understanding;
- `Q-FIT`: problem fit;
- `system/authority.json`: Human consultation for material meaning/value/priority.

However, the current repo does **not yet operationalize an equally explicit design/discovery method** for the transitions among these capabilities.

## 3. Specifically under-specified

Current canonical surfaces do not yet give a comparable operational method for:

1. **Need elicitation and user research**
   - distinguish expressed request, underlying need, symptom, constraint, preference and proposed solution;
   - gather evidence from usage, observation, feedback and context;
   - avoid treating a single utterance as the problem definition.

2. **Problem framing**
   - synthesize multiple observations into a problem statement;
   - separate problem, cause, symptom and solution hypothesis;
   - test whether the existing framing still fits the governing objective.

3. **Design-space exploration**
   - generate materially different solution concepts before converging;
   - make assumptions and trade-offs explicit;
   - compare concepts against needs, evidence, quality and reversibility.

4. **Prototype / concept testing**
   - use low-cost artifacts or simulations to learn before committing architecture;
   - define what a prototype is intended to falsify or clarify;
   - prevent implementation momentum from substituting for learning.

5. **Iteration semantics for product/project development**
   - record `before → intervention → observed effect → learning → reframing/refinement`;
   - distinguish product/knowledge learning from implementation/support progress;
   - make explicit which assumptions were strengthened, weakened or invalidated.

6. **Feedback interpretation**
   - treat feedback as evidence requiring interpretation;
   - distinguish direct product-change request from symptom report;
   - ask for clarification when materially different meanings remain plausible and the chosen interpretation would redirect the project.

7. **Learning-to-requirement promotion**
   - define when repeated evidence is sufficient to refine a requirement, quality target or design principle;
   - preserve candidate/hypothesis state until that threshold is met.

8. **Human-facing design rationale**
   - show the problem model, user need, alternatives considered, evidence, rejected options and learning history;
   - not only the final decision and its consequences.

## 4. Evidence from the recent paleo-type failure

The 2026-09-18/19 maturity/transparency drift is a concrete case:

- Human feedback about shallow/poorly structured output was first a symptom of execution/information-architecture failure.
- The assistant repeatedly reinterpreted that feedback as a new product/research-system problem.
- Each local correction created another branch instead of preserving the validated higher-level need.
- Existing governance later prevented permanent semantic damage, but only after costly cleanup.

This shows the asymmetry directly:

> **The system was better at cleaning up and reconciling the wrong branch than at avoiding the wrong branch through disciplined discovery/design reasoning.**

## 5. Why this matters

A system can satisfy authority, traceability and reconciliation rules while still producing poor product/project development if it:

- frames the wrong problem;
- mistakes symptoms for needs;
- converges on one solution too early;
- validates implementation rather than the problem/solution fit;
- treats user feedback as feature authority;
- measures local progress rather than learning.

Governance is necessary but not sufficient for good design.

## 6. Existing-owner fit

This audit does **not** justify a new fifteenth Building Block.

The strongest Generic-Fit is within existing owners:

- `BB-BOOTSTRAP` — initial owner intent/problem context;
- `BB-CONTEXT` — current need/problem evidence;
- `BB-COMPETENCE` — activate user research, design, requirements and domain competence where needed;
- `BB-RESEARCH` — research/fit evidence;
- `BB-INTEGRATE` — distinguish new evidence from promoted project change;
- `BB-REQUIREMENTS` — validated needs → requirements;
- `BB-DESIGN` — deliberate concept exploration/comparison;
- `BB-ASSURE` — test design claims at the right evidential level;
- `BB-LEARN` — feedback/failure → validated learning;
- `BB-TRACE` / `BB-DERIVE` — human-readable design rationale and learning history.

The gap is **methodological fidelity and operational detail across these existing blocks**, not missing top-level architecture.

## 7. Current disposition

**AUDIT FINDING: REAL GAP, NOT YET A PROMOTED SOLUTION.**

Preserve the following as current evidence:

> `Wissensarbeit` is currently stronger in governance/control/reconciliation than in explicit user-research, design and iterative product/project-development methodology.

Do not yet:
- add a new Requirement family;
- add a new Building Block;
- change the lifecycle;
- introduce a design framework by name;
- implement a design engine;
- change the current execution cursor.

Any future improvement should first compare current needs against established user-research, requirements-engineering, product-discovery, service/design and systems-engineering methods, then refine the smallest existing owners that are actually deficient.

## 8. Candidate acceptance direction for later work

A future design-methodology refinement should be able to demonstrate that, from a Human intervention, the system can:

1. preserve the governing objective;
2. distinguish observation/feedback from inferred need and from proposed solution;
3. identify ambiguity and assumptions;
4. obtain missing Human meaning only when materially necessary;
5. form and compare multiple plausible problem/solution interpretations;
6. test the cheapest high-value uncertainty first;
7. promote only validated learning;
8. show the Human what was learned and why the project changed or did not change.

This is audit evidence only. It does not alter the current `Wissensarbeit` programme cursor.
