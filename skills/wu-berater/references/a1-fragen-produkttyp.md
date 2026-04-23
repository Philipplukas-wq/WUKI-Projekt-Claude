# A1 Bedarfsforderung: Produkttyp-abhängige Fragen

**Ziel:** Die 8 A1-Fragen flexibel an verschiedene Produkttypen anpassen (Bürogeräte, Fahrzeuge, Gartenpflege, Möbel, Liegenschaften).

---

## Schritt 1: Produkttyp klassifizieren (aus Kaufbeschreibung)

```python
def classify_product_type(kaufbeschreibung):
    """
    Klassifiziert Produkt in eine Kategorie für kontextabhängige Fragen.
    """
    kaufbeschreibung_lower = kaufbeschreibung.lower()
    
    # KATEGORIE A: BÜROGERÄTE
    if any(word in kaufbeschreibung_lower for word in ['drucker', 'laptop', 'rechner', 'computer', 'monitor', 'scanner', 'kopier', 'fax']):
        return 'bürogeräte'
    
    # KATEGORIE B: FAHRZEUGE
    if any(word in kaufbeschreibung_lower for word in ['transporter', 'auto', 'fahrzeug', 'lkw', 'pkw', 'bus']):
        return 'fahrzeuge'
    
    # KATEGORIE C: GARTENPFLEGE
    if any(word in kaufbeschreibung_lower for word in ['rasenmäher', 'kettensäge', 'laubsauger', 'vertikutierer', 'gartenpflege', 'rasen']):
        return 'gartenpflege'
    
    # KATEGORIE D: MÖBEL & EINRICHTUNG
    if any(word in kaufbeschreibung_lower for word in ['stuhl', 'tisch', 'schrank', 'regale', 'möbel', 'schreibtisch']):
        return 'möbel'
    
    # KATEGORIE E: LIEGENSCHAFTEN & INFRASTRUKTUR
    if any(word in kaufbeschreibung_lower for word in ['liegenschaft', 'gebäude', 'raum', 'fläche', 'immobilie']):
        return 'liegenschaft'
    
    # KATEGORIE F: WERKZEUGE & KLEINGERÄTE
    if any(word in kaufbeschreibung_lower for word in ['werkzeug', 'bohrmaschine', 'säge', 'multitool', 'kompressor']):
        return 'werkzeuge'
    
    # Default
    return 'sonstiges'
```

---

## Schritt 2: Produkttyp-abhängige Fragen

### KATEGORIE A: BÜROGERÄTE (Drucker, Laptop, etc.)

**8 Fragen (Original):**

1. **FUNKTIONEN** — Welche brauchst du?
   - [ ] Nur Druck  [ ] Druck+Kopie  [ ] Druck+Kopie+Scan  [ ] Alle
   - *oder* [ ] Nicht relevant

2. **KAPAZITÄT ZEITSPANNE** — Pro Monat oder Jahr?
   - [ ] Monat  [ ] Jahr

3. **KAPAZITÄT MENGE** — Wie viel?
   - [Eingabe] Seiten/Monat (oder: Dokumente/Jahr)

4. **FARBE** — Farbdruck?
   - [ ] Ja, CMYK  [ ] Gelegentlich  [ ] Nein, s/w
   - *oder* [ ] Nicht relevant

5. **NETZWERK** — Erforderlich?
   - [ ] Ja, erforderlich  [ ] Optional  [ ] Nein
   - *oder* [ ] Nicht relevant

6. **EINSATZHÄUFIGKEIT** — Wie oft?
   - [ ] Täglich  [ ] 3–4x/Woche  [ ] 1–2x/Woche  [ ] Sporadisch

7. **EINSATZTAGE/JAHR** — Ungefähr?
   - [Eingabe] Tage/Jahr (Standard: 220 für Büro Mo–Fr)

8. **ZUSATZ** — Besonderheiten?
   - [ ] Duplex  [ ] A3-Format  [ ] Hohe Geschwindigkeit  [ ] Keine
   - *oder* [ ] Nicht relevant

---

### KATEGORIE B: FAHRZEUGE (Transporter, PKW, etc.)

**Angepasste Fragen:**

1. **FAHRZEUGTYP** — Was für ein Fahrzeug?
   - [ ] Transporter (Ladefläche)  [ ] PKW (Personentransport)  [ ] Bus/Kleinbus  [ ] Spezialfahrzeug (z.B. Kühlfahrzeug)

2. **LADEFLÄCHE/KAPAZITÄT** — Ungefähre Größe?
   - [Eingabe] Kubikmeter (oder: Kg Tragfähigkeit, oder: Sitzplätze)

