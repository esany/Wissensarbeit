# Prüfunterlagen für Skills (nicht Laufzeit)

Testfälle sind keine Skills und keine Atome. Sie gehören zur Assurance (BB-ASSURE, `tools/evals.py`). Ein Skill-Ordner enthält nur, was bei der Nutzung geladen wird. Die `CONTRACT.md` je Skill bleibt beim Skill.

## Testauftrag (vor jeder Testrunde, in fünf Zeilen)
1. **Frage:** Welche Entscheidung stützt der Test?
2. **Genug, wenn:** Abbruchkriterium.
3. **Kostenleiter** (Orientierung, kein Gatter): lesen, was da ist → deterministisch prüfen (`validate`, `audit`, Unittests) → echte Nutzung auswerten → einzelner Modelllauf → mehrere Läufe oder Vergleich ohne Skill. Nächste Stufe nur, wenn die darunter die Frage nicht beantwortet. Leidet die Qualität des Belegs durch das Sparen, wird nicht gespart (ein Satz Begründung).
4. **Baseline** nur, wenn der Test einen Mehrwert behauptet.
5. **Bewertung** nicht durch dieselbe Instanz, die Fälle und Skill geschrieben hat, wenn der Beleg mehr als ein Urteil sein soll.

Größere Posten (mehrere Unterkontexte oder deutlich mehr als 50.000 Tokens) vorher mit Zahl und Nutzen nennen und kurz auf die Zusage warten. Siehe `AGENTS.md`, Kostenprinzip.

## Inhalt
- `prompt-eval-cases.md`: Testfälle und bisherige Ergebnisse für `prompt`
- `coverage-prompt-skills.md`: Abdeckungsliste der Anforderungen für `prompt` und `failure-pattern-check`
