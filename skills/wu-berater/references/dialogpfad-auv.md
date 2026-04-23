# Dialogpfad AUV: Einmalige Unterjährige WU (Vermerk-Template für Güter A2-1000/0-0-13)

**Zweck:** Befüllung des Templates "WU unterjährig Vermerk.xlsm" für **einmalige, unterjährige Käufe von Gütern des Anlagevermögens und Umlaufvermögens**.

**Geltungsbereich (STRENG):**
- ✅ **Einmalig** (keine Wiederholung, nicht regelmäßig)
- ✅ **Unterjährig** (innerhalb eines Kalenderjahres)
- ✅ **Kauf von Gütern** (nicht Miete, Leasing, Dienstleistung)
- ✅ **Nach A2-1000/0-0-13** klassifiziert als Anlagevermögen oder Umlaufvermögen

**Falls AUV nicht passt:** Siehe `auv-gueterklassifikation.md` (Entscheidungsbaum) oder verwende Dialogpfad B/C für regelmäßige/überjährige Maßnahmen.

---

## Phase 0: Gating-Logic (PRE-CHECK im SKILL.md)

**BEVOR dieser Dialogpfad startet, muss Gating-Logic im SKILL.md durchgeführt werden:**

```
SKILL-Startdialog (alle Pfade):
  1. "Ist diese Maßnahme EINMALIG (nicht regelmäßig/wiederholend)?" → JA/NEIN
  2. "Liegt die Maßnahme INNERHALB eines Kalenderjahres?" → JA/NEIN
  3. "Ist es ein KAUF (nicht Miete, Leasing, Dienstleistung)?" → JA/NEIN
  4. "Werden GÜTER gekauft (nicht Infrastruktur/Dienstleistung)?" → JA/NEIN
  5. "Nach A2-1000/0-0-13: Anlagevermögen oder Umlaufvermögen?" → JA/NEIN

ERGEBNIS:
  ✅ Alle 5 JA? → Dialogpfad AUV (dieses Dokument)
  ❌ Mindestens 1 NEIN? → Dialogpfad A (unterjährig), B (überjährig), oder C (andere)
```

Siehe detailliert: **`auv-gueterklassifikation.md`** (5-Fragen-Entscheidungsbaum mit Beispielen).

---

## Phase 1: Input-Validierung & Metadaten

**Nach Gating-Logic (5 JA) startet dieser Pfad mit Eingabe von Basisdaten:**

| Feld | Typ | Validierung | Beispiel |
|---|---|---|---|
| **Dienststelle** | Text | 2–30 Zeichen, alphanumerisch + Leerzeichen | BAIUDBw, KommBw München |
| **Bearbeiter** | Text | 2–50 Zeichen | Schmid, Sandra (E9b) |
| **Maßnahmenbeginn** | Datum | TT.MM.JJJJ, dieses Kalenderjahr | 15.05.2026 |
| **Kaufbeschreibung** | Text | 5–100 Zeichen, konkret | 100 Schrauben M8x20 oder Betriebsstoff 50L |
| **Geschätzter Kaufpreis** | EUR | 50–500.000 EUR | 2.500,00 oder 1.200 |

### Dialog Phase 1: Erfassung der 5 Basis-Felder

```
SKILL: „Gut, wir füllen das Vermerk-Template für einmalige, unterjährige Güter-Käufe.
        Bitte geben Sie folgende Angaben ein:

1. Dienststelle: [User: BAIUDBw]
2. Bearbeiter (Ihr Name): [User: Schmid, Sandra]
3. Maßnahmenbeginn (TT.MM.JJJJ): [User: 15.05.2026]
4. Was wird gekauft? (kurz & konkret): [User: 100 Schrauben M8x20]
5. Geschätzter Kaufpreis (EUR): [User: 2.500]

→ Validiert… ✅ Alle Eingaben korrekt!"
```

**Validierungs-Code für Phase 1:**

