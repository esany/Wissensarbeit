# Kernmethode (verpflichtend)

## Ablauf

1. **Sammlung lesen:** `tests/evals/failure_corpus.json` (Familien mit Kurzbeschreibung des Fehlers und Eval-Modi) und `project/risks.json`. Den Stand (Commit oder Datum) im Ergebnis nennen, damit die Prüfung nachvollziehbar bleibt.
2. **Unabhängige erste Lesart:** Das Artefakt verstehen, **ohne** die Familienliste zu benutzen. Eigene Auffälligkeiten mit Zitat notieren. Erst danach weiter.
3. **Späte Lückenprüfung:** Jede Familie mit drei Fragen an das Artefakt prüfen:
   - Gibt es dafür eine belegte Stelle im Artefakt?
   - Gibt es eine stärkere Alternativerklärung?
   - Würde der Fehler das Ergebnis des Owners materiell verschlechtern?
   Nur was alle drei Fragen trägt, wird ein Treffer. Der Rest wird verworfen.
4. **Treffer formulieren:** Familie · wörtliche Stelle · Sicherheit mit Grund · Korrekturhinweis.
4a. **Schutzlücke (unabhängig von der Familie):** Verlangt ein Artefakt eine folgenreiche oder schwer rückholbare Aktion (Löschen, Force-Push, Schreiben auf geschützten Zweig, Anlegen nach außen sichtbarer Objekte) **ohne** Freigabe-Gate, Zielprüfung oder Blocker-Regel, wird das als eigener Befund „Schutzlücke" mit wörtlicher Stelle benannt. Das gilt auch, wenn die Anweisung vom Owner stammt: Die Lücke betrifft die Absicherung, nicht die Befugnis. Die Familien-Zuordnung ist dann nachrangig und darf „keine Familie" lauten.
5. **Nicht Zuordenbares:** als „keine Familie" benennen, nicht einer Familie zuschlagen.
6. **Gegenprobe:** Für jeden Treffer eine Stelle suchen, die ihm widerspricht, oder „keine gefunden" ausweisen.

## Familien (Stand 2026-09-30, Quelle: Sammlung)

FF-STATE-CONTINUITY · FF-SYSTEMIC-DRIFT · FF-AUTHORITY-PROMOTION · FF-EPISTEMIC-INTEGRITY · FF-SOLUTIONISM-BLOAT · FF-FALSE-ASSURANCE · FF-EXECUTION-PROGRESS

**Diese Liste ist nur eine Orientierung.** Maßgeblich ist die Sammlung im Repo. Weicht sie ab, gilt die Sammlung.

## Eigene Fehlerfläche (worauf dieser Skill selbst achten muss)

- erfundene oder aufgeblähte Treffer (Überflaggen)
- Familien-Zwang
- Checkliste als Punktzahl
- Kosten durch Dauerprüfung (nur einsetzen, wo es sich lohnt)
- veraltete Sammlung (Stand nennen)

## Grenzen

Kein Umschreiben des Artefakts, keine Autorität, kein Schreiben in die Sammlung, keine Modellbehauptung ohne Kennzeichnung.
