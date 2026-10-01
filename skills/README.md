# Skills (Kandidaten, Branch-Stand)

**Status:** `declared`. Nicht gemergt. Kein Generic Fit. Keine Autorität.

| Skill | Zweck | Kandidat |
|---|---|---|
| `prompt/` | Prompts erstellen (`.prompt`), prüfen (`.prompt review`), Ergebnisse prüfen (`.prompt test`), an Modell und Umgebung anpassen | #63 |
| `failure-pattern-check/` | Artefakte gegen die Fehlerfamilien des Repos prüfen (Atom, wird vom Prompt-Skill genutzt) | #65 |

## So ist jeder Skill aufgebaut

- `skill.md`: Einstieg (Zweck, Auslöser, Autorität, Abschluss, STOP)
- `references/core-method.md`: verpflichtende Kernmethode
- `references/execution-profiles/`: Modell- und Umgebungsprofile (nicht Kern, datiert)
- `CONTRACT.md`: was der Skill leisten muss, **nicht Laufzeit**. Testfälle und Abdeckungsliste liegen in `tests/skills/`

## Nutzung

Codewörter: `.prompt`, `.prompt review`, `.prompt test`. Wie die jeweilige Plattform das Codewort erkennt, ist noch nicht geprüft. Bis dahin das Codewort im Prompt ausdrücklich nennen und `skills/prompt/skill.md` sowie `skills/prompt/references/core-method.md` bereitstellen (Claude Code, Codex, Work: Datei im Repo; Chat: einfügen).

## Grenzen

Die Abdeckung der Anforderungen steht in `tests/skills/coverage-prompt-skills.md`.
