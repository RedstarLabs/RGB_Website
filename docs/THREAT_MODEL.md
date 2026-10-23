# Bedrohungsmodell

## Schutzgüter

- Vertraulichkeit und Integrität der Forschungsantworten.
- Verfügbarkeit und korrekte Reihenfolge der Versuchsdurchführung.
- Schutz des Admin-Tokens und der CSV-Exporte.
- Nachvollziehbarkeit von RGB-Snapshots und Datenformat.

## Bedrohungen und Gegenmaßnahmen

| Bedrohung | Gegenmaßnahme |
| --- | --- |
| Unberechtigter Export | `X-Admin-Token`, sichere Vergleichsfunktion, kein Export bei fehlender Konfiguration. |
| Token-Leak in URL, Logs oder Daten | Header statt URL; keine Tokenwerte in Antworten oder Exportzeilen; Token nur im Seitenspeicher. |
| Spreadsheet-Formula-Injection | Führende `=`, `+`, `-`, `@` werden mit Apostroph escaped. |
| Manipulierte RGB- oder Antwortdaten | Browser ist nicht vertrauenswürdig; RGB kommt nur aus `session_colors`, Schemas und DB-Constraints validieren Werte. |
| Doppelübermittlung | Statusprüfung, aktuelle Farbe, Unique-Constraints und Transaktion. |
| Unvollständiger Export | Exportiert jede gespeicherte Antwort; fehlende Antworten werden nicht fingiert. |
| Verlust oder Änderung der Reihenfolge | RGB, Position und Versuchslänge werden beim Start persistiert. |
| Übermäßige Datenerhebung | Keine Konten, IP-Adressen, Tracking-Skripte oder unnötige Felder. |

## Vertrauensgrenzen

Browser und Admin-Client gelten als nicht vertrauenswürdig. Die Grenzen liegen
zwischen Client und API, API und Datenbank sowie Anwendung und Hosting-/Log-
Infrastruktur. Alle fachlichen Prüfungen erfolgen serverseitig.

## Verbleibende Risiken

Ein statisches API-Token ist keine vollständige Produktionsauthentifizierung.
HTTPS, restriktive Serverkonfiguration, Rate-Limiting, Rotation,
Fehlversuchsüberwachung, sichere Backups und Log-Aufbewahrung müssen vor dem
Livegang ergänzt und geprüft werden. Rechtliche und wissenschaftliche
Freigaben sind offen.
