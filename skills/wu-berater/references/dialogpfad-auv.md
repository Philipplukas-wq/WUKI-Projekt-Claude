# Dialogpfad AUV: Kompakte Unterjährige WU (Vermerk-Template)

**Zweck:** Schnelle Befüllung des Templates "Dokumentation WU unterjährig Vermerk.xlsm" für **einmalige, unterjährige Käufe von Gütern** (Anlagevermögen oder Umlaufvermögen nach A2-1000).

**Geltungsbereich:**
- ✅ **Einmalig** (keine Wiederholung, nicht regelmäßig)
- ✅ **Unterjährig** (innerhalb eines Kalenderjahres)
- ✅ **Kauf von Gütern** (nicht Miete, Leasing, Dienstleistung)
- ✅ **Nach A2-1000/0-0-13** klassifiziert als Anlagevermögen oder Umlaufvermögen

**Falls nicht passend:** Siehe `auv-gueterklassifikation.md` (Entscheidungsbaum) oder verwende Dialogpfad A (detailliert), B (überjährig), C (andere).

---

## Phase 0: Gating-Logic (Startdialog im SKILL)

**Vor Dialogpfad AUV: 3 Screening-Fragen**

```
SKILL: „Bevor wir starten — kurze Screening-Fragen:

1. Ist diese Maßnahme EINMALIG (nicht regelmäßig/wiederholend)?
   [ ] Ja  [ ] Nein → (Nein = Dialogpfad B)

2. Liegt die Maßnahme INNERHALB eines Kalenderjahres?
   [ ] Ja  [ ] Nein → (Nein = Dialogpfad B)

3. Ist es ein KAUF von Gütern (keine Miete, Leasing, Dienstleistung)?
   [ ] Ja  [ ] Nein → (Nein = Dialogpfad C)

Alle 3 Fragen mit Ja? 
→ Perfekt! Starten wir mit Dialogpfad AUV.
   (Die Klassifizierung Anlagevermögen/Umlaufvermögen bestimme ich nach Ihrer Bedarfsbeschreibung.)"
```

---

## Phase 1: Metadaten (5 Eingabe-Felder)

**Erfassung der Basis-Informationen:**

| Feld | Beispiel | Validierung |
|------|----------|-------------|
| **Dienststelle** | BAIUDBw, KommBw München | 2–30 Zeichen, alphanumerisch + Leerzeichen |
| **Bearbeiter** | Schmid, Sandra (E9b) | 2–50 Zeichen |
| **Maßnahmenbeginn** | 15.05.2026 | TT.MM.JJJJ, dieses/nächstes Kalenderjahr |
| **Kaufbeschreibung** | 100 Schrauben M8x20 oder Bohrmaschine | 5–100 Zeichen, konkret |
| **Geschätzter Kaufpreis** | 250,00 oder 2500 | Beliebig (EUR, Dezimal oder Komma akzeptabel) |

**Dialog:**
```
SKILL: „Geben Sie bitte die Basis-Informationen ein:

1. Dienststelle: [User: BAIUDBw]
2. Bearbeiter: [User: Philipp Lukas]
3. Maßnahmenbeginn (TT.MM.JJJJ): [User: 23.04.2026]
4. Was wird gekauft? (kurz & konkret): [User: Bohrmaschine Akku 60Nm]
5. Geschätzter Kaufpreis (EUR): [User: 189.50]

✅ Eingaben validiert! Weiter zu Phase 2."
```

---

## Phase 2: Bedarfsforderung (Kurz & Funktional)

**Ziel:** Kompakte, lösungsneutrale Beschreibung. Ich klassifiziere danach selbst.

**Dialog:**
```
SKILL: „Geben Sie eine KURZE Bedarfsbeschreibung ein.
        Nur Funktionen nennen, KEINE Produktnamen!

Beispiele ✅:
  - ‚Elektrowerkzeug zum Bohren mit Schnellspannfutter'
  - ‚Befestigungsmittel zur Verschraubung M8x20'
  - ‚Betriebsstoff Diesel für Fahrzeuge, 50L'

Beispiele ❌:
  - ‚Bohrmaschine von Scheppach' (Produktname)
  - ‚Shell Diesel Super' (Marke)

Ihre Bedarfsbeschreibung: [User tippt]"
```

**Validierung:**
- ✅ Lösungsneutral (keine Produktnamen, keine Marken)
- ✅ Funktional beschrieben (Anforderungen, nicht Lösung)
- ❌ Verboten: HP, Kyocera, Shell, Würth, etc.

**Nach Phase 2 → AUTO-Klassifizierung (ich analysiere intern):**
```python
# Basierend auf Phase 2 Bedarfsforderung
if 'Bohren' in bedarfsforderung or 'Werkzeug' in bedarfsforderung:
    vermögenstyp = 'Anlagevermögen'  # Geräte = Nichtverbrauchsgüter
elif 'Schrauben' in bedarfsforderung or 'Befestigungsmittel' in bedarfsforderung:
    vermögenstyp = 'Umlaufvermögen'  # Verbrauchsgüter
elif 'Betriebsstoff' in bedarfsforderung or 'Diesel' in bedarfsforderung:
    vermögenstyp = 'Umlaufvermögen'  # Verbrauchsgüter
# Fallback: User bestätigt
```

