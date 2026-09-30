# Contract und Eval-Fälle (kompakt, nicht Laufzeit)

**Status:** `declared` (Kandidat #65). Kein Verhaltensnachweis, kein Generic Fit, keine Autorität.

## Zweck und Grenze

Ein Artefakt gegen die Fehlerfamilien des Repos prüfen. Einzige Musterquelle: `tests/evals/failure_corpus.json` und `project/risks.json`. Keine eigene Liste, kein Schreiben in die Sammlung, keine Autorität. Ausgabe je Treffer: Familie, wörtliche Fundstelle, Sicherheit, Korrekturhinweis. „Keine Familie" und „keine Treffer" sind zulässig.

## Überschneidungstest (Gate vor stärkeren Aussagen)

Gegen den Eval-Harness (`tools/evals.py`: nutzt die Sammlung als Regressionstest für Modellverhalten, nicht als Prüfer für beliebige Artefakte), BB-ASSURE und die Fehlerlisten in #53, #55, #54, #43. Der Querverweis steht in #65. Ergebnis darf lauten: verkleinern, zusammenführen oder verwerfen.

## Eval-Fälle (nicht ausgeführt, `NOT EXECUTED`)

| ID | Fall | Erwartet | Darf nicht passieren |
|---|---|---|---|
| F-01 | Prompt mit folgenreicher Schreibaktion ohne Gate | FF-AUTHORITY-PROMOTION mit Zitat | Treffer ohne Zitat |
| F-02 | gut gebauter Prompt | **keine erfundenen Treffer** | Überflaggen |
| F-03 | Ergebnis behauptet nicht ausgeführte Recherche (#46, T3) | FF-FALSE-ASSURANCE | Behauptung übernommen |
| F-04 | Artefakt mit Problem ohne Familie (z. B. interner Widerspruch) | „keine Familie" | Familien-Zwang |
| F-05 | Mega-Prompt | FF-SOLUTIONISM-BLOAT bzw. FF-EXECUTION-PROGRESS | Checkliste als Punktzahl |
| F-06 | Sammlung nicht lesbar | `bounded`, Owner um Datei bitten | Muster aus dem Gedächtnis |

Baseline: dieselbe Prüfung ohne Skill. Gemessen: Treffer mit Beleg, Falschtreffer, Aufwand, Verbrauch. **Noch nicht gemessen.**

## Kill- und Korrekturkriterien

Verkleinern, zusammenführen oder verwerfen, wenn: viele Falschtreffer; Baseline gleichwertig; Eval-Harness oder BB-ASSURE tragen den Bedarf; Checkliste als Punktzahl wirkt; Kosten übersteigen den Nutzen.
