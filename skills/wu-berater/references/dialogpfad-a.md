# Dialogpfad A: Unterjährige WU

Für **einmalige Käufe ohne Folgeausgaben** — minimale User-Eingaben, maximale Automation.

**Ziel:** Ein vollständiges, BHO-konformes WU-Dokument mit strukturiertem Dialog:
- 4 Eingabe-Felder (Metadaten + Sachverhalt)
- 8 konkrete Dialog-Fragen zur Bedarfsforderung (keine erfundenen Details)
- Strukturierte Ausschlussgründe (keine Freitext-Risiken)
- Automatische Validierung vor Export
- Realistisch: effizienter Prozess, Zeitaufwand abhängig von User-Antworten

**Modi**: Geführter Dialog (Schritt für Schritt) oder Schnelldurchlauf (alle Schritte auf einmal).

---

## Phase 1: Erfassung der 4 Eingabe-Felder (NACH WU-Typ-Bestimmung)

**Hinweis:** Dies ist NICHT der Startdialog. Der Startdialog befindet sich in `SKILL.md` und ist allgemeingültig (vor WU-Typ-Bestimmung).

Sobald die WU als "Dialogpfad A (unterjährig)" klassifiziert wurde, startet Phase 1 mit der Erfassung dieser 4 Angaben:

| Feld | Typ | Beispiel | Verwendung |
|---|---|---|---|
| **Dienststelle** | Text | BAIUDBw, KommBw BwDLZ München | Meta: Dokumentkopf, später für Auswertungen |
| **Bearbeiter** | Text | Schmid, Sandra (E9b) | Meta: Dokumentkopf |
| **Kaufbeschreibung** | Text | „Drucker für die Büros" | Auslöser für A1-Dialog (siehe unten) |
| **Geschätzter Preis** | EUR | 2.500,00 | Auslöser für A4-Dialog (Miete-Vergleich?) |

### Dialog Phase 1: Die 4 Eingabe-Felder erfassen

```
SKILL (nach WU-Typ-Bestimmung): „Gut, wir machen eine unterjährige WU. 
Jetzt brauche ich folgende Angaben zur Vorbereitung:

Geben Sie bitte ein:
1. Dienststelle: [User: BAIUDBw]
2. Bearbeiter (Ihr Name): [User: Schmid, Sandra]
3. Was soll gekauft werden? [User: Drucker für die Büros]
4. Ungefährer Preis? [User: 2.500 EUR]

(Danke! Ich stelle jetzt Fragen zur Bedarfsforderung …)"
```

**Nach Erfassung der 4 Felder → direkt zu A1-Bedarfsforderung-Dialog (Phase 2)**

---

## Schritt A1: Bedarfsforderung konkretisieren

### Dialog (Transformation User-Input → BHO-konforme Anforderung)

Siehe detaillierte Referenz: **`bedarfsforderung-konkret-a.md`** (8 konkrete Fragen, KEINE erfundenen Details)

**WICHTIG — Fallback-Logik bei vagen Antworten (Punkt 2):**

