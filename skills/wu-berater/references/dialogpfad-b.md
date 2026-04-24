# Dialogpfad B: Überjährige WU

Für **mehrjährige Betrachtungen, Investitionen, komplexe Fälle** (9 Pflichtgliederungspunkte der AR A-2400/62).

**Modi**: Geführter Dialog (Schritt für Schritt) oder Schnelldurchlauf (alle Schritte auf einmal).

---

## Phase 0: Input-Validierung (Punkt 5)

**VOR dialogpfad-b startet: Validate dass Startdialog-Eingaben brauchbar sind**

```python
def validate_startdialog_input(dienststelle, sachverhalt, betrachtungszeitraum):
    """
    Prüft Eingaben aus SKILL.md bevor B startet.
    """
    errors = []
    
    # CHECK 1: Dienststelle (2–50 Zeichen, nicht leer)
    if not dienststelle or len(dienststelle) < 2 or len(dienststelle) > 50:
        errors.append("❌ Dienststelle: mindestens 2, maximal 50 Zeichen erforderlich")
    
    # CHECK 2: Sachverhalt (mindestens 10 Zeichen, nicht zu vage)
    if not sachverhalt or len(sachverhalt) < 10:
        errors.append("❌ Sachverhalt: zu kurz oder zu vage. Bitte konkretisieren (mind. 10 Zeichen)")
    if any(word in sachverhalt.lower() for word in ['xxx', 'test', 'asdf', 'keine ahnung']):
        errors.append("⚠️ Sachverhalt wirkt unvollständig. Bitte konkretisieren.")
    
    # CHECK 3: Betrachtungszeitraum (mindestens 2 Jahre)
    try:
        jahre = int(betrachtungszeitraum)
    except ValueError:
        errors.append("❌ Betrachtungszeitraum: Ungültiges Format. Bitte Zahl eingeben (z.B. 5, 10)")
        return errors
    
    if jahre < 2:
        errors.append(f"❌ Betrachtungszeitraum {jahre} Jahren zu kurz. Minimum: 2 Jahre (Dialogpfad B braucht ≥2 Jahre)")
    elif jahre > 30:
        errors.append(f"⚠️ Betrachtungszeitraum {jahre} Jahre sehr lang. Typisch: 5–15 Jahre. Sicher?")
    
    return errors

# Verwendung
errors = validate_startdialog_input(dienststelle, sachverhalt, betrachtungszeitraum)
if errors:
    for error in errors:
        print(error)
    print("\nBitte Eingaben korrigieren bevor wir B-Dialog starten.")
else:
    print("✅ Eingaben validiert, starten B-Dialog")
```

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
| 1.1 | Funktionale Bedarfsforderung (qualitativ + quantitativ) | **a1-fragen-produkttyp.md** (Punkt 1) + Kap. 1.1 | **Inline-Check** (`validate_step('bedarfsforderung', ...)`) |
| 1.2 | Bedarfsprognose (Entwicklung über Betrachtungszeitraum) | **bedarfsprognose-methode.md** + satzmuster-b.md Kap. 1.2 | — |
| 1.3 | Rahmenbedingungen (nur optionsausschließend) — **ACHTUNG: Wird iterativ ergänzt bei Aussonderung (Kap. 3.2)** | **satzmuster-b.md Kap. 1.3 + konkrete Beispiele** | — |
| 2.1–2.7 | Ausgangslage: Ablauf-, Aufbauorganisation, Personal, Material, Infrastruktur, DL, Einnahmen | Kap. 2.1–2.6 | — |
| 2.8 | Haushalterische Darstellung (automatisch berechnen) | Python-Snippet | — |
| 3.1 | Grundsätzlich mögliche Optionen (2–3 Sätze je Option) | Kap. 3.1 | — |
| 3.2 | Aussonderung ungeeigneter Optionen (**Pflichtprüfung**: kein Personal, Haushaltsmittel, Dienstposten, Infrastruktur als Grund!) — **RÜCKKOPPLUNG: Wenn neue RB benötigt, zu Kap. 1.3 ergänzen** | Kap. 3.2 + SKILL.md | **Guard Check mit Kontext** (Punkt 3: Negations-Handling, Grund-Prüfung) |
| 3.3 | Ausführliche Darstellung geeigneter Optionen (je 3.3.x.1–3.3.x.7) | Kap. 3.3.x | — |
| 4.1–4.2 | Annahmen (alle / bestimmte Optionen) | Kap. 4.1–4.2 | — |
| 5.2 | Kapitalwertberechnung (Berechnungsskript verwenden) | Kap. 5.2 | — |
| 5.3 | Kapitalwerte ohne Risiko | Kap. 5.3 | — |
| 5.4 | Risikobetrachtung (Identifizierung, Verteilung, Monetäre Bewertung) | **risikobetrachtung-konkret.md** | — |
| 5.5 | Kapitalwert mit Risiko | Kap. 5.5 | — |
| 6 | Vergleich der Optionen (Tabelle + Einleitungssatz) | Kap. 6 | — |
| 7 | Sensitivitätsanalyse (automatisch berechnen) | Python-Snippet | — |
| 8 | Nichtmonetäre Faktoren / Nutzwertanalyse | satzmuster-b.md Kap. 8 + **nachhaltigkeitskriterien-avv-klima.md** (wenn relevant) | — |
| 9 | Entscheidungsvorschlag (Empfehlung + Begründung) | Kap. 9 | **Vor Export**: `quick_validate()` + `export_safe()` |

