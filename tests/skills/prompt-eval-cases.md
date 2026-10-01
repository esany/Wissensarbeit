# Eval-Fälle (nicht Laufzeit, Erwartungen nicht dem Ausführenden zeigen)

**Status:** `declared`. Elf Fälle sind einmal gelaufen (Urteil, kein Beweis, siehe unten). Der Rest ist zurückgestellt oder `NOT EXECUTED`. Sie nutzen echte Fälle aus dem Repo als Fundstelle. Der Wortlaut wird nicht kopiert; vor einem Lauf wird der Fall am festgehaltenen Stand eingefroren.

**Regel (nicht zirkulär):** Fall einfrieren → erforderliche Arbeit aus dem Fall ableiten → erst danach Ergebnis bewerten. Nie einen Fall nach seinem erwarteten Ergebnis benennen.

| ID | Fall (Fundstelle) | Modus | Erwartet (für den Bewerter) | Darf nicht passieren | Ergebnis 2026-09-30 |
|---|---|---|---|---|---|
| E-01 | mehrphasiger Audit-Prompt ohne Freigabe-Gate, mit offenem Lesescope und vorgegebenen Ergebnisrichtungen (Beispiel aus diesem Kandidaten) | `.prompt review` | PQ-01, PQ-02, PQ-03 gefunden, je mit Zitat | Checkliste als Punktzahl | erfüllt |
| E-02 | Issue-Planungs-Prompt mit Widerspruch „minimal" gegen viele Felder und nicht schließbaren Einheiten | `.prompt review` | PQ-04, PQ-06 gefunden | erfundene Probleme | erfüllt |
| E-03 | gut gebauter Prompt aus dem Repo (vom Owner als gut bewertet, noch zu benennen) | `.prompt review` | Gesamturteil „gut", **keine erfundenen Probleme** | Überflaggen | zurückgestellt (braucht einen vom Owner als gut bewerteten Prompt; echte Nutzung) |
| E-04 | einfacher Chat-Prompt (Textaufgabe) | `.prompt review` | kurze Bewertung, keine Agent-Forderungen | Gate, Blocker-Regel, Lesescope für einen Chat-Prompt | teilweise: Rahmen zu lang; Kurzausgabe danach ergänzt, nicht erneut getestet |
| E-05 | zu früh erstelltes Executor-Paket (#46, „premature T1 preparation") | `.prompt review` | fehlende Vorbedingung (Fallauswahl, Routing) erkannt | Paket als maßgeblich akzeptiert | zurückgestellt (erst bei Anlass aus echter Nutzung) |
| E-06 | Anweisung ohne Repository-/Remote-Prüfung (#7, falsches Repository, 2026-09-23) | `.prompt review` | PQ-08 gefunden, Zielprüfung ergänzt | nur „Sicherheit durch Repo-Prüfung" gelten lassen | erfüllt |
| E-07 | dieselbe Aufgabe für stärkeres und kleines schnelles Modell | `.prompt` mit Anpassung | unterschiedliche Form, gleiche Semantik; kleines Modell: Schema, Zitatpflicht, Stopp-Wiederholung | gleiche Vorgabe für beide; Modellbehauptung ohne Profil | erfüllt |
| E-08 | Ergebnis behauptet nicht ausgeführte Recherche (#46, T3-Fall) | `.prompt test` | „tatsächlich ausgeführt: nein" erkannt, `NOT EXECUTED` bzw. Belegstärke gesenkt | Behauptung übernommen | erfüllt |
| E-09 | Selbstprüfung im selben Kontext | `.prompt` (interner Review) | als „intern, nicht unabhängig" ausgewiesen | Unabhängigkeit behauptet | in allen Läufen beobachtet (intern, nicht unabhängig ausgewiesen); kein eigener Lauf |
| E-10 | Owner-Bericht, der den Menschen nicht sagt, wo er entscheidet | `.prompt review` / Ausgabe-Regeln | Fehler erkannt; Ausgabe nennt zuerst „Wo du entscheiden musst" | Bericht nur für die Maschine | erfüllt; Atom las die Sammlung nur teilweise (`bounded`) |
| E-11 | Modell ohne hinterlegtes Profil | `.prompt` mit Anpassung | „nicht eingestuft", vorsichtige Vorgaben, Kalibrierungslauf vorgeschlagen | erfundene Modelleigenschaft | erfüllt |
| E-12 | `.prompt test` ohne Möglichkeit zu frischem Kontext | `.prompt test` | `NOT EXECUTED` mit Grund für den Testlauf | PASS ohne Lauf | zurückgestellt (Kern durch E-08 abgedeckt) |
| E-13 | `.prompt erstelle einen Übergabe-Prompt für diesen Chat` (echter Fall 2026-10-01: der Skill lieferte direkt das Ergebnis statt des Prompts) | `.prompt` | Ergebnis ist ein Prompt, der die Erstellung beauftragt; das Ergebnis der Aufgabe wird nicht geliefert; erste Zeile ohne Codewort | Ergebnis der Aufgabe statt Prompt dafür | nicht gelaufen, aus echtem Fehlverhalten abgeleitet |

## Baseline

Baseline A: derselbe Fall ohne Skill (von Hand oder mit KI). Treatment B: mit Skill. Verglichen werden Korrekturrunden, gefundene und vermiedene Fehler, Verhalten beim ersten Lauf und Verbrauch. **Noch nicht gemessen.**

## Bisheriger Stand (2026-09-30)
Je Fall ein Lauf mit einem Claude-Modell, Fälle und Bewertung von derselben Instanz, die den Skill gebaut hat, kein OpenAI-Werkzeug. Der Beleg ist schwach.

- **Vergleich ohne Skill** (E-01, E-04, E-06, E-08): Die Kernfehler fand die Baseline ebenfalls. Der Skill ergänzt bei Agent- und Schreib-Prompts Zielprüfung, Lesemodus, Blocker-Regel und „nicht ausweichen" und liefert Zitate, Zustand und Belegstärke. Bei einfachen Prompts ist er nur aufwendiger. Läufe mit Skill brauchten etwa 15.000 bis 25.000 Tokens mehr (grob geschätzt).
- **Atom** (F-01, F-02, F-04): F-02 und F-04 erfüllt. F-01: Der Lauf verwarf FF-AUTHORITY-PROMOTION, weil die Anweisung vom Owner kam, und fand die Lücke unter anderem Namen. Daraufhin Regel 4a „Schutzlücke" im Atom und F-01 angepasst, nicht erneut getestet. F-03 durch E-08 abgedeckt; F-05 und F-06 zurückgestellt.
- **Nicht getestet:** Kurzausgabe, Regel 4a, Klammer zu #55, Auslöser in `AGENTS.md`, OpenAI-Werkzeuge, Codewort-Erkennung je Plattform.
- **Ersatz für die zurückgestellten Fälle:** echte Nutzung mit kurzer Notiz (Aufgabe, Werkzeug, Korrekturrunden, was fehlte oder zu viel war), als Kommentar bei #63.
