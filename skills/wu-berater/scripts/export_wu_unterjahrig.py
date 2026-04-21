"""
WU-Berater: Export-Skript für unterjährige Wirtschaftlichkeitsuntersuchungen
Füllt das Excel-Template 'Template Dokumentation WU unterjährig.xlsm' mit WU-Inhalten.

Verwendung:
    from export_wu_unterjahrig import fill_template
    fill_template(wu_data, output_path)
"""

import openpyxl
from openpyxl.styles import Font, Alignment
from datetime import date
import os
from wu_file_handler import cleanup_lock_files

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Template Dokumentation WU unterjährig.xlsm')
TEMPLATE_PATH = os.path.normpath(TEMPLATE_PATH)

OUTPUT_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Erstellte WU', 'Unterjährig'))


def fill_template(wu_data: dict, output_path: str):
    """
    Befüllt das unterjährige WU-Template mit den übergebenen Daten.

    :param wu_data: Dictionary mit WU-Inhalten (Struktur siehe WU_DATA_SCHEMA)
    :param output_path: Pfad der Ausgabedatei (.xlsm)
    """
    wb = openpyxl.load_workbook(TEMPLATE_PATH, keep_vba=True)
    ws = wb['WU Vermerk']
    meta = wu_data.get('meta', {})
    inhalt = wu_data.get('inhalt', {})

    # Kopfdaten
    ws['B6'] = meta.get('dienststelle', '')
    ws['F6'] = meta.get('bearbeiter', '')
    ws['B7'] = _parse_date(meta.get('datum', ''))
    ws['D7'] = _parse_date(meta.get('beginn_massnahme', meta.get('datum', '')))
    ws['F4'] = f"{meta.get('schutz', 'offen')}\nVersion: {meta.get('datum', '')}"

    # Bedarfsforderung
    ws['B8'] = inhalt.get('bedarfsforderung', '')

    # Häkchen setzen
    checkmark_font = Font(size=11, bold=True, color='1F3864')
    center_align = Alignment(horizontal='center', vertical='center')

    haken = inhalt.get('haken', {})
    haken_map = {
        'kauf_benoetigt':     'A10',
        'bedarf_neu':         'A11',
        'sonstiges_bedarf':   'A12',
        'eigenleistung':      'A14',
        'eigenleistung_sonst':'A15',
        'miete_verbrauch':    'A17',
        'miete_kein_anbieter':'A18',
        'miete_sonstiges':    'A19',
        'keine_folgeausgaben':'A21',
    }
    for key, cell_addr in haken_map.items():
        if haken.get(key, False):
            ws[cell_addr] = '✓'
            ws[cell_addr].font = checkmark_font
            ws[cell_addr].alignment = center_align

    # Freitextfelder
    if inhalt.get('eigenleistung_begruendung'):
        ws['B15'] = inhalt['eigenleistung_begruendung']
    if inhalt.get('miete_begruendung'):
        ws['B19'] = inhalt['miete_begruendung']

    # Voraussichtliche Ausgaben
    if inhalt.get('ausgaben'):
        ws['F22'] = inhalt['ausgaben']

    # Anlage-Blatt
    anlage = wu_data.get('anlage', [])
    if anlage:
        _create_anlage_sheet(wb, anlage, meta.get('datum', ''))

    # Räume Lock-Dateien auf (Excel-Dateien)
    output_dir = os.path.dirname(output_path)
    cleanup_lock_files(output_dir)

    wb.save(output_path)
    print(f'[OK] WU-Dokument gespeichert: {os.path.basename(output_path)}')
    return output_path


def _parse_date(datum_str: str):
    """Konvertiert 'TT.MM.JJJJ' in date-Objekt."""
    try:
        teile = datum_str.split('.')
        return date(int(teile[2]), int(teile[1]), int(teile[0]))
    except Exception:
        return datum_str


def _create_anlage_sheet(wb, anlage: list, datum: str):
    from openpyxl.styles import PatternFill, Border, Side
    from openpyxl.styles import Font as XFont, Alignment as XAlign

    if 'Anlage - Marktrecherche' in wb.sheetnames:
        del wb['Anlage - Marktrecherche']

    ws = wb.create_sheet('Anlage - Marktrecherche')
    header_fill = PatternFill(start_color='1F3864', end_color='1F3864', fill_type='solid')
    thin = Side(style='thin')
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    ws['A1'] = f'Anlage: Marktrecherche (Abrufdatum: {datum})'
    ws['A1'].font = XFont(bold=True, size=12, color='1F3864')
    ws.merge_cells('A1:E1')
    ws.row_dimensions[1].height = 22

    headers = ['Nr.', 'Produkt / Beschreibung', 'Preis (brutto)', 'Quelle (URL)', 'Bemerkung']
    for col, h in enumerate(headers, 1):
        c = ws.cell(row=3, column=col, value=h)
        c.font = XFont(bold=True, color='FFFFFF', size=10)
        c.fill = header_fill
        c.alignment = XAlign(horizontal='center', vertical='center', wrap_text=True)
        c.border = border
    ws.row_dimensions[3].height = 25

    for i, eintrag in enumerate(anlage, 4):
        row_vals = [
            eintrag.get('nr', str(i - 3)),
            eintrag.get('produkt', ''),
            eintrag.get('preis', ''),
            eintrag.get('url', ''),
            eintrag.get('bemerkung', ''),
        ]
        for col, val in enumerate(row_vals, 1):
            c = ws.cell(row=i, column=col, value=val)
            c.alignment = XAlign(wrap_text=True, vertical='top')
            c.border = border
        ws.row_dimensions[i].height = 55

    ws.column_dimensions['A'].width = 5
    ws.column_dimensions['B'].width = 38
    ws.column_dimensions['C'].width = 16
    ws.column_dimensions['D'].width = 55
    ws.column_dimensions['E'].width = 30

    note_row = len(anlage) + 5
    ws.merge_cells(f'A{note_row}:E{note_row}')
    ws[f'A{note_row}'] = 'Hinweis: Screenshots der oben genannten Webseiten als Anlage beifügen (Einfügen → Objekt/Bild).'
    ws[f'A{note_row}'].font = XFont(italic=True, size=9, color='595959')
    ws[f'A{note_row}'].alignment = XAlign(wrap_text=True)


