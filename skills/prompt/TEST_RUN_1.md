# Testlauf 1 (nicht Laufzeit)

**Datum:** 2026-09-30 · **Art:** Urteil, kein Beweis · **Fälle:** E-01, E-04, E-07, E-11 (von E-01 bis E-12; E-02, E-03, E-05, E-06, E-08 bis E-10, E-12 sowie F-01 bis F-06 bleiben `NOT EXECUTED`)

## Ausführung
Je Fall ein frischer Unterkontext eines Claude-Modells (Sonnet-Klasse), Skill-Dateien aus dem Repo gelesen, nichts geschrieben oder gepostet. Je Fall **ein Lauf**. Die Fallvorlagen hat dieselbe Instanz geschrieben, die den Skill gebaut hat. Bewertet hat dieselbe Instanz. Es gab **keinen Baseline-Lauf** ohne Skill.

## Ergebnis je Fall
| Fall | Erwartung (EVAL_CASES) | Ergebnis |
|---|---|---|
| E-01 | PQ-01, PQ-02, PQ-03 mit Zitat, keine Punktzahl | erfüllt. Zusätzlich Widerspruch „vollständig/kurz", fehlendes Ziel, fehlendes Berichtsformat. Verworfene Punkte genannt |
| E-04 | kurze Bewertung, keine Agent-Forderungen | **teilweise**. Keine Agent-Forderungen, Gesamturteil „gut". Aber vier Befunde in Tabelle plus Testvorschlag für eine Vermieter-Mail; ein Befund („Ton doppelt genannt") ist Füllmaterial |
| E-07 | andere Form, gleiche Semantik; kleines Modell mit Schema, Zitatpflicht, Stopp | erfüllt. Großes Modell: ein Prompt. Kleines Modell: Zerlegung in drei Nachrichten, feste Schemata, Stopp-Wiederholung, Warnung bei Missverhältnis, Modell als „nicht eingestuft" |
| E-11 | „nicht eingestuft", vorsichtig, Kalibrierungslauf, keine erfundene Eigenschaft | erfüllt |

## Befunde am Skill
1. **Überflaggen bei einfachen Prompts (E-04):** Der Review dosiert die Ausgabe nicht nach Prompt-Größe. Korrekturkandidat: bei Chat-Prompts Befunde auf wesentliche begrenzen.
2. **Uneinheitliche Atom-Nutzung:** In E-04 und E-01 lief `failure-pattern-check`. In E-11 (nur Erstellen) meldete der Lauf es als „nicht nutzbar", in E-07 wurde es nicht geladen. Die Regel „Atom spät, bei Review" ist in `.prompt` nicht eindeutig.
3. **Kosten der Zerlegung (E-07):** Drei Nachrichten statt einer. Der Lauf hat das offen als Preis benannt. Ob sie nötig ist, zeigt nur ein Kalibrierungslauf mit dem echten kleinen Modell.

## Belegstärke
Schwach. Ein Lauf je Fall, gleiche Modellfamilie wie der Autor, keine Baseline, Bewertung nicht unabhängig. Es zeigt: Die Anweisungen werden im Kern befolgt. Es zeigt nicht: dass der Skill gegenüber Prompts ohne Skill besser ist, und nichts zu OpenAI-Werkzeugen. Reifegrad bleibt `declared`.
