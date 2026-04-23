# Nachhaltigkeitskriterien — Praktisches Verfahren (Kurzfassung)

**NUR FÜR ÜBERJÄHRIGE WU RELEVANT (Dialogpfad B).**
Unterjährige WU: Nachhaltigkeitskriterien nicht erforderlich.

**Rechtliche Grundlage:** AR A-2400/62 § 7 Abs. 2 BHO + AVV Klima (seit 01.01.2022)

**Hintergrund:** AVV Klima formal bindend. In der Bundeswehr-Praxis aktuell nicht konsequent umgesetzt. Dieses Verfahren hält den Dialog **minimal** (User wählt nur: ja/ok/nein) und nutzt **recherchierte Standard-Werte** für jede Maßnahmenart.

---

## Dialog: Nur 2 Fragen

### Frage 1: Ist die Maßnahme energierelevant?

> „Ist diese Maßnahme energierelevant (Fahrzeug, Gebäude, Heizung, IT, Dienstleistung mit Fahrtkomponente)?"

- **JA** → Frage 2
- **NEIN** → Überspringen, fertig

### Frage 2: Sollen Nachhaltigkeitskriterien in WU berücksichtigt werden?

> „Sollen Treibhausgasemissionen monetär in der Kapitalwertberechnung berücksichtigt werden (AVV Klima)? 
> **Standardvorgehen:** Ich verwende recherchierte CO2-Werte für jede Option und rechne sie ein. 
> Sie müssen nur bestätigen oder ablehnen."

- **JA, nutze Standard-Annahmen** → Auto-Berechnung mit Werten unten
- **NEIN** → Nur dokumentieren (Kap. 8), nicht in KW rechnen
- **VIELLEICHT SPÄTER** → Überspringen, kann nachträglich ergänzt werden

---

## Auto-Berechnung: Standard-Werte nach Maßnahmentyp

**Wenn User "JA" sagt, verwende AUTOMATISCH diese recherchierten Werte:**

### 1. Wärmeversorung (Gebäude)

| Option | CO2-Faktor | Anmerkung |
|---|---|---|
| **Gasheizung (konventionell)** | 0,20 kg CO2/kWh | (inkl. Vorkette) |
| **Gasheizung (Brennwerttechnik)** | 0,18 kg CO2/kWh | (+10% effizienter) |
| **Fernwärme (Durchschnitt D)** | 0,15 kg CO2/kWh | (gemischte Erzeugung) |
| **Wärmepumpe + Grünstrom** | 0,05 kg CO2/kWh | (COP 3,5 angenommen) |
| **Solar-Wärmepumpe** | 0,02 kg CO2/kWh | (überwiegend Eigenstrom) |

**Energieverbrauch-Annahmen:**
- Neubau (KfW 55): 50 kWh/m²/Jahr
- Bestandssanierung: 100 kWh/m²/Jahr
- Bestand unsaniert: 150–200 kWh/m²/Jahr

**Beispiel-Berechnung automatisch:**
```
Maßnahme: Heizung für 500 m² Bürogebäude, 10 Jahre, Bestand

Option 1 (Gasheizung):
  Energieverbrauch: 500 m² × 150 kWh = 75.000 kWh/Jahr
  CO2: 75.000 × 0,20 = 15.000 kg = 15 Tonnen/Jahr
  10 Jahre: 150 Tonnen × 55 EUR = 8.250 EUR CO2-Kosten

Option 2 (Wärmepumpe + Grünstrom):
  Energieverbrauch: 500 m² × 75 kWh = 37.500 kWh/Jahr (effizienter)
  CO2: 37.500 × 0,05 = 1.875 kg = 1,875 Tonnen/Jahr
  10 Jahre: 18,75 Tonnen × 55 EUR = 1.031 EUR CO2-Kosten
  
→ CO2-Kostenersparnis: 8.250 - 1.031 = 7.219 EUR für Wärmepumpe
```

---

### 2. Fahrzeugbeschaffung

| Antriebsart | CO2-Emissionen | Quelle |
|---|---|---|
| **Diesel-PKW** | 0,25 kg CO2/km | (200 g/km Norm + Vorkette) |
| **Benzin-PKW** | 0,27 kg CO2/km | (215 g/km Norm + Vorkette) |
| **Hybrid-PKW** | 0,15 kg CO2/km | (120 g/km Norm + Vorkette) |
| **Elektro-PKW (Grünstrom)** | 0,05 kg CO2/km | (40 g/km + Strom) |
| **Elektro-PKW (Strommix)** | 0,08 kg CO2/km | (50 g/km + Strommix) |

**Nutzungs-Annahmen:**
- Dienst-PKW: 10.000–15.000 km/Jahr
- Fahrzeugtransporter: 20.000–30.000 km/Jahr
- Standard: 10.000 km/Jahr, 10 Jahre = 100.000 km

