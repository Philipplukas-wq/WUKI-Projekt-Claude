# Nachhaltigkeitskriterien und AVV Klima — Integration in WU

**NUR FÜR ÜBERJÄHRIGE WU RELEVANT (Dialogpfad B).**

**Quellen:** 
- AR A-2400/62 (§ 7 Abs. 2 BHO)
- AVV Klima (Allgemeine Verwaltungsvorschrift zur Beschaffung klimafreundlicher Leistungen, gültig seit 01.01.2022)

---

## Überblick: Was ist AVV Klima?

Die **AVV Klima** ist eine Verwaltungsvorschrift für alle **Bundesbehörden** (inkl. Bundeswehr), die seit Januar 2022 gilt. Sie verpflichtet zu klimafreundlicher Beschaffung durch:

1. **Energieeffizienz über gesamten Lebenszyklus** (Herstellung, Nutzung, Entsorgung)
2. **Treibhausgasemissionen-Prognose** für den gesamten Lebenszyklus
3. **Monetäre Bewertung** von CO2-Emissionen mittels CO2-Schattenpreis

**Verbindung zu WU (§ 7 BHO / AR A-2400/62):**
> „In diese [WU] sind die Energieeffizienz über den gesamten Lebenszyklus der Leistung 
> und dabei insbesondere der Aspekt der energieeffizientesten Systemlösung sowie 
> soweit mit vertretbarem Aufwand möglich, eine Prognose der verursachten 
> Treibhausgasemissionen während des gesamten Lebenszyklus einzubeziehen."
> (Quelle: AR A-2400/62)

---

## 1. Konkrete Bewertungskriterien

### A. Energieeffizienzanforderungen

**Anforderung:**
Soweit verfügbar, muss die **höchste verfügbare Energieeffizienzklasse** zum Beschaffungszeitpunkt gefordert werden.

**Beispiele nach Maßnahmentyp:**

**Gebäude / Infrastruktur:**
```
KfW-Effizienzhaus 55:    Höchste Klasse (beste Energieeffizienz)
KfW-Effizienzhaus 70:    Hohe Klasse
KfW-Standard (alt):      Baseline
```

**Fahrzeuge:**
```
Euro 6d (ab 2020):       Höchste Klasse (Emissions-Standard)
Euro 5:                  Mittlere Klasse
Ältere Standards:        Nicht empfohlen
```

**Elektrotechnik / Geräte:**
```
A+++, A++:               Höchste Klasse (wenn verfügbar)
A+:                      Hohe Klasse
B, C:                    Untere Klasse
```

### B. Ecolabel und Umweltzeichen

**Anforderung:**
Typ-I-Umweltzeichen nach ISO 14024 sollten eingefordert werden (sofern verfügbar):

- ✅ **Blauer Engel** (Deutsches Umweltzeichen)
- ✅ **EU-Ecolabel** (Europäisches Umweltzeichen)
- ✅ **FSC-Zertifikat** (für Holzprodukte)
- ✅ **GOTS** (für Textilien)

**Dokumentation in WU:**
> „Die Beschaffung sollte bevorzugt auf Produkte mit dem Blauen Engel oder 
> EU-Ecolabel ausgerichtet sein, sofern diese am Markt verfügbar sind."

### C. Lebenszyklusbetrachtung (LCC)

**Anforderung:**
Nicht nur Anschaffungskosten berücksichtigen, sondern **Gesamtkostenvergleich** über Nutzungsdauer:

```
Gesamtkostenvergleich = Akquisitionskosten + Betriebskosten - Restwert

Beispiel Fahrzeug (10 Jahre):
Option 1 (Verbrenner):
  Kauf: 50.000 EUR
  Betrieb (Kraftstoff, Wartung): 40.000 EUR
  Restwert: -5.000 EUR
  SUMME: 85.000 EUR

Option 2 (Elektrofahrzeug):
  Kauf: 60.000 EUR (höher, aber z.T. förderfähig)
  Betrieb (Strom, Wartung): 20.000 EUR (günstiger)
  Restwert: -8.000 EUR (höher)
  SUMME: 72.000 EUR → 13.000 EUR günstiger!
```

---

## 2. CO2-Schattenpreis — Monetäre Bewertung

### Aktuelle CO2-Preise (BEHG — Brennstoffemissionshandelsgesetz)

| Jahr | CO2-Preis |
|---|---|
| **2024** | 45 EUR / Tonne CO2 |
| **2025** | 55 EUR / Tonne CO2 |
| **2026** | 55–65 EUR / Tonne CO2 (Preiskorridor) |
| **2027+** | Marktpreis (im EU-ETS) |

