# Risikobetrachtung — Konkrete Methode (Kap. 5.4)

**Quelle:** AR A-2400/62 Ziffer 5.3 (§ 7 Abs. 2 Satz 2 BHO)

---

## Überblick: Dreischritt-Methode

Gem. § 7 Abs. 2 Satz 2 BHO ist eine **Risikoverteilung zwingend vorzunehmen**. 

Die Risikobetrachtung erfolgt in drei Schritten:
1. **Risikoidentifizierung**: Was genau ist das Risiko?
2. **Risikoverteilung**: Wer trägt das Risiko bei Eintritt?
3. **Monetäre Risikobewertung**: In welcher Höhe werden Haushaltsmittel gebunden?

---

## Schritt 1: Risikoidentifizierung

**Frage:** Welche **Abweichungen vom angestrebten Ziel/Zustand** können in jedem Betrachtungsjahr eintreten?

**Typische Risikoarten** (nach KompZWUBw-Risikoliste):
- Ausfall von Lieferanten / Kontraktpartnern
- Preissteigerungen über Prognosewert hinaus
- Verzögerungen (Beschaffung, Baumaßnahmen, Instandsetzung)
- Personallücken / Fachkräftemangel
- Technische Ausfallrisiken
- Änderung von Rahmenbedingungen (Gesetzesänderungen, Organisationsreformen)
- Qualitätsmängel
- Sicherheitsvorfälle

**Dokumentation:**
> „Folgende Risiken wurden für die Betrachtung identifiziert:
> - [Risiko 1]: [2–3 Sätze Beschreibung, wann/wie es eintritt]
> - [Risiko 2]: [...]"

---

## Schritt 2: Risikoverteilung

**Frage:** **Wer trägt das Risiko, wenn es eintritt?**
- **Einzelplan 14** (Bundeswehr = Auftraggeber)
- **Dritter** (externer Auftragnehmer / Dienstleister)
- **Gemischt** (gerechte Verteilung zwischen Bund und Drittem)

**WICHTIG:** Angestrebt sollte immer eine **gerechte Verteilung** sein. In den meisten Fällen liegt das Risiko jedoch **ausschließlich beim Auftraggeber Bund**, weil:
- Verträge mit Dritten schwer kalkulierbar sind
- Risiken schwer auf Partner zu übertragen sind (rechtlich, praktisch)

**Dokumentation:**
> „Das Risiko [Risiko X] trägt [Einzelplan 14 / Dritter / beidseitig]. Bei einem Ausfall [Szenario] fallen die Kosten [Beschreibung der finanziellen Folge] an."

---

## Schritt 3: Monetäre Risikobewertung — FORMEL

### Risikowertberechnung

```
Risikowert (EUR) = Eintrittswahrscheinlichkeit (%) × Schadenshöhe (EUR)
```

**Beispiel:**
```
Risiko: Ausfall des wirtschaftlichsten Anbieters
Eintrittswahrscheinlichkeit: 25 %
Schadenshöhe: Differenz zu zweitbesten Angebot = 15.000 EUR
→ Risikowert = 0,25 × 15.000 EUR = 3.750 EUR
```

### Eintrittswahrscheinlichkeit — Klassifizierungstabelle

| Risikobeurteilung | Eintrittswahrscheinlichkeit | Verwendungshilfe |
|---|---|---|
| **Sehr hoch** | > 80 % | Nahezu sicher einzutreten (z.B. Preissteigerung auf Basis historischer Daten) |
| **Hoch** | > 60 bis 80 % | Sehr wahrscheinlich (z.B. Lieferverzögerungen bei knappen Ressourcen) |
| **Mittel** | > 40 bis 60 % | Ebenso wahrscheinlich wie unwahrscheinlich (z.B. Personalausfallrisiko) |
| **Niedrig** | > 20 bis 40 % | Eher unwahrscheinlich (z.B. Technisches Ausfallrisiko bei neuer Hardware) |
| **Gering** | ≤ 20 % | Sehr unwahrscheinlich (z.B. seltene Kombinationen von Ausfällen) |

