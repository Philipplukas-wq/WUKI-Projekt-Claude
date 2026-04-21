# Style-Richtlinien für WU-Dokumente

Diese Richtlinien definieren die einheitliche Formatierung aller WU-Dokumente (Word-Template).

---

## Überschriften

### H1 (Kapitel wie "1 Funktionale Bedarfsforderung")
- **Schriftart:** BundesSans Office
- **Größe:** 13 pt
- **Gewichtung:** Fett
- **Ausrichtung:** Linksbündig
- **Zeilenabstand:** Standard

### H2 (Unterkapitel wie "1.1 Funktionale Bedarfsforderung")
- **Schriftart:** BundesSans Office
- **Größe:** 12 pt
- **Gewichtung:** Fett
- **Ausrichtung:** Linksbündig

### H3 (Unter-Unterkapitel wie "1.3.1 Rechtliche Rahmenbedingungen")
- **Schriftart:** BundesSans Office
- **Größe:** 12 pt
- **Gewichtung:** Fett
- **Ausrichtung:** Linksbündig

### H4 (Weitere Gliederungsebenen)
- **Schriftart:** BundesSans Office
- **Größe:** 12 pt
- **Gewichtung:** Fett
- **Ausrichtung:** Linksbündig

---

## Fließtext (Normal / Body)

- **Schriftart:** BundesSans Office
- **Größe:** 11 pt
- **Gewichtung:** Normal (nicht fett)
- **Ausrichtung:** Blocksatz
- **Zeilenabstand:** 1,25
- **Absatzabstände:** Standard

---

## Tabellen

### Rahmen und Linien
- **Farbe:** Schwarz
- **Breite:** Standard
- **Stil:** Durchgehend

### Zellen – Text (nicht Zahlen, nicht Header)
- **Schriftart:** BundesSans Office
- **Größe:** 11 pt
- **Gewichtung:** Normal
- **Ausrichtung:** Linksbündig
- **Vertikalausrichtung:** Oben

### Zellen – Zahlen
- **Schriftart:** BundesSans Office
- **Größe:** 11 pt
- **Gewichtung:** Normal
- **Ausrichtung:** Mittig
- **Vertikalausrichtung:** Oben

### Header-Zeile (erste Zeile der Tabelle)
- **Hintergrundfarbe:** Leichtes Grau (ca. 20–30% Grau)
- **Schriftart:** BundesSans Office
- **Größe:** 11 pt
- **Gewichtung:** Fett
- **Ausrichtung:** Mittig
- **Vertikalausrichtung:** Oben

---

## Tabellennamen/Beschriftungen

- **Position:** Unter der Tabelle
- **Schriftart:** BundesSans Office
- **Größe:** 9 pt
- **Gewichtung:** Normal
- **Formatierung:** Kursiv
- **Ausrichtung:** Linksbündig
- **Zeilenabstand:** Standard

### Format und Beispiele
```
Tabelle 1: Entscheidungsvorschlag – Übersicht der Optionen
Tabelle 2: Ausgangslage – Haushälterische Darstellung
Tabelle 3: Option 1 – Neukauf (Kostenberechnung 10 Jahre)
```

---

## Kopfzeile

- **Inhalt:** WU-Kurztitel (wird bei jeder WU-Erstellung individuell eingefügt)
- **Schriftart:** BundesSans Office
- **Größe:** 11 pt (Standard)
- **Gewichtung:** Normal
- **Ausrichtung:** Linksbündig oder Standard
- **Format:** `WU [Kurztitel]` (z.B. "WU Gabelstapler BwDLZ Mayen")

---

## Seitenränder (Standard)

- **Oben:** 2,54 cm
- **Unten:** 2,54 cm
- **Links:** 2,54 cm
- **Rechts:** 2,54 cm

---

## Zusammenfassung Schriftarten

| Element | Schriftart | Größe | Gewichtung | Ausrichtung |
|---------|-----------|-------|-----------|------------|
| H1 | BundesSans Office | 13 pt | Fett | Links |
| H2 | BundesSans Office | 12 pt | Fett | Links |
| H3 | BundesSans Office | 12 pt | Fett | Links |
| H4 | BundesSans Office | 12 pt | Fett | Links |
| Fließtext | BundesSans Office | 11 pt | Normal | Blocksatz |
| Tabellen (Text) | BundesSans Office | 11 pt | Normal | Links |
| Tabellen (Zahlen) | BundesSans Office | 11 pt | Normal | Mittig |
| Tabellen (Header) | BundesSans Office | 11 pt | **Fett** | **Mittig** |
| Tabellennamen | BundesSans Office | 9 pt | Normal (Kursiv) | Links |
| Kopfzeile | BundesSans Office | 11 pt | Normal | Links |

---

## Anwendung im Skill

Diese Richtlinien werden **automatisch angewendet** bei der WU-Erstellung:
- Der wu-berater Skill nutzt diese Formatierungen beim Export in das Word-Template
- Alle zukünftigen WU-Dokumente folgen dieser einheitlichen Formatierung
- Bei Änderungen an diesen Richtlinien muss die Export-Funktion (`export_wu_ueberjahrig.py`) entsprechend angepasst werden