**Verwendung in WU:**
> Für die Berechnung von Treibhausgasemissionen wird mindestens der gültige 
> BEHG-Preis angesetzt. Gem. AVV Klima ist der aktuelle Schattenpreis 
> (2025: 55 EUR/Tonne) zu verwenden.

### Berechnung der CO2-Kosten

```
CO2-Kosten = Gesamte Treibhausgasemissionen × CO2-Schattenpreis

Beispiel:
Option 1: 50 Tonnen CO2 über 10 Jahre × 55 EUR/Tonne = 2.750 EUR (weitere Kostenfaktor)
Option 2: 20 Tonnen CO2 über 10 Jahre × 55 EUR/Tonne = 1.100 EUR (günstiger)

Differenz: 1.650 EUR Nachteil für Option 1
```

---

## 3. Integration in Kapitalwertberechnung

### Berechnung der Gesamtkapitalwerte

**Option A — ohne Nachhaltigkeitsaspekte (klassisch):**
```
KW = Akquisitionskosten + Betriebskosten (abgezinst) - Restwert
```

**Option B — mit CO2-Schattenpreis (AVV Klima-konform):**
```
KW = Akquisitionskosten + Betriebskosten + CO2-Kosten (alle abgezinst) - Restwert

Beispiel (vereinfacht):
Option 1 (Standard):     KW = 85.000 EUR + 2.750 EUR CO2 = 87.750 EUR
Option 2 (Öko):          KW = 72.000 EUR + 1.100 EUR CO2 = 73.100 EUR
→ Option 2 ist 14.650 EUR günstiger (mit Nachhaltigkeitskosten)
```

### Wie Treibhausgasemissionen berechnet werden

**Datenquellen:**
1. **Herstellerangaben** (z.B. CO2-Fußabdruck des Produkts)
2. **UBA-Datenbank** (Umweltbundesamt bietet Factsheets)
3. **Ökobilanzdatenbanken** (z.B. ecoinvent, GaBi)
4. **Marktstudien** (konkrete Prognosen für Branche)

**Beispiel — Gebäude-Wärmeversorgung:**
```
Gasheizung (Option 1):
  - Jahresverbrauch: 50.000 kWh Erdgas/Jahr
  - CO2-Faktor Erdgas: ca. 0,202 kg CO2/kWh
  - Jährliche Emissionen: 50.000 × 0,202 = 10.100 kg CO2 = 10,1 Tonnen/Jahr
  - 10 Jahre: 101 Tonnen CO2

Wärmepumpe mit Grünstrom (Option 2):
  - Jahresverbrauch: 12.000 kWh Strom/Jahr (weil effizienter)
  - CO2-Faktor Grünstrom: ca. 0,050 kg CO2/kWh
  - Jährliche Emissionen: 12.000 × 0,050 = 600 kg CO2 = 0,6 Tonnen/Jahr
  - 10 Jahre: 6 Tonnen CO2

CO2-Kostenersparnis:
  (101 - 6) Tonnen × 55 EUR = 5.225 EUR
```

---

## 4. Dokumentation in der WU — Wo gehört's hin?

### Position in der WU-Struktur

Die AVV Klima-Aspekte können in der WU an **mehreren Stellen** dokumentiert werden (gem. AR A-2400/62):

**A) Im Bedarf (Kap. 1.1):**
```
Funktionaler Bedarf: „Sicherstellung der Wärmeversorgung unter Nutzung 
von erneuerbaren Energieträgern"
→ Legt Nachhaltigkeitsziel bereits im Bedarf fest
```

**B) In den Rahmenbedingungen (Kap. 1.3):**
```
Rahmenbedingung (Sonstiges/Nachhaltig):
„Die Maßnahme muss nach AVV Klima und Bundes-Klimaschutzgesetz 
energieeffizient ausgeführt werden. Es ist eine Prognose der 
Treibhausgasemissionen durchzuführen."
```

**C) In den nichtmonetären Faktoren (Kap. 8):**
```
Nicht-monetäre Kriterien (separate Nutzwertanalyse):
- Energieeffizienz: 0–3 Punkte
- Nachhaltigkeitszertifizierungen: 0–3 Punkte
- CO2-Reduktionspotenzial: 0–3 Punkte
```

### Satzmuster für Kap. 5 (Berechnung mit CO2-Kosten)

**Einleitung:**
> „Gemäß AVV Klima werden neben den direkten Kosten auch die Treibhausgasemissionen 
> über den gesamten Lebenszyklus monetär bewertet. Für jede Option erfolgt eine 
> Prognose der CO2-Emissionen mit anschließender Kostenberechnung."

