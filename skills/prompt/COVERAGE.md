# Abdeckungsliste Version 1 (nicht Laufzeit)

**Stand:** 2026-09-30 · Branch-Stand, nicht gemergt · Kandidat #63 (mit #65)
**Grundlage:** Anforderungsbasis in #63 (Kommentar `5918364422`) und Präzisierung (Kommentar `5919129851`). Jede **bestätigte** Anforderung hat hier einen Status. Nichts fällt still weg.

**Bedeutung der Status**
- `umgesetzt`: als Anweisung im Paket enthalten. **Das Verhalten ist nicht getestet** (Reifegrad `declared`).
- `teilweise`: Teil umgesetzt, Rest mit Grund offen oder zurückgestellt.
- `zurückgestellt`: bewusst nicht in Version 1, mit Grund.
- `kein Auftrag`: Entscheidung oder Freigabe, keine Anforderung an den Skill.

Orte: **S** = `skills/prompt/skill.md` · **K** = `skills/prompt/references/core-method.md` · **P** = `skills/prompt/references/execution-profiles/` · **A** = `skills/failure-pattern-check/` · **E** = `skills/prompt/EVAL_CASES.md`

## 1. Owner-Aussagen

| ID | Anforderung (kurz) | Status | Ort | Hinweis |
|---|---|---|---|---|
| O-1 | generische Prinzipien, situativ differenzieren | umgesetzt | K A, C.1, E | |
| O-2 | beim Erstellen nach Konzeptphase strukturiert statt unstrukturiert | umgesetzt | K B | |
| O-3 | Skills, die das automatisierte Erstellen von Prompts prüfen oder unterstützen; allgemein | umgesetzt | S Zweck; K B, C | |
| O-4 | Kontext abfragen: Modell, Chat oder Code/Codex, Claude und ChatGPT | umgesetzt | S Kontext klären; P | |
| O-5 | tokensparend, nicht geizig, Sparvorschläge, besonders Code, Claude, Codex, Work | umgesetzt | S Kosten; K F; P agent-code | |
| O-6 | differenzieren: detaillierter oder andere Anforderungen je Modell | umgesetzt | K E | |
| O-7 | Modelle (Opus, Haiku, Sol, Luna) | umgesetzt, ersetzt | P openai | ersetzt durch L-7 |
| O-8 | ohne zu vereinfachen; alle Anforderungen; keine KI-Phänomene | teilweise | diese Datei; A; K A.8, C.3 | Spannung „ohne zu vereinfachen" gegen „kompakt" bleibt offen (Standard kompakt, auf Wunsch ausführlich) |
| O-9 | nicht wie ein Kind behandeln | umgesetzt | S Ausgabe und Sprache | |
| O-10 | keine technische Kompetenz vorausgesetzt | umgesetzt | S Ausgabe und Sprache | |
| O-11 | Grenzen, die der Owner entscheidet | umgesetzt | S Autorität | Decision Brief; sagt, wo der Owner entscheidet |
| O-12 | im Repo verankert, plattformunabhängig, `.prompt`, `.prompt review`, Review Teil der Erstellung, interne QS | teilweise | S Auslöser; K B.7; P | Im Repo: ja (Branch). Erkennung des Codeworts je Plattform: zurückgestellt (Z-1) |
| O-13 | modular und organisch; prüfen, wo Module neue Kompositionen finden | teilweise | zwei Pakete; S Zusammenspiel | Überschneidungstest erledigt (Kommentare in #63, #65, #55, #48). Kompositionsprüfung mit weiteren Nutzern offen (Z-5) |
| O-14 | Adaptivität: was braucht das Modell | umgesetzt | K E; P | |
| O-15 | Entscheidung 1: Kandidat festhalten | kein Auftrag | #63 | festgehalten |
| O-16 | Entscheidung 2: Option A | kein Auftrag | K B | Erstellen als dünne Schicht |
| O-17 | Bericht für den Menschen; wo entscheiden | umgesetzt | S Ausgabe und Sprache | „Wo du entscheiden musst" zuerst |
| O-18 | nicht vorgreifen | umgesetzt | S Ausgabe und Sprache | |
| O-19 | genau das Erfragte liefern | umgesetzt | S Ausgabe und Sprache | |

## 2. Spätere Owner-Antworten (Kommentar `5919129851`)

| ID | Anforderung | Status | Ort | Hinweis |
|---|---|---|---|---|
| L-1 | „Work" ist ein Coding-Chatmodus von OpenAI | umgesetzt | P openai, agent-code | |
| L-2 | alle Limits, keine API-Optionen | umgesetzt | S Kontext, Kosten; P agent-code | **kein API-Profil angelegt**, bewusst |
| L-3 | „keine KI-Phänomene" = Fehlmuster des Repos aktiv vermeiden | umgesetzt | A; K A.8, C.3 | Sammlung `failure_corpus.json` ist einzige Quelle |
| L-4 | Codewort `.prompt` einheitlich | umgesetzt | S Auslöser | `/prompt` ist nicht Teil des Kerns |
| L-5 | `.prompt test` als Sub-Modus, Urteil kein Beweis | umgesetzt | S; K D | |
| L-6 | Fehlmuster-Prüfung als eigener Baustein (Atom) | umgesetzt | A | Kandidat #65 |
| L-7 | Modelle Astra, Sol, Luna | teilweise | P openai | Inhalte **nicht gegen OpenAI-Dokumentation geprüft** (Z-2) |

## 3. Abgeleitete Anforderungen

| ID | Anforderung (kurz) | Status | Ort | Hinweis |
|---|---|---|---|---|
| D-1 | prüft Prompts und unterstützt das Erstellen; beide Modi | umgesetzt | S Auslöser; K B, C | |
| D-2 | allgemein einsetzbar, nicht projektgebunden | teilweise | S | Kern allgemein. Musterquelle von A ist die Sammlung des Host-Repos |
| D-3 | generische Prinzipien, situative Unterschiede ausweisen | umgesetzt | K A, C.1, E | |
| D-4 | beim Erstellen strukturiert | umgesetzt | K B | |
| D-5 | Qualitätsbewertung eines Prompts | umgesetzt | K C.4 | Gesamturteil: Zustand und ein Satz |
| D-6 | berücksichtigt, ob ein Prompt KI-erzeugt ist | umgesetzt | S Eingaben | fragt nicht danach |
| D-7 | Prognose bei unverändertem Einsatz | umgesetzt | K C.4 | als Prognose gekennzeichnet |
| D-8 | Feedback für die erzeugende KI | umgesetzt | K G | |
| D-9 | funktioniert ohne Entstehungs-Chat | umgesetzt | S Ausgabe und Sprache | |
| D-10 | Test-/Review-Bausteine anhängbar | umgesetzt | K C.2 | |
| D-11 | vollständiger Prompt, nicht nur Änderungen | umgesetzt | K C.6 | |
| D-12 | Folgeprompts auf Anforderung | umgesetzt | K B | |
| D-13 | Codewort als Auslöser | umgesetzt | S Auslöser | |
| D-14 | Review Teil der Erstellung, interne QS | umgesetzt | K B.7 | als „intern" ausgewiesen |
| D-15 | Zielmodell und Umgebung abfragen | umgesetzt | S Kontext klären | |
| D-16 | Anbieterunterschiede Claude/OpenAI | umgesetzt | P | Inhalte ungeprüft |
| D-17 | Anpassung an Modell und Umgebung | umgesetzt | K E | |
| D-18 | berücksichtigte Modelle | teilweise | P openai, claude | Claude-Modelle: keine Einordnung, „nicht eingestuft" (Z-2) |
| D-19 | plattformunabhängig, im Repo | teilweise | Paket; P | Kern neutral, auf Branch. Plattform-Erkennung und Träger je Plattform offen (Z-1, Z-3) |
| D-20 | möglichst tokensparend, nicht geizig | umgesetzt | S Kosten; K F | |
| D-21 | aktive Sparvorschläge | umgesetzt | K F | |
| D-22 | einfache Sprache, nicht kindlich, nicht vereinfachend | teilweise | S Ausgabe und Sprache | Spannung bleibt offen |
| D-23 | Decision Brief, wo der Owner entscheidet | umgesetzt | S Autorität | |
| D-24 | nicht über den erfragten Schritt hinaus | umgesetzt | S Ausgabe und Sprache | |
| D-25 | kopierfertig, für sich verständlich | umgesetzt | S Ausgabe und Sprache | |
| D-26 | modular, organisch, freie Reihenfolge, Re-Entry, Auslassung | umgesetzt | S Zusammenspiel | zwei Pakete |
| D-27 | keine selbstgeprägten Begriffe; Kriterien am Text beobachtbar | umgesetzt | K A.8 | |

## 4. KI-Vorschläge (unbestätigt), gruppenweise

Diese Vorschläge sind keine bestätigten Anforderungen. Sie sind übernommen, wo sie aus Repo-Regeln oder echten Fehlerfällen stammen.

| ID | Gruppe | Status | Ort | Hinweis |
|---|---|---|---|---|
| KV-1 | Kontextabfrage (Limit, Zugriff, einmalig/iterativ, Fehlerkosten, Leser, Standardannahmen, nicht nachfragen bei Erkennbarem, Zielrepository) | umgesetzt | S | |
| KV-2 | allgemeine Prüfkriterien | umgesetzt | K C.1 | Lückenprüfung, keine Punktzahl |
| KV-3 | Agent/Code-Kriterien | umgesetzt | K C.1, C.2; P agent-code | |
| KV-4 | Differenzierung (Stufen, Dimensionen, Warnung, Zerlegung, datierte Anbieterhinweise, Kalibrierungslauf) | umgesetzt | K E; P | API-Profil entfällt (Owner) |
| KV-5 | Kosten | umgesetzt | S; K F | |
| KV-6 | Ausgabe (Zustände, Annahmen, Befunde mit Zitat, Stärken, Änderungsliste, Testvorschlag, Feedback, kompakt) | umgesetzt | S; K C, G | |
| KV-7 | Aufbau (knappe Hauptdatei, Referenzen, Trigger) | umgesetzt | Paket | „Entwurf vor Ablage" durch Freigabe erledigt |
| KV-8 | Test (nichts „geprüft" ohne Test, Eval-Fälle, NOT EXECUTED) | teilweise | S Abschluss; E | Verhaltenstests **nicht ausgeführt** (Z-4) |
| KV-9 | Grenzen (keine Modellbehauptung ohne Kennzeichnung, kein PASS ohne Lauf, keine schädliche Sparempfehlung) | umgesetzt | K H | |

## 5. Bewusst zurückgestellt oder offen

| ID | Punkt | Grund |
|---|---|---|
| Z-1 | Erkennung des Codeworts je Plattform (ChatGPT, Work, Codex, Claude) | Test auf der Plattform nötig |
| Z-2 | Modelleinordnung (Astra, Sol, Luna gegen OpenAI-Dokumentation; Claude-Modelle) | Information fehlt, Quellen nicht lesbar |
| Z-3 | technischer Träger je Plattform (Kopfdaten, Dateiname) | spätere Entscheidung (#52 §39) |
| Z-4 | Verhaltenstests E-01 bis E-12 und F-01 bis F-06 | nicht ausgeführt (`NOT EXECUTED`) |
| Z-5 | Überschneidung mit #55 und BB-CONTEXT im Verhalten | beide nicht als Laufzeit verfügbar |
| Z-6 | Ergebnisprüfung: Abgrenzung zu #55, BB-ASSURE, Trial-Protokoll #46 | Zuständigkeit offen |
| Z-7 | ein vom Owner als gut bewerteter Repo-Prompt für E-03 | fehlt |
| Z-8 | Spannung „ohne zu vereinfachen" gegen „kompakt" | Owner-Entscheidung |

## 6. Wie diese Liste geprüft wurde

Strukturprüfung: Jede ID O-1 bis O-19, L-1 bis L-7 und D-1 bis D-27 kommt genau einmal vor und hat einen Status. Ergebnis: siehe Commit-Bericht. Das ist eine **formale** Prüfung. Sie sagt nichts über die Qualität des Verhaltens.
