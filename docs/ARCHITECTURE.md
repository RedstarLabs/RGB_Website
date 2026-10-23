# Architektur

## Geltungsbereich

Dieses Dokument beschreibt die für Phase 0 festgelegten Leitplanken. Die
Anwendung ist noch nicht implementiert und nicht für eine reale Erhebung
freigegeben.

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

Diese Komponenten sind Zielentscheidungen aus der Projektspezifikation. Die
Implementierung erfolgt erst in den folgenden Roadmap-Phasen.

## Geplante Schichten

1. HTTP/API-Schicht: Routing, Protokollierung ohne unnötige personenbezogene
   Daten und HTTP-Fehlerbehandlung.
2. Service-Schicht: Sitzungsablauf, Validierung der Versuchsregeln und
   Exportablauf ohne direkte HTTP-Abhängigkeit.
3. Repository-Schicht: zentraler Zugriff auf persistierte Daten.
4. Datenbankschicht: SQLAlchemy-Modelle und Alembic-Migrationen.
5. Darstellungs- und statische Ressourcen: serverseitige Templates, CSS und
   JavaScript ohne Tracking- oder Werbeskripte.

Die genaue Modulstruktur wird mit der jeweiligen Implementierung festgelegt;
dieses Dokument erzeugt bewusst kein leeres Gerüst für spätere Phasen.

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