3. **JAHRESFAHRLEISTUNG** — Wie viele km/Jahr?
   - [Eingabe] km/Jahr (z.B. 15.000, 50.000)

4. **EINSATZHÄUFIGKEIT** — Wie oft pro Woche?
   - [ ] Täglich  [ ] 3–4x/Woche  [ ] 1–2x/Woche  [ ] Nach Bedarf (unregelmäßig)

5. **EINSATZTAGE/JAHR** — Anzahl Tage?
   - [Eingabe] Tage/Jahr (z.B. 220, 250, 365)

6. **MOTORTYP** — Verbrennungs- oder Elektrofahrzeug?
   - [ ] Verbrennungsmotor (Benzin/Diesel)  [ ] Elektrisch  [ ] Hybrid  [ ] Egal

7. **SPEZIALANFORDERUNGEN** — Besonderheiten?
   - [ ] Kühlbox erforderlich  [ ] GPS/Telemetrie  [ ] Besondere Sicherheitsausstattung  [ ] Keine

8. **NICHT RELEVANT** — Alle Antworten vorhanden?
   - [ ] Ja, fertig  [ ] Noch weitere Infos erforderlich

---

### KATEGORIE C: GARTENPFLEGE (Rasenmäher, Kettensäge, etc.)

**Angepasste Fragen:**

1. **GERÄTETYP & FUNKTIONEN** — Was für Funktionen?
   - Rasenmäher: [ ] Mulchen  [ ] Fangkorb  [ ] Handgerät  [ ] Motorgetrieben
   - Kettensäge: [ ] Handgerät  [ ] Elektro  [ ] Benzin-Motor
   - Laubsauger: [ ] Nur Saugen  [ ] Saugen+Blasen  [ ] Mulch-Funktion

2. **FLÄCHE/KAPAZITÄT** — Arbeitsumfang?
   - [Eingabe] Quadratmeter/Saison (z.B. 5.000 qm für Rasenmäher)
   - *oder* [Eingabe] lfd. Meter (für Kettensäge)

3. **SAISON/EINSATZZEIT** — Wie lange pro Jahr?
   - [Eingabe] Monate (z.B. April–Oktober = 7 Monate) ODER Tage/Jahr
   - (für Gartenpflege oft saisonal, nicht ganzjährig)

4. **EINSATZHÄUFIGKEIT** — Wie oft pro Woche/Monat?
   - [ ] 1x/Woche  [ ] 2x/Woche  [ ] 1–2x/Monat  [ ] Nach Bedarf

5. **EINSATZTAGE/JAHR** — Ungefähre Tage?
   - [Eingabe] Tage/Jahr (Standard für Rasenmäher: 20 Tage, April–Oktober)

6. **MOTORTYP** — Handbetrieb oder Motor?
   - [ ] Handbetrieb (manuell)  [ ] Elektro (Kabel)  [ ] Akku/Batterie  [ ] Benzin-Motor

7. **SPEZIALANFORDERUNGEN** — Besonderheiten?
   - [ ] Mulch-Funktion  [ ] Selbstfahrer (Rasenmäher)  [ ] Lange Lebensdauer (5+ Jahre)  [ ] Leise Betrieb  [ ] Keine

8. **NICHT RELEVANT** — Alles klar?
   - [ ] Ja, weiter  [ ] Noch Fragen

---

### KATEGORIE D: MÖBEL & EINRICHTUNG (Stühle, Schränke, etc.)

**Angepasste Fragen:**

1. **MÖBELTYP & FUNKTION** — Was für Möbel?
   - [ ] Arbeitsplatz-Sitzplatz  [ ] Konferenz-Stuhl  [ ] Schrank/Regal  [ ] Schreibtisch  [ ] Sonstiges

2. **MENGE** — Wie viele Stück?
   - [Eingabe] Anzahl (z.B. 5 Stühle, 1 Schrank)

3. **ABMESSUNGEN/EIGENSCHAFTEN** — Größe/Spezifikationen?
   - [Eingabe] z.B. "Höhe 180cm, Breite 80cm" oder "für 10 Personen"

4. **EINSATZBEREICH** — Wo werden die Möbel benutzt?
   - [ ] Dauerhaft im Büro  [ ] Lagerbereiche  [ ] Kantine/Aufenthaltsraum  [ ] Flure/öffentlich  [ ] Mobil/flexibel

5. **NUTZUNGSDAUER** — Wie lange Lebensdauer erforderlich?
   - [ ] 5 Jahre  [ ] 10 Jahre  [ ] 15+ Jahre  [ ] Unbegrenzt

6. **BESONDERE ANFORDERUNGEN** — Spezialanforderungen?
   - [ ] Ergonomisch zertifiziert  [ ] Höhenverstellbar  [ ] Behindertengerecht  [ ] Brand-/Verschleißfestigkeit  [ ] Keine

