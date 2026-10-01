# Skills (Kandidaten, Branch-Stand)

**Status:** Kandidaten. Nicht gemergt. Kein Generic Fit. Keine Autorität. Evidence maturity wird je Skill getrennt geführt.

| Skill | Zweck | Kandidat | Evidence maturity |
|---|---|---|---|
| `prompt/` | Prompts erstellen (`.prompt`), prüfen (`.prompt review`), Ergebnisse prüfen (`.prompt test`), an Modell und Umgebung anpassen | #63 | `executable`; reale Nutzungsevidenz vorhanden; nicht `regression-protected` |
| `failure-pattern-check/` | Artefakte gegen die Fehlerfamilien des Repos prüfen (Atom, wird vom Prompt-Skill genutzt) | #65 | `declared` (unverändert; in dieser Statuskorrektur nicht neu bewertet) |

## Reifegradlogik

Identity/Disposition und Evidence maturity sind getrennt. Für Evidence maturity gilt die in #52 wiederverwendete Skala aus PR #37:

`declared → wired → executable → regression-protected → real-use-demonstrated → human-effective → robust/restartable`

Reale Nutzungsevidenz kann vorhanden sein, ohne dass eine fehlende Zwischenstufe übersprungen wird. Beim Prompt-Skill ist `executable` die höchste durchgängig getragene Stufe; reale Nutzung ist zusätzlich belegt, aber eine belastbare Regression-Protection fehlt.

## So ist jeder Skill aufgebaut

- `skill.md`: Einstieg (Zweck, Auslöser, Autorität, Abschluss, STOP)
- `references/core-method.md`: verpflichtende Kernmethode
- `references/execution-profiles/`: Modell- und Umgebungsprofile (nicht Kern, datiert)
- `CONTRACT.md`: was der Skill leisten muss, **nicht Laufzeit**. Testfälle und Abdeckungsliste liegen in `tests/skills/`

## Nutzung

Codewörter: `.prompt`, `.prompt review`, `.prompt test`. Wie die jeweilige Plattform das Codewort erkennt, ist noch nicht geprüft. Bis dahin das Codewort im Prompt ausdrücklich nennen und `skills/prompt/skill.md` sowie `skills/prompt/references/core-method.md` bereitstellen (Claude Code, Codex, Work: Datei im Repo; Chat: einfügen).

## Grenzen

Die Abdeckung der Anforderungen steht in `tests/skills/coverage-prompt-skills.md`.