---

## Bedarfsprognose (Kap. 1.2)

Siehe detaillierte Referenz: **`bedarfsprognose-methode.md`**

Dialog-Logik (Standard → Ausnahme):
1. **FRAGE:** "Bleibt der Bedarf über [Betrachtungszeitraum] konstant?"
   - **JA (Standard)** → Quelle = Ausgangslage (Kap. 2), einfacher Satz
   - **NEIN (Ausnahme)** → User nennt jährliche Bedarfe + Quelle → Tabelle erstellen
2. **Quelle dokumentieren:**
   - Konstant: Verweis auf Kap. 2
   - Variabel: Schriftliche Quelle (Mail, Beschluss, Stellungnahme) beifügen
   - **Fallback:** Wenn User keine Quelle kennt → Vorschlag: Fachbereich-Aussage per Mail

---

## AVV Klima — Nachhaltigkeitskriterien (Praktisches Verfahren)

**NUR RELEVANT FÜR ÜBERJÄHRIGE WU (diesen Dialogpfad).**
Unterjährige WU: nicht erforderlich.

Siehe: **`nachhaltigkeitskriterien-praktisch.md`**

**Dialog mit User — Nur 2 Fragen (User wählt: ja/nein/später):**

```
FRAGE 1: "Ist diese Maßnahme energierelevant 
         (Fahrzeug, Gebäude, Heizung, IT, Dienstleistung mit Fahrtanteil)?"
         → JA: Frage 2 | NEIN: überspringen

FRAGE 2: "Sollen CO2-Emissionen monetär in der WU berücksichtigt werden? 
         Ich verwende recherchierte Standard-Werte — Sie bestätigen nur."
         → JA: Auto-Berechnung | NEIN: nur dokumentieren | SPÄTER: auslassen
```

**Wenn JA:**
- Ich recherchiere CO2-Faktoren für **diese Maßnahmenart** (z.B. "Heizung" → Gasheizung 0,20 kg CO2/kWh, Wärmepumpe 0,05 kg CO2/kWh)
- Schlage konkrete Werte vor mit Quelle (UBA 2024, ADAC, etc.)
- Berechne CO2-Kosten automatisch (55 EUR/Tonne BEHG 2025)
- Rechne in Kapitalwertberechnung (Kap. 5.5) ein
- Dokumentiere in Kap. 4, 5, 8 automatisch

---

## Korrektur-Workflow (Punkt 4)

