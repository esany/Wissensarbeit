# System Analysis + Finding-Driven Deep Research — Package Specification

**Status:** package specification candidate for Issue #44 pre-implementation review  
**Parent:** Issue #43 — System Analysis + Finding-Driven Deep Research  
**Work Owner:** Issue #44 — Contract, package spec and eval contract  
**Skill Contract:** `SKILL_CONTRACT.md` on the same #44 specification branch  
**Development baseline:** PR #47 — `DEVELOPMENT_PLAN.md` at accepted head `d97043d736bd03386667e107358194a521030266`  
**Method provenance:** `esany/pflege-arnshaugk-historie` PR #123 at reviewed head `e112a8985e8c5149b6f84fb3ae8174a6202a40a2`

This document specifies how the reviewed Skill semantics are to be divided into a small, complete, reviewable package. It does **not** implement the package.

The package design follows one rule:

> Put required behavior in the default execution path; isolate only those materials whose early loading would create leading bias, whose use is genuinely conditional, or whose content is vendor-specific.

Lean means complete fit-for-purpose execution with no unnecessary package structure.

---

## 1. Package Goal

The package MUST allow a fresh competent executor to perform the complete Skill Contract without consulting:

- the originating development chat;
- Histo-Orla project history;
- PR #123 reasoning narrative;
- the #43/#44 planning discussion;
- the Wissensarbeit framework vocabulary;
- any undocumented implementation convention.

The package MUST preserve:

- empirical reconstruction before diagnosis;
- current evidence before inherited interpretation;
- Need → System / Interface analysis;
- finding-derived Research Agenda;
- finding-driven external research;
- competing explanations and counterevidence;
- theory / investigation-method / empirical-evidence separation;
- proportional research depth;
- analytical reconnection;
- bounded completion and `unresolved`;
- host-project authority boundaries;
- STOP before solution development.

Package structure MUST NOT weaken these behaviors in order to reduce file count or prompt length.

---

## 2. Initial Package Shape and Presence Requirements

The initial implementation MUST contain these default-path files:

```text
skills/system-analysis-deep-research/
├── skill.md
└── references/
    └── core-method.md
```

The optional late-helper references MAY be instantiated when #45 implements those optional capabilities:

```text
references/
├── challenge-checklist.md
└── disciplinary-discovery-map.md
```

If present, they remain subject to the late-loading rules in this specification and MUST NOT become default-path inputs.

The first package SHOULD also include the reviewed ChatGPT-specific execution profile:

```text
references/
└── execution-profiles/
    └── chatgpt-deep-research.md
```

That profile is recommended for the initial package but is not part of the vendor-neutral Core.

This is the smallest currently justified package split: `skill.md` and `core-method.md` are physically mandatory; the two helper modules are optional capabilities; the ChatGPT execution profile is recommended rather than Core-mandatory.

The following #44 assurance/design artifacts are intentionally **not runtime package inputs**:

```text
SKILL_CONTRACT.md
PACKAGE_SPEC.md
EVAL_CONTRACT.md
DEVELOPMENT_PLAN.md
```

They define, review, and evaluate the implementation. A normal Skill execution MUST NOT require loading them.

---

## 3. Why This Split Exists

The split is functional rather than documentary.

### 3.1 `skill.md`

Owns activation, admission, orchestration, hard boundaries, and reference-loading rules.

### 3.2 `references/core-method.md`

Owns the detailed mandatory epistemic method needed for complete default execution.

### 3.3 `references/challenge-checklist.md`

Owns optional late completeness/challenge prompts that would create anchoring risk if loaded before empirical findings exist.

### 3.4 `references/disciplinary-discovery-map.md`

Owns optional search-vocabulary / disciplinary discovery assistance that would create research framing bias if treated as the primary research structure.

### 3.5 `references/execution-profiles/chatgpt-deep-research.md`

Owns ChatGPT-specific capability and activation guidance without changing generic Skill semantics.

No additional reference file is justified merely because the Contract contains another conceptual distinction.

---

## 4. `skill.md` Contract

`skill.md` is the package entry point.

It MUST be concise enough to remain operationally usable while containing every rule necessary to:

1. determine whether the Skill applies;
2. admit or bound the task based on source/evidence access;
3. admit or bound the task based on execution capability;
4. preserve authority boundaries;
5. route the executor into the mandatory Core method;
6. control optional/late reference loading;
7. determine whether the result is fully complete, bounded, or unresolved;
8. stop before solution development.

### 4.1 Required content

`skill.md` MUST contain, in compact operational form:

- Skill purpose;
- trigger;
- non-trigger;
- required input classes;
- Source/Evidence Admission rules;
- Capability Admission rules;
- no-silent-downgrade rule;
- Core epistemic invariants;
- authority boundary;
- host-project promotion boundary;
- instruction to load and follow `references/core-method.md` for execution;
- Late-Helper Admission rules;
- execution-profile admission rule;
- completion / bounded-completion behavior;
- explicit STOP boundary.