7. **FARBE/DESIGN** — Vorgaben?
   - [ ] Farbvorgabe (welche: _______)  [ ] Design-Standard (z.B. modular)  [ ] Keine Vorgabe

8. **NICHT RELEVANT** — Alles beantwortet?
   - [ ] Ja, genug Info  [ ] Weitere Details erforderlich

---

### KATEGORIE E: LIEGENSCHAFTEN & INFRASTRUKTUR (Gebäude, Raum, etc.)

⚠️ **Hinweis:** Liegenschaften sind oft überjährig (Dialogpfad B) — nur unterjährig, wenn z.B. Raummiete, provisorische Fläche.

**Angepasste Fragen:**

1. **LIEGENSCHAFTSTYP** — Was wird benötigt?
   - [ ] Bürofläche  [ ] Lagerfläche  [ ] Spezialraum (z.B. Labor)  [ ] Parkplatz  [ ] Sonstiges

2. **FLÄCHE** — Größe?
   - [Eingabe] Quadratmeter (z.B. 100 qm)

3. **STANDORT** — Geografische Anforderung?
   - [Eingabe] Stadt/Region oder Nähe zu Standort

4. **NUTZUNGSDAUER** — Wie lange?
   - [ ] Bis Jahresende  [ ] 1 Jahr  [ ] 2–3 Jahre  [ ] Länger (→ evtl. Dialogpfad B)

5. **EINSATZTAGE/JAHR** — Auslastung?
   - [Eingabe] Tage/Jahr oder % Auslastung

6. **SPEZIALAUSSTATTUNG** — Was wird benötigt?
   - [ ] Strom/Wasser/Gas  [ ] Heizung/Kühlung  [ ] Internetanbindung  [ ] Sicherheit (Alarm)  [ ] Keine

7. **MIETUNG vs. KAUF** — Ist Miete denkbar?
   - [ ] Nur Kauf  [ ] Miete wäre auch okay  [ ] Egal

8. **NICHT RELEVANT** — Klar?
   - [ ] Ja, weiter  [ ] Noch Fragen

---

### KATEGORIE F: WERKZEUGE & KLEINGERÄTE (Bohrmaschine, Säge, etc.)

**Angepasste Fragen:**

1. **GERÄTETYP & FUNKTIONEN** — Welche Funktionen?
   - [Auswahl je nach Gerät, z.B. für Bohrmaschine: Schlag-Funktion, Drehmoment, etc.]

2. **KAPAZITÄT** — Leistung/Größe?
   - [Eingabe] z.B. "500 Watt", "Spannbereich 0–13 mm", "Max. Schnittkraft"

3. **EINSATZHÄUFIGKEIT** — Wie oft pro Woche/Monat?
   - [ ] Täglich  [ ] 2–3x/Woche  [ ] 1x/Woche  [ ] Gelegentlich

4. **EINSATZTAGE/JAHR** — Ungefähre Tage?
   - [Eingabe] Tage/Jahr

5. **STROMVERSORGUNG** — Kabel, Akku oder Benzin?
   - [ ] Kabelgebunden (230V)  [ ] Akku/Batterie  [ ] Benzin-Motor  [ ] Egal

6. **ROBUSTHEIT** — Wie robust muss es sein?
   - [ ] Gelegentliche Nutzung (Hobby)  [ ] Regelmäßige Nutzung (Handwerk)  [ ] Intensiv (Dauereinsatz)

7. **ZUSATZAUSSTATTUNG** — Besonderheiten?
   - [ ] Koffer/Transport-Box  [ ] Ersatz-Akkus  [ ] Zubehör-Set  [ ] Keine

8. **NICHT RELEVANT** — Alles klar?
   - [ ] Ja, genug Info  [ ] Weitere Details

---

## Schritt 3: Fallback-Annahmen pro Kategorie

Wenn User vage antwortet, werden Standardannahmen pro Kategorie verwendet:

### BÜROGERÄTE (Drucker/Laptop)
```
✓ Funktionen: Druck+Kopie (Drucker) / Standard-Rechenleistung (Laptop)
✓ Kapazität: 10.000 S./Monat (Drucker) / 10 GB Speicher (Laptop)
✓ Farbe: Ja
✓ Netzwerk: Ja
✓ Einsatzhäufigkeit: Täglich, Mo–Fr
✓ Einsatztage/Jahr: 220 Tage
```

### FAHRZEUGE (Transporter)
```
✓ Fahrzeugtyp: Transporter
✓ Ladefläche: 8–10 qm (Standard)
✓ Jahresfahrleistung: 15.000 km/Jahr
✓ Einsatzhäufigkeit: 2–3x/Woche
✓ Einsatztage/Jahr: 100–120 Tage
✓ Motortyp: Verbrennungsmotor (Diesel)
```

