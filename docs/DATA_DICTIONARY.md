# Datenwörterbuch

## Status

Dieses Datenwörterbuch ist die Phase-0-Spezifikation für die in Phase 1
vorläufig implementierten SQLAlchemy-Modelle. Fachliche Regeln der
Versuchslogik werden in späteren Phasen ergänzt.

## Antwortdatensatz

| Feld | Typ | Inhalt und Einschränkung |
| --- | --- | --- |
| `id` | technische Kennung | Interne Kennung; konkretes Format wird mit dem Datenbankschema festgelegt. |
| `session_id` | Zeichenkette | Zufällige Kennung der Umfragesitzung; kein Personenbezug soll daraus abgeleitet werden können. |
| `trial_number` | Ganzzahl | Durchgang innerhalb der Sitzung, vorgesehen 1 bis 10. |
| `color_r` | Ganzzahl | Rotwert der angezeigten Farbe, 0 bis 255. |
| `color_g` | Ganzzahl | Grünwert der angezeigten Farbe, 0 bis 255. |
| `color_b` | Ganzzahl | Blauwert der angezeigten Farbe, 0 bis 255. |
| `emotion` | Zeichenkette | Genau eine zum Zeitpunkt der Erhebung versionierte Emotionskategorie. |
| `color_order` | Ganzzahl | Position der Farbe innerhalb der Sitzung. |
| `experiment_version` | Versionswert | Version der Versuchsdefinition, damit Änderungen vergleichbar bleiben. |

Ein Erstellungszeitpunkt wird nur aufgenommen, wenn dafür vor der
Implementierung ein dokumentierter Zweck festgestellt wurde. Namen,
E-Mail-Adressen, Matrikelnummern und IP-Adressen gehören nicht zum
wissenschaftlichen Antwortdatensatz.

## Emotionskategorien

Als vorläufige Standardkonfiguration sind Freude, Trauer, Wut, Angst, Ekel,
Überraschung und Vertrauen vorgesehen. Die endgültige Liste und ihre
Versionierung müssen vor Beginn einer realen Erhebung festgelegt werden.

## CSV-Export

Der Export enthält genau eine Zeile pro Antwort und diese Spalten in der
angegebenen Reihenfolge:

```text
session_id,trial_number,color_r,color_g,color_b,emotion,color_order,experiment_version
```

Die Datei wird UTF-8-kodiert erzeugt. Spaltennamen, Reihenfolge und Datentypen
bleiben stabil und werden mit der Implementierung getestet. Der Export darf
nur nach erfolgreicher Administrator-Authentifizierung ausgeliefert werden
und muss direkt mit pandas verarbeitbar sein.

Die Beispielwerte aus der README sind synthetisch. Dieses Dokument legt keine
Aufbewahrungsfrist oder Datenbanktechnologie für den Produktivbetrieb
zusätzlich zur Architektur-Spezifikation fest.
