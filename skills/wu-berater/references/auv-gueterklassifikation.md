# AUV: Güterklassifizierung nach A2-1000/0-0-13

**Geltungsbereich:** Dialogpfad AUV darf NUR befüllt werden für:
- ✅ **Einmalig** (keine Wiederholung, nicht regelmäßig)
- ✅ **Unterjährig** (innerhalb eines Kalenderjahres)
- ✅ **Kauf von Gütern** (nicht Miete, Leasing, Dienstleistung)

---

## Klassifizierung: Versorgungsgüter (A2-1000/0-0-13)

```
Versorgungsgüter
│
├─ VERBRAUCHSGUT (Gut des Umlaufvermögens)
│  ├─ MENGENVERBRAUCHSGUT
│  │  ├─ Munition
│  │  ├─ Betriebsstoff (Benzin, Diesel, Öl)
│  │  ├─ Wasser
│  │  ├─ Verpflegungs- und Futtermittel
│  │  ├─ Bekleidung**
│  │  ├─ Bau- und Deckungsmaterial
│  │  ├─ Spermaterial
│  │  ├─ Feste Brennstoffe
│  │  └─ Dekontaminationsmittel
│  │
│  └─ EINZELVERBRAUCHSGUT
│     ├─ Teile von Sätzen
│     ├─ Austauschteile* (*AT mit Rückführungscode 4 gekennzeichnet)
│     ├─ Ersatzteile (z.B. für Geräte)
│     ├─ EVG San
│     ├─ Zubehör und Vorratsteile
│     ├─ Technische Gase
│     ├─ Farben und Lacke
│     └─ Werk- und Verbrauchsmaterial
│
└─ NICHTVERBRAUCHSGUT (Gut des Anlagevermögens)
   ├─ Geräte (Drucker, Scanner, Monitor, etc.)
   ├─ Sätze (zusammenhängende Ausrüstung)
   ├─ Großgeräte (große Anlagen/Maschinen)
   ├─ Endgeräte (z.B. Laptops, Tablets)
   ├─ Einbaugeräte (in Liegenschaft/Fahrzeug)
   ├─ Hauptgeräte (Hauptkomponenten)
   └─ Sonstige Geräte (nicht näher klassifizierbar)
```

**Hinweis:** Von der grundsätzlichen Einteilung kann aus Gründen der effektiven Bewirtschaftung in Einzelfällen abgewichen werden.

---

## 🔴 KRITISCH: Einmalig vs. Regelmäßig

### Wann ist "EINMALIG" für AUV geeignet?

**✅ EINMALIG — AUV passt:**
```
- Kauf von 100 Schrauben (jetzt, einmal)
- Kauf von 50 Litern Betriebsstoff (Jahresbedarf auf einmal)
- Beschaffung von 10 Ersatzteilen für ein Gerät
- Einmalige Betankung eines Fahrzeugs (als finanzwirksame Maßnahme)
- Kauf von Möbeln für neuen Büroraum (einmalig)
- Beschaffung von Baumaterial für ein Projekt (abgeschlossen Ende 2026)
```

**❌ REGELMÄSSIG — AUV passt NICHT:**
```
- Monatliche Bestellung von Schrauben (regelmäßige Versorgung)
- Quarterly-Liefervertrag für Betriebsstoff (wiederholte Lieferung)
- Abonnement-ähnliche Wartung von Geräten
- Laufende Betankung von Fahrzeugen (wiederkehrend)
- Jährlicher Einkauf von Baumaterial (wiederkehrend)
- Laufende Ersatzteilversorgung (ständig erforderlich)
```

---

## Entscheidungsbaum: Passt AUV?

```
START: "Was wird gekauft?"
   │
   ├─ FRAGE 1: Ist es ein KAUF (nicht Miete, Leasing, Dienstleistung)?
   │  ├─ NEIN → ❌ AUV passt nicht (→ Dialogpfad B/C)
   │  └─ JA → gehe zu FRAGE 2
   │
   ├─ FRAGE 2: Ist es EINMALIG (nicht regelmäßig, keine Wiederholung)?
   │  ├─ NEIN → ❌ AUV passt nicht (→ Dialogpfad B/C für regelmäßige Verträge)
   │  └─ JA → gehe zu FRAGE 3
   │
   ├─ FRAGE 3: Liegt die Maßnahme INNERHALB eines Kalenderjahres?
   │  ├─ NEIN → ❌ AUV passt nicht (→ Dialogpfad B überjährig)
   │  └─ JA → gehe zu FRAGE 4
   │
   ├─ FRAGE 4: Ist es ein Kauf von GÜTERN (Nichtverbrauchsgut oder Verbrauchsgut)?
   │  ├─ JA → gehe zu FRAGE 5
   │  └─ NEIN (z.B. Infrastruktur-Maßnahme) → ❌ AUV passt nicht (→ Dialogpfad B/C)
   │
   └─ FRAGE 5: Klassifizierung nach A2-1000
      │
      ├─ NICHTVERBRAUCHSGUT (Anlagevermögen)
      │  └─ ✅ AUV PASST (Geräte, Sätze, Endgeräte, etc.)
      │
      └─ VERBRAUCHSGUT (Umlaufvermögen)
         ├─ Mengenverbrauchsgut (regelmäßig benötigt, aber jetzt einmalig)
         │  └─ ✅ AUV PASST (z.B. einmalige 50L Betriebsstoff)
         └─ Einzelverbrauchsgut (Ersatzteile, Zubehör)
            └─ ✅ AUV PASST (z.B. Austauschteile für Gerät)

═══════════════════════════════════════════════════════════
ERGEBNIS: ✅ AUV PASST
═══════════════════════════════════════════════════════════
```

