# Kernmethode (verpflichtend)

Diese Datei wird bei jeder Nutzung des Skills geladen. Sie beschreibt, **wie** `.prompt`, `.prompt review` und `.prompt test` arbeiten.

## A. Grundregeln

1. **Kleinste ausreichende Anweisung.** Kein Mega-Template, keine maximale Kompression. Nur Elemente, die die Aufgabe braucht.
2. **Fidelity vor Tokenersparnis.** Bedeutung, Unsicherheit und Autoritätsgrenzen dürfen nie zugunsten von Kürze verloren gehen.
3. **Unabhängig lesen, dann prüfen.** Zuerst den Prompt verstehen und Befunde aus dem Text bilden, erst danach Listen als Lückenprüfung nutzen. Listen sind keine Punktzahl.
4. **Jeder Befund trägt ein wörtliches Zitat** aus dem geprüften Text. Ohne Beleg kein Befund.
5. **Unsicherheit bleibt sichtbar.** Plausibel ist nicht belegt.
6. **Interner Review ist nicht unabhängig.** Grenze ausweisen.
7. **Keine Modellbehauptung ohne Kennzeichnung** als Annahme oder Quelle. Modelle, für die kein Profil vorliegt, sind „nicht eingestuft".
8. **Keine selbst erfundenen Begriffe oder Skalen.** Begriffe des Repos verwenden (Decision Brief, Fehlerfamilien, Kandidat, `declared`).

## B. `.prompt`: Erstellen

Erstellen ist eine **dünne Schicht**. Es gibt hier keine eigene Methode für Kontextauswahl oder Aufgabenkompilierung, weil diese Aufgaben bei BB-CONTEXT und Kandidat #55 liegen.

1. **Kontext klären** (siehe `skill.md`). Nur Fehlendes erfragen, Standardannahmen ausweisen.
2. **Ableiten vor Fragen.** Was sich aus dem Stand oder dem Repo ergibt, nicht vom Owner erfragen.
3. **Basis beschaffen:** Sind BB-CONTEXT oder #55 nutzbar, deren Ergebnis verwenden. Sind sie nicht nutzbar, arbeitet der Skill mit allgemeiner Fähigkeit und kennzeichnet den Entwurf als **Übergangslösung**.
4. **Bausteine wählen** (nur was nötig ist):
   - Ziel und Zweck; Kontext **per Verweis**, nicht als Wiederholung
   - Erfolgs- oder Abschlusskriterium
   - Scope und Nicht-Ziele, Verbote mit Begründung
   - Autoritätsgrenze (was der Ausführende nicht entscheiden darf)
   - erlaubte und nicht erlaubte Eingaben
   - Ausgabeformat; Regel für Unsicherheit („wenn Information fehlt, sage das")
   - bei Repo-Arbeit: **Zielrepository und Remote prüfen** und bei Abweichung stoppen
   - bei Lesen: **Lesemodus** (vollständig, Bereich, Suche, nur Metadaten) und Suchbudget
   - bei folgenreichen Schreibaktionen: **Freigabe-Gate** (erst lesen und entwerfen, nach Freigabe schreiben) und **Blocker-Regel** (bei Konflikt oder fehlendem Zugriff nichts schreiben, berichten, stoppen)
   - bei Review-Aufgaben: **Unabhängigkeitsbedingung** (frischer Kontext, kein Gedankengang des Schreibers) oder ausgewiesene Grenze
   - **Vorbedingungen** prüfen (z. B. Fallauswahl, Modellwahl), sonst Entwurf
   - **Stopp** am Ende
5. **Vorgegebene Hinweise neutral formulieren:** Fundort und Frage statt Ergebnisrichtung, mit Gegenprobe („eine widersprechende Stelle oder ‚keine gefunden'").
6. **An Modell und Umgebung anpassen** (Abschnitt E).
7. **Internen Review durchführen** (Abschnitt C), Befunde einarbeiten. Dabei gilt die Regel zum Atom aus C (Schritt 2a) und die Dosierung aus C (Schritt 3a). Das Atom `failure-pattern-check` liegt im selben Repo unter `skills/failure-pattern-check/` und ist nutzbar. „Nicht nutzbar" gilt nur für BB-CONTEXT und #55 (Schritt 3).
8. **Ausgeben:** vollständiger Prompt, kurze Annahmenliste, Hinweis „intern geprüft, ungetestet (`declared`)", Kostenhinweis.

## C. `.prompt review`: Prüfen

1. **Unabhängige erste Lesart.** Was will der Prompt? Befunde mit Zitat sammeln, ohne Checkliste.
2. **Späte Lückenprüfung:**
   a) Skill `failure-pattern-check` auf den Prompt anwenden (Fehlerfamilien des Repos). **Regel:** anwenden bei Agent-, Code-, schreibenden, mehrphasigen oder Repo-Prompts, und wenn die Fehlerkosten nicht niedrig sind. **Entfällt** bei einem einfachen Chat-Prompt (eine Aufgabe, nur Text, niedrige Fehlerkosten); dann ausweisen: „Fehlerfamilien-Prüfung nicht angewendet: einfacher Chat-Prompt". Gilt im Modus `.prompt` (interner Review) wie in `.prompt review`. Ist die Sammlung nicht lesbar: Zustand `bounded` mit Grund.
   b) Prompt-Formkriterien (Abschnitt C.1) als Fragen an den Text.