**Beispiel-Berechnung automatisch:**
```
Maßnahme: Dienst-PKW, 100.000 km über 10 Jahre

Option 1 (Diesel):
  100.000 km × 0,25 kg CO2/km = 25.000 kg = 25 Tonnen
  25 Tonnen × 55 EUR = 1.375 EUR CO2-Kosten

Option 2 (Elektro, Grünstrom):
  100.000 km × 0,05 kg CO2/km = 5.000 kg = 5 Tonnen
  5 Tonnen × 55 EUR = 275 EUR CO2-Kosten
  
→ CO2-Kostenersparnis: 1.100 EUR für Elektro
```

---

### 3. Dienstleistungen mit Fahrtkomponente (Reinigung, Wartung, Inspektionen)

| Transport-Modus | CO2-Faktor | Anmerkung |
|---|---|---|
| **Diesel-Van (üblich)** | 0,25 kg CO2/km | (Lieferverkehr) |
| **Hybrid-Van** | 0,15 kg CO2/km | (+40% effizienter) |
| **Elektro-Van (Grünstrom)** | 0,05 kg CO2/km | (klein e-Transporter) |

**Chemikalien:**
| Material | CO2-Faktor |
|---|---|
| Standard-Reiniger | 3–4 kg CO2/Liter |
| Bio-Reiniger / Öko-Produkte | 2–2,5 kg CO2/Liter |

**Beispiel-Berechnung automatisch:**
```
Maßnahme: Reinigungsdienstleistung, 200 Fahrtkilometer/Monat, 10 Jahre

Transport (Diesel-Van):
  200 km/Monat × 12 = 2.400 km/Jahr
  2.400 km/Jahr × 0,25 kg CO2/km = 600 kg = 0,6 Tonnen/Jahr
  10 Jahre: 6 Tonnen × 55 EUR = 330 EUR CO2-Kosten

Chemikalien (Standard, 10 L/Monat):
  10 L/Monat × 12 = 120 L/Jahr
  120 L × 3,5 kg CO2/L = 420 kg = 0,42 Tonnen/Jahr
  10 Jahre: 4,2 Tonnen × 55 EUR = 231 EUR CO2-Kosten

TOTAL Standard: 330 + 231 = 561 EUR

---

Alternativen:

Transport (Elektro-Van):
  2.400 km/Jahr × 0,05 kg CO2/km = 120 kg = 0,12 Tonnen/Jahr
  10 Jahre: 1,2 Tonnen × 55 EUR = 66 EUR

Chemikalien (Bio):
  120 L × 2,25 kg CO2/L = 270 kg = 0,27 Tonnen/Jahr
  10 Jahre: 2,7 Tonnen × 55 EUR = 149 EUR

TOTAL Öko-Variante: 66 + 149 = 215 EUR

→ CO2-Kostenersparnis: 346 EUR durch Öko-Option
```

---

### 4. IT / Rechenzentrum

| Komponente | CO2-Faktor |
|---|---|
| **Server (On-Premise, Standard-Strom)** | 0,40 kg CO2/kWh (Betrieb) |
| **Cloud-Lösung (Rechenzentrum, Grünstrom)** | 0,08 kg CO2/kWh (Betrieb) |
| **Produktion (durchschnittlich)** | 0,15 kg CO2/kg Gerätewicht |

**Beispiel-Berechnung automatisch:**
```
Maßnahme: Server/Speicherlösung 5 Jahre

Option 1 (On-Premise):
  Energieverbrauch: ca. 500 kW peak, ca. 2.000 kWh/Monat = 24.000 kWh/Jahr
  CO2: 24.000 × 0,40 = 9.600 kg = 9,6 Tonnen/Jahr
  5 Jahre: 48 Tonnen × 55 EUR = 2.640 EUR
  
  Plus Produktion (Hardware: ca. 50 kg): 50 × 0,15 = 7,5 kg = 7,5 kg CO2 (einmalig, vernachlässigbar)

Option 2 (Cloud, Grünstrom):
  Energieverbrauch (effizienter gemeinsam genutzt): ca. 800 kWh/Monat = 9.600 kWh/Jahr
  CO2: 9.600 × 0,08 = 768 kg = 0,768 Tonnen/Jahr
  5 Jahre: 3,84 Tonnen × 55 EUR = 211 EUR

→ CO2-Kostenersparnis: 2.429 EUR durch Cloud
```

---

## Dokumentation in der WU — Automatisch vorbereitet

**Wenn User zustimmt, werden diese Zeilen automatisch in die WU eingefügt:**

### Kap. 4 (Annahmen):
```
4.3 Annahmen für die Berechnung von Optionen

CO2-Schattenpreis (AVV Klima):
Nach dem Brennstoffemissionshandelsgesetz (BEHG) wird ein CO2-Schattenpreis 
von 55 EUR/Tonne CO2 (Stand 2025) für die Berechnung angesetzt. 
(Quelle: BMF, BEHG §10 Abs. 2)

Energieeffizienzsstandards:
- [Maßnahmentyp]: [CO2-Faktor Option 1], [CO2-Faktor Option 2], etc.
  (Grundlage: recherchierte Markstudien/UBA-Daten [Datum])
```

