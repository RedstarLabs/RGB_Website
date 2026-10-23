# RGB_Website – Journal

## 2026-10-23 – Projekt erstellt

Das Projekt wurde mit dem zentralen `new_project`-Standard erstellt.

Grundstruktur, Python-Umgebung und Entwicklungsdokumentation wurden angelegt.

## 2026-10-23 – Phase 0: Projektgrundlage und Spezifikation

Die Entwicklungsumgebung wurde mit uv, pytest und Ruff eingerichtet. Die
Konfiguration umfasst ein reproduzierbares Lockfile, lokale
Umgebungsvariablen über `.env.example` sowie den Ausschluss von Geheimnissen
und lokalen Datenbankdateien aus Git.

Die Phase-0-Dokumentation zu Architektur, Datenformat, Datenschutz und
Bedrohungsmodell wurde angelegt. Offene rechtliche, betriebliche und
wissenschaftliche Entscheidungen sind ausdrücklich als offen dokumentiert.

Geprüft wurden `uv sync --dev`, der minimale pytest-Lauf mit einem bestandenen
Test sowie Ruff-Linting und Formatprüfung. Ein Commit wurde nicht erstellt;
das Einchecken der Projektdateien bleibt offen.

## 2026-10-23 – Phase 1: Minimales Backend und Datenbank

Eine minimale FastAPI-Anwendung mit konfigurierbarem `/health`-Endpoint wurde
ergänzt. Die Datenbankschicht verwendet SQLAlchemy 2.x, SQLite lokal und eine
über `DATABASE_URL` konfigurierbare Verbindung für PostgreSQL beziehungsweise
andere unterstützte SQLAlchemy-Dialekte. Alembic verwaltet eine
Initialmigration.

Vorläufige Modelle für Umfragesitzungen und Antworten sind über getrennte
Repositories und einen Service erreichbar. Datenbank-Constraints verhindern
ungültige Durchgangs- und RGB-Werte; nach einem fehlgeschlagenen Commit führt
der Service einen Rollback aus. Es wurden bewusst keine Umfragelogik,
Farbauswahl, Oberfläche, CSV-Exporte oder Administrationsauthentifizierung
implementiert.

Geprüft wurden der lokale Uvicorn-Start mit erfolgreichem Health-Aufruf,
Alembic `upgrade head` und `current`, fünf pytest-Tests, Ruff sowie
`git diff --check`. Ein Commit wurde nicht erstellt.
