# Datenschutz

## Vorläufiger Status

Dieses Dokument ist eine technische Datenschutzanforderung für Phase 0 und
keine Rechtsberatung, Datenschutzerklärung oder Bestätigung der
DSGVO-Konformität. Die Anwendung ist nicht für eine reale Datenerhebung
freigegeben.

## Datenminimierung

Erhoben werden sollen ausschließlich die für die Forschungsfrage und den
Ablauf notwendigen Antwortdaten: zufällige Sitzungskennung, Durchgang,
angezeigte RGB-Werte, Emotion, Reihenfolge und versionierte
Versuchsdefinition. Namen, E-Mail-Adressen und Matrikelnummern werden nicht
erhoben. Teilnehmende benötigen kein Benutzerkonto.

IP-Adressen werden nicht in der wissenschaftlichen Datenbank gespeichert.
Cookies, Tracking-Pixel, Analyseanbieter, Werbung und unnötige externe
Dienste sind nicht vorgesehen. Technische Server- und Proxy-Logs müssen auf
das notwendige Maß begrenzt werden.

## Technische Schutzmaßnahmen

- Öffentlicher Betrieb ausschließlich über HTTPS.
- Datenbankzugriff nur vom Backend aus.
- CSV-Exporte ausschließlich nach Administrator-Authentifizierung.
- Geheimnisse und Zugangsdaten nur über die Laufzeitumgebung, nie im
  Repository.
- Backups, Löschung und Aufbewahrung werden vor dem Livegang dokumentiert.

## Offene rechtliche und betriebliche Entscheidungen

Vor Veröffentlichung müssen verantwortliche Stelle, Kontaktmöglichkeit,
Rechtsgrundlage, erforderliche Einwilligungsinformationen, Verfahren für
Widerruf und Löschanfragen, Aufbewahrungsfristen, Hosting-Anbieter,
Auftragsverarbeitung, Hosting-Logs, mögliche Drittlandtransfers sowie die
Notwendigkeit einer Datenschutz-Folgenabschätzung oder Ethikprüfung geklärt
werden. Auch das konkrete Authentifizierungsverfahren für Administratoren ist
noch offen.

Die veröffentlichten Datenschutzhinweise müssen die tatsächlich eingesetzte
Bereitstellung und alle Datenflüsse abbilden. Bis dahin darf das Projekt weder
vollständige Anonymität noch DSGVO-Konformität behaupten.
