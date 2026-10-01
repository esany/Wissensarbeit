# Fehlmuster-Prüfung (Atom)

**Status:** `declared` · Skill-Kandidat #65 · nicht gemergt · kein Generic Fit · keine Autorität

## Zweck

Ein kleiner, wiederverwendbarer Baustein. Er prüft ein **Artefakt** (Prompt, KI-Ergebnis, Issue-Text, Plan) gegen die **Fehlerfamilien des Repos** und meldet je Treffer: Familie, wörtliche Stelle, Sicherheit, Korrekturhinweis.

Frage: Welches der im Repo belegten typischen KI-Fehlmuster, die die Ergebnisse des Owners verschlechtern, trifft auf dieses Artefakt zu, und wo genau?

## Einzige Musterquelle

- `tests/evals/failure_corpus.json` (Fehlerfamilien)
- `project/risks.json` (Risiken R-001 bis R-010)

Dieser Skill führt **keine eigene Fehlerliste**. Neue Muster werden über den Repo-Prozess in die Sammlung aufgenommen, nicht hier.

**Ist die Sammlung in der Umgebung nicht lesbar:** Ergebnis `bounded`, mit Grund. Den Owner bitten, die Datei einzufügen. Keine Muster aus dem Gedächtnis ergänzen und nicht so tun, als wäre geprüft worden.

## Auslöser

- Aufruf durch den Skill `prompt` (Review, Test) oder ausdrücklich durch den Owner
- Bei folgenreichen Artefakten, Ergebnisprüfung und Review
- **Nicht** für einfache Chat-Prompts und nicht als Dauerprüfung

## Methode

Siehe `references/core-method.md`. Kurz: Der Skill arbeitet **spät**, erst nachdem eine unabhängige erste Lesart des Artefakts stattgefunden hat. Er dient der Lückenprüfung, nie als Punktzahl.

## Ausgabe je Treffer

- **Familie** (ID aus der Sammlung, z. B. FF-AUTHORITY-PROMOTION) und, wo passend, Risiko-ID
- **wörtliche Fundstelle** im Artefakt
- **Sicherheit** (hoch, mittel, niedrig, mit Begründung)
- **Korrekturhinweis**

**Ausgabe knapp:** nur Treffer und „keine Familie"-Punkte, je mit Zitat. Die übrigen Familien in einer Zeile („kein Treffer: …"), ohne Begründung je Familie, es sei denn, der Owner fragt danach. **„Keine Familie" ist ein zulässiges Ergebnis.** Es wird nichts in eine Familie gezwungen. „Keine Treffer" ist ebenfalls zulässig und wird ohne erfundene Probleme ausgegeben.

## Autorität und Grenzen

- Findet und benennt. Schreibt nichts um, schafft keine Autorität, schreibt nicht in die Sammlung und nicht in Repo, Issues oder PRs.
- Jeder Treffer braucht ein Zitat. Ohne Beleg kein Treffer.
- Die Prüfung ist ein **Urteil, kein Beweis**.
- Keine Parallelskala, keine neue Ontologie: Familien- und Risiko-IDs des Repos.

## Abschluss

`complete` · `bounded` (mit Grund) · `unresolved` · `NOT EXECUTED` (mit Grund). Danach STOP.
