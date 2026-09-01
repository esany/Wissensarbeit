# Wissensarbeit

Git-native Referenzimplementierung und künftiges Projekt-Template für KI-gestützte, transdisziplinäre Wissens- und Konzeptarbeit.

## Ziel

Der fachliche Problem Owner arbeitet an Domänenfragen, Ziel, Bedeutung, Priorität und Akzeptanz. Das System übernimmt so weit wie möglich Recherche, Kompetenzaktivierung, technische Übersetzung, Strukturierung, Umsetzung, Traceability, Qualitätssicherung und Projektbetrieb.

**Human-in-the-loop, not human-as-workflow-engine.**

## Kernidee

- Git/GitHub ist dauerhafter, nachvollziehbarer Projektzustand; Chat ist Werkstatt, nie exklusives Projektgedächtnis.
- Neue Aspekte werden systemisch integriert (`fuse/refine/reframe/supersede/conflict/reject/defer`), nicht angehängt.
- KI-Ausgaben sind zunächst Candidates; materielle Promotion folgt expliziter Authority.
- Deterministische Regeln werden als Code/Tests/CI ausgeführt; fachliches Urteil bleibt als Urteil sichtbar.
- Fachliche, methodische, technische und Schnittstellenkompetenzen werden je Problem erkannt, bei Bedarf gegen SOTA/Best Practice recherchiert und projektspezifisch synthetisiert.
- Das Endprodukt kann Forschung, Konzept, Datenmodell, Backend, Frontend, Infrastruktur oder reine Software ohne KI sein.

## v0.1 – Operational Spine

```text
Issue / Input
    -> inspect/context
    -> Analyse / Kompetenzbedarf
    -> Requirement / Criterion / Decision Candidate
    -> Implementation Candidate
    -> validate / trace / audit
    -> PR + Review
    -> Merge = kanonische Zustandsänderung
    -> derive = menschenlesbare Projektsicht
```

## Repository-Bereiche

- `project/` – Ziel, Requirements, Qualitätsmodell, Risiken und Entscheidungen.
- `domain/` – projektspezifischer Domain-/Methodenkern; im Template bewusst minimal.
- `system/` – generische Lifecycle-, Authority- und Kompetenzverträge.
- `tools/` – kleiner ausführbarer Operational Core.
- `tests/` – negative und positive Regressionen.
- `.github/` – Issue-/PR-UX und CI.
- Produktcode (`src/`, `backend/`, `frontend/`, `database/`, ...) entsteht nur, wenn ein konkretes Projekt ihn benötigt; standardmäßig im selben Projekt-Repo.

## Lokal / CI

```bash
python tools/work.py validate
python tools/work.py inspect
python tools/work.py trace REQ-001
python tools/work.py derive
python tools/work.py audit
python -m unittest discover -s tests -v
```

## Nicht-Ziele der v0.1

Kein Agentenframework, keine Workflow-Engine, keine universelle Ontologie, keine vorgeschriebene Datenbank, keine Cloud-/Microservice-Plattform und keine KI-Pflicht im späteren Produkt. Infrastruktur wird aus nachgewiesenem Bedarf abgeleitet.
