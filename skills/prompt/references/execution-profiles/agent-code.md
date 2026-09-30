# Profil: Code / Agent (z. B. Claude Code, Codex, Work)

**Status:** umgebungsspezifisches Profil, nicht Kern. Stand 2026-09-30, ungeprüft gegen Produktdokumentation.

## Merkmale

- Echte Aktionen sind möglich: Dateien lesen und schreiben, Branches, Commits, Issues und PRs.
- Läufe sind länger; Kontext wächst; Limits (Sitzung, Woche, je Modus) können mitten im Lauf erschöpft sein.
- Projektregeln liegen oft in Dateien, die das Werkzeug liest (z. B. `AGENTS.md`, `CLAUDE.md`). Der Prompt verweist darauf, statt sie zu wiederholen.

## Pflichtbausteine im Prompt (siehe Kernmethode B.4)

- Zielrepository und Remote prüfen, bei Abweichung stoppen
- Freigabe-Gate vor folgenreichen Schreibaktionen (erst lesen und entwerfen, nach Freigabe schreiben)
- Blocker-Regel (bei Konflikt oder fehlendem Zugriff nichts schreiben, berichten, stoppen)
- Lesemodus je Quelle und Suchbudget
- Stopp am Ende und definiertes Berichtsformat
- Bei Review-Aufgaben: Unabhängigkeitsbedingung

## Kosten und Limits

Der Prompt sollte so gebaut sein, dass ein Abbruch durch ein Limit **keinen Zustand verliert**: Zwischenstände werden in einem Übergabe-Record gesichert, der Zustand heißt `incomplete`, nicht „fertig". Modell und Modus nach Aufgabe wählen (Zuständigkeit Kandidat #48), schwere Denkarbeit im Chat vorbereiten, nur die nicht ersetzbare Ausführung in den knappen Modus geben.

## Grenzen

Was das konkrete Werkzeug kann, steht im Anbieterprofil. Ein Produktname beweist keine Fähigkeit: Fähigkeit prüfen statt annehmen.