**Szenario 1: User korrigiert Kap. 1.1 (Bedarfsforderung)**
```
USER: „Die Bedarfsforderung stimmt nicht"
SKILL: „Welcher Teil ändert sich? Bedarf? Prognose? Rahmenbedingungen?"

→ User korrigiert spezifisches Kapitel
→ AUTOMATISCH NEU BERECHNEN:
   - Kap 3.3.x (Optionen): Kostenkalkulationen neu anpassen
   - Kap 5.2, 5.3, 5.5 (Kapitalwerte): Neu berechnen
   - Kap 6, 7, 9: Neu generieren (Vergleich, Sensitivität, Entscheidung)
→ User BESTÄTIGT Bedarfsforderung, Rest wird auto-aktualisiert
```

**Szenario 2: User korrigiert Kap. 3.2 (Aussonderung)**
```
USER: „Ein anderer Grund ist relevanter"
SKILL: „Welche Option wird anders beurteilt? Beschreibung anpassen"

→ Kap 3.2 wird angepasst
→ AUTOMATISCH NEU:
   - Kap 3.3: Geeignete Optionen neu berechnen (weniger/mehr Optionen?)
   - Kap 5.2, 5.3, 5.5: Kapitalwerte für neue Optionenmenge
   - Kap 6, 9: Vergleich und Entscheidung neu generieren
→ Keine Neubestätigung von Kap. 1–2 nötig
```

**Szenario 3: User korrigiert Kap. 4 (Annahmen)**
```
USER: „Der Zinssatz sollte 1.5% sein, nicht 1.2%"
SKILL: „Annahme ändern und neu berechnen"

→ Kap. 4 wird angepasst
→ AUTOMATISCH NEU:
   - Kap 5.2, 5.3, 5.5: Kapitalwerte mit neuem Zinssatz
   - Kap 6, 7, 9: Vergleich und Sensitivität neu generieren
→ Kosten (Kap. 3.3) bleiben gleich
```

**Allgemeine Regel:**
```
Nach jeder Korrektur:
  1. Betroffenes Kapitel wird angepasst
  2. Abhängige Kapitel werden AUTO-AKTUALISIERT (nicht erneut bestätigen)
  3. VOR RE-EXPORT: 6-Punkt-Validierung läuft erneut
```

---

## Infrastruktur-Kostenberechnung (Kap. 2.5 + 3.3.5)

Siehe detaillierte Referenz: **`infrastruktur-kostenberechnung.md`**

Kurzzusammenfassung für Dialog:
- **Bundessicht-Standard:** Kaltmiete NICHT ansetzen
- **Ansetzen:** Bauunterhalt (15 % Kaltmiete) + BImA-Verwaltung (4 % Kaltmiete) + Medienverbräuche
- **Medienverbräuche-Pauschal:** ca. 30–53 EUR/m²/Jahr (oder konkret messen)
- **Rechenweg MUSS dokumentiert werden** in jedem Kapitel (2.5 und 3.3.5)

---

## WebRecherche-Plausibilitätsprüfung (Punkt 6)

**Bei Kostenrecherchen (Kap. 3.3): Automatisch prüfen ob Preise realistisch sind**