3. **Befund-Format:** Zitat · Problem · mögliche Folge · Änderungsvorschlag · **Art** (`deterministic`, `procedural`, `judgement`) · Sicherheit (hoch, mittel, niedrig, mit Grund). „Keine Familie" ist zulässig.
3a. **Dosierung:** Der Umfang folgt der Größe des Prompts und den Fehlerkosten. Bei einem einfachen Chat-Prompt höchstens die 2–3 wesentlichen Befunde, als kurze Liste statt Tabelle. Keine Füllbefunde (Harmloses, Stilfragen, bereits Gutes als Mangel). Testvorschlag nur bei Bedarf. Bei Agent- oder Repo-Prompts gilt der volle Umfang.
4. **Gesamturteil:** der Zustand (`complete`, `bounded`, `blocked`, `unresolved`, `needs-decision`) und **ein Satz** in Worten: „gut", „mit Vorbehalt" oder „so nicht einsetzen", mit den wichtigsten 3–5 Gründen.
   **Prognose:** „Was passiert, wenn der Prompt so eingesetzt wird?" (als Prognose gekennzeichnet, nicht als Test).
5. **Stärken** kurz nennen, damit sie beim Überarbeiten erhalten bleiben.
6. **Verbesserte Fassung** vollständig und kopierfertig, dazu **Änderungsliste** (geändert / bewusst unverändert).
7. **Testvorschlag:** 1–2 Fälle mit bekanntem Ergebnis für eine frische Sitzung.
8. **Kosten- und Limithinweise.**

### C.1 Prompt-Formkriterien (Fragen an den Text)