### 4.2 Required default behavior

When the Skill is triggered, the default execution path MUST load:

```text
skill.md
→ references/core-method.md
```

The executor MUST NOT need to infer that the Core method exists or decide whether it is worth loading.

### 4.3 What `skill.md` MUST NOT contain

It MUST NOT contain:

- the long Challenge/Completeness checklist;
- a broad catalogue of academic disciplines;
- Histo-Orla-specific findings or causal language;
- a fixed catalogue of expected system failures;
- vendor-specific UI or product instructions;
- a required output mega-template;
- fixed source counts;
- implementation/runtime schemas;
- a workflow state machine;
- framework mapping;
- solution-development guidance.

It MAY name optional references and state their admission conditions without reproducing their leading content.

---

## 5. `references/core-method.md` Contract

`core-method.md` is mandatory for every substantive execution of the Skill.

Its purpose is to hold the detailed method without turning `skill.md` into a very large entry file.

It MUST operationalize, without changing, the Skill Contract's complete epistemic path:

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

### 5.1 Required method content

The file MUST include operational guidance sufficient to preserve:

- present versus historical evidence;
- source/evidence-class distinctions where material;
- prior-audit revalidation;
- Need → System translation analysis without presuming mismatch;
- positive/protective mechanisms as valid findings;
- competing explanations before explanatory closure;
- finding-derived research questions;
- Tier A/B/C depth responsibilities;
- separation of theory, investigation methodology, and empirical evidence;
- Related Work by mechanism/conditions rather than feature similarity;
- Best Practice as conditional evidence;
- active counterevidence search;
- Search Boundaries for material negative/completeness claims;
- saturation/stop judgement;
- finding → research → reconnection traceability;
- `Unresearched Major Finding`;
- `Unanchored Research`;
- current/historical finding semantics;
- bounded completion;
- final solution-development STOP.

### 5.2 No hidden helper leakage

`core-method.md` MUST NOT reproduce the contents of the Challenge/Completeness checklist or disciplinary discovery map.

It MAY state that these references exist and under what conditions they may be loaded.

### 5.3 No independent semantics

`core-method.md` is an implementation of the reviewed Contract, not another authority layer.

If its wording conflicts with `SKILL_CONTRACT.md`, the implementation is defective and must be corrected; the reference file does not silently redefine the Contract.

---

## 6. `references/challenge-checklist.md` Contract

This reference is optional and deliberately late-loaded.

Its purpose is omission challenge, not initial diagnosis generation.

### 6.1 Admission

It MAY be loaded only after:

1. empirical reconstruction has occurred; and
2. initial material findings / problem or mechanism clusters have been formed without the checklist.

It MUST NOT be part of the default initial context presented before those conditions are met.

### 6.2 Allowed content

It MAY contain candidate blind-spot classes such as:

- under- or over-formalization;
- need/representation mismatch;
- local versus end-to-end effects;
- coordination burden;
- transferred cognitive work;
- insufficient or excessive control;
- provenance/state loss;
- premature or insufficient generalization;
- automation overreach or underuse;
- proxy success versus real utility;
- recovery/feedback gaps;
- data, reliability, rights, security, operational, or domain-quality concerns.

These are challenge vocabulary only.

### 6.3 Required challenge behavior

For each checklist candidate, the reference MUST require questions equivalent to:

1. Is the candidate actually supported by project evidence?
2. Is there a stronger alternative explanation?
3. Is the opposite problem equally plausible?
4. Would the issue materially affect the Research Agenda?

Unsupported checklist candidates MUST be discarded.

### 6.4 Prohibition

The checklist MUST NOT:

- create findings merely because an item exists in the file;
- determine the primary report structure;
- be used as a completeness score;
- require every candidate to be discussed;
- be treated as an ontology of system problems.

---

## 7. `references/disciplinary-discovery-map.md` Contract

This reference is optional and deliberately late-loaded.

Its purpose is vocabulary and field discovery when a material finding or Research Agenda item lacks sufficient theoretical, methodological, or empirical search direction.

### 7.1 Admission

It MAY be loaded only when:

- empirical findings already exist; and
- a specific Research Agenda item needs help identifying relevant fields, concepts, terminology, methods, or search vocabulary.

It MUST NOT be used to decide in advance which disciplines the project "should" exhibit.

### 7.2 Allowed content

It MAY list broad candidate areas such as:

