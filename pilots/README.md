# Pilots

Pilots test the generic contracts against real project work. Case material remains
in its case repository; this repository retains only provenance, dispositioned
generic learnings, and executable regressions.

The original generic pilot closure is documented in
`generic-pilot-learnings/pilot-closure.md`. Its regression fixtures exercise
existing context, integration, assurance, trace, and learning mechanisms. They do
not add a building block or grant implementation authority.

Fresh cross-project evidence from `esany/paleo-type` is recorded in
`paleo-type-2026-09-13/generic-learnings.md`. It is pilot evidence with explicit
Generic-Fit dispositions, not automatic Core promotion. The corresponding fresh
whole-repository audit of Wissensarbeit is persisted at
`../project/audits/WA-AUDIT-2026-09-13.md`.

The original `paleo-type` pilot record is intentionally pinned to its 2026-09-13
checkpoint. Later material movement is preserved as dated deltas rather than
retroactively rewriting the snapshot:

- `../project/audits/WA-AUDIT-2026-09-14-PALEO-TYPE-DELTA.md` records
  `paleo-type@3df61570a74b258570127b0a5650df89e7f6c596` through the closed
  pre-synthesis Research phase and refines the Context-Fidelity hypothesis.
- `../project/audits/WA-AUDIT-2026-09-17-PALEO-TYPE-DELTA.md` records current
  `paleo-type@81a9be5ac37c47830c2bb1a53025197a18096c17` plus PR #224 only as open
  falsification evidence. It adds the empirically supported programme-transition
  reconciliation lesson, non-generative `NONE`/unset semantics, Project-purpose
  recoverability, bounded repair→cursor recovery, and the distinction between
  scientific capability, reliability, restartability and overhead.

The 2026-09-17 delta changes the Wissensarbeit execution sequence inside PR #33:
P2 Fidelity Manifest preflight is no longer immediately ready. The next persisted
step is `p2-post-pr33-baseline-reconciliation`; after PR #33 is reviewed/merged,
that step must bind the actual merged `main` execution cursor, reconciliation
packet, derived current-state view and exact audit evidence before P2 preflight can
be exposed as ready. P2 implementation remains separately unauthorized.

Cross-clock freshness is now checked by `tools/state_freshness.py` and regression
tests. This adds no state store: it validates agreement among the existing
`project/execution_state.json`, `project/reconciliation.json` and
`project/CURRENT_STATE.md` owners/views.

All records in PR #33 remain reviewable branch evidence until merged; they do not
become accepted `main` state merely by existing on the review branch. Issue #7
retains planning-thread continuity while the executable cursor remains in
`project/execution_state.json`.