**Option 1 (beispielhaft):**
> „Option 1 (Gasheizung) verursacht jährlich ca. 10,1 Tonnen CO2. Über den 
> Betrachtungszeitraum von 10 Jahren ergibt sich eine Gesamtemissionsmenge von 
> 101 Tonnen CO2. Mit dem CO2-Schattenpreis von 55 EUR/Tonne (BEHG 2025) entstehen 
> CO2-Kosten in Höhe von 5.555 EUR. Diese werden in der Kapitalwertberechnung 
> berücksichtigt."

**Vergleich Kapitalwert (mit CO2):**
```
| Option | Investition + Betrieb | CO2-Kosten | Gesamtkapitalwert |
|---|---|---|---|
| 1 (Gas) | 85.000 EUR | 5.555 EUR | 90.555 EUR |
| 2 (Wärmepumpe) | 95.000 EUR | 330 EUR | 95.330 EUR |
```

> „Berücksichtigung von Treibhausgasen zeigt: Obwohl die Wärmepumpe höhere 
> Anschaffungskosten hat, ist sie insgesamt teurer, wenn Betriebskosten (Strom günstiger 
> als Gas) eingerechnet werden. Die CO2-Kostenersparnis von 5.225 EUR spricht zusätzlich 
> für Option 2."

---

## 5. Checkliste: Wann und wie Nachhaltigkeit in WU einbeziehen?

### Entscheidungslogik

**Frage:** Ist die Maßnahme für AVV Klima-Betrachtung relevant?

✅ **JA, wenn:**
- Beschaffungswert ≥ 10.000 EUR
- Energieverbrauch über Lebenszyklus ist signifikant (z.B. Fahrzeuge, Gebäude, IT)
- Mehrere Optionen mit unterschiedlichen Energieeffizienzen verfügbar
- Bundesdirektive oder interne Policy zu Nachhaltigkeit besteht

❌ **NEIN, wenn:**
- Beschaffungswert < 10.000 EUR
- Keine Energierelevanz (z.B. einfache Büromöbel)
- Nur eine realistische Option (kein Vergleich möglich)

### Arbeitsschritte bei Relevanz

**Schritt 1: Energieeffizienzanforderungen formulieren**
- [ ] Höchste verfügbare EE-Klasse ermitteln (Marktrecherche)
- [ ] Ecolabel-Anforderungen setzen (optional)
- [ ] In Rahmenbedingungen (Kap. 1.3) oder Bedarf (Kap. 1.1) dokumentieren

**Schritt 2: Treibhausgasemissionen prognostizieren**
- [ ] Energieverbrauch pro Option ermitteln (Herstellerangaben, UBA-Daten)
- [ ] CO2-Faktor für Energieträger recherchieren (Strom, Gas, Öl, etc.)
- [ ] Emissionen über Betrachtungszeitraum berechnen
- [ ] Dokumentation in Kap. 5.1 (Annahmen)

**Schritt 3: CO2-Kosten berechnen**
- [ ] Aktuellen BEHG-CO2-Preis ermitteln (siehe Tabelle oben)
- [ ] CO2-Emissionen × CO2-Schattenpreis = Kostenfaktor
- [ ] In Kapitalwertberechnung (Kap. 5.2–5.5) einrechnen

**Schritt 4: Dokumentieren**
- [ ] Kap. 4 (Annahmen): CO2-Preis, Emissionsfaktoren, EE-Anforderungen
- [ ] Kap. 5 (Berechnung): CO2-Kostenberechnung pro Option
- [ ] Kap. 6 (Vergleich): Kapitalwertvergleich MIT CO2-Kosten
- [ ] Kap. 8 (optional): Nichtmonetäre Faktoren (z.B. Nachhaltigkeitszertifikate)

---

## 6. Konkrete Beispiele nach Maßnahmentyp

### A. Wärmeversorgung (Gebäude)

**Optionen:**
1. Gasheizung (alt): ca. 0,20 kg CO2/kWh
2. Gasheizung (neu, effizient): ca. 0,18 kg CO2/kWh
3. Wärmepumpe mit Grünstrom: ca. 0,05 kg CO2/kWh
4. Solar-Wärmepumpe: ca. 0,02 kg CO2/kWh

**Berechnung (100 m² Gebäude, 50 kWh/m²/Jahr = 5.000 kWh/Jahr):**
```
Option 1 (Gas alt):      5.000 kWh × 0,20 = 1.000 kg = 1,0 Tonne/Jahr
Option 2 (Gas neu):      5.000 kWh × 0,18 = 900 kg = 0,9 Tonne/Jahr
Option 3 (Wärmepumpe):   5.000 kWh ÷ 3,5 × 0,05 = 70 kg = 0,07 Tonne/Jahr
→ 10 Jahre × 55 EUR/Tonne
  Option 1: 100 Tonnen × 55 EUR = 5.500 EUR
  Option 2: 90 Tonnen × 55 EUR = 4.950 EUR
  Option 3: 7 Tonnen × 55 EUR = 385 EUR
```

