# Contract (kompakt, nicht Laufzeit)

Dieses Dokument gehört **nicht** zur Laufzeit des Skills. Es beschreibt, was der Skill leisten muss und woran man es prüft. Laufzeit: `skill.md` und `references/core-method.md`.

**Status:** `declared` (Kandidat #63). Es gibt keinen geprüften Verhaltensnachweis, keinen Generic Fit und keine Admission über diese Version hinaus.

## Zweck

Prompts erstellen, prüfen, anpassen und Ergebnisse gegen den Auftrag prüfen, plattformunabhängig, mit dünner Erstellen-Schicht.

## Ein- und Ausgaben

| Modus | Eingabe | Ausgabe |
|---|---|---|
| `.prompt` | Aufgabe, Kontext, Zielmodell, Umgebung | vollständiger Prompt, Annahmen, Hinweis „intern geprüft, ungetestet", Kostenhinweis |
| `.prompt review` | vorhandener Prompt | Gesamturteil, Befunde mit Zitat, Prognose, Stärken, verbesserte Fassung, Änderungsliste, Testvorschlag |
| `.prompt test` | Ergebnis und Auftrag, auf Wunsch Testlauf | Testbericht (Art je Befund, Ausführungsangaben, Belegstärke, Kosten) |

## Invarianten

1. Ergebnis ist Kandidat, schafft keine Autorität.
2. Kleinste ausreichende Anweisung, kein Mega-Template.
3. Fidelity vor Tokenersparnis.
4. Interner Review ist nicht unabhängig und wird so ausgewiesen.
5. Kein stilles Abwerten bei fehlender Fähigkeit.
6. Plattformneutraler Kern; Modell- und Umgebungsspezifisches nur in datierten Profilen.
7. Wesentliche Entscheidungen als Decision Brief in einfacher Sprache.
8. Begriffe des Repos, keine Parallelskalen.
9. Jeder Befund mit wörtlichem Zitat.
10. Kein Schreiben in Repo, Issues, PRs.

## Fehlerfläche (PQ-01 bis PQ-12)

PQ-01 Anker durch Ergebnisrichtung · PQ-02 fehlendes Freigabe-Gate · PQ-03 offener Lesescope · PQ-04 interne Widersprüche · PQ-05 Mega-Prompt, Wiederholung, Verbotsdichte · PQ-06 nicht schließbare Einheiten · PQ-07 neue Begriffe oder Parallelskalen · PQ-08 falsches Ziel (Repository nicht geprüft) · PQ-09 Missverhältnis Prompt zu Modell/Umgebung · PQ-10 Unabhängigkeits-Overclaim · PQ-11 Checkliste als Punktzahl · PQ-12 Autoritäts-Laundering.

Zuordnung zu den Fehlerfamilien des Repos: `references/core-method.md` C.3 (abgeleitet). Maßgeblich ist `tests/evals/failure_corpus.json`.

## Abgrenzung (Ergebnis des Überschneidungstests)

- **Gedeckt bei anderen:** Kontextauswahl (BB-CONTEXT), Aufgabenkompilierung (#55), Kosten-/Routing-Abwägung (#48). Dieser Skill nutzt sie.
- **Hier neu:** Prompt-Review auf Fehlmuster, Anpassung des Prompt-Textes an Modell und Umgebung, Schutzmuster im Prompt, Testbericht.
- **Offen:** Zuständigkeit für Ergebnisprüfung gegen Auftrag (teilweise bei #55, BB-ASSURE, Trial-Protokoll #46).

## Autorität

Kandidat, keine Autorität. Kein Requirement, kein Building Block, kein Cursor-Wechsel, kein Generic Fit, kein Merge.

## Eval-Grenze

Fälle in `EVAL_CASES.md`. **Nicht zirkulär:** Fälle einfrieren, erforderliche Arbeit ableiten, erst danach bewerten. Baseline A: Prompt ohne Skill (von Hand oder mit KI). Treatment B: mit Skill. Gemessen: Korrekturrunden, gefundene und vermiedene Fehler, Verhalten beim ersten Lauf, Verbrauch. Bestehen heißt nicht „Generic Fit".

## Kill- und Korrekturkriterien

Verkleinern, zusammenführen oder verwerfen, wenn: Baseline gleichwertig oder weniger Aufwand; #55, #48 oder BB-CONTEXT tragen den Bedarf; Review erfindet Probleme oder wirkt als Punktzahl; Owner muss mehr korrigieren als ohne Skill; Grenze zu #55/#48 nicht haltbar; Skill wird zum verdeckten Planer.

## Offene Punkte

- Plattform-Erkennung des Codeworts (ChatGPT, Work, Codex, Claude): ungeprüft
- Einordnung der Modelle (Astra, Sol, Luna, Claude-Modelle): nicht gegen Anbieterdokumentation geprüft
- Technischer Träger je Plattform (Kopfdaten, Dateiname): spätere Entscheidung
- Ergebnisprüfung: Abgrenzung zu #55 und BB-ASSURE
- Abhängigkeit von #55 und BB-CONTEXT (beide nicht als Laufzeit verfügbar)