```python
# Normal-Kostenbereiche pro Leistungstyp (€/Jahr oder €/Einheit)
normal_ranges = {
    # Dienstleistungen
    'Reinigung': (50, 200),  # EUR/m²/Jahr
    'Bewachung': (40, 120),  # EUR/m²/Jahr
    'IT-Support': (50, 500),  # EUR/Benutzer/Jahr
    'Wartung': (30, 300),  # EUR/Gerät/Jahr
    
    # Investitionen
    'Fahrzeuge': (20000, 100000),  # EUR/Stück
    'Gebäude': (500, 5000),  # EUR/m²
    'IT-Infrastruktur': (100, 10000),  # EUR/Arbeitsplatz
}

def plausibilitaet_pruefen_kosten(kostenart, geschaetzter_preis, einheit='EUR'):
    """
    Prüft ob recherchierter Preis realistisch ist (Punkt 6).
    """
    if kostenart not in normal_ranges:
        return None  # Keine Referenz vorhanden
    
    min_range, max_range = normal_ranges[kostenart]
    
    if geschaetzter_preis < min_range:
        print(f"⚠️ WARNUNG: {kostenart} {geschaetzter_preis:.2f} {einheit} ist ungewöhnlich niedrig.")
        print(f"   Normal für {kostenart}: {min_range}–{max_range} {einheit}")
        user_confirm = input("Trotzdem verwenden? [Ja/Nein]: ")
        return user_confirm.lower() == 'ja'
    
    elif geschaetzter_preis > max_range * 2:
        print(f"⚠️ WARNUNG: {kostenart} {geschaetzter_preis:.2f} {einheit} ist ungewöhnlich hoch (Ausreißer).")
        print(f"   Normal für {kostenart}: {min_range}–{max_range} {einheit}")
        print(f"   Mögliche Ursachen: Spezialleistung, Premium-Angebot, Fehler in Recherche?")
        user_confirm = input("Trotzdem verwenden? [Ja/Nein]: ")
        return user_confirm.lower() == 'ja'
    
    return True  # Preis im normalen Range

# Verwendung in Kap. 3.3
preis_ok = plausibilitaet_pruefen_kosten('Reinigung', 120, 'EUR/m²/Jahr')
if not preis_ok:
    print("Bitte Kostenpreis überprüfen oder nochmal recherchieren")
else:
    print("✅ Kostenpreis akzeptiert")
```

---

## Kapitalwertberechnung (5.2) — Strukturierter Dialog

**Ziel:** Pro verbleibender Option (nach Aussonderung in Kap. 3.2) alle Kostenpositionen, Einnahmen und Risiken erfassen.

**Kategorie-Standard-Preissteigerungsraten** (aus Kap. 4.1-4.2 / Parameter-Blatt):
| Kategorie | Standard PSR |
|---|---|
| Personal | 2,6% |
| Material | 2,5% |
| Infrastruktur | 3,8% |
| Dienstleistungen | 2,4% |

### Dialog-Ablauf pro Option:

**AUSGABEN:**
```
FRAGE: "Welche Ausgabenpositionen hat Option [X]?
        (Person, Material, Infrastruktur, Dienstleistungen — mehrere möglich)"

PRO KATEGORIE:
  ├─ FRAGE: "Bezeichnung der Ausgabe? z.B. 'Personal' oder 'Wartungsleistung'"
  │  INPUT: [Bezeichnung]
  │
  ├─ FRAGE: "Höhe im Referenzjahr (EUR/Jahr)?"
  │  INPUT: [Betrag, z.B. 50.000]
  │
  ├─ FRAGE: "Preissteigerungsrate? (Standard für [Kategorie]: [PSR]%)"
  │  OPTION: ✓ Standard nutzen / Abweichung eingeben
  │  INPUT: [PSR % oder ENTER für Standard]
  │
  └─ FRAGE: "Weitere Ausgaben in [Kategorie]?"
     ├─ JA → zurück zu "Bezeichnung"
     └─ NEIN → nächste Kategorie
```

**EINNAHMEN (falls vorhanden):**
```
FRAGE: "Hat Option [X] Einnahmen?
        (z.B. Drittgeschäft, Restwert, Erlöse — oder NEIN)"

WENN JA:
  → Gleiche Struktur wie Ausgaben
  → Bezeichnungen typisch: "Restwert", "Drittgeschäft", "Verkaufserlöse"
  → Beträge positiv (Einnahmen)
```