### B. Fahrzeugbeschaffung

**Typische CO2-Emissionen (pro Fahrzeugklasse):**
```
Diesel-PKW:              ca. 0,25 kg CO2/km (200 g/km Normbedingungen)
Benzin-PKW:              ca. 0,27 kg CO2/km (215 g/km)
Hybrid-PKW:              ca. 0,15 kg CO2/km (120 g/km)
Elektro-PKW (Grünstrom): ca. 0,05 kg CO2/km (40 g CO2/km)
```

**Berechnung (10.000 km/Jahr, 10 Jahre):**
```
Diesel: 10.000 × 0,25 × 10 = 25.000 kg = 25 Tonnen → 1.375 EUR CO2-Kosten
Elektro: 10.000 × 0,05 × 10 = 5.000 kg = 5 Tonnen → 275 EUR CO2-Kosten
→ Ersparnis: 1.100 EUR durch CO2-Kostenersparnis
```

### C. Reinigungsdienstleistung (Fahrtkosten + Chemikalien)

**Emissionen pro Fahrtkilometer:**
```
Reinigungstransporte (Diesel-Van): ca. 0,25 kg CO2/km
Bio-Chemikalien: ca. 2 kg CO2/Liter
Standard-Chemikalien: ca. 3 kg CO2/Liter
```

**Berechnung (200 Fahrtkilometer/Monat, umweltfreundliche Chemikalien):**
```
Fahrtkilometer: 200 km/Monat × 12 = 2.400 km/Jahr
  CO2: 2.400 × 0,25 = 600 kg/Jahr = 0,6 Tonnen
  10 Jahre: 6 Tonnen × 55 EUR = 330 EUR CO2-Kosten

Bio-Chemikalien (10 Liter/Monat): 120 Liter/Jahr
  CO2: 120 × 2 kg = 240 kg/Jahr = 0,24 Tonnen
  10 Jahre: 2,4 Tonnen × 55 EUR = 132 EUR CO2-Kosten

TOTAL: 330 + 132 = 462 EUR CO2-Kosten für Öko-Option
→ Vs. Standard-Chemikalien: 330 + (2,4 × 3 = 7,2 Tonnen × 55) = 330 + 396 = 726 EUR
→ Öko-Option spart 264 EUR an CO2-Kosten!
```

---

## 7. Quellen und Referenzen

### Für Energiefaktoren und CO2-Daten:
- **Umweltbundesamt (UBA):** [www.umweltbundesamt.de](https://www.umweltbundesamt.de)
  - CO2-Faktoren für Strom, Gas, Öl
  - Ökobilanzdaten
  
- **BEHG CO2-Preise:** [Brennstoffemissionshandelsgesetz](https://www.bmwk.de)
  - Aktuelle und zukünftige CO2-Preise

- **KfW-Effizienzklassen:** [www.kfw.de](https://www.kfw.de)
  - Standards für Gebäude und Sanierung

### Für Zertifizierungen:
- **Blauer Engel:** [www.blauer-engel.de](https://www.blauer-engel.de)
- **EU-Ecolabel:** [www.eu-ecolabel.de](https://www.eu-ecolabel.de)

---

## Zusammenfassung: Nachhaltigkeitskriterien in WU

✅ **AVV Klima ist seit 01.01.2022 bindend** für Bundesbeschaffung ab 10.000 EUR

✅ **Zwei Kernaspekte:**
1. Energieeffizienz (höchste verfügbare Klasse)
2. Treibhausgasemissionen über Lebenszyklus (mit CO2-Schattenpreis monetär bewertet)

✅ **CO2-Schattenpreis 2025:** 55 EUR/Tonne CO2 (BEHG)

✅ **Integration in WU:**
- Bedarf (Kap. 1.1), Rahmenbedingungen (Kap. 1.3), oder nichtmonetäre Faktoren (Kap. 8)
- Annahmen (Kap. 4): CO2-Faktoren, EE-Anforderungen
- Berechnung (Kap. 5): CO2-Kosten in Kapitalwertberechnung
- Vergleich (Kap. 6): Gesamt-KW mit Nachhaltigkeitskosten

✅ **Fallbeispiele verfügbar:** Wärmeversorgung, Fahrzeuge, Dienstleistungen