---

## Konkrete Beispiele

### ✅ AUV PASST

| Gut | Kategorie | Grund |
|-----|-----------|-------|
| Drucker kaufen | Nichtverbrauchsgut/Gerät | Einmalig, unterjährig, Anlagevermögen |
| 5 Bürostühle kaufen | Nichtverbrauchsgut/Sätze | Einmalig, unterjährig, Anlagevermögen |
| Transporter kaufen | Nichtverbrauchsgut/Gerät | Einmalig, unterjährig, Anlagevermögen |
| 50L Betriebsstoff kaufen | Verbrauchsgut/Mengenverbrauch | Einmaliger Kauf (nicht regelmäßig), Umlaufvermögen |
| 100 Schrauben kaufen | Verbrauchsgut/Einzelverbrauch | Einmaliger Kauf, Umlaufvermögen |
| Ersatzteile für Gerät | Verbrauchsgut/Einzelverbrauch | Einmaliger Kauf, Umlaufvermögen |
| Farben für Projekt | Verbrauchsgut/Einzelverbrauch | Einmaliger Kauf (Projekt endet 2026), Umlaufvermögen |

### ❌ AUV PASST NICHT

| Gut | Kategorie | Grund |
|-----|-----------|-------|
| Monatliche Schrauben-Lieferung | Verbrauchsgut | **Regelmäßig**, nicht einmalig |
| Jahresvertrag Betriebsstoff | Verbrauchsgut | **Wiederholte Lieferung**, nicht einmalig |
| IT-Support-Vertrag | Dienstleistung | **Nicht Kauf**, außerdem regelmäßig |
| Leasingvertrag Fahrzeug | Mietvertrag | **Nicht Kauf**, Leasing |
| Reinigungsvertrag | Dienstleistung | **Nicht Kauf** |
| Gebäuderenovierung | Infrastruktur | Keine **Güter**, eher Dienstleistung/Infrastruktur |

---

## Integration in Dialogpfad AUV

**Im Startdialog (nach WU-Typ-Bestimmung):**

Wenn Nutzer "Unterjährig, Kauf" sagt → prüfen:

```python
def passt_auv(sachverhalt, guttyp, betrachtungszeitraum_jahre, ist_einmalig):
    """
    Prüft ob Dialogpfad AUV geeignet ist.
    """
    
    # CHECK 1: Einmalig?
    if not ist_einmalig:
        return False, "❌ AUV passt nicht: Maßnahme ist regelmäßig/wiederholend. → Dialogpfad B/C"
    
    # CHECK 2: Unterjährig?
    if betrachtungszeitraum_jahre >= 2:
        return False, "❌ AUV passt nicht: Betrachtungszeitraum ≥2 Jahre. → Dialogpfad B"
    
    # CHECK 3: Kauf (nicht Miete/Leasing/DL)?
    if guttyp in ['dienstleistung', 'miete', 'leasing']:
        return False, "❌ AUV passt nicht: Keine Güter-Beschaffung. → Dialogpfad B/C"
    
    # CHECK 4: Gut des Anlage- oder Umlaufvermögens?
    # (Nach A2-1000 klassifiziert)
    if guttyp in ['nichtverbrauchsgut', 'verbrauchsgut_einmalig']:
        return True, "✅ AUV passt: Einmalige Güterbeschaffung, unterjährig"
    
    return False, "❌ AUV passt nicht: Nicht klassifizierbar"
```

---

## Grenzfälle & Klärungen

### "Betriebsstoff — einmalig oder regelmäßig?"

```
SZENARIO 1: "Betankung Fahrzeug für diesen Einsatz"
→ einmalig, unterjährig → ✅ AUV PASST

SZENARIO 2: "Jahresversorgung Betriebsstoff auf einmal kaufen"
→ einmalig (gekauft einmal im Jahr), unterjährig → ✅ AUV PASST

SZENARIO 3: "Monatliche Betankung (wiederkehrend)"
→ regelmäßig → ❌ AUV PASST NICHT (→ Dialogpfad B mit Verträgen)
```

### "Ersatzteile — wann passt AUV?"

```
SZENARIO 1: "10 Ersatzteile für ein Gerät kaufen (jetzt, einmalig)"
→ ✅ AUV PASST

SZENARIO 2: "Laufende Ersatzteilversorgung für mehrere Geräte"
→ regelmäßig → ❌ AUV PASST NICHT
```

---

## Checklist: Muss ich Dialogpfad AUV nutzen?

Beantworte diese Fragen mit JA:

- [ ] Ist es ein KAUF (nicht Miete, Leasing, Dienstleistung)?
- [ ] Ist die Maßnahme EINMALIG (keine Wiederholung)?
- [ ] Liegt die Maßnahme INNERHALB eines Kalenderjahres?
- [ ] Nach A2-1000: Nichtverbrauchsgut ODER Verbrauchsgut (einmalig)?

**Alle JA?** → ✅ Dialogpfad AUV  
**Mindestens ein NEIN?** → ❌ Dialogpfad B oder C

---

**Quelle:** A2-1000/0-0-13 (Versorgungsgüter-Klassifizierung)  
**Gültigkeit:** Nur für Dialogpfad AUV (einmalig, unterjährig)