---

## Phase 3: Bisherige Bedarfsdeckung (A10/A11/A12)

**Frage:** Wie wurde der Bedarf bisher erfüllt?

```
SKILL: „Wie wurde der Bedarf bisher gedeckt?

[ ] ☐ A10: Der Bedarf wurde bisher durch Kauf / Eigenbestände erfüllt
    → Checkbox A10 wird markiert

[ ] ☐ A11: Der Bedarf ist neu entstanden und wurde bisher nicht erfüllt
    → Checkbox A11 wird markiert

[ ] ☐ A12: Sonstiges / Andere Situation
    → Checkbox A12 wird markiert
    → [Freitextfeld, max. 100 Zeichen]"
```

**Mapping zu Template:**
- A10 = Bisherige Bedarfsdeckung: Kauf
- A11 = Bisherige Bedarfsdeckung: Neu
- A12 = Bisherige Bedarfsdeckung: Sonstiges (mit User-Text)

---

## Phase 4: Eigenleistungs-Ausschluss (A14/A15)

**BUNDESWEHR-REGEL:** Eigenleistung wird IMMER ausgeschlossen (die Bundeswehr produziert keine Waren).

**Frage:** Welcher Grund für den Ausschluss passt am besten?

```
SKILL: „Warum kann der Bedarf nicht durch Eigenleistung gedeckt werden?

[ ] ☐ A14: Der Bedarf umfasst ein Verbrauchsgut, welches innerhalb 
           der Bundeswehr nicht vorhanden ist
    → Checkbox A14 wird markiert
    → (Vorgefertigter Text)

[ ] ☐ A15: Sonstiges / Ein anderer Grund
    → Checkbox A15 wird markiert
    → [Freitextfeld für Begründung, max. 100 Zeichen]
    YOU: ‚Werkzeug muss eigenständig verfügbar sein'"
```

**Mapping zu Template:**
- A14 = Eigenleistungs-Ausschluss: Vorgefertigter Grund
- A15 = Eigenleistungs-Ausschluss: User-definierter Grund (mit Begründung in F15)

**Validierung:**
- ✅ MINDESTENS eine Checkbox (A14 oder A15) wird IMMER markiert
- ❌ Keine Exception — Eigenleistung ist IMMER ausgeschlossen

---

## Phase 5: Miete/Leasing-Ausschluss (A17/A18/A19) — NUR für Anlagevermögen

**Kontext:** Diese Phase ist NUR relevant, wenn Klassifizierung = Anlagevermögen (Nichtverbrauchsgüter).  
Für Umlaufvermögen (Verbrauchsgüter) wird diese Phase übersprungen.

```
SKILL: „(Nur für Nichtverbrauchsgüter)

Kann der Bedarf durch Miete / Leasing / Dienstleistung gedeckt werden?

[ ] ☐ Nein, aus folgendem Grund:

    [ ] ☐ A17: Kein Anbieter für Miete / Leasing verfügbar
        → Checkbox A17 wird markiert
    
    [ ] ☐ A18: Miete ist nicht wirtschaftlich
        → Checkbox A18 wird markiert
    
    [ ] ☐ A19: Sonstiges / Ein anderer Grund
        → Checkbox A19 wird markiert
        → [Freitextfeld für Begründung, max. 100 Zeichen]

[ ] Ja, Miete ist eine Option → Wechsel zu Dialogpfad D (detaillierte Wirtschaftlichkeitsprüfung)
[ ] Nicht relevant / Keine Angabe → Zu Phase 6"
```

**Mapping zu Template:**
- A17 = Miete-Ausschluss: Grund 1 (Kein Anbieter)
- A18 = Miete-Ausschluss: Grund 2 (Nicht wirtschaftlich)
- A19 = Miete-Ausschluss: Grund 3 (Sonstiges, mit Begründung in F19)

**Validierung:**
- ✅ MINDESTENS eine Checkbox (A17, A18 oder A19) wird markiert
- ❌ Freitext in A19 darf nicht leer sein, wenn A19 markiert

---

## Phase 6: Kaufpreis (Finaler Check)

```
SKILL: „Bestätigen Sie den Kaufpreis:

Ihr Preis aus Phase 1: 189,50 EUR

[ ] ☐ Preis ist korrekt → Zu Phase 7 (Export)
[ ] ☐ Preis anpassen: [Neuer Preis eingeben]
[ ] ☐ Ich recherchiere den realistischen Marktpreis (WebRecherche)
        → Zu Phase 6b"
```

### Phase 6b: WebRecherche Kaufpreis (Optional)

