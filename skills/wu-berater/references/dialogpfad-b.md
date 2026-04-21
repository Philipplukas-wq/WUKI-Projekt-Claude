# Dialogpfad B: Überjährige WU

Für **mehrjährige Betrachtungen, Investitionen, komplexe Fälle** (9 Pflichtgliederungspunkte der AR A-2400/62).

**Modi**: Geführter Dialog (Schritt für Schritt) oder Schnelldurchlauf (alle Schritte auf einmal).

---

## Vorbereitung

**Betrachtungszeitraum**: Mache einen konkreten Vorschlag:
- Fahrzeuge / Geräte: 10 Jahre
- IT: 5 Jahre
- Infrastruktur / Gebäude: 15–25 Jahre
- Dienstleistungsverträge: Laufzeit + Verlängerungsoptionen
- Faustregel: Nutzungsdauer = Betrachtungszeitraum (mind. 5 Jahre)

**Überblick** (am Ende befüllen nach allen Kapiteln):
```python
wu_data['ueberblick'] = {
    'betrachtungsgegenstand': f"In der vorliegenden Untersuchung wird {sachverhalt} für {dienststelle} betrachtet. Untersucht werden {n} Optionen über {jahre} Jahre.",
    'entscheidungsvorschlag': f"Empfohlen wird {beste_option}. Kapitalwert: {kw_mit_risiko} EUR (siehe Anlage Marktrecherche, Nr. 1).",
}
```

---

## Kapitel 1–9

Befolge die Struktur der AR A-2400/62. **Satzmuster** sind in `satzmuster-b.md` dokumentiert — nicht hier wiederholen.

| Kapitel | Inhalt | Satzmuster in satzmuster-b.md | Validierung |
|---------|--------|------|------|
| 1.1 | Funktionale Bedarfsforderung (qualitativ + quantitativ) | Kap. 1.1 | **Inline-Check** (`validate_step('bedarfsforderung', ...)`) |
| 1.2 | Bedarfsprognose (Entwicklung über Betrachtungszeitraum) | Kap. 1.2 | — |
| 1.3 | Rahmenbedingungen (nur optionsausschließend) — **ACHTUNG: Wird iterativ ergänzt bei Aussonderung (Kap. 3.2)** | Kap. 1.3 | — |
| 2.1–2.7 | Ausgangslage: Ablauf-, Aufbauorganisation, Personal, Material, Infrastruktur, DL, Einnahmen | Kap. 2.1–2.6 | — |
| 2.8 | Haushalterische Darstellung (automatisch berechnen) | Python-Snippet | — |
| 3.1 | Grundsätzlich mögliche Optionen (2–3 Sätze je Option) | Kap. 3.1 | — |
| 3.2 | Aussonderung ungeeigneter Optionen (**Pflichtprüfung**: kein Personal, Haushaltsmittel, Dienstposten, Infrastruktur als Grund!) — **RÜCKKOPPLUNG: Wenn neue RB benötigt, zu Kap. 1.3 ergänzen** | Kap. 3.2 + SKILL.md | **Guard Check** (`validate_step('aussonderung', ...)`) |
| 3.3 | Ausführliche Darstellung geeigneter Optionen (je 3.3.x.1–3.3.x.7) | Kap. 3.3.x | — |
| 4.1–4.2 | Annahmen (alle / bestimmte Optionen) | Kap. 4.1–4.2 | — |
| 5.2 | Kapitalwertberechnung (Berechnungsskript verwenden) | Kap. 5.2 | — |
| 5.3 | Kapitalwerte ohne Risiko | Kap. 5.3 | — |
| 5.4 | Risikobetrachtung (Identifizierung, Verteilung, Monetäre Bewertung) | Kap. 5.4.2 | — |
| 5.5 | Kapitalwert mit Risiko | Kap. 5.5 | — |
| 6 | Vergleich der Optionen (Tabelle + Einleitungssatz) | Kap. 6 | — |
| 7 | Sensitivitätsanalyse (automatisch berechnen) | Python-Snippet | — |
| 8 | Nichtmonetäre Faktoren / Nutzwertanalyse | SKILL.md | — |
| 9 | Entscheidungsvorschlag (Empfehlung + Begründung) | Kap. 9 | **Vor Export**: `quick_validate()` + `export_safe()` |

---

## Kapitalwertberechnung (5.2)

```python
import sys
sys.path.insert(0, 'P:/WUKI_Projekt/Claude/skills/wu-berater/scripts')
from berechnung_kapitalwert import berechne_alle_optionen, erstelle_kw_uebersicht

optionen = [
    Option('Option 1', investition=..., kostenpositionen=[
        Kostenposition('Personal', ..., PSR_PERSONAL),
        ...
    ]),
]
ergebnisse = berechne_alle_optionen(optionen, zinssatz=0.012, jahre=...)
```

---

## Sensitivitätsanalyse (7)

```python
from berechnung_kapitalwert import erstelle_sensitivitaet
sensitivitaet_text = erstelle_sensitivitaet(optionen, ergebnisse, risikowerte, zinssatz=0.012, jahre=...)
wu_data['kap6_9']['sensitivitaet'] = sensitivitaet_text
```

Das Skript berechnet Break-even automatisch. Frage den Nutzer nicht danach.

---

## Export

```python
from export_wu_ueberjahrig import fill_template, build_filename, erstelle_abschlusscheckliste

outpath = build_filename(wu_data['meta']['datum'], 'Sachverhalt', wu_data['meta']['dienststelle'])
fill_template(wu_data, outpath)
print(erstelle_abschlusscheckliste(wu_data, outpath))
```

Vollständiges Schema: `WU_DATA_SCHEMA` am Ende von `export_wu_ueberjahrig.py`.