**Hinweis:** Die Eintrittswahrscheinlichkeit **stellt eine Annahme dar** und muss unter Gliederungspunkt 4 („Annahmen") dokumentiert werden.

**Sonderfall — Grenzwert 50 %:**
> Bei einer Eintrittswahrscheinlichkeit von **> 50 %** ist im Einzelfall zu prüfen, ob das „Risiko" nicht bereits als **feste Annahme in der Berechnung** berücksichtigt werden sollte (statt als Risiko mit Wahrscheinlichkeit).

---

## Schadenshöhe — Konkrete Beispiele

### 1. Ausfall des wirtschaftlichsten Interessenten
```
Szenario: Der günstigste Bieter kann die Leistung nicht erbringen.
Schadenshöhe = Differenz zwischen erstem und zweitem Angebot (EUR)
Beispiel: Bestes Angebot 100.000 EUR, nächstbestes 115.000 EUR → Schaden = 15.000 EUR
```

### 2. Verzögerungen bei Baumaßnahmen
```
Szenario: Baumaßnahme verzögert sich um 3 Monate.
Schadenshöhe = Fortführung von Mietkosten während der Verzögerung
Beispiel: Hallenmiete 5.000 EUR/Monat × 3 Monate = 15.000 EUR
```

### 3. Verzögerungen bei Instandsetzungsmaßnahmen
```
Szenario: Wartung / Instandsetzung verzögert sich um 4 Wochen.
Schadenshöhe = Kosten für Ersatzleistung / Ersatzgerät während Ausfallzeit
Beispiel: Ersatzbeschaffung von Transportleistungen 3.000 EUR/Woche × 4 = 12.000 EUR
```

### 4. Zeitliche Verzögerung bei Nachbesetzung / Neueinstellung
```
Szenario: Erforderliche Personalposition kann nicht zeitgerecht besetzt werden.
Schadenshöhe = Kosten für externe Leistungserbringung statt Eigenleistung
Beispiel: Extern beauftragter Dienstleister kostet 5.000 EUR/Monat, 
          interne Lösung würde 2.000 EUR/Monat kosten → Schaden = 3.000 EUR/Monat × 12 = 36.000 EUR/Jahr
```

### 5. Qualitätsmängel / Nachbesserungen
```
Szenario: Erbrachte Leistung entspricht nicht Spezifikation.
Schadenshöhe = Kosten für Nachbesserung / Neuerbringung
Beispiel: Nachbesserungsarbeiten kosten 8.000 EUR
```

---

## Dokumentation im WU-Kapitel 5.4 — Satzmuster

### Tabelle: Übersicht Risiken mit Wertung

```
| Risiko | Ursache/Szenario | WhoTrägt | Eintrittswahrscheinlichkeit | Schadenshöhe (EUR) | Risikowert (EUR) |
|---|---|---|---|---|---|
| Ausfall Lieferant | Insolvenz / Nichterfüllung | E14 | 20 % | 15.000 | 3.000 |
| Preissteigerung | Inflation > Annahme | E14 | 40 % | 25.000 | 10.000 |
| Personalausfallrisiko | Krankheit / Fluktuation | E14 | 50 % | 18.000 | 9.000 |
| **GESAMT** | — | — | — | — | **22.000** |
```

### Fließtext nach Tabelle

**Beispiel 1 (einfach):**
> „Die identifizierten Risiken wurden bewertet. Das bedeutsamste Risiko ist die Möglichkeit von Preissteigerungen über die in Kapitel 4 getroffene Annahme (2,6 % p.a. für Personalkosten) hinaus. Bei einer Eintrittswahrscheinlichkeit von 40 % und einem geschätzten Mehrkostenpotenzial von 25.000 EUR ergibt sich ein Risikowert von 10.000 EUR. Ein Personalausfallrisiko wird mit 9.000 EUR bewertet. Die Gesamtrisikowertung für alle Optionen beträgt 22.000 EUR."

**Beispiel 2 (differenziert nach Optionen):**
> „Die Risikobetrachtung zeigt, dass Option 2 (Fremdbezug) ein höheres Ausfallrisiko trägt (Lieferantenausfall mit 20 % Wahrscheinlichkeit, Schadenshöhe 15.000 EUR), während Option 1 (Eigenbetrieb) das Personalausfallrisiko trägt (50 % Wahrscheinlichkeit, 18.000 EUR Schadenshöhe). Option 3 (Kooperation) verteilt das Risiko zwischen Bund und Partner."

---

## Integration in Kapitalwertberechnung

**Wichtig:** Der Risikowert wird bei Verwendung der **Kapitalwertmethode** ebenfalls **diskontiert**:

```python
# Pseudocode für Kapitalwertberechnung mit Risiko
kapitalwert_mit_risiko = kapitalwert_ohne_risiko + diskontierter_risikowert

# Der diskontierte Risikowert wird wie andere Zahlungsströme mit dem Kalkulationszinssatz abgezinst
diskontierter_risikowert = risikowert_summe / (1 + zinssatz)^betrachtungsjahre
```

---

## Entscheidungshilfe: Wann wird Risiko zur Annahme?

**Faustregel:**
- **> 50 % Eintrittswahrscheinlichkeit** → Prüfe, ob dies bereits als **feste Annahme** berücksichtigt werden sollte (z.B. „Preissteigerung wird mit 3,5 % statt 2,6 % angenommen" statt als Risiko)
- **≤ 50 %** → Bleibe bei Risikobewertung

**Nutzen dieser Unterscheidung:**
- Transparenz: Der Leser sieht sofort, welche Szenarien als sicher (in Annahmen) vs. möglich (als Risiko) behandelt werden
- Robustheit: Sensitivitätsanalyse kann dann prüfen, ab wann die sichere Annahme zum Risiko wird

