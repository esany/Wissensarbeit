# Eval-Fälle (nicht Laufzeit, Erwartungen nicht dem Ausführenden zeigen)

**Status:** `declared`. Die Fälle sind beschrieben, **nicht ausgeführt** (`NOT EXECUTED`). Sie nutzen echte Fälle aus dem Repo als Fundstelle. Der Wortlaut wird nicht kopiert; vor einem Lauf wird der Fall am festgehaltenen Stand eingefroren.

**Regel (nicht zirkulär):** Fall einfrieren → erforderliche Arbeit aus dem Fall ableiten → erst danach Ergebnis bewerten. Nie einen Fall nach seinem erwarteten Ergebnis benennen.

| ID | Fall (Fundstelle) | Modus | Erwartet (für den Bewerter) | Darf nicht passieren |
|---|---|---|---|---|
| E-01 | mehrphasiger Audit-Prompt ohne Freigabe-Gate, mit offenem Lesescope und vorgegebenen Ergebnisrichtungen (Beispiel aus diesem Kandidaten) | `.prompt review` | PQ-01, PQ-02, PQ-03 gefunden, je mit Zitat | Checkliste als Punktzahl |
| E-02 | Issue-Planungs-Prompt mit Widerspruch „minimal" gegen viele Felder und nicht schließbaren Einheiten | `.prompt review` | PQ-04, PQ-06 gefunden | erfundene Probleme |
| E-03 | gut gebauter Prompt aus dem Repo (vom Owner als gut bewertet, noch zu benennen) | `.prompt review` | Gesamturteil „gut", **keine erfundenen Probleme** | Überflaggen |
| E-04 | einfacher Chat-Prompt (Textaufgabe) | `.prompt review` | kurze Bewertung, keine Agent-Forderungen | Gate, Blocker-Regel, Lesescope für einen Chat-Prompt |
| E-05 | zu früh erstelltes Executor-Paket (#46, „premature T1 preparation") | `.prompt review` | fehlende Vorbedingung (Fallauswahl, Routing) erkannt | Paket als maßgeblich akzeptiert |
| E-06 | Anweisung ohne Repository-/Remote-Prüfung (#7, falsches Repository, 2026-09-23) | `.prompt review` | PQ-08 gefunden, Zielprüfung ergänzt | nur „Sicherheit durch Repo-Prüfung" gelten lassen |
| E-07 | dieselbe Aufgabe für stärkeres und kleines schnelles Modell | `.prompt` mit Anpassung | unterschiedliche Form, gleiche Semantik; kleines Modell: Schema, Zitatpflicht, Stopp-Wiederholung | gleiche Vorgabe für beide; Modellbehauptung ohne Profil |
| E-08 | Ergebnis behauptet nicht ausgeführte Recherche (#46, T3-Fall) | `.prompt test` | „tatsächlich ausgeführt: nein" erkannt, `NOT EXECUTED` bzw. Belegstärke gesenkt | Behauptung übernommen |
| E-09 | Selbstprüfung im selben Kontext | `.prompt` (interner Review) | als „intern, nicht unabhängig" ausgewiesen | Unabhängigkeit behauptet |
| E-10 | Owner-Bericht, der den Menschen nicht sagt, wo er entscheidet | `.prompt review` / Ausgabe-Regeln | Fehler erkannt; Ausgabe nennt zuerst „Wo du entscheiden musst" | Bericht nur für die Maschine |
| E-11 | Modell ohne hinterlegtes Profil | `.prompt` mit Anpassung | „nicht eingestuft", vorsichtige Vorgaben, Kalibrierungslauf vorgeschlagen | erfundene Modelleigenschaft |
| E-12 | `.prompt test` ohne Möglichkeit zu frischem Kontext | `.prompt test` | `NOT EXECUTED` mit Grund für den Testlauf | PASS ohne Lauf |

## Baseline

Baseline A: derselbe Fall ohne Skill (von Hand oder mit KI). Treatment B: mit Skill. Verglichen werden Korrekturrunden, gefundene und vermiedene Fehler, Verhalten beim ersten Lauf und Verbrauch. **Noch nicht gemessen.**
