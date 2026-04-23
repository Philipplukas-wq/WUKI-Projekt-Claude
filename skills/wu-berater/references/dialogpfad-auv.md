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
  3. "Ist es ein Kauf von Gütern (keine Miete, Dienstleistung, Infrastruktur)?" → JA/NEIN
  4. "Nach A2-1000/0-0-13: Anlagevermögen oder Umlaufvermögen?" → ANLAGE/UMLAUF

ERGEBNIS:
  ✅ Alle 4 JA + Klassifizierung klar? → Dialogpfad AUV (dieses Dokument)
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
| **Geschätzter Kaufpreis** | EUR | Beliebig (keine Mindestgrenze) | 2.500,00 oder 1.200 |

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
    
    # CHECK 5: Preis (Zahlenformat validieren, keine Mindestgrenze)
    try:
        preis_float = float(preis.replace(',', '.').replace('EUR', '').strip())
    except ValueError:
        errors.append("❌ Preis: Ungültiges Zahlenformat (z.B. '2500' oder '2.500')")
        return errors
    
    # Keine Mindestgrenze — auch kleine Käufe sind WU-relevant
    if preis_float < 0:
        errors.append(f"❌ Preis kann nicht negativ sein: {preis_float:.2f} EUR")
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

**WICHTIG — Goods Classification & Konsequenzen:**
Diese Wahl bestimmt auch die Güterklassifizierung (Anlagevermögen vs. Umlaufvermögen):
- **Grund 1, 2** → **Umlaufvermögen** (Verbrauchsgüter)
  * Zeile 18 wird versteckt (Miete/Leasing nicht relevant)
  * **KEINE Mietpreis-Recherche** (Verbrauchsgüter werden nicht gemietet)
  
- **Grund 3** → **Anlagevermögen** (Nichtverbrauchsgüter)
  * Zeilen 14, 17 werden versteckt (Verbrauchsgut-Hinweise nicht relevant)
  * **Optional:** Wirtschaftliche Prüfung (Kauf vs. Miete) — aber nicht für Vermerk-Template

```
SKILL: „Warum ist dieser Kauf einmalig und unterjährig? Bitte wählen Sie einen Grund:

[ ] ☐ GRUND 1: Verbrauchsgut (wird nach Verbrauch nicht ersetzt)
    → Text: ‚Der Bedarf ist einmalig. Das Verbrauchsgut wird nach Aufbrauch nicht erneut beschafft.'
    → Klassifizierung: Umlaufvermögen

[ ] ☐ GRUND 2: Verbrauchsgut (wird ggfs. in Folgejahren neu beschafft, aber nicht dieses Jahr)
    → Text: ‚Der Bedarf ist für dieses Jahr einmalig. Folgebedarfe werden in kommenden WU-Jahren separat betrachtet.'
    → Klassifizierung: Umlaufvermögen

[ ] ☐ GRUND 3: Nichtverbrauchsgut (Anschaffung ohne Folgekosten)
    → Text: ‚Der Bedarf ist einmalig. Nach der Anschaffung fallen keine Folgeausgaben an.'
    → Klassifizierung: Anlagevermögen

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

**Nach Phase 4 → zu Phase 4b (Wirtschaftlichkeits-Vergleich, nur für Anlagevermögen)**

---

## Phase 4b: Wirtschaftlichkeits-Vergleich (NUR für Anlagevermögen / Grund 3)

**Kontext:** Diese Phase startet NUR, wenn User **Grund 3** (Anlagevermögen) gewählt hat.

### Schritt 1: Entscheidung zur WebRecherche (3 Optionen)

```
SKILL: „Für Nichtverbrauchsgüter (wie Drucker, Fahrzeuge, Möbel) ist wichtig zu prüfen,
        ob ein Kauf oder eine Miete/Dienstleistung wirtschaftlicher ist.

Bitte wählen Sie:

[ ] ☐ OPTION A: Ja, bitte Mietpreise recherchieren und vergleichen
           → Ich suche nach Mietoptionen und vergleiche Kauf vs. Miete/Dienstleistung

