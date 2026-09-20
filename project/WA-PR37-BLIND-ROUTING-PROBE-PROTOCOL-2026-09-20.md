# WA-PR37 Blind Routing Probe Protocol — 2026-09-20

Status: **pre-oracle evidence protocol / independent execution pending / no promotion claim**

## Purpose

Test whether a fresh instance can route a newly recognized material signal back to persistent known Human–AI collaboration candidate evidence without being given the expected candidate or routing outcome.

This protocol exists because **prompt-blind is not repository-blind**. The visible regression cases `WA-EVAL-031..033` remain useful tests, but their `expect` fields are present in `tests/fixtures/eval_cases.json`; they therefore cannot serve as strict blind evidence for an instance that can inspect the full PR repository.

## Probe surface

Strict blind evidence uses:

- `tests/probes/routing_fresh_context_stimuli_v1.json` — stimulus-only probe definitions; no expected candidate IDs, routing outcomes or grading oracle;
- `tools/eval_integrity.py render-probe-bundle <probe_id>` — renders one stimulus plus an isolated operational repository context;
- `tests/probes/fresh_context_trial_contract.json` — capture contract for the raw trial record;
- `tools/eval_integrity.py validate-probe-trial <record>` — deterministic integrity validation of the capture.

The current stimulus-only probes use opaque `RP-*` identifiers. Their definitions must not contain `OC-*` identifiers or oracle-like fields.

## Isolation boundary

The tested instance receives **only** the rendered bundle. It must not have access during the trial to:

- the full repository or Git history;
- `tests/**`, including visible eval fixtures and probe definitions;
- `tools/**`, including grading/integrity code;
- prior trial outputs;
- any external oracle or expected answer;
- prior conversation context.

The bundle contains only the explicit operational allowlist declared in the stimulus document. Context content is read from Git at the exact recorded revision, not from mutable working-tree files.

The bundle manifest records:

- exact repository revision;
- probe/stimulus identity;
- exact accessible context paths;
- SHA-256 of each accessible context file;
- SHA-256 of instructions and stimulus.

`bundle_identity` hashes that manifest and is persisted with the trial record.

## Evidence sequence

1. **Freeze revision.** Use the exact PR head intended for the trial.
2. **Validate definitions.** Run `python tools/eval_integrity.py validate-probes`.
3. **Render isolated bundle.** Run `python tools/eval_integrity.py render-probe-bundle <probe_id>`.
4. **Execute fresh.** Give only that rendered bundle to a fresh instance with no external repository/eval/oracle/prior-trial access.
5. **Capture first.** Persist the raw response unchanged together with the required trial metadata, bundle manifest and bundle identity.
6. **Validate capture.** Run `python tools/eval_integrity.py validate-probe-trial <record>`.
7. **Only after response persistence:** reveal/persist a separate oracle and grade the captured response.
8. **Qualitative review:** determine whether the routing is semantically correct and evidence-calibrated.
9. After evidence capture, the probe may be converted into an ordinary visible regression case if useful.

## Required trial metadata

A valid pre-oracle capture binds:

- probe identity;
- exact repository revision;
- isolated context mode and exact accessible-path allowlist;
- bundle manifest and bundle identity;
- `fresh_instance=true`;
- `external_repository_access=false`;
- `prior_trial_access=false`;
- `oracle_access=false`;
- unchanged raw response;
- `response_captured_before_oracle_reveal=true`.

These fields are an integrity record, not proof of semantic correctness or psychological freshness. The stronger control is that the tested instance is technically given only the isolated bundle and the oracle is not persisted before capture.

## Current evidence status

- Routing mechanism and referential fidelity: separately reviewed/assured.
- `WA-EVAL-031..033`: visible regression cases only; **not strict blind evidence**.
- `RP-*` probe definitions: stimulus-only/pre-oracle.
- Independent fresh-instance raw responses: **not yet persisted**.
- Oracle/grading for `RP-*`: **must remain unpersisted until after raw response capture**.
- PR #37 therefore remains **not yet a Promotion Candidate** on the basis of blind behavior evidence.

## Non-goals

This protocol does not create a new workflow engine, candidate registry, matcher service, Building Block, priority, admission or implementation authority. It is a bounded evidence-control for the already-defined routing behavior.