```python
def validate_phase1_auv(dienststelle, bearbeiter, massnahmenbeginn, kaufbeschreibung, preis):
    """
    Validierung der Phase 1 Eingaben für Dialogpfad AUV.
    """
    errors = []
    
    # CHECK 1: Dienststelle
    if not dienststelle or len(dienststelle) < 2 or len(dienststelle) > 30:
        errors.append("❌ Dienststelle: mindestens 2, maximal 30 Zeichen erforderlich")
    if not re.match(r'^[A-Za-z0-9äöüß\s\-\.]+$', dienststelle):
        errors.append("❌ Dienststelle: Nur Buchstaben, Zahlen, Umlaute, Leerzeichen")
    
    # CHECK 2: Bearbeiter
    if not bearbeiter or len(bearbeiter) < 2 or len(bearbeiter) > 50:
        errors.append("❌ Bearbeiter: mindestens 2, maximal 50 Zeichen erforderlich")
    
    # CHECK 3: Maßnahmenbeginn (Datum validieren)
    try:
        beginn_date = datetime.strptime(massnahmenbeginn, '%d.%m.%Y')
        today = datetime.now()
        if beginn_date > today.replace(year=today.year + 1):
            errors.append(f"❌ Maßnahmenbeginn: muss dieses oder nächstes Kalenderjahr sein")
    except ValueError:
        errors.append("❌ Maßnahmenbeginn: Ungültiges Format. Bitte TT.MM.JJJJ verwenden (z.B. 15.05.2026)")
    
    # CHECK 4: Kaufbeschreibung (konkret, nicht zu allgemein)
    if not kaufbeschreibung or len(kaufbeschreibung) < 5 or len(kaufbeschreibung) > 100:
        errors.append("❌ Kaufbeschreibung: mindestens 5, maximal 100 Zeichen erforderlich")
    
    # CHECK 5: Preis (EUR Range 50–500.000)
    try:
        preis_float = float(preis.replace(',', '.').replace('EUR', '').strip())
    except ValueError:
        errors.append("❌ Preis: Ungültiges Zahlenformat (z.B. '2500' oder '2.500')")
        return errors
    
    if preis_float < 50:
        errors.append(f"⚠️ Preis sehr niedrig ({preis_float:.2f} EUR). Ist das wirklich richtig? (Min. 50 EUR)")
    elif preis_float > 500000:
        errors.append(f"⚠️ Preis sehr hoch ({preis_float:.2f} EUR). Max. 500.000 EUR für unterjährig.")
    
    return errors
```

**Nach Phase 1 → direkt zu Phase 2 (Bedarfsforderung)**

---

## Phase 2: Bedarfsforderung (KOMPAKT — User tippt direkt)

**UNTERSCHIED zu Dialogpfad A:** Kein 8-Fragen-Dialog. Stattdessen: User tippt kurze Bedarfsforderung direkt ein.

**Grund:** Das Vermerk-Template hat nur **einen Bedarfsforderungs-Feld** (nicht mehrere Felder wie Dialogpfad A). Kompakte, funktionale Beschreibung reicht aus.

### Dialog Phase 2: Bedarfsforderung eingeben

```
SKILL: „Geben Sie bitte eine KURZE Bedarfsforderung ein.
        Wichtig: Nur Funktionen nennen, KEINE Produktnamen!

Beispiele ✅:
  - ‚Verbindungsmittel zur Verschraubung M8x20'
  - ‚Betriebsstoff für Fahrzeuge, Typ Diesel, 50L'
  - ‚Wartungsmittel für Reinigung von Oberflächen'

Beispiele ❌ (nicht erlaubt):
  - ‚100er Schrauben von Würth'
  - ‚Shell Diesel Super'
  - ‚HG-Reiniger XXX-Marke'

Ihre Bedarfsforderung: [User tippt 20–150 Zeichen]"
```

**User-Input Beispiele für AUV:**
```
100 Schrauben M8x20 (Verbrauchsgut/Einzelverbrauch)
→ User: „Verbindungsmittel zur Verschraubung, Gewindedurchmesser M8, Länge 20mm, Kopfform Senkkopf"

50L Betriebsstoff Diesel (Verbrauchsgut/Mengenverbrauch)
→ User: „Motorenöl für Fahrzeuge, Typ Diesel, Menge 50 Liter"

Drucker (Nichtverbrauchsgut/Gerät)
→ User: „Druckfähigkeit für Büroprozesse mit Kopierfunktion und Netzwerkanbindung"
```

**Validierung Phase 2:**