- domain-specific scholarship/professional methods;
- requirements/software/architecture/empirical software engineering;
- HCI, information behaviour, and sensemaking;
- CSCW, coordination, organization, and distributed cognition;
- safety, resilience, incident, and error research;
- epistemology, philosophy/sociology of science, and interdisciplinarity;
- knowledge management, information systems, and research infrastructure;
- data/provenance/reproducibility/research software;
- human-AI interaction and automation studies.

The list is discovery vocabulary, not a required research portfolio.

### 7.3 Required behavior

The executor MUST be free to:

- add fields not listed;
- split or combine listed areas;
- ignore irrelevant areas;
- revise terminology during research.

The reference MUST NOT become the report outline.

---

## 8. Execution Profiles

Execution profiles are optional environment-specific modules.

They MAY describe:

- how a particular environment activates research capabilities;
- which source connections or retrieval modes are available;
- relevant execution limits;
- what runtime evidence should be preserved;
- how to recognize that a required capability is unavailable.

They MUST NOT alter:

- trigger semantics;
- evidence standards;
- the Research Agenda Gate;
- research-depth responsibility;
- counterevidence requirements;
- authority;
- completion semantics;
- the solution-development STOP.

### 8.1 Profile loading

An execution profile MAY be loaded during Capability Admission or before a capability-dependent execution phase.

Unlike Challenge/Discovery helpers, it need not wait until findings exist because its function is capability mapping, not problem framing.

### 8.2 ChatGPT Deep Research profile

The first package SHOULD include:

`references/execution-profiles/chatgpt-deep-research.md`

because the provenance contains a concrete reviewed execution profile and the Skill is expected to support genuine multi-source research in ChatGPT without contaminating the generic Core.

This profile MUST:

- remain explicitly non-Core;
- avoid a frozen model-version requirement;
- defer current product activation details to current official product documentation where necessary;
- require the project reconstruction → findings → Research Agenda → finding-driven research sequence;
- preserve citations/source links and access limits;
- preserve the STOP boundary;
- never treat activation of a product feature as proof that Tier-A obligations were satisfied.

Additional vendor profiles are not part of the initial package unless a real execution need exists.

---

## 9. Multi-Repository Handling

A separate `multi-repository.md` module is **not required in the initial package**.

Reason:

- the Skill Contract is defined over an investigation object/system, not a single storage repository;
- an investigated system may already draw evidence from multiple repositories or source locations;
- cross-project evaluation in #46 can run each case separately and does not require one multi-repository execution;
- the v3 Multi-Repository Appendix is useful provenance but does not establish a current Contract requirement for a dedicated runtime module.

If later evidence shows that a single Skill execution across multiple independent repositories introduces a distinct methodological problem not handled by the Core, a separate extension MAY be added after review.

Until then, no extra file is justified.

---

## 10. Loading Model

The package MUST preserve this loading behavior:

```text
TRIGGER / ADMISSION
        │
        ├─ load skill.md
        │
        ├─ load core-method.md
        │
        └─ optionally load matching execution profile
                 │
                 ↓
EMPIRICAL RECONSTRUCTION
        ↓
INITIAL FINDINGS / CLUSTERS
        │
        ├─ optional challenge-checklist.md
        │        only for omission challenge
        │
        ↓
RESEARCH AGENDA
        │
        ├─ optional disciplinary-discovery-map.md
        │        only when field/term discovery is needed
        │
        ↓
FINDING-DRIVEN RESEARCH
        ↓
RECONNECTION / COVERAGE / STOP
```

An implementation MAY realize "loading" through whatever mechanism its host Skill system uses.

The package specification requires the semantic staging, not a particular loader API.

---

## 11. Context and Duplication Discipline

The package MUST minimize repeated normative prose while remaining restartable and executable.

### 11.1 Single operational home

Each operational rule SHOULD have one primary runtime home.

Examples:

- activation/admission/boundaries → `skill.md`;
- detailed Core execution → `core-method.md`;
- late challenge vocabulary → `challenge-checklist.md`;
- late field/search vocabulary → `disciplinary-discovery-map.md`;
- product activation/capabilities → execution profile.

Small repetition is allowed where required to make a hard boundary impossible to miss, especially:

- no leading diagnosis;
- no silent downgrade;
- no authority transfer;
- STOP before solution development.

### 11.2 No assurance-document dependency

Runtime files MAY be traceable to Contract clauses during implementation/review, but a fresh executor MUST NOT have to open:

- `SKILL_CONTRACT.md`;
- `PACKAGE_SPEC.md`;
- `EVAL_CONTRACT.md`;
- `DEVELOPMENT_PLAN.md`;
- Histo-Orla provenance files

in order to know how to execute the Skill.

---

## 12. Fresh-Executor Requirement

The implemented package MUST be self-sufficient for a fresh competent executor.

Given:

- the package;
- an investigation request;
- the host project's accessible sources;
- the available research/execution capabilities;