**RISIKEN (falls identifiziert in Kap. 5.4):**
```
FRAGE: "Welche Risiken sind für Option [X] relevant?"
       (aus Risikoidentifizierung Kap. 5.4)

PRO RISIKO:
  ├─ Bezeichnung: [aus Kap. 5.4]
  ├─ FRAGE: "Schadenshöhe im Referenzjahr (EUR)?"
  │  INPUT: [Betrag]
  │
  ├─ FRAGE: "Risiko-Kategorie? (Personal / Material / Infrastruktur / DL)"
  │  INPUT: [Kategorie → nutze Standard-PSR dieser Kategorie]
  │
  └─ FRAGE: "Eintrittswahrscheinlichkeit? (z.B. 15% = 0,15)"
     OPTION: ✓ Konstant für alle Jahre / Variabel pro Jahr
     INPUT: [EW % oder {2025: 15%, 2026: 0%, ...}]
```

### Implementierung im Skill:

```python
import sys
sys.path.insert(0, 'P:/WUKI_Projekt/Claude/skills/wu-berater/scripts')
from berechnung_kapitalwert import (
    berechne_alle_optionen, erstelle_kw_uebersicht,
    Option, Kostenposition, Einnahmeposition, Risiko,
    PSR_PERSONAL, PSR_MATERIAL, PSR_INFRASTRUKTUR, PSR_DIENSTLEISTUNGEN
)

# Für jede geeignete Option aus Kap. 3.2:
optionen = []

for option_name in suitable_options:
    # Dialog durchführen für diese Option
    # (siehe Ablauf oben)
    
    # Dann Option-Objekt erstellen:
    opt = Option(
        name=option_name,
        investition=investition_jahr0,  # falls vorhanden
        kostenpositionen=[
            Kostenposition('Personal', 50000, PSR_PERSONAL, 'Personal'),
            Kostenposition('Wartung', 5000, PSR_DIENSTLEISTUNGEN, 'Dienstleistungen'),
            # ... weitere Positionen
        ],
        einnahmen=[
            Einnahmeposition('Restwert', 15000, 0.0, 'Restwert'),  # Einnahmen sind positiv
            # ... weitere Einnahmen
        ],
        risiken=[
            Risiko('Ausfall Lieferant', -10000, 0.15, PSR_MATERIAL, 'Material'),
            # ... weitere Risiken
        ]
    )
    optionen.append(opt)

# Berechnung
ergebnisse = berechne_alle_optionen(
    optionen,
    zinssatz=float(wu_data['kap4']['diskontierungszinssatz']),  # z.B. 0.012
    jahre=betrachtungsjahre
)

# Ergebnisse in wu_data speichern
wu_data['kap5_2'] = {
    'optionen': ergebnisse,
}
```

**Wichtig:**
- Einnahmen sind positive Beträge (Restwert, Drittgeschäft)
- Risiken sind negative Schadenshöhen
- Die Sortierung erfolgt automatisch nach KW mit Risiko (beste Option = niedrigste Kosten incl. Risiko)

---

## Sensitivitätsanalyse (7)

```python
from berechnung_kapitalwert import erstelle_sensitivitaet
sensitivitaet_text = erstelle_sensitivitaet(optionen, ergebnisse, risikowerte, zinssatz=0.012, jahre=...)
wu_data['kap6_9']['sensitivitaet'] = sensitivitaet_text
```

Das Skript berechnet Break-even automatisch. Frage den Nutzer nicht danach.

---

## Export mit erweiterten Validierungschecks (Punkt 2)

**VOR dem Export: 6-Punkt-Validierung**