def erstelle_abschlusscheckliste_unterjahrig(wu_data: dict, output_path: str) -> str:
    """
    Gibt die Abschlusscheckliste für eine unterjährige WU zurück.
    """
    meta   = wu_data.get('meta', {})
    inhalt = wu_data.get('inhalt', {})
    anlage = wu_data.get('anlage', [])

    haken = inhalt.get('haken', {})
    gesetzte_haken = [k for k, v in haken.items() if v]

    auto_befuellt = [
        f'Dokumentkopf (Dienststelle: {meta.get("dienststelle", "")}, '
        f'Bearbeiter: {meta.get("bearbeiter", "")}, Schutz: offen)',
        'Bedarfsforderung (qualitativ + quantitativ)',
        f'Bisherige Bedarfsdeckung (Haken: {", ".join(gesetzte_haken)})',
        'Ausschluss Eigenleistung (Begründung)',
        'Ausschluss Miete/Leasing (inkl. Preisvergleich)',
        'Bestätigung Unterjährigkeit (keine Folgeausgaben)',
        f'Voraussichtliche Ausgaben: {inhalt.get("ausgaben", "–")} €',
        f'Anlage Marktrecherche: {len(anlage)} Quellen (separates Blatt)',
    ]

    manuell_erforderlich = [
        'Checkboxen in der Excel-Datei manuell setzen (Klick auf die Kontrollkästchen)',
        'Screenshots der Marktrecherche-Webseiten in Anlage einfügen',
        'Bearbeiter/-in prüfen (Zelle F6)',
    ]

    checkliste = (
        f'\n{"="*55}\n'
        f'ABSCHLUSS-CHECKLISTE (unterjährige WU)\n'
        f'Datei: {output_path}\n'
        f'{"="*55}\n\n'
        f'Automatisch befüllt:\n'
    )
    for item in auto_befuellt:
        checkliste += f'  [x] {item}\n'
    checkliste += '\nNoch manuell zu ergänzen:\n'
    for item in manuell_erforderlich:
        checkliste += f'  [ ] {item}\n'
    checkliste += f'\n{"="*55}\n'
    return checkliste


def build_filename(datum: str, sachverhalt: str, dienststelle: str, version: int = 1) -> str:
    """Vollständiger Ausgabepfad: <OUTPUT_DIR>/JJJJMMTT_WU_[Sachverhalt]_[Dienststelle]_Version_N.xlsm"""
    teile = datum.split('.')
    jjmmtt = teile[2] + teile[1] + teile[0] if len(teile) == 3 else datum.replace('.', '')
    s = sachverhalt.replace(' ', '_').replace('/', '_')
    d = dienststelle.replace(' ', '_').replace('/', '_')
    filename = f"{jjmmtt}_WU_{s}_{d}_Version_{version}.xlsm"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    return os.path.join(OUTPUT_DIR, filename)


WU_DATA_SCHEMA = {
    "meta": {
        "dienststelle":      "BAIUDBw ...",
        "bearbeiter":        "Vorname Nachname",
        "datum":             "TT.MM.JJJJ",
        "beginn_massnahme":  "TT.MM.JJJJ",
        "schutz":            "offen",
        "version":           "1",
    },
    "inhalt": {
        "bedarfsforderung":            "Funktionale, lösungsneutrale Bedarfsbeschreibung ...",
        "haken": {
            "kauf_benoetigt":          True,
            "bedarf_neu":              False,
            "sonstiges_bedarf":        False,
            "eigenleistung":           False,
            "eigenleistung_sonst":     True,
            "miete_verbrauch":         False,
            "miete_kein_anbieter":     False,
            "miete_sonstiges":         True,
            "keine_folgeausgaben":     True,
        },
        "eigenleistung_begruendung":   "kein geeignetes Gerät im Eigenbestand ...",
        "miete_begruendung":           "wirtschaftlich nicht vorteilhaft ...",
        "ausgaben":                    205.00,
    },
    "anlage": [
        {"nr": "1", "produkt": "...", "preis": "...", "url": "https://...", "bemerkung": "..."},
    ],
}