```
SKILL: „Recherchiere Marktpreise für: Bohrmaschine Akku 60Nm

📊 MARKTPREIS-RECHERCHE:

Spannbreite: 150,00 – 250,00 EUR
Durchschnitt: 189,50 EUR
Empfehlung: 189,50 EUR

Passt dieser Preis oder ändern Sie ihn?

[ ] ☐ 189,50 EUR bestätigen → Zu Phase 7
[ ] ☐ Anderen Preis eingeben: [Eingabe]"
```

---

## Phase 7: Export (VOLLSTÄNDIG AUTO)

```python
from export_wu_unterjahrig import fill_template, build_filename

# Datenstruktur für Export (basierend auf alle Phasen)
wu_data = {
    'meta': {
        'dienststelle':     'BAIUDBw',                    # Phase 1
        'bearbeiter':       'Philipp Lukas',              # Phase 1
        'datum':            '2026-04-23',                 # AUTO: heute
        'beginn_massnahme': '2026-04-23',                 # Phase 1
        'schutz':           'offen',                      # FEST
        'version':          '1',                          # FEST
    },
    'inhalt': {
        'vermögenstyp':     'Anlagevermögen',             # AUTO nach Phase 2
        'bedarfsforderung': '[Phase 2 Text]',             # Kurze Beschreibung
        'haken': {
            'kauf_benoetigt':         True,               # IMMER True in AUV
            'eigenleistung_grund1':   True,               # A14 (Phase 4)
            'eigenleistung_grund2':   False,              # A15 (Phase 4, optional)
            'miete_grund1':           False,              # A17 (Phase 5, falls Anlagevermögen)
            'miete_grund2':           False,              # A18 (Phase 5, falls Anlagevermögen)
            'miete_grund3':           True,               # A19 (Phase 5, falls Anlagevermögen)
            'keine_folgeausgaben':    True,               # IMMER True in AUV
        },
        'eigenleistung_begruendung': '[Phase 4 Text]',   # Phase 4, falls A15 markiert
        'miete_begruendung':         '[Phase 5 Text]',   # Phase 5, falls A19 markiert
        'ausgaben':                  189.50,             # Phase 6
    },
    'anlage': [
        {
            'quelle': '[Phase 6b Quelle, falls WebRecherche]',
            'datum': '2026-04-23',
            'ergebnis': '189,50 EUR',
            'bemerkung': 'Kaufpreis (Marktrecherche)',
            'link': '[URL falls WebRecherche]'
        },
    ],
}

# Export
outpath = build_filename(wu_data['meta']['datum'], 'Bohrmaschine', 'BAIUDBw', version=1)
fill_template(wu_data, outpath)
print(f"✅ AUV-Dokument exportiert: {outpath}")
```

**Nach Export:**
- Excel-Datei wird generiert: `20260423_WU_Bohrmaschine_BAIUDBw_Version_1.xlsm`
- Template ist befüllt mit alle Metadaten, Bedarfsforderung, Checkboxen, Kaufpreis
- Anlagen-Blatt enthält Quellenangaben (falls WebRecherche durchgeführt)

---

## Zusammenfassung: Workflow Dialogpfad AUV

| Phase | Input | Template-Felder |
|-------|-------|-----------------|
| **Phase 0** | 3 Screening-Fragen | (keine) |
| **Phase 1** | 5 Metadaten-Felder | B6, F6, B7, D7 |
| **Phase 2** | Bedarfsforderung (kurz, funktional) | B8 |
| **AUTO nach Phase 2** | (Auto-Klassifizierung) | A5 oder D5 |
| **Phase 3** | Bisherige Bedarfsdeckung (A10/A11/A12) | A10, A11, A12 |
| **Phase 4** | Eigenleistungs-Ausschluss-Grund | A14, A15, F15 |
| **Phase 5** | Miete/Leasing-Ausschluss-Grund (nur Anlagevermögen) | A17, A18, A19, F19 |
| **Phase 6** | Kaufpreis (mit opt. WebRecherche) | F22 |
| **Phase 7** | AUTO (Export) | Excel-Datei `.xlsm` |

**Zeitaufwand:** 3–5 Minuten pro Maßnahme (ohne WebRecherche)  
**Ergebnis:** BHO-konformes WU-Dokument im Vermerk-Format

---

## Checkliste: Ist AUV passend?

Beantworte folgende Fragen mit JA:

- [ ] Ist die Maßnahme **EINMALIG** (keine Wiederholung)?
- [ ] Liegt die Maßnahme **INNERHALB eines Kalenderjahres**?
- [ ] Ist es ein **KAUF von Gütern** (keine Miete, Leasing, Dienstleistung)?

**Alle JA?** → ✅ Dialogpfad AUV  
**Mindestens ein NEIN?** → ❌ Dialogpfad B (überjährig) oder C (andere)

---

## Verweise

- `auv-gueterklassifikation.md` — Entscheidungsbaum für A2-1000-Klassifizierung
- `export_wu_unterjahrig.py` — Export-Funktion (fill_template, build_filename)
- `Dokumentation WU unterjährig Vermerk.xlsm` — Template-Datei