```python
def validate_wu_ueberjahrig_extended(wu_data):
    """
    Erweiterte Validierung vor Export (analog zu Dialogpfad A).
    """
    errors = []
    warnings = []
    
    # CHECK 1: Bedarfsforderung — Produktnamen prüfen
    bedarfsforderung = wu_data.get('kap1_3', {}).get('bedarfsforderung', '').lower()
    forbidden_produktnamen = [
        'drucker', 'hp', 'canon', 'kyocera', 'brother',
        'laptop', 'dell', 'lenovo', 'hp', 'thinkpad',
        'transporter', 'vw', 'mercedes', 'iveco',
        'bürostuhl', 'steelcase', 'haworth'
    ]
    
    for name in forbidden_produktnamen:
        if name in bedarfsforderung:
            errors.append(
                f"❌ Kap. 1.1 (Bedarfsforderung) enthält Produktnamen '{name}'. "
                f"Bitte lösungsneutral reformulieren (nur Funktionen nennen)."
            )
            break
    
    # CHECK 2: Kapitalwerte — Realismus-Prüfung
    for option in wu_data.get('kap3_optionen', []):
        kosten = option.get('gesamtkosten_pro_jahr', 0)
        if kosten < 50:
            warnings.append(
                f"⚠️ {option['name']}: Jahreskosten sehr niedrig ({kosten:.2f} EUR). "
                f"Ist das realistisch?"
            )
        elif kosten > 10000000:
            warnings.append(
                f"⚠️ {option['name']}: Jahreskosten sehr hoch ({kosten:.2f} EUR). "
                f"Plausibilität prüfen."
            )
    
    # CHECK 3: Aussonderung — auf verbotene Gründe prüfen
    aussonderung_text = wu_data.get('kap3_2', {}).get('aussonderung_begruendung', '').lower()
    forbidden_grounds = [
        'haushaltsmittel', 'haushalt', 'budget', 'geld',
        'dienstposten', 'personal', 'mitarbeiter',
        'infrastruktur', 'raum'
    ]
    
    for ground in forbidden_grounds:
        if ground in aussonderung_text:
            errors.append(
                f"❌ Kap. 3.2 (Aussonderung) enthält unzulässigen Grund: '{ground}'. "
                f"Reformulieren Sie als Rahmenbedingung oder zeitliche Frist."
            )
            break
    
    # CHECK 4: Pflichtfelder — alles vorhanden?
    pflichtfelder = [
        ('Bedarfsforderung', wu_data.get('kap1_3', {}).get('bedarfsforderung')),
        ('Ausgangslage', wu_data.get('kap2_1', {}).get('ausgangslage')),
        ('Optionsbeschreibung', wu_data.get('kap3_1', {}).get('optionen')),
        ('Kapitalwertberechnung', wu_data.get('kap5_2', {}).get('kapitalwert')),
    ]
    
    for feldname, wert in pflichtfelder:
        if not wert:
            errors.append(f"❌ Pflichtfeld '{feldname}' fehlt oder leer")
    
    # CHECK 5: Anlage Marktrecherche — vorhanden?
    anlagen = wu_data.get('anlagen', [])
    if len(anlagen) < 1:
        errors.append("❌ Anlage Marktrecherche (Nr. 1) fehlt")
    
    # CHECK 6: Risikobewertung dokumentiert?
    risikobetrachtung = wu_data.get('kap5_4', {}).get('risikobetrachtung')
    if not risikobetrachtung:
        warnings.append("⚠️ Kap. 5.4 (Risikobetrachtung) nicht dokumentiert")
    
    return errors, warnings
```

**Verwendung vor Export:**

```python
from export_wu_ueberjahrig import fill_template, build_filename, erstelle_abschlusscheckliste

errors, warnings = validate_wu_ueberjahrig_extended(wu_data)

if errors:
    print(f"❌ FEHLER gefunden:\n")
    for error in errors:
        print(f"  {error}")
    print("\nBitte Eingaben korrigieren und erneut versuchen.")
    sys.exit(1)

if warnings:
    print(f"⚠️ WARNUNGEN:\n")
    for warning in warnings:
        print(f"  {warning}")
    
    user_confirm = input("\nTrotzdem exportieren? [Ja/Nein]: ")
    if user_confirm.lower() != 'ja':
        sys.exit(0)

# EXPORT
outpath = build_filename(wu_data['meta']['datum'], 'Sachverhalt', wu_data['meta']['dienststelle'])
fill_template(wu_data, outpath)
print(erstelle_abschlusscheckliste(wu_data, outpath))
```

Vollständiges Schema: `WU_DATA_SCHEMA` am Ende von `export_wu_ueberjahrig.py`.
