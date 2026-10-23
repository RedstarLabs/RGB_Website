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

## 2026-10-23 – Phase 2: Versuchsdurchführung und Antwort-API

Eine vorläufige, versionierte RGB-Palette (`1.0`) und die sieben zentralen
Emotionswerte wurden implementiert. Beim Start werden zehn unterschiedliche
Farben ohne Wiederholung zufällig ausgewählt und als `session_colors`
persistent mit ihrer Position gespeichert. Versuche besitzen die Zustände
`in_progress` und `completed`; nach zehn gültigen Antworten wird der Versuch
abgeschlossen.

Die API stellt Start-, Status- und Antwort-Endpunkte bereit. Statusantworten
enthalten nur Fortschritt und die nächste Farbe. RGB-Werte werden serverseitig
aus der persistenten Palette übernommen; ungültige, unbekannte, nicht aktuelle
oder doppelte Antworten werden abgelehnt. Eine Alembic-Migration ergänzt die
Versuchs- und Farbzuordnungsdaten.

Die Palette und die Auswahlstrategie sind vorläufige technische
Festlegungen. Vor einer realen Erhebung müssen sie wissenschaftlich bestätigt
und zusammen mit dem Umgang mit Abbrüchen und Wiederaufnahme verbindlich
festgelegt werden. Oberfläche, CSV-Export und Administration bleiben
außerhalb dieser Phase.
