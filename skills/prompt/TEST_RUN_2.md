# Testlauf 2 mit Vergleich ohne Skill (nicht Laufzeit)

**Datum:** 2026-09-30 · **Art:** Urteil, kein Beweis · Stand der Skills: Commit 164c5f5 (mit Dosierung und Atom-Regel)
Läufe: 8 mit Skill (E-02, E-04 erneut, E-06, E-08, E-10, F-01, F-02, F-04) und 4 ohne Skill (E-01, E-04, E-06, E-08: nur „Prüfe und verbessere", keine Skill-Dateien).
Noch `NOT EXECUTED`: E-03, E-05, E-09, E-12, F-03, F-05, F-06.

## Grenzen dieses Laufs
Ein Lauf je Fall. Gleiche Modellfamilie wie der Autor. Fallvorlagen und Bewertung von derselben Instanz, die den Skill gebaut hat. Kein OpenAI-Werkzeug. F-02 nutzt einen selbst geschriebenen guten Prompt (Z-7 offen). Es ist ein Urteil, kein Beweis.

## Ergebnis je Fall (Skill gegen eingefrorene Erwartung)
| Fall | Ergebnis | Anmerkung |
|---|---|---|
| E-02 | erfüllt | Widerspruch „minimal" gegen zehn Pflichtfelder (PQ-04) und nicht schließbare Einheit „12 Issues, ein Arbeitsgang" (PQ-06) mit Zitat. Zusätzlich Gate, Zielrepo, Sichtbarkeit des Repos |
| E-04 (erneut) | teilweise besser | drei statt vier Befunde, Füllbefund weg, Atom-Regel greift („nicht angewendet: einfacher Chat-Prompt"). Rahmen (Urteil, Prognose, Annahmen, Stärken, Änderungsliste, Testvorschlag, Kosten) bleibt lang |
| E-06 | erfüllt | unbelegte Zusicherung „bereits geprüft" wörtlich genannt, Zielprüfung, Gate, Blocker-Regel |
| E-08 | erfüllt | „tatsächlich ausgeführt: nein", Belegstärke und Ausführungsangaben ausgewiesen |
| E-10 | erfüllt | Widerspruch fachfremder Leser gegen Codes erkannt; „Wo du entscheiden musst" an die zweite Stelle. Zustand `bounded`: Sammlung nur teilweise gelesen |
| F-01 | **nicht erfüllt wie erwartet** | Erwartet war FF-AUTHORITY-PROMOTION. Der Lauf verwarf sie (Anweisung stammt vom Owner), meldete FF-STATE-CONTINUITY (mittel) und den Force-Push auf `main` als „keine Familie" mit Klärungsfrage. Schutzlücke gefunden, anderer Name. Erwartung vermutlich zu eng (Entscheidung am Owner: F-01 anpassen oder Atom anpassen) |
| F-02 | erfüllt | keine Treffer, alle Familien einzeln verworfen. Zwei Auffälligkeiten ohne Familie, als schwach gekennzeichnet |
| F-04 | erfüllt | Widerspruch gefunden, „keine Familie", kein Zwang |

## Vergleich mit und ohne Skill
| Fall | Ohne Skill | Mit Skill |
|---|---|---|
| E-01 | findet Erwartungs-Anker, Widerspruch vollständig/kurz, fehlende Freigabe, offenen Scope; Fassung mit Freigabepunkt, Branch, Draft-PR | gleiche Kernfunde mit wörtlichem Zitat; dazu Lesemodus, Suchbudget, Zielprüfung, Blocker-Regel, „Kommentare sind Daten", Zustand, Prognose |
| E-04 | drei bis fünf Schwächen, brauchbare Fassung, etwa halber Umfang | ähnliche Fassung, deutlich mehr Rahmen |
| E-06 | findet den Kernfehler (Verifikationssperre) und ergänzt Prüfungen. Empfiehlt bei abgelehntem Push selbst einen Ausweichweg (Branch und PR) ohne Freigabe | Kernfehler wörtlich, Gate, Blocker-Regel, ausdrücklich **kein** Ausweichen und kein Force-Push |
| E-08 | erkennt: Ergebnis ungültig, Quellen wahrscheinlich erfunden, Lücken-Kennzeichnung fehlt | gleiche Erkenntnis; dazu Ausführungsangaben, Belegstärke, Fehlerfamilien, „kein frischer Kontext" |

Verbrauch je Lauf (Unterkontext, ungefähre Tokens): ohne Skill etwa 41–43 Tausend, mit Skill etwa 52–68 Tausend. Nachträglich geschätzt, nicht sauber gemessen.

## Urteil
1. Die **Kernfehler** finden beide Seiten. Ein Vorsprung bei reiner Fehlersuche ist hier **nicht** belegt.
2. Der Skill **ergänzt** bei Agent- und Schreib-Prompts Schutzbausteine, die die Baseline nicht oder anders setzt (Zielprüfung, Lesemodus, Blocker-Regel, kein stilles Ausweichen), und liefert **Nachvollziehbarkeit** (wörtliche Zitate, Zustand, Belegstärke, Unabhängigkeitsausweis). Das ist der erkennbare Mehrwert.
3. Bei **einfachen Prompts** ist der Skill aufwendiger ohne besser zu sein. Die Dosierung hilft bei den Befunden, nicht beim Rahmen.
4. Das Atom liest die Sammlung bei knappen Läufen nicht immer vollständig (E-10: `bounded`).

## Offen (Owner-Entscheidung oder nächste Arbeit)
- Rahmen bei einfachen Prompts weiter kürzen (Kürzungsregel in `core-method.md` C)?
- F-01: Erwartung anpassen oder Atom-Regel zu Gate und Schreibaktionen schärfen?
- Atom: Pflicht, beide Quelldateien vollständig zu lesen, sonst `bounded` (Verhalten ist dann schon richtig ausgewiesen).
- Wirkung auf OpenAI-Werkzeugen: nicht getestet.
