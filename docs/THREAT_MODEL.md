# Bedrohungsmodell

## Status und Annahmen

Das Modell gilt für die geplante öffentliche Web-App. Es ist eine
Phase-0-Grundlage; konkrete Kontrollen werden in den späteren Phasen
implementiert und getestet.

## Schutzgüter

- Vertraulichkeit und Integrität der Forschungsantworten.
- Verfügbarkeit der Umfrage und zuverlässige Speicherung bestätigter
  Antworten.
- Schutz von Administrationszugängen und CSV-Exporten.
- Nachvollziehbarkeit von Versuchsdefinition und Datenformat.
- Datenschutz durch Vermeidung unnötiger personenbezogener Daten.

## Bedrohungen und vorgesehene Gegenmaßnahmen

| Bedrohung | Risiko | Vorgesehene Gegenmaßnahme |
| --- | --- | --- |
| Unberechtigter Export oder Datenbankzugriff | Forschungsdaten werden offengelegt | Getrennter Administrationsbereich, sichere Authentifizierung, Backend-only-Datenbankzugriff, HTTPS. |
| Manipulierte oder ungültige Antworten | Datenqualität und Vergleichbarkeit sinken | Serverseitige syntaktische und fachliche Validierung, versionierte Versuchsdefinition, Tests. |
| Doppelte oder verlorene Übermittlung | Antworten fehlen oder werden mehrfach gezählt | Bestätigte Speicherung vor dem nächsten Durchgang, idempotente Speicherung und robuste Fehlerzustände in späteren Phasen. |
| Missbrauch öffentlicher Endpunkte | Verfügbarkeit oder Datenqualität wird beeinträchtigt | Rate-Limiting, Missbrauchsbeobachtung und sichere Fehlerbehandlung in den Phasen 4 und 6. |
| Geheimnis in Quellcode, Logs oder Fehlerantworten | Administrationszugang oder Daten werden kompromittiert | Umgebungsvariablen, `.gitignore`, begrenzte Logs und Prüfung von Fehlerantworten. |
| Kompromittiertes Hosting oder Backup | Daten werden außerhalb der Anwendung offengelegt | Hosting-, Backup- und Zugriffskonzept vor dem Livegang prüfen und dokumentieren. |
| Tracking oder übermäßige Protokollierung | Unnötige personenbezogene Daten entstehen | Keine Tracking-Dienste, keine IP-Adressen in der Forschungsdatenbank, Log-Minimierung. |

## Vertrauensgrenzen

Die Grenzen liegen zwischen Browser und Backend, Backend und Datenbank sowie
Backend und Administrationszugang. Der Browser gilt als nicht vertrauenswürdig;
alle fachlichen Prüfungen müssen serverseitig erfolgen. Der Betreiber der
Hosting- und Logging-Infrastruktur ist als gesondert zu prüfende
Vertrauensgrenze zu behandeln.

## Noch offene Punkte

Die konkrete Authentifizierung, Rate-Limits, CSRF-Anforderungen,
Sitzungsverwaltung, Log- und Backup-Aufbewahrung sowie das Produktions- und
Hostingmodell werden vor der jeweiligen Implementierung beziehungsweise vor
dem Livegang festgelegt. Dieses Dokument nimmt diese Entscheidungen nicht
vorweg.