```python
def validate_phase2_bedarfsforderung(bedarfsforderung):
    """
    Validiert Bedarfsforderung: kurz, funktional, lösungsneutral.
    """
    errors = []
    
    # CHECK 1: Länge (20–150 Zeichen, nicht zu lang für Vermerk)
    if len(bedarfsforderung) < 20:
        errors.append("❌ Bedarfsforderung zu kurz (min. 20 Zeichen). Bitte detaillierter.")
    elif len(bedarfsforderung) > 150:
        errors.append("❌ Bedarfsforderung zu lang (max. 150 Zeichen). Bitte kürzer fassen.")
    
    # CHECK 2: Verbotene Produktnamen / Marken
    forbidden_brands = [
        'hp', 'kyocera', 'brother', 'canon', 'ricoh', 'xerox',  # Drucker
        'dell', 'lenovo', 'thinkpad', 'hp', 'apple',  # Laptops
        'shell', 'aral', 'bp', 'esso', 'conoco',  # Benzinmarken
        'würth', 'fischer', 'hg-reiniger', 'kärcher'  # Marken
    ]
    bedarfsforderung_lower = bedarfsforderung.lower()
    for brand in forbidden_brands:
        if brand in bedarfsforderung_lower:
            errors.append(f"❌ Bedarfsforderung enthält Marke/Produktname '{brand}'. "
                         f"Bitte lösungsneutral formulieren (nur Funktion/Spezifikation).")
            break
    
    # CHECK 3: Funktional / Lösungsneutral? (einfache Heuristik)
    # Sollte Zahlen, Einheiten oder funktionale Wörter haben
    has_specifics = any(char.isdigit() for char in bedarfsforderung) or \
                    any(unit in bedarfsforderung.lower() for unit in ['m8', 'liter', 'l', 'stück', 'fähigkeit'])
    
    if not has_specifics:
        warnings.append("⚠️ Bedarfsforderung könnte spezifischer sein. "
                       "Bitte Maße/Einheiten/Funktionen nennen (z.B. 'M8x20', '50L', 'Netzwerk').")
    
    return errors, warnings
```

**Nach Phase 2 Validierung → weiterzur zu Phase 3 (Bisherige Bedarfsdeckung)**

---

## Phase 3: Bisherige Bedarfsdeckung (CHECKBOXEN)

**Frage:** Wie wurde der Bedarf bisher erfüllt?

```
SKILL: „Bitte wählen Sie aus, wie der Bedarf bisher gedeckt wurde:

[ ] ☐ Kauf: Bedarf wurde durch vorhandene Bestände / Eigenbestände erfüllt
    → Text: ‚Der Bedarf wurde bisher durch Eigenbestände erfüllt.'

[ ] ☐ Neu: Bedarf ist neu entstanden
    → Text: ‚Der Bedarf ist neu entstanden und wurde bisher nicht erfüllt.'

[ ] ☐ Sonstiges: Andere Situation
    → [Textfeld für User-Eingabe, max. 100 Zeichen]"
```

**Validierung Phase 3:**
- Mindestens eine Option muss ausgewählt sein
- Falls „Sonstiges": Text darf nicht leer sein

**Nach Phase 3 → zu Phase 4 (Unterjährigkeit-Begründung)**

---

## Phase 4: Unterjährigkeit-Begründung (CHECKBOXEN mit Guard Check)

**Frage:** Warum ist diese Maßnahme EINMALIG und UNTERJÄHRIG?

```
SKILL: „Warum ist dieser Kauf einmalig und unterjährig? Bitte wählen Sie einen Grund:

[ ] ☐ GRUND 1: Verbrauchsgut (wird nach Verbrauch nicht ersetzt)
    → Text: ‚Der Bedarf ist einmalig. Das Verbrauchsgut wird nach Aufbrauch nicht erneut beschafft.'

[ ] ☐ GRUND 2: Verbrauchsgut (wird ggfs. in Folgejahren neu beschafft, aber nicht dieses Jahr)
    → Text: ‚Der Bedarf ist für dieses Jahr einmalig. Folgebedarfe werden in kommenden WU-Jahren separat betrachtet.'

[ ] ☐ GRUND 3: Nichtverbrauchsgut (Anschaffung ohne Folgekosten)
    → Text: ‚Der Bedarf ist einmalig. Nach der Anschaffung fallen keine Folgeausgaben an.'

[ ] ☐ GRUND 4 (Sonstiges): [Freitextfeld, max. 100 Zeichen]"
```

**Guard Check Phase 4:**