the executor MUST be able to determine:

- whether the Skill triggers;
- what evidence is sufficient to proceed or bound claims;
- what capabilities are sufficient;
- how to reconstruct the system;
- how to form findings without leading diagnosis;
- how and when to derive a Research Agenda;
- how deeply to research;
- when optional helpers may be admitted;
- how to reconnect research;
- how to expose unresolved limitations;
- when execution is complete;
- where authority ends.

If the executor must rediscover these semantics from development history, the package is incomplete.

---

## 13. Failure and Capability Behavior in the Package

Failure behavior MUST remain visible in the default package path.

It MUST NOT be hidden only in an optional reference.

The default package MUST support:

- insufficient current evidence;
- inaccessible material sources;
- contradictory evidence;
- unclear source authority;
- inability to reach required research depth;
- inability to inspect relevant primary evidence;
- provenance/traceability limitations;
- bounded completion;
- `unresolved`.

A capability-specific execution profile MAY explain how a particular product exposes such limitations, but it MUST NOT redefine their epistemic consequences.

---

## 14. Output Form

The package MUST NOT require one fixed final report template.

It MUST require reviewable availability of the Contract's result content and traceability.

The implementation MAY use:

- prose;
- compact tables;
- linked sections;
- structured blocks;
- another reviewable representation.

The package MUST NOT optimize for uniform headings at the expense of actual evidence discrimination.

A Coverage Matrix MAY be provided as a useful end-stage representation, but mechanical completion of a matrix MUST NOT constitute completion.

---

## 15. Explicit Non-Requirements

The initial package MUST NOT require:

- a workflow engine;
- a new ontology;
- a persistent execution state machine;
- a new truth store;
- JSON/database schemas for findings;
- a required plugin framework;
- a fixed report schema;
- fixed source counts;
- fixed finding counts;
- a generic model router;
- a generic research scheduler;
- a dedicated multi-repository module;
- framework/Building-Block mapping;
- host-project migration;
- automatic promotion of Skill findings into project state.

No such mechanism may be added in #45 merely because it would make implementation more elegant.

---

## 16. Implementation Boundary for #45

#45 receives this package specification only after R1 review/disposition.

Implementation MUST:

- create the runtime package described here;
- represent every Contract-required behavior;
- keep optional helpers behind the specified admission boundaries;
- keep vendor-specific details outside the Core;
- avoid adding runtime scaffolding not demonstrated necessary;
- preserve a reviewable trace from Contract clauses to package content.

Implementation MUST NOT use #45 to reopen settled Skill semantics.

If implementation discovers that the package split cannot satisfy a Contract requirement without a material semantic decision, implementation MUST stop and return that ambiguity to the Contract/Package review boundary.

---

## 17. Package-Conformance Checks

A future R2 review MUST be able to verify at least:

### Default path

- `skill.md` exists;
- `core-method.md` exists and is required by the default execution path;
- default execution can perform the complete Contract method.

### Late-helper protection

- challenge checklist content is not preloaded into empirical reconstruction;
- disciplinary discovery content is not used to structure initial analysis;
- admission conditions are explicit.

### Vendor boundary

- generic Core contains no product-specific activation instructions;
- execution profile does not redefine epistemic semantics;
- model/version specifics are not frozen into the Core.

### Failure behavior

- source/evidence limitations are visible;
- capability limitations are visible;
- no silent research-depth downgrade;
- bounded completion and `unresolved` are supported.

### Authority

- no solution development;
- no automatic project-truth promotion;
- no authority transfer from execution mode.

### Package economy

- no required file exists solely to mirror another artifact;
- no speculative runtime/state/framework mechanism is introduced;
- a fresh executor does not need development-history files.

A package can fail conformance even when all expected files exist.

---

## 18. Deferred Decisions

The following are intentionally deferred because they are implementation details that do not alter Skill semantics:

- exact prose length of `skill.md`;
- exact internal heading structure of runtime files;
- host-specific metadata required by the eventual Skill packaging system;
- exact reference-link syntax required by that host;
- deterministic lint/package checks that become useful once files exist;
- whether execution-profile product instructions require later factual refresh.

These MAY be decided in #45 only if they do not change this specification or the Skill Contract.

---

## 19. Package Completion Boundary

The package design is sufficient when a future implementation can be built without deciding:

- which method stages are mandatory;
- which content is default versus late;
- whether Challenge/Discovery helpers may lead analysis;
- where vendor-specific instructions belong;
- whether a multi-repository extension is mandatory;
- whether failure behavior belongs in the default path;
- whether assurance/development artifacts are runtime dependencies;
- whether runtime infrastructure is required.

Those decisions are fixed here.

The implementation remains free to choose the simplest technical realization that preserves them.

**No implementation is authorized by this specification.**
