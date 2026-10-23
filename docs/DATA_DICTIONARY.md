# Datenwörterbuch

## Status

Dieses Datenwörterbuch ist die Phase-0-Spezifikation für die in Phase 1 und 2
vorläufig implementierten SQLAlchemy-Modelle. Die Versuchsdurchführung nutzt
eine versionierte Farbpalette; die endgültige wissenschaftliche
Versuchsdefinition muss vor einer realen Erhebung bestätigt werden.

## Versuch und Farbzuordnung

| Feld | Typ | Inhalt und Einschränkung |
| --- | --- | --- |
| `survey_sessions.id` | zufällige Zeichenkette | Nicht sprechende Versuchskennung ohne zusätzliche Personendaten. |
| `survey_sessions.status` | `in_progress`/`completed` | Statusübergang nach zehn gültigen Antworten. |
| `survey_sessions.palette_version` | Versionswert | Version der verwendeten festen Palette. |
| `session_colors.color_id` | Zeichenkette | Stabile ID einer Palettefarbe. |
| `session_colors.position` | Ganzzahl | Persistierte Position 1 bis 10 innerhalb des Versuchs. |
| `session_colors.color_r/g/b` | Ganzzahlen | Zur ID gehörende RGB-Werte, jeweils 0 bis 255. |

## Antwortdatensatz

| Feld | Typ | Inhalt und Einschränkung |
| --- | --- | --- |
| `id` | technische Kennung | Interne Kennung; konkretes Format wird mit dem Datenbankschema festgelegt. |
| `session_id` | Zeichenkette | Zufällige Kennung der Umfragesitzung; kein Personenbezug soll daraus abgeleitet werden können. |
| `color_id` | Zeichenkette | Referenz auf eine dem Versuch zugeordnete Palettefarbe. |
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

## Vorläufige Phase-2-Palette

Die implementierte Palette hat die Version `1.0` und enthält die IDs `red`,
`orange`, `yellow`, `green`, `cyan`, `blue`, `purple`, `pink`, `brown`, `gray`,
`navy` und `teal`. Pro Versuch werden zehn unterschiedliche Farben ohne
Wiederholung zufällig ausgewählt. Palette und Auswahlstrategie sind
technische Phase-2-Festlegungen und müssen vor der realen Erhebung
wissenschaftlich bestätigt und versioniert werden.

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