```python
def validate_phase4_grund(grund_enum, freitext_sonstiges=None):
    """
    Guard Check für Phase 4: Prüfe auf verbotene Begründungen.
    """
    errors = []
    
    # Erlaubte Gründe: 1–3 (strukturiert), 4 (Freitext mit Prüfung)
    if grund_enum not in [1, 2, 3, 4]:
        errors.append("❌ Bitte wählen Sie einen der 4 Gründe")
        return errors
    
    # Falls Grund 4 (Sonstiges): Freitext-Prüfung
    if grund_enum == 4:
        if not freitext_sonstiges or len(freitext_sonstiges) < 5:
            errors.append("❌ Bitte erklären Sie den Grund (min. 5 Zeichen)")
        
        # Prüfe auf VERBOTENE Begründungen
        forbidden_patterns = [
            'haushalt', 'budget', 'personal', 'dienstposten', 
            'infrastruktur', 'raum', 'mittel', 'kosten',
            'keine mittel', 'kein geld'
        ]
        freitext_lower = freitext_sonstiges.lower()
        for pattern in forbidden_patterns:
            if pattern in freitext_lower:
                errors.append(f"❌ '{pattern}' ist keine zulässige Begründung für Einmaligkeit.")
                break
    
    return errors
```

**Nach Phase 4 → zu Phase 5 (Ausgaben/Kosten)**

---

## Phase 5: Ausgaben / Kosten (NUMERISCH)

**Eingabe des Kaufpreises nochmal zur Bestätigung (oder Anpassung):**

```
SKILL: „Bestätigen Sie den Kaufpreis (oder passen Sie ihn an):

Kaufpreis (EUR): [Eingabe, vorausgefüllt mit Phase 1 Feld 5]
                  z.B. 2.500 oder 2500

→ Validiert… ✅ Preis OK"
```

**Validierung Phase 5:**
- Range: 50–500.000 EUR
- Zahlenformat: Dezimaltrennzeichen `'.'` oder `','` akzeptabel
- Optional: Warnung bei extremen Werten

**Nach Phase 5 → zu Phase 6 (Hinweis Folgeausgaben)**

---

## Phase 6: Hinweis zu Folgeausgaben (INFO-BOX)

**Automatische Info-Box (kein User-Input nötig):**

```
⚠️ WICHTIG — Folgeausgaben NICHT dokumentieren:

Das Vermerk-Template ist NUR für einmalige Anschaffungen ausgelegt.

Folgende Ausgaben gehören NICHT in diese WU:
  ❌ Wartungs- und Instandhaltungskosten
  ❌ Verbrauchsmaterialien (Toner, Öl, Spermaterial)
  ❌ Ersatzteile / Austauschteile
  ❌ Lizenzen / Abonnements
  ❌ Neuanschaffungen in Folgejahren

Falls Sie solche Ausgaben haben:
  → Separate WU für regelmäßige/wiederkehrende Kosten (Dialogpfad B)
  → Oder separate WU in Folgejahren (neuer Dialogpfad AUV)

Passt das zu Ihrer Situation? [Ja / Abbrechen]
```

**Nach Phase 6 → zu Phase 7 (Export)**

---

## Phase 7: Export zum Vermerk-Template (VOLL-AUTO)

**Mapping Dialogpfad AUV → Template-Felder:**