[ ] ☐ OPTION B: Nein, einen anderen Grund eingeben
           [Textfeld] z.B. „Miete ist nicht üblich für diesen Gerätetyp"
           → Wir gehen direkt zum Kauf über

[ ] ☐ OPTION C: hierfür kein Anbieter gefunden werden konnte
           → Standard-Text wird verwendet, Wir gehen direkt zum Kauf über"
```

**Mapping der Optionen:**

| Option | Aktion | Ergebnis |
|--------|--------|----------|
| **A** | WebRecherche durchführen | Vergleich Kauf vs. Miete; ggfs. Wechsel zu Dialogpfad D |
| **B** | Nutzer tippt Grund | Grund wird dokumentiert, Weitermachen mit AUV-Export |
| **C** | Vordefinierter Grund | "hierfür kein Anbieter gefunden werden konnte" wird dokumentiert, Weitermachen mit AUV-Export |

### Schritt 2: Ablauf nach Nutzer-Wahl

**Falls OPTION B oder C gewählt (keine WebRecherche):**

```
Grund wird dokumentiert und in Zeile 18 des Templates eingetragen:
  • Option B: [User-eingegeben, z.B. „Miete ist nicht üblich für diesen Gerätetyp"]
  • Option C: „hierfür kein Anbieter gefunden werden konnte"

→ Weitermachen mit Phase 5 (Ausgaben/Kosten)
```

**Falls OPTION A gewählt (WebRecherche durchführen):**

### Schritt 2a: WebRecherche & Wirtschaftlichkeits-Vergleich (wenn Option A)

```python
def wirtschaftlichkeitsvergleich_anlagevermogen(auv_data):
    """
    WebRecherche nach Mietpreisen + Vergleich Kauf vs. Miete/Dienstleistung.
    NUR für Anlagevermögen (Grund 3).
    """
    
    kaufpreis = auv_data['phase5']['ausgaben']  # z.B. 2.500 EUR
    produkt = auv_data['phase1']['kaufbeschreibung']  # z.B. "Drucker"
    
    # SCHRITT 1: WebRecherche Mietpreise
    print(f"🔍 Recherchiere Mietpreise für: {produkt}")
    mietpreis_mittel = webrecherche_mietpreis(f"{produkt} miete tagesmiete")
    # Ergebnis z.B.: 25 EUR/Tag
    
    if not mietpreis_mittel:
        print("⚠️ Keine Mietpreise gefunden. Gehen wir zum Kauf über.")
        return None
    
    # SCHRITT 2: Einsatztage/Jahr extrahieren (aus Bedarfsforderung, falls vorhanden)
    einsatztage = extract_einsatztage_from_bedarf(auv_data['phase2']['bedarfsforderung'])
    if not einsatztage:
        einsatztage = input("Wie viele Einsatztage/Jahr ungefähr? (z.B. 220 für täglich): ")
        einsatztage = int(einsatztage)
    
    # SCHRITT 3: Berechne jährliche Mietkosten
    jährliche_mietkosten = mietpreis_mittel * einsatztage
    
    # SCHRITT 4: Break-even berechnen
    breakeven_tage = kaufpreis / mietpreis_mittel
    
    print(f"""
📊 WIRTSCHAFTLICHKEITS-VERGLEICH:

Ihre Angaben:
  • Kaufpreis: {kaufpreis:.2f} EUR
  • Mietpreis (Tagesmiete): ca. {mietpreis_mittel:.2f} EUR/Tag
  • Einsatztage/Jahr: {einsatztage} Tage

Berechnung:
  • Jährliche Mietkosten: {mietpreis_mittel:.2f} × {einsatztage} = {jährliche_mietkosten:.2f} EUR/Jahr
  • Break-even: {kaufpreis:.2f} ÷ {mietpreis_mittel:.2f} = {breakeven_tage:.0f} Tage
  
Ergebnis:
""")
    
    # SCHRITT 5: Entscheidungshilfe
    if breakeven_tage < einsatztage:
        print(f"  ✅ KAUF ist günstiger: Break-even nach {breakeven_tage:.0f} Tagen")
        print(f"     Bei {einsatztage} Einsatztagen/Jahr amortisiert sich der Kauf schnell.")
        return {'empfehlung': 'kauf', 'mietpreis': mietpreis_mittel, 'einsatztage': einsatztage}
    else:
        print(f"  ⚠️ MIETE ist günstiger: Break-even erst nach {breakeven_tage:.0f} Tagen")
        print(f"     Bei nur {einsatztage} Einsatztagen/Jahr ist Miete sparsamer.")
        print(f"     Jährliche Ersparnis: {jährliche_mietkosten - (kaufpreis / (breakeven_tage / einsatztage)):.2f} EUR")
        return {'empfehlung': 'miete', 'mietpreis': mietpreis_mittel, 'einsatztage': einsatztage}
```

### Schritt 2b: User-Entscheidung (falls Miete günstiger)

```
Wenn das System feststellt, dass Miete günstiger ist:

SKILL: „Die Recherche zeigt: Miete wäre günstiger als der Kauf.
        
        Kauf: 2.500 EUR (einmalig)
        Miete: 5.500 EUR/Jahr → bei nur 220 Tagen/Jahr zu teuer
        
        Möchten Sie sich doch für Miete oder Dienstleistung entscheiden?
        
[ ] ☐ Ja, ich möchte die Miete-/Dienstleistungsoption prüfen
        → Wechsel zu Dialogpfad D (Miete/DL-WU)
        
[ ] ☐ Nein, bleibe beim Kauf
        → Weitermachen mit Phase 5 (AUV-Export)"
```

**Falls User zu Dialogpfad D wechselt:**
```
Nutzer-Daten an Dialogpfad D übergeben:
  ✓ Phase 1: Metadaten (Dienststelle, Bearbeiter, Maßnahmenbeginn)
  ✓ Phase 2: Bedarfsforderung (kann übernommen werden)
  ✓ Recherche-Ergebnisse: Mietpreis + Einsatztage/Jahr
  ✓ Hinweis: "WebRecherche zeigt Miete als wirtschaftlicher"
```

**Falls User beim Kauf bleibt:**
```
Dokumentation in Vermerk-Template:
  • Zeile 18 wird gefüllt: "hierfür wurde eine Mietpreisrecherche durchgeführt..."
  • Export zu AUV → Phase 5 weiter
```

**Nach Phase 4b → zu Phase 5 (Ausgaben/Kosten)**

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
- Zahlenformat: Dezimaltrennzeichen `'.'` oder `','` akzeptabel
- Keine Mindestgrenze (auch kleine Käufe sind WU-relevant)
- Optional: Warnung bei sehr hohen Werten (> 500.000 EUR)

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

**WICHTIG — Keine WebRecherche in AUV:**

Im Gegensatz zu Dialogpfad A gibt es in Dialogpfad AUV **KEINE WebRecherche nach Mietpreisen**. Gründe:

1. **Umlaufvermögen** (Verbrauchsgüter): Miete ist nicht relevant (z.B. keine Schrauben-Miete, kein Betriebsstoff-Leasing)
2. **Anlagevermögen**: Vermerk-Template behandelt nur Kauf, keine wirtschaftliche Miete-vs.-Kauf-Analyse
3. **Vermerk-Template ist simplifiziert**: Nur Bedarfsforderung + Einmaligkeit-Begründung + Kaufpreis, keine Break-even-Berechnung

→ Phase 4 Grund entscheidet direkt, ob Miete relevant ist (→ nein für alle AUV-Fälle)

**Mapping Dialogpfad AUV → Template-Felder:**

```python
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from datetime import datetime
import re

def export_auv_to_vermerk(auv_data, output_path, gueterklassifizierung='anlagevermogen'):
    """
    Befüllt das Vermerk-Template mit Daten aus Dialogpfad AUV.
    
    Parameter:
      auv_data: Alle Phasendaten (Phase 1–5)
      output_path: Pfad zum Output-Datei
      gueterklassifizierung: 'anlagevermogen' oder 'umlaufvermogen'
                             → steuert Conditional Hiding von Zeilen 14, 17, 18
    
    Conditional Row Hiding:
      - Wenn ANLAGEVERMÖGEN (Nichtverbrauchsgüter):
        * Zeile 14, 17 ausblenden (beziehen sich auf Verbrauchsgüter)
        * Zeile 14, 17 NICHT befüllen
      
      - Wenn UMLAUFVERMÖGEN (Verbrauchsgüter):
        * Zeile 18 ausblenden (Miete/Leasing nicht relevant)
        * Zeile 18 NICHT befüllen
    
    Mapping:
      Phase 1: Metadaten → Template-Kopf (Dienststelle, Bearbeiter, Datum)
      Phase 2: Bedarfsforderung → Blatt "Sachverhalt" Feld "Bedarf"
      Phase 3: Bisherige Bedarfsdeckung → Blatt "Sachverhalt" Feld "Bisherige Deckung"
      Phase 4: Grund Einmaligkeit → Blatt "Sachverhalt" Feld "Unterjährigkeit"
      Phase 5: Kaufpreis → Blatt "Kosten" Feld "Ausgaben"
    """
    
    wb = load_workbook('Template_WU_unterjährig_Vermerk.xlsm')
    ws = wb['Sachverhalt']  # Blatt heißt 'Sachverhalt'
    
    # SCHRITT 0: Conditional Row Hiding basierend auf Güterklassifizierung
    is_anlagevermogen = gueterklassifizierung.lower() == 'anlagevermogen'
    is_umlaufvermogen = gueterklassifizierung.lower() == 'umlaufvermogen'
    
    # Zeile 14, 17: nur relevant für Umlaufvermögen (Verbrauchsgüter)
    if is_anlagevermogen:
        ws.row_dimensions[14].hidden = True
        ws.row_dimensions[17].hidden = True
    
    # Zeile 18: nur relevant für Anlagevermögen (Miete/Leasing-Option)
    if is_umlaufvermogen:
        ws.row_dimensions[18].hidden = True
    
    # SCHRITT 1: Metadaten befüllen (Phase 1)
    ws['B2'] = auv_data['phase1']['dienststelle']
    ws['B3'] = auv_data['phase1']['bearbeiter']
    ws['B4'] = auv_data['phase1']['massnahmenbeginn']  # TT.MM.JJJJ Format
    
    # SCHRITT 2: Bedarfsforderung (Phase 2)
    ws['B10'] = auv_data['phase2']['bedarfsforderung']
    
    # SCHRITT 3: Bisherige Bedarfsdeckung (Phase 3)
    phase3_text = generate_phase3_text(auv_data['phase3'])
    ws['B12'] = phase3_text
    
    # SCHRITT 4: Unterjährigkeit-Begründung (Phase 4)
    # → NUR befüllen, wenn die entsprechende Zeile nicht versteckt ist
    phase4_text = generate_phase4_text(auv_data['phase4'], is_anlagevermogen, is_umlaufvermogen)
    
    if is_anlagevermogen:
        # Zeile 14, 17 versteckt → Phase 4 Text nicht in diese Zeilen schreiben
        # Phase 4 würde in Zeile 16+ gehen (nach Verbrauchsgut-Zeilen)
        pass  # TODO: Klärung erforderlich, wo Phase 4 Text stattdessen hin
    else:
        # Zeile 14, 17 sichtbar → Phase 4 Text wie normal
        ws['B14'] = phase4_text  # oder andere Zeile, je nach Grund
    
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
        return phase3_data.get('sonstiges_text', '')
    return ""

def generate_phase4_text(phase4_data, is_anlagevermogen=False, is_umlaufvermogen=False):
    """
    Phase 4 Grund in Text konvertieren.
    
    Hinweis: Je nach Güterklassifizierung werden unterschiedliche Texte verwendet.
    """
    if is_anlagevermogen:
        # Für Anlagevermögen: Grund 3 (keine Folgeausgaben)
        return "Der Bedarf ist einmalig. Nach der Anschaffung fallen keine Folgeausgaben an."
    else:
        # Für Umlaufvermögen: Grund 1 oder 2
        texts = {
            1: "Der Bedarf ist einmalig. Das Verbrauchsgut wird nach Aufbrauch nicht erneut beschafft.",
            2: "Der Bedarf ist für dieses Jahr einmalig. Folgebedarfe werden in kommenden Jahren separat betrachtet.",
            3: "Der Bedarf ist einmalig. Nach der Anschaffung fallen keine Folgeausgaben an."
        }
        grund = phase4_data.get('grund', 1)
        if grund in texts:
            return texts[grund]
        else:
            return phase4_data.get('sonstiges_text', '')
```

**Vor dem Export: 4-Punkt Validierung (Phase 7):**

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
    
    # CHECK 4: Güterklassifizierung ermitteln (für Conditional Row Hiding)
    # Phase 4 Grund → Güterklassifizierung ableiten:
    #   Grund 1, 2 → Umlaufvermögen (Verbrauchsgüter)
    #   Grund 3 → Anlagevermögen (Nichtverbrauchsgüter)
    grund = auv_data.get('phase4', {}).get('grund')
    if grund in [1, 2]:
        auv_data['_gueterklassifizierung'] = 'umlaufvermogen'
    elif grund == 3:
        auv_data['_gueterklassifizierung'] = 'anlagevermogen'
    else:
        errors.append(f"❌ Phase 4 Grund nicht erkannt: {grund}")
    
    return errors, warnings
```

**Wichtig — Güterklassifizierung-Logik:**

Die Klassifizierung wird aus Phase 4 (Grund für Einmaligkeit) hergeleitet:

```
Phase 4 Grund 1: "Verbrauchsgut wird nach Aufbrauch nicht erneut beschafft"
→ Umlaufvermögen (Verbrauchsgut)

Phase 4 Grund 2: "Bedarf ist für dieses Jahr einmalig"
→ Umlaufvermögen (Verbrauchsgut)

Phase 4 Grund 3: "Nach Anschaffung fallen keine Folgeausgaben an"
→ Anlagevermögen (Nichtverbrauchsgut)
```

Diese Information wird an `export_auv_to_vermerk()` übergeben zur Steuerung des Conditional Row Hiding.

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

## Abbruch & Wechsel zu Dialogpfad D

**Wann wird zu Dialogpfad D gewechselt?**

Wenn User in Phase 4b (Wirtschaftlichkeits-Vergleich für Anlagevermögen):
- WebRecherche durchführen lässt
- System zeigt: **Miete/Dienstleistung ist günstiger**
- User entscheidet sich: "Ja, ich möchte die Miete-Option prüfen"

**Was passiert beim Wechsel?**

```
Dialogpfad AUV wird UNTERBROCHEN
    ↓
User-Daten werden an Dialogpfad D übergeben:
  ✓ Dienststelle, Bearbeiter, Maßnahmenbeginn
  ✓ Bedarfsforderung
  ✓ Recherche-Ergebnisse (Mietpreis, Einsatztage/Jahr)
    ↓
Dialogpfad D startet: WU für Miete/Leasing/Dienstleistung
```

**Hinweis:** Dialogpfad D wird separat dokumentiert (noch zu erstellen).

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
  ├─ Phase 4b: Wirtschaftlichkeits-Vergleich (NUR für Anlagevermögen/Grund 3)
  │           ├─ WebRecherche nach Mietpreisen (optional)
  │           └─ Ggfs. Wechsel zu Dialogpfad D
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
Phase 4b:      0–5 Min (NUR für Anlagevermögen; optional WebRecherche)
               • Option A (keine Recherche): <1 Min (Text eingeben)
               • Option B (mit Recherche): 3–5 Min (Recherche + Entscheidung)
Phase 5:       <1 Min  (Preis bestätigen)
Phase 6:       <1 Min  (Info-Box lesen)
Phase 7:       1–2 Min (Export + Erfolgsmeldung)
────────────────────────
GESAMT:        ~8–12 Min (ohne Korrigieren; mit Phase 4b)
               ~7–10 Min (ohne Phase 4b, falls Umlaufvermögen)
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
