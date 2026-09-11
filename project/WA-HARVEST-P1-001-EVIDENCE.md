# WA-HARVEST-P1-001

P1 of #7 executes the smallest real E2E conversation harvest requested by #5.

- Source/session: persisted `WA-HARVEST-SEED-003`, archived primary chat `00-Audit der Repositories`, chat `6a97167d-70fc-83eb-8b97-3ae4f5d7f0cf`, with the four persisted turn IDs in the JSON artifact.
- Artifact: `project/conversation_harvest_p1_v1.json`.
- Reused mechanism: the existing Foundation harvest contract and `tools/work.py` validation path; no second PM/requirement store, building block, architecture, or canonical requirement was added.
- Material items: 4. Dispositions: 3 `refine`, 1 `defer`; all result in explicit persistent `no_change` actions.
- Owner-source boundary: every record keeps source role separate from acceptance/promotion; no Owner item is promoted to Requirement, Decision, or Architecture.
- Scope boundary: all four items are `generic`; project-specific content is not promoted into core.
- Idempotency: stable record IDs and the persisted idempotency key `sha256:WA-HARVEST-SEED-003:P1:v1`; semantic source identity `(chat_id, turn_id)` now fails closed, including the regression `same source turn + different record ID => FAIL`.
- Assurance: 74 tests pass; `python3 tools/work.py validate`, `audit`, and `derive` pass; the pre-existing Foundation harvest remains valid.
- Restart: **pending independent #11 assurance**. This artifact is restartable in Git, but no independent fresh-context proof is claimed here.
- Provenance gap: repository evidence contains the stable source/turn references and persisted seed claims, not the original chat body; this limitation remains explicit.
- CI/formal validation is not Domain Truth or Owner Acceptance.
