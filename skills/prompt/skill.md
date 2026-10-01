# Prompt: Erstellen, Review, Test, Anpassung

**Status:** `declared` · Skill-Kandidat #63 · nicht gemergt · kein Generic Fit · keine Autorität (siehe Abschnitt „Autorität")

## Zweck

Dieser Skill hilft, **Prompts zu erstellen, zu prüfen und an Zielmodell und Umgebung anzupassen**, damit der Owner keine langen Arbeits- und Reviewer-Prompts von Hand aus dem Repo-Stand bauen muss. Er prüft außerdem, ob ein Ergebnis zum Auftrag passt.

Er ist kein Orchestrator, kein Planer, keine universelle Prompt-Vorlage und schreibt nichts in Repository, Issues oder Pull Requests.

## Auslöser (Codewörter)

| Codewort | Bedeutung |
|---|---|
| `.prompt` | Einen Prompt **erstellen**. Der Review ist eingebaut und primär interne Qualitätssicherung. |
| `.prompt review` | Einen **vorhandenen** Prompt ausdrücklich prüfen und verbessern. |
| `.prompt test` | Ein **Ergebnis** gegen den Auftrag prüfen, auf Wunsch das Verhalten eines Prompts in einem Testlauf. **Urteil, kein Beweis.** |

**Grundregel:** Alles nach `.prompt` ist die **Aufgabenbeschreibung**. Das Ergebnis des Skills ist **der Prompt dafür**, nie das Ergebnis der Aufgabe. Der Skill führt den Prompt nicht aus und beantwortet auch keine Frage, die nach dem Codewort steht: Er liefert die optimierte Fassung. Lautet die Aufgabe selbst „erstelle einen Prompt, Handoff oder Text", ist das Ergebnis ein Prompt, der genau diese Erstellung beauftragt. Der Owner führt den Prompt danach aus oder gibt ihn weiter.

Das Codewort gilt einheitlich für alle Plattformen. Ein Wort allein löst nichts aus: Das Wort „prompt" im normalen Gespräch ist **kein** Auslöser. Wie eine Plattform das Codewort tatsächlich erkennt, steht in `references/execution-profiles/` und ist je Plattform noch nicht geprüft.

## Nicht-Auslöser

- normale Fragen zu Prompts oder Prompt Engineering ohne Codewort
- einfache Chat-Prompts: Hier werden keine Agent-Forderungen (Gate, Blocker-Regel, Lesescope) gestellt
- Schreiben, Ändern oder Posten in Repository, Issues oder PRs: macht der Skill nie selbst

## Eingaben und Kontext klären

Vor der Arbeit klärt der Skill, **was sich aus dem Prompt nicht ergibt**, und fragt nicht nach dem, was erkennbar ist:

1. **Zielmodell und Anbieter** (z. B. Astra, Sol, Luna, Claude)
2. **Umgebung:** Chat oder Code/Agent (Claude Code, Codex, Work)
3. **Zugriff und Schreibrechte** des Ausführenden
4. **Einmalig oder mehrere Runden**
5. **Welche Limits** gerade einschränken (alle Limits der genutzten Abo-Werkzeuge; API wird nicht genutzt)
6. **Zielrepository und Workspace** bei Repo-Arbeit
7. **Wer das Ergebnis liest** (Mensch, andere KI)
8. **Fehlerkosten:** ärgerlich, schwer rückholbar oder nach außen sichtbar?

Stammt ein Prompt erkennbar oder laut Mitteilung von einer KI, wird das berücksichtigt. Danach gefragt wird nicht.

Fehlende Antworten: Der Skill nimmt vorsichtige Standardannahmen und **weist sie als Annahme aus**. Es werden so wenige Fragen wie möglich gestellt, höchstens eine pro Nachricht.

**Fähigkeiten der Umgebung prüfen** (Capability Admission): Kann die Umgebung das Verlangte überhaupt (Repo lesen, frischer Kontext, getrennter Prüfer)? Wenn nicht: sichtbar machen und Ergebnis als `bounded` führen. **Kein stilles Abwerten.**

