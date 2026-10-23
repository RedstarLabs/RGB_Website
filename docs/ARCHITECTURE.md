# Architektur

## Geltungsbereich

Dieses Dokument beschreibt die für Phase 0 festgelegten Leitplanken und die
in Phase 1 implementierte technische Grundlage. Die Anwendung ist nicht für
eine reale Erhebung freigegeben.

## Zielarchitektur

Die Anwendung soll zunächst als schlanke, serverseitig ausgelieferte Web-App
entstehen:

- Ein Python-Backend mit FastAPI stellt die HTTP-Schnittstellen bereit.
- Pydantic validiert externe Eingaben und Ausgaben.
- Geschäftliche Versuchslogik bleibt von HTTP-Routen getrennt.
- SQLAlchemy 2.x kapselt den Datenbankzugriff; Alembic verwaltet Migrationen.
- SQLite dient der lokalen Entwicklung, PostgreSQL ist für den öffentlichen
  Produktivbetrieb vorgesehen.
- HTML, CSS und JavaScript bilden die Oberfläche. Ein separates
  Frontend-Framework ist derzeit nicht vorgesehen.

Die minimale Backend- und Datenbankgrundlage ist in Phase 1 umgesetzt. Phase
2 ergänzt die fachliche Versuchsdurchführung über eine API. Phase 3 bindet
eine statische, serverseitig ausgelieferte HTML/CSS/JavaScript-Oberfläche an
diese API an; Exporte und Administration bleiben späteren Phasen vorbehalten.

## Geplante Schichten

1. HTTP/API-Schicht: Routing, Protokollierung ohne unnötige personenbezogene
   Daten und HTTP-Fehlerbehandlung.
2. Service-Schicht: Sitzungsablauf, Validierung der Versuchsregeln und
   Exportablauf ohne direkte HTTP-Abhängigkeit.
3. Repository-Schicht: zentraler Zugriff auf persistierte Daten.
4. Datenbankschicht: SQLAlchemy-Modelle und Alembic-Migrationen.
5. Darstellungs- und statische Ressourcen: serverseitige Templates, CSS und
   JavaScript ohne Tracking- oder Werbeskripte.

Die aktuelle Modulstruktur folgt diesen Schichten unter `src/rgb_website/`.
Die Versuchspalette und Emotionsauswahl liegen zentral in `experiment.py`.
API-Schemas und Routen bleiben von Service- und Repository-Logik getrennt.
Die Oberfläche liegt in `static/` und enthält keine eigene Versuchs- oder
Zufallslogik. Es gibt bewusst noch keine Exportfunktion oder
Administrationsauthentifizierung.

## Phase-3-Oberfläche

`GET /` liefert die statische Studienoberfläche. Das Frontend ruft ausschließlich
die vorhandenen Endpunkte `POST /api/experiments`,
`GET /api/experiments/{session_id}` und
`POST /api/experiments/{session_id}/responses` auf. Es speichert keine
Versuchs- oder Antwortdaten in `localStorage` oder `sessionStorage`.

## Phase-2-API

- `POST /api/experiments` startet einen Versuch mit zufälliger, persistierter
  Reihenfolge und liefert die erste Farbe.
- `GET /api/experiments/{session_id}` liefert Status, Fortschritt und nur die
  nächste noch zu beantwortende Farbe.
- `POST /api/experiments/{session_id}/responses` akzeptiert `color_id`, eine
  Emotion, die Durchgangsnummer und die Versuchsversionskennung.

RGB-Werte werden nicht vom Client akzeptiert, sondern aus der unveränderlichen
Farbzuordnung des Versuchs übernommen. Ein Versuch wird nach zehn Antworten
auf `completed` gesetzt. Unbekannte, nicht aktuelle oder bereits beantwortete
Farben werden abgelehnt.

## Datenfluss und Grenzen

Teilnehmende sollen keine Konten benötigen. Eine zufällige Sitzungskennung
ordnet Antworten einer Umfragesitzung zu. Antworten werden erst nach
bestätigter Speicherung an den nächsten Durchgang weitergegeben. Der
Administrationsbereich bleibt von den öffentlichen Umfragefunktionen getrennt
und schützt CSV-Exporte durch Authentifizierung.

IP-Adressen werden nicht in der wissenschaftlichen Datenbank gespeichert.
Server- und Proxy-Logs müssen auf betriebsnotwendige Informationen begrenzt
werden. HTTPS ist für den öffentlichen Betrieb verpflichtend.

## Noch zu entscheidende Punkte

Vor der Implementierung beziehungsweise Veröffentlichung müssen insbesondere
die Farbauswahlstrategie, der Umgang mit identischen Farben, die
Wiederaufnahme abgebrochener Sitzungen, die konkrete
Administrationsauthentifizierung, Hosting und Protokollaufbewahrung festgelegt
werden. Dieses Dokument stellt hierfür keine stillschweigenden Entscheidungen
dar.