**Immer:** Ist die Aufgabe benannt? Sind Zweck und Kontext geliefert? Gibt es Ziel und Erfolgskriterium? Sind Regeln positiv oder begründet formuliert? Sind Anweisung, Kontext, Daten, Beispiele getrennt? Ist das Ausgabeformat festgelegt? Ist Unsicherheit erlaubt? Sind Beispiele mehrere, vielfältig und als Beispiel markiert (ein Einzelbeispiel wird sonst kopiert)? Ist die Aufgabe zerlegt, wenn sie zu groß ist? Ist eine Rolle nur gesetzt, wo sie wirkt? Sind Länge und Wiederholung angemessen? Gibt es Widersprüche (auch Mengen- und Zahlenwidersprüche, z. B. „minimal" bei sehr vielen Feldern)? Überwiegen Verbote? Gibt es unbegründete Tricks oder Druckformulierungen? Bei Quellenarbeit: Sind Belege vor Argumenten verlangt? Ist ein Test vorgesehen, mit einer Änderung pro Durchlauf?

**Zusätzlich bei Agent/Code:** Freigabe-Gate? Blocker-Regel? Begrenzter Lesescope mit Lesemodus? Suchbudget? Duplikat- und Zuständigkeitscheck vor Neuanlage? Hinweise neutral mit Gegenprobe? Wörtliche Zitate als Fundstelle? Keine erzwungene Mehrdeutigkeit? Schließbare Arbeitseinheiten, benannte Reihenfolge und Verlinkung? Selbstprüfung von unabhängiger Prüfung getrennt, Grenze ausgewiesen? Herkunftszeile für erzeugte Texte? Neue Begriffe oder Skalen markiert? Verweis auf Projektregeln (z. B. `AGENTS.md`, `CLAUDE.md`) statt Wiederholung? Zielrepository geprüft? Stopp am Ende? Berichtsformat vorgegeben? Entwurf statt Ersatzhandlung bei fehlender Schreibmöglichkeit?

### C.2 Anhangbausteine (auf Wunsch kopierfertig)

Der Owner kann diese Bausteine an einen bestehenden Prompt anhängen. Jeder Baustein steht für sich:

- **Freigabe-Gate:** „Führe nur Phase 1 aus (nur lesen, Entwurf, Bericht). Schreibe nichts in Repo, Issues oder PRs. Danach STOP und auf meine ausdrückliche Freigabe warten. Phase 2 nur nach Freigabe."
- **Blocker-Regel:** „Bei belegtem Branch, konkurrierendem Schreiber, geänderter Lage, fehlendem Schreibzugriff oder nicht zugänglicher Schlüsselquelle: nichts schreiben, Befund berichten, STOP. Nicht auf anderen Branch oder Pfad ausweichen."
- **Suchbudget und Lesemodus:** „Höchstens 3 gezielte Suchrunden je Teilfrage, danach `unresolved` mit Begründung. Nenne je Quelle den Lesemodus (vollständig, Bereich, Suche, nur Metadaten) und bei Bereich oder Suche Scope bzw. Suchbegriffe."
- **Hinweise als Hinweise:** „Die genannten Vorbeobachtungen sind Hinweise, keine erwarteten Ergebnisse. Belege jeden Befund mit eigenem wörtlichen Zitat und nenne eine widersprechende Stelle oder ‚keine gefunden'. Weise aus, wo du einem Hinweis nicht folgst."
- **Zielprüfung:** „Prüfe vor der ersten Aktion Zielrepository und Remote. Weicht etwas ab, stoppe und berichte."
- **Vorab-Selbstcheck:** „Nenne in höchstens 5 Zeilen, wo dieser Auftrag widersprüchlich, unklar oder in einem Lauf nicht ausführbar ist, und wie du damit umgehst. Beginne danach."
- **Unabhängigkeitsgrenze:** „Dies ist eine interne Prüfung im selben Kontext. Weise aus, dass sie nicht unabhängig ist."

### C.3 Typische Prompt-Fehler und Fehlerfamilien (abgeleitet, nicht maßgeblich)

Maßgeblich ist `tests/evals/failure_corpus.json`. Diese Zuordnung ist eine abgeleitete Hilfe:

| Fehler | Familie |
|---|---|
| Anker durch Ergebnisrichtung | Epistemische Integrität |
| fehlendes Gate vor Schreibaktionen | Autoritäts-/Promotionskriechen |
| offener Lesescope, nicht nachprüfbare Tiefe | Falsche Absicherung |
| interne Widersprüche | keine Familie (formspezifisch) |
| Mega-Prompt, Wiederholung, Verbotsdichte | Solutionismus/Überformung, Ausführung/Fortschritt |
| nicht schließbare Arbeitseinheiten | Ausführung/Fortschritt |
| neue Begriffe, Parallelskalen | Epistemische Integrität, Überformung |
| falsches Ziel (Repository nicht geprüft) | Ausführung/Fortschritt, Autorität (nächste Passung) |
| Missverhältnis Komplexität zu Modell/Umgebung | Ausführung/Fortschritt |
| Unabhängigkeits-Overclaim | Falsche Absicherung |
| Checkliste als Punktzahl | Falsche Absicherung |
| Autoritäts-Laundering („vom Owner übernommen" ohne Beleg) | Autoritätskriechen |

## D. `.prompt test`: Testen

**Urteil, kein Beweis.** Im Repo bedeutet „Test" meist deterministisch; dieser Modus liefert ein Urteil und sagt das.

1. **Ergebnis gegen Auftrag:** Sind die verlangten Ausgaben da? Sind Behauptungen belegt? **Wurde tatsächlich ausgeführt, was behauptet wird** (z. B. Recherche, Tool-Aufrufe)? Autoritätsgrenzen eingehalten? Stopp eingehalten? Fehlerfamilien (Skill `failure-pattern-check`, spät).
2. **Testlauf (nur auf Wunsch):** Den Prompt in einem **frischen Kontext** ausführen. Nur wenn die Umgebung das kann. Sonst `NOT EXECUTED` mit Grund. Nicht zwischen gültigen Erstläufen nachbessern, ein nachgebesserter Prompt ist ein neuer Lauf.
3. **Testbericht:**
   - **Art je Befund:** `deterministic` (softwareprüfbar, z. B. Pflichtfelder, Zitat vorhanden, Stopp vorhanden), `procedural`, `judgement`
   - **Ausführungsangaben:** Modell, Modus, Denkstufe; frischer Kontext ja/nein; unabhängig ja/nein; Rohausgabe vor der Bewertung gesichert ja/nein; tatsächlich ausgeführt ja/nein
   - **Belegstärke:** Ein einzelner Lauf mit einem Modell ist kein robuster Beleg.
   - **Kosten:** Testläufe verbrauchen Limits. Ein Vergleich über mehrere Modelle nur auf Anforderung und mit Kostenhinweis.

## E. Anpassung an Modell und Umgebung

**Dimensionen:** Detailgrad der Anweisung · Aufgabengröße je Lauf · Ausgabeschema · Nachweispflicht (wörtliches Zitat) · Wiederholung der Stopp-Regel · Anzahl der Beispiele · Art der Selbstprüfung (externe Checkliste statt eigener Reflexion) · Enge der Tool-Führung.

**Stufen als Orientierung, nicht als Tatsache über ein Modell:**
- **stärker:** Ziel und Begründung genügen, Wiederholungen meiden, mehrere Phasen in einem Prompt möglich
- **klein/schnell:** ein Schritt pro Prompt, festes Schema, mehr Beispiele, wörtliche Zitate verlangen, Stopp-Regeln wiederholen, externe Checkliste, Tool-Schritte eng führen

**Zuordnung:** Nur was in `references/execution-profiles/` für das Modell steht. **Ohne Profil gilt „nicht eingestuft":** vorsichtige Vorgaben (kleine Schritte, Schema, Zitate), Hinweis und Vorschlag eines Kalibrierungslaufs (derselbe Fall, ein Lauf).

**Warnung bei Missverhältnis:** Ist die Prompt-Komplexität für Modell oder Umgebung zu hoch (z. B. mehrphasiger Audit für ein kleines, schnelles Modell), Zerlegung oder anderes Modell vorschlagen.

**Master und Varianten:** Ein vollständiger Prompt, Varianten für andere Modelle daraus ableiten statt neu schreiben.

**Umgebung:** Chat (Mensch im Loop, Text als Ergebnis, geringeres Risiko) · Code/Agent (echte Aktionen, zusätzliche Bausteine aus B.4). Siehe Profile.

## F. Kosten und Limits

Relative Kosten (niedrig, mittel, hoch) mit Hauptgrund; 2–3 Sparvorschläge, konkret zum Prompt; „Nicht sparen bei". Mögliche Hebel: Modell je Teilaufgabe wählen; Phasen-Gate als Schutz vor teuren Korrekturrunden; gezielt lesen statt pauschal (mit Lesemodus); dauerhafte Regeln in Projektdateien statt im Prompt; kurze Ausgabeformate; frische Sitzung mit Übergabe statt sehr langem Kontext; Unteragenten nur für unabhängige Prüfung. Keine Zahlen zu Tokens oder Limits. Routing und Modellwahl gehören zu Kandidat #48, hier nur anbinden.

## G. Feedback an eine andere KI

Konkret und nummeriert; was behalten, was ändern; Begründung mitgeben; Änderungsliste verlangen; kopierfertig.

## H. Grenzen

Keine PASS- oder OK-Aussage über Prüfungen, die nicht gelaufen sind. Keine Sparempfehlung, die Gate, Quellenlektüre mit Belegfunktion, Gegenprobe oder unabhängige Prüfung entfernt. Keine Modellbehauptung ohne Kennzeichnung. Kein Schreiben in Repo, Issues oder PRs. Kein Orchestrator, kein Planer.
