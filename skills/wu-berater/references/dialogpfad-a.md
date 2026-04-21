# Dialogpfad A: Unterjährige WU

Für **einmalige Käufe ohne Folgeausgaben** (6 Schritte).

**Modi**: Geführter Dialog (Schritt für Schritt) oder Schnelldurchlauf (alle Schritte auf einmal).

---

## Schritte A1–A6

Follge diese Reihenfolge. **Satzmuster** sind in `satzmuster-ac.md` dokumentiert.

| Schritt | Inhalt | Satzmuster in satzmuster-ac.md | Validierung |
|---------|--------|------|------|
| A1 | Bedarfsforderung (funktional, lösungsneutral, qualitativ + quantitativ) | A1 | **Inline-Check** (`validate_step('bedarfsforderung', ...)`) — prüft auf Lösungsneutralität + Quantifizierung |
| A2 | Bisherige Bedarfsdeckung | A2 | — |
| A3 | Ausschluss Eigenleistung (**Pflichtprüfung**: kein Personal, Dienstposten, Haushaltsmittel, Infrastruktur als Grund!) | A3 | **Guard Check** (`validate_step('aussonderung', ...)`) — warnt vor unzulässigen Gründen |
| A4 | Ausschluss Miete/Leasing (automatische Webrecherche + Break-even Berechnung) | A4 | **Guard Check** (`validate_step('aussonderung', ...)`) — wie A3 |
| A5 | Bestätigung Unterjährigkeit (keine Folgeausgaben) | A5 | — |
| A6 | Kostenermittlung & Export | Python-Snippet | **Vor Export**: `quick_validate()` + `export_safe()` |

**Pflichtprüfung bei A3**: Fehlendes Personal, Dienstposten, Haushaltsmittel und Infrastruktur sind **keine zulässigen Ausschlussgründe**. Prüfe, ob eine zeitliche Rahmenbedingung zulässig formuliert werden kann — Nutzer auf Belegpflicht hinweisen.

---

## Export (5.2)

```python
import sys
sys.path.insert(0, 'P:/WUKI_Projekt/Claude/skills/wu-berater/scripts')
from export_wu_unterjahrig import fill_template, build_filename, erstelle_abschlusscheckliste_unterjahrig

wu_data = {
    'meta': {
        'dienststelle':     '[Dienststelle]',
        'bearbeiter':       '[Name]',
        'datum':            '[TT.MM.JJJJ]',
        'beginn_massnahme': '[TT.MM.JJJJ]',
        'schutz':           'offen',
        'version':          '1',
    },
    'inhalt': {
        'bedarfsforderung': '[Text aus A1]',
        'haken': {
            'kauf_benoetigt':      True,
            'eigenleistung_sonst': True,
            'miete_sonstiges':     True,
            'keine_folgeausgaben': True,
        },
        'eigenleistung_begruendung': '[Text aus A3]',
        'miete_begruendung':         '[Text aus A4 inkl. Preisvergleich]',
        'ausgaben':                  0,  # Kaufpreis als Zahl
    },
    'anlage': [
        {'nr': '1', 'produkt': '[Produkt]', 'preis': '[Preis]', 'url': '[URL]', 'bemerkung': 'Kaufpreis, [Datum]'},
        {'nr': '2', 'produkt': '[Mietangebot]', 'preis': '[Miete/Tag]', 'url': '[URL]', 'bemerkung': 'Mietpreisvergleich, [Datum]'},
    ],
}

outpath = build_filename(wu_data['meta']['datum'], '[Sachverhalt]', wu_data['meta']['dienststelle'])
fill_template(wu_data, outpath)
print(erstelle_abschlusscheckliste_unterjahrig(wu_data, outpath))
```