```python
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from datetime import datetime
import re

def export_auv_to_vermerk(auv_data, output_path):
    """
    Befüllt das Vermerk-Template mit Daten aus Dialogpfad AUV.
    
    Mapping:
      Phase 1: Metadaten → Template-Kopf (Dienststelle, Bearbeiter, Datum)
      Phase 2: Bedarfsforderung → Blatt "Sachverhalt" Feld "Bedarf"
      Phase 3: Bisherige Bedarfsdeckung → Blatt "Sachverhalt" Feld "Bisherige Deckung"
      Phase 4: Grund Einmaligkeit → Blatt "Sachverhalt" Feld "Unterjährigkeit"
      Phase 5: Kaufpreis → Blatt "Kosten" Feld "Ausgaben"
      Phase 6-7: Export
    """
    
    wb = load_workbook('Template_WU_unterjährig_Vermerk.xlsm')
    ws = wb['Sachverhalt']  # Annahme: Blatt heißt 'Sachverhalt'
    
    # SCHRITT 1: Metadaten befüllen (Phase 1)
    ws['B2'] = auv_data['phase1']['dienststelle']  # Annahme: Feld B2
    ws['B3'] = auv_data['phase1']['bearbeiter']    # Annahme: Feld B3
    ws['B4'] = auv_data['phase1']['massnahmenbeginn']  # TT.MM.JJJJ Format
    
    # SCHRITT 2: Bedarfsforderung (Phase 2)
    ws['B10'] = auv_data['phase2']['bedarfsforderung']  # Text-Feld
    
    # SCHRITT 3: Bisherige Bedarfsdeckung (Phase 3)
    phase3_text = generate_phase3_text(auv_data['phase3'])
    ws['B12'] = phase3_text
    
    # SCHRITT 4: Unterjährigkeit-Begründung (Phase 4)
    phase4_text = generate_phase4_text(auv_data['phase4'])
    ws['B14'] = phase4_text
    
    # SCHRITT 5: Kaufpreis (Phase 5)
    ws['B16'] = float(auv_data['phase5']['ausgaben'])
    
    # Speichern
    wb.save(output_path)
    return True

def generate_phase3_text(phase3_data):
    """Phase 3 Checkbox-Antwort in Text konvertieren."""
    if phase3_data['option'] == 1:
        return "Der Bedarf wurde bisher durch Eigenbestände erfüllt."
    elif phase3_data['option'] == 2:
        return "Der Bedarf ist neu entstanden und wurde bisher nicht erfüllt."
    elif phase3_data['option'] == 3:
        return phase3_data['sonstiges_text']
    return ""

def generate_phase4_text(phase4_data):
    """Phase 4 Grund in Text konvertieren."""
    texts = {
        1: "Der Bedarf ist einmalig. Das Verbrauchsgut wird nach Aufbrauch nicht erneut beschafft.",
        2: "Der Bedarf ist für dieses Jahr einmalig. Folgebedarfe werden in kommenden Jahren separat betrachtet.",
        3: "Der Bedarf ist einmalig. Nach der Anschaffung fallen keine Folgeausgaben an."
    }
    if phase4_data['grund'] in texts:
        return texts[phase4_data['grund']]
    else:
        return phase4_data['sonstiges_text']
```

**Vor dem Export: 3-Punkt Validierung (Phase 7):**

```python
def validate_auv_before_export(auv_data):
    """
    Final validation vor Export zu Vermerk-Template.
    """
    errors = []
    warnings = []
    
    # CHECK 1: Alle Pflichtfelder vorhanden?
    required_fields = [
        ('phase1', 'dienststelle'),
        ('phase1', 'bearbeiter'),
        ('phase2', 'bedarfsforderung'),
        ('phase3', 'option'),
        ('phase4', 'grund'),
        ('phase5', 'ausgaben'),
    ]
    for phase, field in required_fields:
        if field not in auv_data.get(phase, {}):
            errors.append(f"❌ Pflichtfeld fehlt: {phase}.{field}")
    
    # CHECK 2: Preis im zulässigen Bereich (50–500k EUR)?
    try:
        preis = float(auv_data['phase5']['ausgaben'])
        if preis < 50 or preis > 500000:
            warnings.append(f"⚠️ Preis außerhalb Normalbereich: {preis:.2f} EUR")
    except (ValueError, KeyError):
        errors.append("❌ Kaufpreis ungültig")
    
    # CHECK 3: Bedarfsforderung OK? (keine Marken, nicht zu kurz)
    bedarf = auv_data['phase2']['bedarfsforderung'].lower()
    forbidden = ['hp', 'dell', 'lenovo', 'shell', 'aral', 'würth']
    for brand in forbidden:
        if brand in bedarf:
            errors.append(f"❌ Bedarfsforderung enthält Markenname '{brand}'. Lösungsneutral formulieren.")
            break
    
    return errors, warnings
```

**Erfolgreiche Export-Meldung:**

```
✅ Vermerk erfolgreich exportiert!

Datei: 20260423_WU_Schrauben_BAIUDBw_AUV_Version_1.xlsm

Vor dem Versand prüfen:
  ☐ Dienststelle + Bearbeiter richtig?
  ☐ Bedarfsforderung lösungsneutral (keine Marken)?
  ☐ Kaufpreis korrekt?
  ☐ Grund für Einmaligkeit nachvollziehbar?

→ Dann: speichern, ggfs. PDF exportieren, versenden.
```

---

## Zusammenfassung: Dialogpfad AUV (Vermerk-Template) — Struktur-Übersicht

**UNTERSCHIEDE von Dialogpfad A:**