### GARTENPFLEGE (Rasenmäher)
```
✓ Gerätetyp: Rasenmäher mit Motorantrieb
✓ Fläche: 5.000 qm/Saison
✓ Saison: April–Oktober (7 Monate)
✓ Einsatzhäufigkeit: 1–2x/Woche
✓ Einsatztage/Jahr: 20–25 Tage (Saison)
✓ Motortyp: Benzin-Motor (Standard)
```

### MÖBEL (Bürostühle)
```
✓ Möbeltyp: Arbeitsplatz-Sitzplatz
✓ Menge: 5 Stück (typisch für Büro)
✓ Lebensdauer: 10 Jahre (Standard Büromöbel)
✓ Einsatzbereich: Dauerhaft im Büro
✓ Ergonomie: Ja, zertifiziert
```

### LIEGENSCHAFTEN (Bürofläche)
```
✓ Liegenschaftstyp: Bürofläche
✓ Fläche: 100 qm
✓ Standort: am aktuellen Standort
✓ Nutzungsdauer: 1 Jahr
✓ Auslastung: 80 % (ca. 200 Tage/Jahr)
```

### WERKZEUGE (Bohrmaschine)
```
✓ Gerätetyp: Akku-Bohrschrauber
✓ Kapazität: 18 V Akku
✓ Einsatzhäufigkeit: 2–3x/Woche
✓ Einsatztage/Jahr: 50 Tage
✓ Stromversorgung: Akku (mobil)
```

---

## Schritt 4: Bedarfsforderung-Generierung pro Kategorie

Nach Dialog werden Bedarfsforderungen kategoriespezifisch generiert:

### BÜROGERÄTE (Drucker)
> „Die [Dienststelle] benötigt eine Druck- und Kopierfunktionalität zur Unterstützung der Büroprozesse. Der Bedarf umfasst eine Kapazität von mindestens 10.000 Seiten pro Monat mit Mindestanforderungen: Farbdruck (CMYK), Netzwerkanbindung (LAN/WLAN). Das Gerät ist voraussichtlich täglich während der Regelarbeitszeit (Mo–Fr, 220 Tage/Jahr) einzusetzen."

### FAHRZEUGE (Transporter)
> „Die [Dienststelle] benötigt eine Transportfähigkeit zur Beförderung von Material und Personal. Der Bedarf umfasst ein Nutzfahrzeug mit Mindestanforderungen: Ladefläche mindestens 8 m³, Tragfähigkeit mindestens 1.000 kg, 2 Sitzplätze. Das Fahrzeug ist voraussichtlich 2–3 mal pro Woche in Logistikfahrten zu etwa 15.000 km/Jahr einzusetzen."

### GARTENPFLEGE (Rasenmäher)
> „Die [Dienststelle] benötigt eine Grünflächenpflege-Kapazität zur Unterhaltung der Liegenschaftsflächen. Der Bedarf umfasst eine Rasenmaschine mit Mindestanforderungen: Antrieb motorisiert (Benzin- oder Elektroantrieb), Arbeitsbreite mindestens 50 cm, Kapazität mindestens 5.000 qm pro Saison. Das Gerät ist voraussichtlich während der Vegetationsperiode (April–Oktober, ca. 20 Einsatztage/Jahr) einzusetzen."

### MÖBEL (Bürostühle)
> „Die [Dienststelle] benötigt Sitzmöbel zur ergonomischen Ausstattung der Arbeitsplätze. Der Bedarf umfasst [Anzahl] Bürostühle mit Mindestanforderungen: Höhenverstellbarkeit, Rückenlehnen-Neigung, ergonomische Zertifizierung (DIN EN 1335). Die Möbel sind für den Dauereinsatz im Bürobereich vorgesehen und sollten eine Lebensdauer von mindestens 10 Jahren aufweisen."

---

## Integration in Dialogpfad A

```
SKILL (Phase 1 → A1):
1. Aus Kaufbeschreibung Produkttyp klassifizieren: classify_product_type()
2. Produkttyp-kategorieabhängige Fragen laden (8 Fragen)
3. Dialog führen mit kontextabhängigen Fragen
4. Fallback-Annahmen pro Kategorie nutzen
5. Bedarfsforderung kategoriespezifisch generieren
```

**In dialogpfad-a.md anpassen:**
- A1-Dialog verweist auf `a1-fragen-produkttyp.md`
- `intelligenter_a2_default()` wird mit Produkttyp-Info aufgerufen
- Fallback-Annahmen werden aus Kategorie-Mapping geladen
