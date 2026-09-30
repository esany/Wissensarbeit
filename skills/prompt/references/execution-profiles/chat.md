# Profil: Chat

**Status:** umgebungsspezifisches Profil, nicht Kern. Stand 2026-09-30, ungeprüft gegen Produktdokumentation.

## Merkmale

- Mensch ist im Loop, Ergebnis ist Text, der Owner prüft ihn selbst.
- Kein eigener Repo-Zugriff, keine Schreibaktionen durch den Ausführenden, sofern die Umgebung nichts anderes bereitstellt.
- Geringeres Risiko: Agent-Bausteine (Freigabe-Gate, Blocker-Regel, Lesescope) werden **nicht** verlangt, außer der Prompt soll später in einer Agent-Umgebung laufen.

## Folgen für den Prompt

- Kurz, ein Ziel, ein Ausgabeformat.
- Kontext als eingefügter Text oder Verweis, den der Owner mitliefert.
- Kein Aufbau für mehrphasige Läufe, sofern die Aufgabe klein ist.

## Grenzen

Was ein Chat tatsächlich kann (Dateien lesen, Websuche, frischer Kontext), hängt von Anbieter und Tarif ab und ist im jeweiligen Anbieterprofil zu klären. Fehlt eine Fähigkeit, gilt „kein stilles Abwerten": sichtbar machen.