Wenn User nicht strukturiert antwortet (z.B. nur „Ja" / „Nein" / „Keine Ahnung"), geht der Dialog NICHT sofort zu Auto-Generierung über.

```
USER: „Drucker für die Büros"
SKILL: „1. Welche Funktionen brauchst du? Optionen: [ ] Nur Druck [ ] Druck+Kopie [ ] Druck+Kopie+Scan"
USER: „Weiß nicht genau"

→ FALLBACK-LOGIK (wenn User unstrukturiert antwortet):
SKILL: „Okay, basierend auf ‚Büro-Drucker' mache ich folgende Standardannahmen:
  
  ✓ Funktionen: Druck + Kopie (üblich bei Bürodruckern)
  ✓ Kapazität: 10.000 Seiten/Monat (Standard für Büroumgebung)
  ✓ Farbdruck: Ja (oft benötigt)
  ✓ Netzwerk: Ja (moderner Standard)
  ✓ Einsatzhäufigkeit: Täglich, Mo–Fr (220 Tage/Jahr)
  
  Passen diese Annahmen zu deiner Situation? 
  [ ] Ja, so ist es richtig → weitermachen mit Bedarfsforderung
  [ ] Einiges stimmt nicht → welcher Punkt? [Checkboxen für F1-F8]
  [ ] Komplett neu durchgehen → alle 8 Fragen strukturiert"
```

**Workflow:**
- Falls User ✓ „Ja, so ist es richtig" → mit Bedarfsforderung-Generierung weitermachen
- Falls User korrigiert → nur für geänderte Punkte neue Fragen (F1–F8)
- Falls User „detailliert" will → alle 8 Fragen im vollen Dialog

---

**SKILL **generiert Bedarfsforderung** mit bestätigten Antworten:

> „Die [Dienststelle] benötigt eine Druck- und Kopierfähigkeit zur Unterstützung der Büroprozesse. Der Bedarf umfasst eine Kapazität von mindestens 10.000 Seiten pro Monat mit folgenden Mindestanforderungen: Farbdruck (CMYK), Netzwerkanbindung (LAN/WLAN). Das Gerät ist voraussichtlich täglich während der Regelarbeitszeit (Mo–Fr, 220 Tage/Jahr) einzusetzen."

**Inline-Validierung:**
- ✅ Enthält keine Produktnamen? JA
- ✅ Nennt nur Funktionen? JA
- ✅ Alle Details aus Antworten? JA (NICHTS erfunden)
- ✅ Mindestens 2 messbare Anforderungen? JA (10.000 S./M., Farbe, Netzwerk, 220 Tage/Jahr)

→ **Bestätigung an User: „Stimmt diese Bedarfsforderung? [Ja / Korrigieren]"**

---

## Schritte A1–A6

Folge diese Reihenfolge. **Satzmuster** sind in `satzmuster-ac.md` dokumentiert.

| Schritt | Inhalt | Satzmuster in satzmuster-ac.md | Validierung | Automatisierung |
|---------|--------|------|------|------|
| A1 | **Bedarfsforderung konkretisieren** (8 Fragen strukturiert, keine erfundenen Details) | A1 | ✅ **Inline-Check** (`validate_step('bedarfsforderung', ...)`) | ⚡ Auto-Dialog + Auto-Generierung |
| A2 | Bisherige Bedarfsdeckung (intelligenter Default) | A2 | — | Semi-Auto: Vorschlag basierend auf Sachverhalt (User bestätigt oder editiert) |
| A3 | **Ausschluss Eigenleistung** (Structured Choices, Guard Check) | A3 | ✅ **Guard Check** (`validate_step('aussonderung', ...)`) | Semi-Auto: Checkboxen (4 Optionen), Guard prüft automatisch |
| A4 | **Ausschluss Miete/Leasing** (WebRecherche + User-Bestätigung der Annahmen) | A4 | ✅ **Guard Check** | Semi-Auto: Recherche ja, aber User bestätigt Einsatztage + Mietpreis; Fallback bei Fehler |
| A5 | Bestätigung Unterjährigkeit (keine Folgeausgaben) | A5 | — | Auto: Standard-Text (User bestätigt) |
| A6 | **Kostenermittlung & Export zu Excel** (erweiterte Validierung) | Python-Snippet | ✅ **Vor Export**: 6 Auto-Checks (`validate_wu_unterjahrig_extended()`) | ⚡ Auto: Sanitizing + Excel-Export |

**Pflichtprüfung bei A3 & A4 (Guard Checks):**
- Fehlendes Personal, Dienstposten, Haushaltsmittel, Infrastruktur sind **KEINE zulässigen Ausschlussgründe**
- Bei zeitlichen Rahmenbedingungen: Nutzer auf Belegpflicht hinweisen (z.B. „Ein Eigenleistungs-Gerät kann bis [Datum] nicht bereitgestellt werden. Dies ist durch Aussage [Dienststelle] vom [Datum] dokumentiert (vgl. Anlage [X]).")

---

## Detaillierte Workflow für A1–A6

### A1: Bedarfsforderung konkretisieren (AUTO-DIALOG)

**User-Input verfügbar:** „Drucker für die Büros", Preis: 2.500 EUR

**SKILL führt strukturiertes 8-Fragen-Dialog:**

Siehe detailliert: **`bedarfsforderung-konkret-a.md`** (exakte Fragen 1–8 mit Optionen)

```
SKILL: „Damit ich die Bedarfsforderung BHO-konform formuliere, brauche ich folgende Infos:

1. FUNKTIONEN — Welche brauchst du?
   [ ] Nur Druck  [ ] Druck+Kopie  [ ] Druck+Kopie+Scan  [ ] Alle

2. KAPAZITÄT ZEITSPANNE — Pro Monat oder Jahr?
   [ ] Monat  [ ] Jahr

3. KAPAZITÄT MENGE — Wie viel?
   [Eingabe] Seiten/Monat

4. FARBE — Farbdruck?
   [ ] Ja, CMYK  [ ] Gelegentlich  [ ] Nein, s/w

5. NETZWERK — Erforderlich?
   [ ] Ja, erforderlich  [ ] Optional  [ ] Nein

6. EINSATZHÄUFIGKEIT — Wie oft?
   [ ] Täglich  [ ] 3-4x/Woche  [ ] 1-2x/Woche  [ ] Sporadisch

7. EINSATZTAGE/JAHR — Ungefähr?
   [Eingabe] Tage/Jahr

8. ZUSATZ — Besonderheiten?
   [ ] Duplex  [ ] A3-Format  [ ] Hohe Geschwindigkeit  [ ] Keine
```

User antwortet strukturiert über Checkboxen + Zahleneingaben

**SKILL generiert Bedarfsforderung** (nur aus echten Antworten, siehe bedarfsforderung-konkret-a.md)

**Inline-Validierung:**
```
✅ Bedarfsforderung validiert
   - Keine Produktnamen: BESTANDEN
   - Funktional + lösungsneutral: BESTANDEN
   - Messbar quantitativ: BESTANDEN (10.000 S./Monat)
   - Messbar qualitativ: BESTANDEN (Farbe, Netzwerk)
```

**Bestätigung an User:**
```
„Bedarfsforderung:
[Volltext]

Passt das so? [Ja / Nein / Korrigieren]"
```

---

### A2: Bisherige Bedarfsdeckung (SEMI-AUTO mit intelligentem Default)

**Intelligenter Default basierend auf Sachverhalt:**

```python
def intelligenter_a2_default(kaufbeschreibung, bedarfsforderung):
    """
    Generiert A2-Text basierend auf Schlüsselwörtern in Kaufbeschreibung.
    """
    
    # Extrahiere Produkttyp aus Bedarfsforderung für Singular/Plural
    def extract_product_type(bedarfsforderung):
        # z.B. "Druckfähigkeit" → "Drucker"
        # "Transportfähigkeit" → "Transporter"
        # "Sitzmöbel" → "Sitzmöbel"
        words = bedarfsforderung.lower().split()
        for word in ['druck', 'transport', 'sitz', 'rechen']:
            if word in bedarfsforderung.lower():
                return word.capitalize() + 'lösung'  # Fallback
        return 'Ausrüstung'  # Generic Fallback
    
    produkttyp = extract_product_type(bedarfsforderung)
    
    # Logik
    if any(word in kaufbeschreibung.lower() for word in ['neu', 'neu hinzugekommen', 'neu erforderlich']):
        return "Der Bedarf ist neu entstanden und wurde bisher nicht erfüllt."
    
    elif any(word in kaufbeschreibung.lower() for word in ['alt', 'ersatz', 'austausch', 'zu alt']):
        return f"Der Bedarf wurde bisher durch einen älteren {produkttyp} gedeckt, der nicht mehr ausreichend kapazitätsgerecht ist und daher ersetzt werden soll."
    
    elif any(word in kaufbeschreibung.lower() for word in ['zusätzlich', 'ergänzung', 'erweiterung']):
        return f"Der Bedarf wird zusätzlich zu bestehenden {produkttyp}n erfüllt, da die bisherige Kapazität nicht ausreicht."
    
    else:
        # Fallback: Generic
        return f"Der Bedarf wurde bisher durch vergleichbare Beschaffungen gedeckt und wird durch die geplante {produkttyp} ersetzt/ergänzt."

# Beispiel
default_text = intelligenter_a2_default("Drucker für die Büros", bedarfsforderung_aus_a1)
# Output: "Der Bedarf wurde bisher durch einen älteren Drucker gedeckt, ..."
```

**USER SIEHT:**
```
„Bisherige Bedarfsdeckung:

Vorschlag:
[Auto-generierter Text z.B. „Der Bedarf wurde bisher durch einen älteren Drucker gedeckt, …"]

Passt das? 
[ ] Ja, so ist es richtig
[ ] Nein, anders formulieren: [Freitext]
```

**Fallback:** Wenn User nichts sagt → Vorschlag wird übernommen (echte Semi-Auto)

---

### A3: Ausschluss Eigenleistung (SEMI-AUTO mit striktem Guard Check)

**Keine Freitext-Eingaben — nur Structured Choices mit Auto-Generierung:**

```
SKILL: „Warum scheidet Eigenleistung aus? Bitte wähle EINEN Grund:

GRUND 1: Kein geeignetes Gerät/Material intern vorhanden
┌─────────────────────────────────────────────────────────┐
│ [ ] Grund 1                                              │
│     → Generierter Satz:                                  │
│     „Eine Eigenleistung scheidet aus, da kein geeignetes│
│      Gerät intern vorhanden ist."                        │
└─────────────────────────────────────────────────────────┘

GRUND 2: Verbrauchsgut/Material ist verbraucht
┌─────────────────────────────────────────────────────────┐
│ [ ] Grund 2                                              │
│     → Generierter Satz:                                  │
│     „Eine Eigenleistung scheidet aus, da das bisherige   │
│      Verbrauchsgut verbraucht ist und durch Neubeschaffung
│      ersetzt werden muss."                               │
└─────────────────────────────────────────────────────────┘

GRUND 3: Zeitliche Frist — Maßnahme muss bis [DATUM] abgeschlossen sein
┌─────────────────────────────────────────────────────────┐
│ [ ] Grund 3 [DATUM eingeben: __________]                │
│             [Quellenangabe: __________]                 │
│     → Generierter Satz:                                  │
│     „Eine Eigenleistung scheidet aus, da die Beschaffung│
│      bis [DATUM] abgeschlossen sein muss. Eine Eigenleis-
│      tungs-Vorbereitung ist in diesem Zeitraum nicht    │
│      möglich (vgl. Anlage [X]: [Quellenangabe])."      │
└─────────────────────────────────────────────────────────┘

GRUND 4: Spezialisierte Fachkompetenz erforderlich, intern nicht vorhanden
┌─────────────────────────────────────────────────────────┐
│ [ ] Grund 4 [Quellenangabe: __________]                 │
│     → Generierter Satz:                                  │
│     „Eine Eigenleistung scheidet aus, da die erforderliche
│      Fachkompetenz intern nicht vorhanden ist (vgl. Anlage
│      [X]: [Quellenangabe])."                            │
└─────────────────────────────────────────────────────────┘

⚠️ AUTOMATISCH BLOCKIERT (Guard Check):
    ❌ Freitext mit Worten: „Haushalt", „Personal", „Dienstposten", „Infrastruktur"
    ❌ Fehlertext: „Dieser Grund ist nicht zulässig. Verwende eine der 4 Optionen oben."
"
```

**Guard Check Logik:**
```python
def validate_a3_grund(user_choice, datum=None, quellenangabe=None):
    """
    Prüft A3-Grund gegen verbotene Schlüsselwörter.
    KEINE Freitext-Eingaben außer Datum und Quellenangabe.
    """
    forbidden_patterns = [
        r'(?:haushalt|budget|mittel|geld)', 
        r'(?:personal|dienstposten|stellen)',
        r'(?:infrastruktur|raum|ressourcen)',
        r'(?:kosten|ausgaben|teuer)'
    ]
    
    # user_choice ist ENUM (Grund 1-4), keine Freitext
    if user_choice not in [1, 2, 3, 4]:
        return ❌ FEHLER: „Bitte wähle einen der 4 vorgegebenen Gründe."
    
    # Grund 3 & 4 erfordern Quellenangabe
    if user_choice in [3, 4] and not quellenangabe:
        return ❌ FEHLER: „Quellenangabe erforderlich (z.B. 'Schreiben Personalstelle vom XYZ')"
    
    return ✅ Grund ist zulässig
```

**Guard Check — AUTOMATISCHE PRÜFUNG:**
```python
def validate_a3_grund(grund_text):
    forbidden_patterns = [
        r'(?:haushalt|budget|mittel|geld)', 
        r'(?:personal|dienstposten|stellen)',
        r'(?:infrastruktur|raum|ressourcen)',
        r'(?:kosten|ausgaben|teuer)'
    ]
    
    for pattern in forbidden_patterns:
        if re.search(pattern, grund_text, re.IGNORECASE):
            return ❌ FEHLER: „Dieser Grund ist nicht zulässig. 
                           Verwende bitte nur die vorgegebenen Optionen."
    
    return ✅ Grund ist zulässig
```

**Belegpflicht bei zeitlichen Rahmenbedingungen:**
Wenn User „Grund 3" wählt, MUSS User:
- Konkretes Datum eingeben
- Quellenangabe/Anlage-Referenz eingeben (z.B. „Schreiben Personalstelle vom 15.04.2026")

**Text wird ins Dokument übernommen** (keine weitere Korrektur nötig)

---

### A4: Ausschluss Miete/Leasing (SEMI-AUTO mit WebRecherche — Punkt 3)

**NICHT vollständig automatisch — WebRecherche ja, aber mit User-Bestätigung der Annahmen:**

```python
# SCHRITT 1: WebRecherche Mietpreise
kaufpreis = 2500  # aus Feld 4
produkt = "Drucker"  # aus Feld 3 extrahiert

try:
    # WebRecherche: Mietpreise für Drucker
    mietpreis_range = webrecherche_mietpreis(f"{produkt} mieten Tagesmiete")
    # Ergebnis z.B.: (15, 35)  # EUR/Tag Range
    mietpreis_mittel = (mietpreis_range[0] + mietpreis_range[1]) / 2  # z.B. 25 EUR/Tag
except:
    # Fallback wenn WebRecherche fehlschlägt
    print("⚠️ WebRecherche Mietpreise fehlgeschlagen. Bitte manuell eingeben.")
    mietpreis_mittel = None

# SCHRITT 2: Dem User zeigen, was aus Bedarfsforderung extrahiert wurde
einsatztage_jahr = extract_einsatztage_from_bedarfsforderung(bedarfsforderung)
# z.B. 220 (aus „220 Tage/Jahr")

print(f"""
RECHERCHE-ERGEBNISSE — Bitte bestätigen:

Ihre Angaben (aus Bedarfsforderung):
  • Einsatzhäufigkeit: täglich
  • Einsatztage pro Jahr: {einsatztage_jahr} Tage
  • Kaufpreis: {kaufpreis} EUR

Mietpreis-Recherche:
  • Tagesmiete für {produkt}: ca. {mietpreis_mittel:.2f} EUR/Tag
  • Quelle: [URL aus WebRecherche]
  
Jährliche Mietkosten: {mietpreis_mittel * einsatztage_jahr:.2f} EUR/Jahr
Break-even: {kaufpreis / mietpreis_mittel:.0f} Einsatztage

⚠️ WICHTIG — Bitte prüfen:
  [ ] Sind die {einsatztage_jahr} Einsatztage/Jahr korrekt?
      (oder soll es eine andere Zahl sein: ___ Tage)
  
  [ ] Passt der Mietpreis von ca. {mietpreis_mittel:.2f} EUR/Tag?
      (oder realistischer: ___ EUR/Tag)
  
  Sobald bestätigt, berechne ich Break-even neu falls nötig.
""")
```

**SCHRITT 3: User bestätigt Annahmen**

```
USER bestätigt:
  ✓ 220 Einsatztage/Jahr → stimmt
  ✓ 25 EUR/Tag Mietpreis → stimmt

DANN: Break-even berechnen und Text generieren
```

**Output (nach Bestätigung):**
> „Eine Anmietung ist wirtschaftlich nicht vorteilhaft. Tagesmiete ca. 25 EUR (Anlage MR, Nr. 2), Kaufpreis ca. 2.500 EUR (Anlage MR, Nr. 1). Amortisations-Break-even: 100 Einsatztage. Da das Gerät täglich eingesetzt wird (220 Tage/Jahr), ist der Kauf deutlich wirtschaftlicher."

**Fallback-Szenario 1: WebRecherche fehlgeschlagen**
```
SKILL: „⚠️ WebRecherche Mietpreise für [Produkttyp] konnte nicht durchgeführt werden.
        (Grund: Netzwerkfehler / Keine Ergebnisse / Rate Limiting)
        
        Drei Optionen:
        [ ] A) Mit anderen Suchbegriffen erneut versuchen
            Suchbegriff: [Eingabe] → [Skill recherchiert erneut]
        
        [ ] B) Manuell eingeben
            Tagesmiete für [Produkttyp]: ___ EUR/Tag
            [Skill berechnet Break-even mit eingegebener Zahl]
        
        [ ] C) A4 überspringen
            (Dann entfällt die Miete-Ausschlussbegründung im Dokument
             und nur das Kaufpreis-Angebot wird dokumentiert)"
```

**Fallback-Szenario 2: WebRecherche erfolgreich, aber User zweifelt Ergebnis**
```
SKILL (nach Recherche): „⚠️ Recherche zeigt: Tagesmiete ca. 25 EUR/Tag
        Sie haben Zweifel?
        
        [ ] A) Diese Zahl ist zu hoch/niedrig. Korrekt ist: ___ EUR/Tag
        [ ] B) Mit anderen Suchbegriffen neu recherchieren
        [ ] C) A4 komplett weglassen (kein Miete-Text im Dokument)"
```

**Implementierungs-Hinweis:**
```python
try:
    mietpreis_range = webrecherche_mietpreis(produkt)
    # Erfolgreich → User-Bestätigung Dialog
except WebSearchError:
    # Fallback: Optionen A/B/C anzeigen
    user_choice = ask_user(fallback_optionen)
    if user_choice == 'A':
        mietpreis = user_input("Tagesmiete eingeben")
    elif user_choice == 'B':
        # Erneut mit neuem Suchbegriff
    elif user_choice == 'C':
        # A4 komplett überspringen → a4_begruendung = None
```

---

### A5: Bestätigung Unterjährigkeit (AUTO)

**Automatischer Text** (wird vom User bestätigt):
> „Für [Produkt/Bezeichnung] fallen nach Anschaffung keine Folgeausgaben an. Einmalige Ausgabe im Haushaltsjahr [Jahr], kein weiterer Kapitalbedarf in Folgejahren."

---

### A6: Kostenermittlung & Export (VOLL-AUTO)

```python
# Sammle alle Daten
wu_data = {
    'meta': {
        'dienststelle':     'BAIUDBw',
        'bearbeiter':       'Schmid, Sandra',
        'datum':            '2026-04-23',
        'beginn_massnahme': '2026-05-15',
        'schutz':           'offen',
        'version':          '1',
    },
    'inhalt': {
        'bedarfsforderung': '[aus A1]',
        'haken': {
            'kauf_benoetigt':      True,
            'eigenleistung_sonst': True,
            'miete_sonstiges':     True,
            'keine_folgeausgaben': True,
        },
        'eigenleistung_begruendung': '[aus A3]',
        'miete_begruendung':         '[aus A4 – AUTO]',
        'a2_bisherige_bedarfsdeckung': '[aus A2]',
        'ausgaben':                  2500,  # EUR aus Feld 4
    },
    'anlage': [
        {'nr': '1', 'produkt': 'Drucker XYZ', 'preis': '2.500 EUR', 'url': '[WebRecherche]', 'bemerkung': 'Kaufpreis, 2026-04-23'},
        {'nr': '2', 'produkt': 'Drucker Tagesmiete', 'preis': '20 EUR/Tag', 'url': '[WebRecherche]', 'bemerkung': 'Mietpreisvergleich, 2026-04-23'},
    ],
}

# VALIDIERUNG vor Export
validator = WuValidator(wu_type='unterjahrig')
is_valid, errors, warnings = validator.validate(wu_data)

if not is_valid:
    print(f"❌ Fehler gefunden: {errors}")
    # Rückkopplung an User
else:
    # EXPORT
    outpath = build_filename(wu_data['meta']['datum'], 'Drucker', 'BAIUDBw')
    success, outpath, summary = export_safe(wu_data, ...)
    print(f"✅ Dokument exportiert: {outpath}")
```

**Ergebnis:** Excel-Datei `20260423_WU_Drucker_BAIUDBw_Version_1.xlsm` mit allen Kapiteln ausgefüllt und bereit zum Versand.

---

## Korrektur-Workflow (Punkt 9 — wenn User Änderungen will)

**Szenario 1: User korrigiert A1 Bedarfsforderung**
```
USER: „Kann ich die Bedarfsforderung noch ändern?"
SKILL: „Ja, welchen Teil möchtest du anpassen?
        [ ] Funktionen
        [ ] Kapazität
        [ ] Farbe
        [ ] Netzwerk
        [ ] Einsatzhäufigkeit
        [ ] Alles neu machen"

→ NEUER DIALOG für geänderte Punkte
→ A1 wird NEU generiert
→ A2–A6 werden basierend auf neuer A1 NEU berechnet
→ Keine Neubestätigung der bereits korrekten A2–A3 nötig
```

**Szenario 2: User mag A4 WebRecherche-Ergebnis nicht**
```
USER: „Der Mietpreis von 25 EUR/Tag passt nicht"
SKILL: „Okay, drei Optionen:
        [ ] Mit anderen Suchbegriffen erneut recherchieren
        [ ] Manuell eingeben (z.B. 35 EUR/Tag)
        [ ] Punkt A4 komplett überspringen (= kein Miete-Ausschluss-Text)"

→ A4 wird ANGEPASST (nicht ganz neu)
→ Break-even neu berechnet
→ Text wird neu generiert
```

**Szenario 3: User möchte Details nach der Generierung ändern**
```
Allgemein:
- Jeder Schritt A1–A5 kann nach Generierung noch angepasst werden
- User kann Freitext editieren (aber Validierung wird erneut durchgeführt)
- Vor Export werden alle Änderungen nochmal validiert
```

---

## Warum A3 und A4? — Redundanz erklärt (Punkt 11)

**Frage:** „Die Bedarfsforderung sagt bereits, was gebraucht wird. Warum müssen wir EXTRA dokumentieren, dass Eigenleistung / Miete ausscheidet?"

**Antwort:**

1. **Bedarfsforderung (A1)** = WAS wird gebraucht?
   - Funktional beschrieben (z.B. „Druckfähigkeit")
   - Nicht: wie wird es beschafft

2. **Ausschluss-Gründe (A3 + A4)** = WARUM diese spezifischen Optionen nicht?
   - Explizite Begründung für Revisor/Prüfer
   - Nachvollziehbar, warum nicht Eigenleistung / Miete
   - **BHO-Anforderung:** Alle geprüften Optionen müssen dokumentiert sein

**Beispiel:**
```
A1 Bedarfsforderung:
→ „[Dienststelle] benötigt eine Druckfähigkeit …"
  (Was: Funktion, nicht Lösung)

A3 Ausschluss Eigenleistung:
→ „Eine Eigenleistung scheidet aus, da kein geeignetes Gerät intern vorhanden ist."
  (Warum: konkrete Situation)

A4 Ausschluss Miete:
→ „Eine Anmietung ist wirtschaftlich nicht vorteilhaft …"
  (Warum: Kostenvergleich)

Resultat: Nur Option KAUF bleibt übrig → dokumentiert und begründet
```

**Das ist nicht redundant, sondern VOLLSTÄNDIG.**

---

## Workflow-Übersicht: Dialogpfad A (nach Startdialog + WU-Typ-Bestimmung)

**Kontext:** Dieser Workflow startet nach:
1. ✅ Startdialog (SKILL.md) beantwortet
2. ✅ WU als "Dialogpfad A (unterjährig)" klassifiziert
3. ✅ User wählt "Geführter Dialog" oder "Schnelldurchlauf"

| Phase | Nutzer-Input | System-Verarbeitung |
|-------|--------|--------|
| **Phase 1: Eingabe** | Gibt 4 Felder ein (Dienststelle, Bearbeiter, Kaufbeschreibung, Preis) | Speichert Eingaben |
| **A1** | Beantwortet 8 Fragen zu Bedarfsforderung (oder bestätigt Standardannahmen) | Auto-generiert Bedarfsforderung aus echten Daten (KEINE erfundenen Details) |
| **A1-Check** | Prüft + bestätigt A1 Bedarfsforderung oder korrigiert | Validierung: keine Produktnamen, lösungsneutral |
| **A2** | Bestätigt/korrigiert A2 (intelligenter Default) | Generiert A2-Vorschlag basierend auf Sachverhalt |
| **A3** | Wählt Grund für A3 (Structured Choices, keine Freitext) | Guard Check prüft auf verbotene Gründe |
| **A4** | Bestätigt A4 Mietpreis-Annahmen oder korrigiert | WebRecherche + Break-even-Berechnung; prüft Einsatztage/Jahr |
| **A5** | Bestätigt A5 Standard-Text | (Auto, kein Input nötig) |
| **Validierung** | Prüft Export-Validierung (Checkliste) | Erweiterte Validierung: Produktnamen, Preis-Realismus, verbotene Gründe |
| **Export** | Bestätigt Export oder Korrekturwünsche | Sanitiert Dateiname, exportiert zu Excel |

**Ergebnis:** Vollständiges, validiertes, BHO-konformes WU-Dokument.
*Zeitaufwand abhängig von User-Input und WebRecherche-Ergebnissen.*

---

## Export (A6 — Detaillierte Implementierung)

**Export erfolgt vollständig automatisch nach Bestätigung durch User.**

```python
import sys
from datetime import datetime
sys.path.insert(0, 'P:/WUKI_Projekt/Claude/skills/wu-berater/scripts')
from export_wu_unterjahrig import fill_template, build_filename
from wu_builder import WuValidator

# Datenstruktur WU_DATA (Sammlung aller Eingaben aus A1–A5)
wu_data = {
    'meta': {
        'dienststelle':     '[aus Feld 1]',          # z.B. 'BAIUDBw'
        'bearbeiter':       '[aus Feld 2]',          # z.B. 'Schmid, Sandra (E9b)'
        'datum':            datetime.now().strftime('%d.%m.%Y'),  # AUTO: heute
        'beginn_massnahme': '[User-Eingabe oder Auto]',  # z.B. '15.05.2026'
        'schutz':           'offen',                 # FEST
        'version':          '1',                     # FEST
    },
    'inhalt': {
        # A1: Bedarfsforderung (AUTO-GENERIERT aus Dialog)
        'bedarfsforderung': '[Volltext aus A1-Dialog]',
        
        # A2: Bisherige Bedarfsdeckung
        'a2_bisherige_bedarfsdeckung': '[Text aus A2]',
        
        # A3: Eigenleistungs-Ausschluss
        'eigenleistung_begruendung': '[Text aus A3]',
        
        # A4: Miete-Ausschluss (AUTO)
        'miete_begruendung': '[AUTO-generiert aus A4 + Webrecherche]',
        
        # A5: Unterjährigkeit
        'a5_unterjährigkeit': '[Standard-Text A5]',
        
        # Häkchen für Validierung
        'haken': {
            'kauf_benoetigt':      True,    # immer True in Dialog A
            'eigenleistung_sonst': True,    # aus A3 bestätigt
            'miete_sonstiges':     True,    # aus A4 bestätigt
            'keine_folgeausgaben': True,    # aus A5 bestätigt
        },
        
        # Kaufpreis (aus Feld 4)
        'ausgaben': float('[Feld 4: Preis in EUR]'),  # z.B. 2500.00
    },
    
    # Anlagen: Marktrecherche-Einträge (AUTO-generiert)
    'anlage': [
        {
            'nr': '1',
            'produkt': '[Produkt-Kategorie, z.B. "Drucker mit Kopierfunktion"]',
            'preis': '[Kaufpreis EUR]',
            'url': '[WebRecherche-URL oder „Marktabfrage"]',
            'bemerkung': f'Kaufpreis, {datetime.now().strftime("%d.%m.%Y")}',
        },
        {
            'nr': '2',
            'produkt': '[Produkt-Kategorie, z.B. "Drucker Tagesmiete"]',
            'preis': '[Mietpreis EUR/Tag]',
            'url': '[WebRecherche-URL oder „Marktabfrage"]',
            'bemerkung': f'Mietpreisvergleich, {datetime.now().strftime("%d.%m.%Y")}',
        },
    ],
}

# SCHRITT 1: Validierung vor Export (Punkt 8 — erweiterte Auto-Checks)
print("🔍 Validiere WU vor Export…")

def validate_wu_unterjahrig_extended(wu_data):
    """
    Erweiterte Validierung vor Export mit spezifischen Prüfungen.
    """
    errors = []
    warnings = []
    
    # CHECK 1: Bedarfsforderung — Produktnamen prüfen
    forbidden_produktnamen = [
        'drucker', 'kyocera', 'brother', 'hp', 'canon', 'ricoh',
        'laptop', 'dell', 'hp', 'lenovo', 'thinkpad',
        'transporter', 'vw', 'mercedes', 'iveco',
        'bürostuhl', 'steelcase', 'haworth'
    ]
    bedarfsforderung_lower = wu_data['inhalt']['bedarfsforderung'].lower()
    
    for name in forbidden_produktnamen:
        if name in bedarfsforderung_lower:
            errors.append(
                f"❌ Bedarfsforderung enthält Produktnamen '{name}'. "
                f"Bitte lösungsneutral reformulieren (nur Funktionen nennen)."
            )
            break  # nur eine Fehlermeldung
    
    # CHECK 2: Kaufpreis — Realismus-Prüfung
    preis = wu_data['inhalt']['ausgaben']
    if preis < 50:
        warnings.append(
            f"⚠️ Kaufpreis sehr niedrig ({preis:.2f} EUR). "
            f"Ist das wirklich realistisch?"
        )
    elif preis > 500000:
        warnings.append(
            f"⚠️ Kaufpreis sehr hoch ({preis:.2f} EUR). "
            f"Sollte das wirklich eine unterjährige WU sein (kein Kreditrahmen)?"
        )
    
    # CHECK 3: Eigenleistungs-Ausschluss — auf verbotene Gründe prüfen
    eigenleistung_text = wu_data['inhalt']['eigenleistung_begruendung']
    forbidden_grounds = [
        'personal', 'haushaltsmittel', 'haushalt', 'budget', 
        'dienstposten', 'infrastruktur', 'raum', 'mittel'
    ]
    
    for ground in forbidden_grounds:
        if ground in eigenleistung_text.lower():
            errors.append(
                f"❌ A3 (Ausschluss Eigenleistung) enthält unzulässigen Grund: '{ground}'. "
                f"Reformulieren Sie als zeitliche Rahmenbedingung mit Beleg."
            )
            break
    
    # CHECK 4: Miete-Ausschluss — auf verbotene Gründe prüfen
    miete_text = wu_data['inhalt']['miete_begruendung']
    if ground in miete_text.lower():
        errors.append(
            f"❌ A4 (Ausschluss Miete) enthält unzulässigen Grund: '{ground}'. "
        )
    
    # CHECK 5: Pflichtfelder — alles vorhanden?
    if not wu_data['inhalt'].get('bedarfsforderung'):
        errors.append("❌ Bedarfsforderung fehlt")
    if not wu_data['inhalt'].get('eigenleistung_begruendung'):
        errors.append("❌ Ausschluss Eigenleistung fehlt")
    if not wu_data['inhalt'].get('miete_begruendung'):
        warnings.append("⚠️ Ausschluss Miete fehlt (optional, wenn nicht relevant)")
    
    # CHECK 6: Anlage Marktrecherche — vorhanden?
    if len(wu_data['anlage']) < 1:
        errors.append("❌ Anlage Marktrecherche Nr. 1 (Kaufpreis) fehlt")
    
    return errors, warnings

errors, warnings = validate_wu_unterjahrig_extended(wu_data)

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

# SCHRITT 2: Dateiname generieren
outpath = build_filename(
    datum=wu_data['meta']['datum'],
    sachverhalt='[aus Feld 3 extrahiert, z.B. "Drucker"]',
    dienststelle=wu_data['meta']['dienststelle']
)
# Beispiel-Output: '20260423_WU_Drucker_BAIUDBw_Version_1.xlsm'

# SCHRITT 3: Excel-Template befüllen
print(f"📝 Exportiere zu: {outpath}")
fill_template(wu_data, outpath)

# SCHRITT 4: Erfolgsmeldung mit Checkliste
print(f"""
✅ WU erfolgreich exportiert!

Datei: {outpath}

Vor dem Versand bitte kurz prüfen:
  ☐ Metadaten (Dienststelle, Bearbeiter, Datum) korrekt?
  ☐ Bedarfsforderung eindeutig + ohne Produktnamen?
  ☐ Kaufpreis korrekt eingetragen?
  ☐ Alle Quellenangaben mit „Anlage Marktrecherche, Nr. X"?

Dann: Dokument speichern, ggf. PDF-Export durchführen, versenden.
""")
```

**Dateiname-Generierung mit Sanitizing (Punkt 7):**
```python
def build_filename_safe(datum, sachverhalt, dienststelle):
    """
    Generiert sicheren Dateinamen ohne Umlaute, Leerzeichen, Sonderzeichen.
    """
    # 1. Extrahiere Produkttyp aus Sachverhalt
    produkt = extract_first_noun(sachverhalt)  # z.B. „Drucker für die Büros" → „Drucker"
    
    # 2. Sanitize: Nur alphanumerisch + Unterstriche
    produkt_safe = re.sub(r'[^\w\-]', '', produkt).strip()  # → „Drucker"
    
    # 3. Sanitize: Dienststelle
    dienststelle_safe = re.sub(r'[^\w\-]', '', dienststelle).strip()  # z.B. „BAIUDBw"
    
    # 4. Zusammenbauen
    return f"{datum.strftime('%Y%m%d')}_WU_{produkt_safe}_{dienststelle_safe}_Version_1.xlsm"

# Beispiele:
build_filename_safe('2026-04-23', 'Drucker für die Büros', 'BAIUDBw')
→ '20260423_WU_Drucker_BAIUDBw_Version_1.xlsm' ✅

build_filename_safe('2026-04-23', 'Laptops (5 Stück)', 'KommBw München')
→ '20260423_WU_Laptops_KommBw_Version_1.xlsm' ✅
```

**Dateiname-Konvention (sicher):**
```
YYYYMMDD_WU_[SachverhaltSafe]_[DienststelleSafe]_Version_[Nr].xlsm

Beispiel: 20260423_WU_Drucker_BAIUDBw_Version_1.xlsm
```

---

## Ablauf-Diagramm: A1–A6 mit Fallback & Validierung

```
START (User startet WU-Erstellung)
    ↓
┌──────────────────────────────────────────────────────────┐
│ PHASE 1: Eingabe (Min 0–1)                               │
│ - Dienststelle: [User-Input]                             │
│ - Bearbeiter: [User-Input]                               │
│ - Was wird gekauft?: [User-Input]                        │
│ - Ungefährer Preis?: [User-Input]                        │
└──────────────────────────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────────────────┐
│ A1: BEDARFSFORDERUNG (Min 1–4)                           │
│ SKILL: 8 konkrete Dialog-Fragen (keine erfundenen Details)
│                                                           │
│ ┌─ User antwortet strukturiert (5–10 Min)                │
│ │  → Auto-generiert Bedarfsforderung                     │
│ │  → Inline-Validierung                                  │
│ │  → User bestätigt                                      │
│ │                                                        │
│ └─ User antwortet vage / unstrukturiert                  │
│    → FALLBACK: Standardannahmen mit Bestätigung          │
│    → User wählt: akzeptieren / detailliert durchgehen    │
│    → Dann wie oben                                       │
│                                                          │
│ ✅ A1 ist lösungsneutral, keine Produktnamen             │
└──────────────────────────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────────────────┐
│ A2: BISHERIGE BEDARFSDECKUNG (Min 5–6)                  │
│ SKILL: Intelligenter Default basierend auf Sachverhalt   │
│                                                          │
│ → User bestätigt Vorschlag ODER korrigiert               │
│ → Fallback: Ohne Input wird Vorschlag übernommen         │
└──────────────────────────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────────────────┐
│ A3: AUSSCHLUSS EIGENLEISTUNG (Min 6–7)                  │
│ SKILL: Structured Choices (KEINE Freitext)              │
│                                                          │
│ User wählt EINEN Grund:                                  │
│  [ ] Kein Gerät vorhanden                                │
│  [ ] Verbrauchsgut verbraucht                            │
│  [ ] Zeitliche Frist (mit Datum + Beleg)                │
│  [ ] Spezialisierte Kompetenz fehlt (mit Beleg)          │
│                                                          │
│ ✅ Guard Check: automatisch prüft auf verbotene Gründe    │
│    (Personal, Haushaltsmittel, Infrastruktur)            │
└──────────────────────────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────────────────┐
│ A4: AUSSCHLUSS MIETE/LEASING (Min 7–9)                  │
│ SKILL: WebRecherche + Semi-Auto mit User-Bestätigung    │
│                                                          │
│ ┌─ WebRecherche erfolgreich (2–3 Min)                    │
│ │  → Mietpreise recherchieren                            │
│ │  → User prüft Annahmen (Einsatztage/Jahr, Mietpreis)   │
│ │  → User bestätigt oder gibt Werte manuell ein          │
│ │  → Break-even berechnen                                │
│ │                                                        │
│ └─ WebRecherche fehlgeschlagen                           │
│    → Fallback: User gibt Mietpreis manuell ein ODER      │
│    → A4 wird übersprungen (kein Miete-Text ins Dokument) │
└──────────────────────────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────────────────┐
│ A5: BESTÄTIGUNG UNTERJÄHRIGKEIT (Min 9–10)              │
│ SKILL: Standard-Text (Auto)                              │
│ → User bestätigt                                         │
└──────────────────────────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────────────────┐
│ A6: EXPORT mit ERWEITERTE VALIDIERUNG (Min 10–12)        │
│ SKILL: Multiple Auto-Checks vor Export                   │
│                                                          │
│ Checks:                                                  │
│  ✓ Produktnamen in Bedarfsforderung? (❌ Fehler)         │
│  ✓ Preis realistisch? (⚠️ Warnung bei extremen Werten)   │
│  ✓ Verbotene Gründe in A3/A4? (❌ Fehler)                │
│  ✓ Alle Pflichtfelder ausgefüllt? (❌ Fehler)            │
│  ✓ Anlage Marktrecherche vorhanden? (❌ Fehler)          │
│                                                          │
│ → Dateiname: Sanitized (keine Umlaute/Leerzeichen)      │
│ → Excel-Template befüllen                               │
│ → Erfolgsmeldung + Checkliste vor Versand                │
└──────────────────────────────────────────────────────────┘
    ↓
END: WU-Dokument exportiert, validiert, versandbereit (Format: .xlsm)

═══════════════════════════════════════════════════════════════════
Prozess: Strukturierter Dialog mit Fallback & Validierung
Effizienz: Minimale User-Eingaben, maximale Automation
Sicherheit: 6 Validierungs-Punkte vor Export
```