### Kap. 5.2 (Kapitalwertberechnung):
```
Unter Berücksichtigung der Treibhausgasemissionen ergeben sich folgende 
zusätzliche CO2-Kosten pro Option:

| Option | CO2-Emissionen (Tonnen) | CO2-Kosten (EUR) |
|---|---|---|
| Option 1 | [X Tonnen] | [X EUR] |
| Option 2 | [X Tonnen] | [X EUR] |
| Option [N] | [X Tonnen] | [X EUR] |

Diese CO2-Kosten werden in der Gesamtkapitalwertberechnung (Kap. 5.5) berücksichtigt.
```

### Kap. 5.5 (Kapitalwert mit Risiko + CO2):
```
| Option | KW ohne Risiko | CO2-Kosten | Gesamtkapitalwert |
|---|---|---|---|
| Option 1 | [X EUR] | [X EUR] | [X EUR] |
| Option 2 | [X EUR] | [X EUR] | [X EUR] |
```

### Kap. 8 (Nichtmonetäre Faktoren):
```
Energieeffizienz und Nachhaltigkeit:

Nach AVV Klima wurden Treibhausgasemissionen monetär in der Kapitalwertberechnung 
berücksichtigt (siehe Kap. 4, 5). 

Zusätzlich zu den CO2-Kosten werden folgende nichtmonetäre Faktoren berücksichtigt:

| Kriterium | Option 1 | Option 2 | Gewicht |
|---|---|---|---|
| Energieeffizienzklasse | [z.B. KfW 70] | [z.B. KfW 55] | Mittel |
| Erneuerbare Energieträger | [Nein] | [Ja, 100% Grünstrom] | Mittel |
| Umweltzeichen | [Keine] | [Blauer Engel] | Niedrig |

Option [X] erfüllt die Nachhaltigkeitskriterien besser.
```

---

## Checkliste: Was passiert automatisch?

✅ **User sagt JA** → Ich:
1. Recherchiere CO2-Faktoren für **diese Maßnahmenart** (basierend auf Sachverhalt)
2. Schlage konkrete Werte vor: „Option 1 (Gas): 0,20 kg CO2/kWh, Option 2 (Wärmepumpe): 0,05 kg CO2/kWh"
3. Berechne CO2-Kosten automatisch mit 55 EUR/Tonne (aktueller BEHG-Standard)
4. Rechne CO2-Kosten in Kapitalwertberechnung (Kap. 5.5) ein
5. Dokumentiere in Kap. 4, 5, 8 automatisch

❌ **User sagt NEIN** → Ich:
1. Überspringe CO2-Kosten in KW-Berechnung
2. Dokumentiere in Kap. 8 (nichtmonetär): „Nachhaltigkeitsaspekte wurden nicht monetär bewertet"
3. Fertig.

⏸️ **User sagt VIELLEICHT SPÄTER** → Ich:
1. Notiere: „[CO2-Berechnung offen]" in Entwurf
2. Kann User nach Export nachtragen

---

## Quellen für Standard-Werte

- **Wärme:** UBA-Datenbank, KfW-Standards
- **Fahrzeuge:** ADAC CO2-Emissionsfaktoren, EU-Norm
- **Dienstleistungen:** Logistik-Branchenstandards
- **IT:** Rechenzentrum-Benchmarks
- **CO2-Preis:** BEHG (aktuell 55 EUR/Tonne 2025)

Alle Werte sind **recherchiert und dokumentierbar**, User muss keine Eigenrecherche betreiben.

---

## Summe: Der Dialog

```
ICH: "Energierelevant? (Fahrzeug, Gebäude, Heizung, Dienstleistung mit Fahrtanteil)"
USER: "Ja, Heizung"

ICH: "Sollen CO2-Emissionen monetär berücksichtigt werden (AVV Klima)? 
     Ich verwende Standard-Werte — Sie müssen nur bestätigen."
USER: "Ok, ja"

ICH: [Auto-Berechnung mit recherchierten Werten]
     "Ich verwende:
      - Gasheizung: 0,20 kg CO2/kWh (UBA 2024)
      - Wärmepumpe: 0,05 kg CO2/kWh (mit Grünstrom, UBA 2024)
      - CO2-Preis: 55 EUR/Tonne (BEHG 2025)
      
      Ergebnis: Option 1 kostet 8.250 EUR CO2-Kosten, 
                Option 2 kostet 1.031 EUR CO2-Kosten
      
      → Option 2 spart 7.219 EUR CO2-Kosten."

USER: "Ok"

ICH: [Automatisch in Kap. 5.5 einrechnen + dokumentieren]
```

**Mehr nicht.**

