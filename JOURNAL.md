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