| Kriterium | Dialogpfad A | Dialogpfad AUV |
|-----------|---|---|
| **Template** | "WU unterjährig Kerntemplate.xlsm" (mehrseitig) | "WU unterjährig Vermerk.xlsm" (kompakt, 1 Seite) |
| **Gating** | NACH Start-Dialog | Phase 0: 5-Fragen-Check VOR Beginn |
| **Bedarfsforderung** | Phase A1: 8-Fragen-Dialog (Produkttyp-spezifisch, Fallback) | Phase 2: User tippt direkt (20–150 Zeichen) |
| **Bisherige Deckung** | Phase A2: Intelligenter Default (6-Punkt Heuristik) | Phase 3: 3-Punkt Checkbox-Auswahl |
| **Eigenleistungs-Ausschluss** | Phase A3: Nicht direkt relevant (WU ist schon Kauf) | Phase 4: Grund für Einmaligkeit (4 Optionen) |
| **Miete-Ausschluss** | Phase A4: WebRecherche + Break-even-Berechnung | Phase 4: (nicht relevant — Kauf steht fest) |
| **Folgeausgaben-Check** | Phase A5: Standard-Text | Phase 6: Info-Box (kein Input) |
| **Export** | A6: zu Kerntemplate (A1–A5 Felder) | Phase 7: zu Vermerk-Template (kompakt) |
| **Zielgruppe** | Sämtliche unterjährige WU (alle Produkttypen) | NUR einmalige, unterjährige Güter-Käufe |

**PHASENKÜRZEL:**

```
Dialogpfad AUV:
  ├─ Phase 0: Gating-Logic (5-Fragen-Check, SKILL.md)
  ├─ Phase 1: Input-Validierung & Metadaten (5 Felder)
  ├─ Phase 2: Bedarfsforderung (kompakt, 20–150 Zeichen)
  ├─ Phase 3: Bisherige Bedarfsdeckung (Checkboxen)
  ├─ Phase 4: Unterjährigkeit-Begründung (Checkboxen + Guard Check)
  ├─ Phase 5: Ausgaben / Kaufpreis (Validierung)
  ├─ Phase 6: Hinweis Folgeausgaben (Info-Box)
  └─ Phase 7: Export zum Vermerk-Template
```

**ZEIT-AUFWAND (ungefähr):**

```
Phase 1:       2–3 Min (5 Felder eingeben + validieren)
Phase 2:       2–3 Min (Bedarfsforderung tippen)
Phase 3:       1 Min   (Checkbox auswählen)
Phase 4:       1 Min   (Grund auswählen)
Phase 5:       <1 Min  (Preis bestätigen)
Phase 6:       <1 Min  (Info-Box lesen)
Phase 7:       1–2 Min (Export + Erfolgsmeldung)
────────────────────────
GESAMT:        ~7–10 Min (ohne Korrigieren)
```

---

## Referenzen für AUV-Spezifika

- **`auv-gueterklassifikation.md`** — A2-1000/0-0-13 Güterklassifizierung (Verbrauchsgut vs. Nichtverbrauchsgut, Entscheidungsbaum)
- **`SKILL.md`** — Startdialog mit Phase 0 Gating-Logic (5 JA/NEIN-Fragen)
- **`dialogpfad-a.md`** — Referenz für Dialogpfad A (zum Vergleich: 8-Fragen-Dialog statt direktem Input)

---

## Abgrenzung zu anderen Pfaden

**Wann ist AUV geeignet?**
- ✅ Einmalig + unterjährig + Kauf + Güter + (Anlagevermögen ODER Umlaufvermögen nach A2-1000)
- ✅ Beispiele: 100 Schrauben, 50L Betriebsstoff, 1 Drucker, 1 Rasenmäher

**Wann NICHT AUV?**
- ❌ Regelmäßig (z.B. monatliche Schrauben-Lieferung) → Dialogpfad B (Verträge)
- ❌ Überjährig (z.B. 3-Jahres-Projekt) → Dialogpfad B
- ❌ Dienstleistung (z.B. Reinigung, IT-Support) → Dialogpfad B/C
- ❌ Nicht nach A2-1000 klassifizierbar → Dialogpfad B/C

Siehe **`auv-gueterklassifikation.md`** für detaillierten Entscheidungsbaum mit konkreten Beispielen.

---

**Quelle & Gültigkeitsumfang:**
- Basiert auf Vermerk-Template "WU unterjährig Vermerk.xlsm"
- Gültig nur für einmalige, unterjährige Käufe von Gütern des Anlagevermögens und Umlaufvermögens nach A2-1000/0-0-13
- Dialogpfad A bleibt unverändert als Referenz für Kerntemplate
- Dialogpfad B/C für andere WU-Typen (regelmäßig, überjährig, nicht-Güter)
