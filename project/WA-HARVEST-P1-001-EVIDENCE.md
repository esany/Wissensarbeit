# WA-HARVEST-P1-001

P1 of #7 executes the smallest real E2E conversation harvest requested by #5.

- Source/session: persisted `WA-HARVEST-SEED-003`, archived primary chat `00-Audit der Repositories`, chat `6a97167d-70fc-83eb-8b97-3ae4f5d7f0cf`, with the four persisted turn IDs in the JSON artifact.
- Artifact: `project/conversation_harvest_p1_v1.json`.
- Reused mechanism: the existing Foundation harvest contract and `tools/work.py` validation path; no second PM/requirement store, building block, architecture, or canonical requirement was added.
- Material items: 4. Dispositions: 3 `refine`, 1 `defer`; all result in explicit persistent `no_change` actions.
- Owner-source boundary: every record keeps source role separate from acceptance/promotion; no Owner item is promoted to Requirement, Decision, or Architecture.
- Scope boundary: all four items are `generic`; project-specific content is not promoted into core.
- Idempotency: stable record IDs and the persisted idempotency key `sha256:WA-HARVEST-SEED-003:P1:v1`; semantic source identity `(chat_id, turn_id)` now fails closed, including the regression `same source turn + different record ID => FAIL`.
- Assurance: 77 tests pass; `python3 tools/work.py validate`, `audit`, and `derive` pass; the pre-existing Foundation harvest remains valid.
- Restart: **independently assured / PASS** by `WA-RESTART-2026-09-11-02` in Issue #11 against `caed6ec7c100d56813569aa13884a446cbffb82b`; Gate A = PASS and Gate B = PASS. Terminal evidence: https://github.com/esany/Wissensarbeit/issues/11#issuecomment-5632821967.
- Restart scope boundary: this PASS proves restartability of the tested persistent state. It does **not** prove semantic completeness of historical sources, Domain Truth, or Owner Acceptance.
- Provenance gaps remain explicit, including the Foundation `REQ-009` `provenance-gap / high uncertainty`; independent restart assurance does not heal or reinterpret them.
- Provenance gap: repository evidence contains the stable source/turn references and persisted seed claims, not the original chat body; this limitation remains explicit.
- CI/formal validation is not Domain Truth or Owner Acceptance.