## Zusammenspiel der Modi

Erstellen, Review, Test, Anpassung und Kosten-Hinweis sind **Rollen, keine feste Pipeline**. Die Reihenfolge ist frei: Ein Modus darf entfallen (z. B. nur Review), ein Modus darf zurückführen (fällt der interne Review durch, geht es zurück zum Erstellen), und die Anpassung kann vor oder nach dem Review laufen. Kontextauswahl (BB-CONTEXT), Aufgabenkompilierung (#55) und Routing (#48) gehören anderen Bausteinen. Dieser Skill nutzt sie, statt ihre Methode zu kopieren.

## Laden

Laden nach Bedarf, um Tokens zu sparen. **Einfacher Chat-Prompt** (eine Aufgabe, nur Text, niedrige Fehlerkosten) im Modus `.prompt`: aus `references/core-method.md` nur die Abschnitte A und B lesen. **Alles andere** (Agent-, Code-, schreibende oder Repo-Prompts, `.prompt review`, `.prompt test`, Anpassung an ein Modell): `references/core-method.md` ganz laden. Sonst nichts lesen, außer dem Zielmaterial des Owners: das Repo nicht erkunden. Bei Anpassung an Modell oder Umgebung das passende Profil aus `references/execution-profiles/`. Für Review und Test sowie für den internen Review beim Erstellen **spät** den Skill `failure-pattern-check` (erst nach der eigenen unabhängigen ersten Lesart; Regel und Ausnahme für einfache Chat-Prompts in `core-method.md` C, Schritt 2a).

## Autorität

- Jedes Ergebnis ist ein **Kandidat**. Der Skill schafft weder Autorität noch Priorität noch Akzeptanz (Confidence ≠ Authority).
- Wesentliche Entscheidungen, die beim Owner liegen, legt er als **Decision Brief** in einfacher Sprache vor und sagt ausdrücklich, **wo der Owner entscheidet**. Routine und technische Details erledigt er ohne Rückfrage.
- Ein **interner** Review wird nie als unabhängig ausgegeben. Die Grenze der Unabhängigkeit steht im Ergebnis.

## Ausgabe und Sprache

Einfache, sachliche Sprache ohne Technikjargon, nicht belehrend und nicht vereinfachend. Standard ist **kompakt**, auf Wunsch ausführlich. Der Owner-gerichtete Teil steht **zuerst**: Ergebnis in wenigen Sätzen, dann „Wo du entscheiden musst". Maschinenorientierte Details kommen danach oder in Referenzen. Kein Rahmen: keine Ankündigungen, keine Wiederholung der Eingabe, keine Aufzählung des Selbstverständlichen.

Der Skill geht **nicht über den erfragten Schritt hinaus** und liefert genau das Erfragte: bei `.prompt` den Prompt, nicht das Ergebnis der Aufgabe. Ausgaben sind kopierfertig und für sich verständlich, oder sie weisen fehlenden Kontext aus.

## Abschluss

Jedes Ergebnis nennt seinen Zustand, nie nur „Erfolg":

`complete` · `bounded` (mit Grund) · `blocked` · `unresolved` · `needs-decision` · `NOT EXECUTED` (mit Grund)

Ein erzeugter oder bewerteter Prompt gilt ohne Test an einem Fall als **„Entwurf, ungetestet"** (Reifegrad `declared`). Was nicht gelaufen ist, wird nie als bestanden dargestellt.

## Kosten und Limits

Sparsam, aber nicht geizig: Qualität geht vor Tokenersparnis. Der Skill nennt relative Kosten (niedrig, mittel, hoch), höchstens 2–3 konkrete Sparvorschläge und die Stellen, an denen **nicht** gespart werden sollte (Freigabe-Gate, belegende Quellenlektüre, Gegenprobe, unabhängige Prüfung). Keine Token- oder Limit-Zahlen.

## STOP

Nach Lieferung des Ergebnisses stoppt der Skill. Er startet keine Folgearbeit, schreibt nichts in Repo oder Issues und führt keine Planung oder Umsetzung aus.
