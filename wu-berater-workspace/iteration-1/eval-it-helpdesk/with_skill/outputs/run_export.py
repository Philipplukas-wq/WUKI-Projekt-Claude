"""
Export-Skript: WU IT-Helpdesk-Support BAIUDBw Bonn
Erzeugt: 20260415_WU_IT-Helpdesk-Support_BAIUDBw_Bonn_Version_1.xlsm

Ausführen mit:
    python run_export.py
"""

import sys
import os

sys.path.insert(0, 'P:/WUKI_Projekt/Claude/skills/wu-berater/scripts')
from export_wu_dienstleistung import (
    fill_template,
    build_filename,
    erstelle_abschlusscheckliste_dienstleistung,
)

OUTPUT_DIR = 'P:/WUKI_Projekt/Claude/wu-berater-workspace/iteration-1/eval-it-helpdesk/with_skill/outputs'

wu_data = {
    'meta': {
        'dienststelle':               'BAIUDBw Bonn',
        'massnahmenverantwortlicher': '',   # manuell eintragen (Zelle D5)
        'bearbeiter':                 'Sarah Müller',
        'datum':                      '15.04.2026',
        'beginn_massnahme':           '01.07.2026',
        'ende_massnahme':             '31.12.2026',
        'schutz':                     'offen',
        'version':                    '1',
    },

    'bedarf': {
        'bezeichnung': 'IT-Helpdesk-Support für PC-Arbeitsplätze BAIUDBw Bonn',
        'beschreibung_zielsetzung': (
            'Für ca. 50 PC-Arbeitsplätze der Dienststelle BAIUDBw Bonn ist im Zeitraum '
            '01.07.2026 bis 31.12.2026 eine qualifizierte IT-Betreuung und ein '
            'Anwender-Helpdesk sicherzustellen. Die Leistung umfasst die Entgegennahme, '
            'Klassifizierung und Lösung von IT-Störungen und Serviceanfragen der '
            'Nutzerinnen und Nutzer (1st- und 2nd-Level-Support), die Sicherstellung '
            'der Betriebsfähigkeit der Arbeitsplatz-IT, die Koordination von '
            'Eskalationen an übergeordnete IT-Instanzen sowie den Hardwaretausch im '
            'Schadensfall. Der Bedarf besteht werktäglich während der Dienstzeit '
            '(Mo–Fr, 07:00–17:00 Uhr). Mit der Maßnahme soll die Arbeitsfähigkeit '
            'von ca. 50 Beschäftigten der Dienststelle sichergestellt werden.'
        ),
    },

    'rahmenbedingungen': [
        # RB 1: Sicherheitsanforderungen (schränkt Anbieterkreis ein)
        (
            'Teile der betreuten IT-Systeme unterliegen den Anforderungen der '
            'Verschlusssachenanweisung VS-NfD. Externe Dienstleister müssen die '
            'erforderlichen Sicherheitsüberprüfungen für eingesetztes Personal '
            'nachweisen können. Diese Rahmenbedingung schränkt den Kreis geeigneter '
            'externer Anbieter ein.'
        ),
        # RB 2: Zeitliche Rahmenbedingung
        (
            'Die Maßnahme muss spätestens zum 01.07.2026 wirksam sein, da der '
            'bestehende Vertrag mit der Firma Bechtle am 30.06.2026 ausläuft. '
            'Optionen mit langen Vorlaufzeiten (z.B. Personalgewinnung und Einarbeitung '
            'für Eigenleistung) sind daher nicht realisierbar.'
        ),
    ],

    'ausgangslage': (
        'Die IT-Betreuung für ca. 50 PC-Arbeitsplätze der Dienststelle BAIUDBw Bonn '
        'wird seit ca. 2 Jahren durch die Firma Bechtle GmbH & Co. KG als externen '
        'Dienstleister erbracht. Eigenes IT-Personal für den Betrieb des Helpdesks '
        'ist nicht mehr vorhanden — entsprechende Dienstposten wurden im Rahmen der '
        'Auslagerung aufgegeben bzw. nicht mehr besetzt. Der bestehende Vertrag hat '
        'eine monatliche Vergütung von 4.200 € (brutto), was für den '
        'Betrachtungszeitraum von sechs Monaten (01.07.–31.12.2026) Gesamtausgaben '
        'von 25.200 € ergibt. Der Vertrag läuft am 30.06.2026 aus.'
    ),

    'optionen': {
        # Option 1: Eigenleistung — ausgesondert
        'opt1_ausgesondert': True,
        'opt1_begruendung': (
            'Option 1 (Eigenleistung) ist nicht realisierbar: Die Dienststelle '
            'BAIUDBw Bonn verfügt seit der Auslagerung vor ca. zwei Jahren über '
            'kein eigenes IT-Personal mehr, das für den Helpdesk-Betrieb qualifiziert '
            'wäre. Freie Dienstposten für IT-Fachkräfte stehen nicht zur Verfügung. '
            'Eine kurzfristige Personalgewinnung und Einarbeitung bis zum 01.07.2026 '
            'ist angesichts der zeitlichen Rahmenbedingung nicht möglich '
            '(Stellenbesetzungsverfahren im öffentlichen Dienst: typischerweise '
            '6–12 Monate).'
        ),

        # Option 2: Bundeswehrinterne Dienststelle — ausgesondert
        'opt2_ausgesondert': True,
        'opt2_begruendung': (
            'Option 2 (bundeswehrinterne Dienststelle) ist nicht bedarfsdeckend: '
            'Es ist keine bundeswehrinterne Dienststelle bekannt, die in der Lage '
            'wäre, den Helpdesk-Support für BAIUDBw Bonn im erforderlichen Umfang '
            'und ab dem 01.07.2026 zusätzlich zu übernehmen. Regionale IT-'
            'Unterstützungskapazitäten aus anderen Dienststellen stehen nicht zur '
            'Verfügung.'
        ),

        # Option 3: BWI GmbH — geeignet
        'opt3_ausgesondert': False,
        'opt3_begruendung': '',

        # Option 4: Externer Dienstleister — geeignet
        'opt4_ausgesondert': False,
        'opt4_begruendung': '',
    },

    'kosten': {
        # Option 3: BWI GmbH
        # 90 €/AP/Monat × 50 AP × 6 Monate = 27.000 €
        # (siehe Anlage Marktrecherche, Nr. 2)
        'opt3': {
            'tagegeld':          0,
            'personal_eur':      0,
            'material_eur':      0,
            'infrastruktur_eur': 0,
            'dl_extern_eur':     0,
            'dl_wartung_eur':    0,
            'dl_sonstiges_eur':  27000,   # IT-Helpdesk-Support BWI GmbH 6 Monate
        },

        # Option 4: Externer Dienstleister (Bechtle/Neuvergabe)
        # 4.200 €/Monat × 6 Monate = 25.200 €
        # (siehe Anlage Marktrecherche, Nr. 1 und Nr. 3)
        'opt4': {
            'tagegeld':          0,
            'personal_eur':      0,
            'material_eur':      0,
            'infrastruktur_eur': 0,
            'dl_extern_eur':     0,
            'dl_wartung_eur':    0,
            'dl_sonstiges_eur':  25200,   # IT-Helpdesk-Support extern 6 Monate
        },
    },

    'risiko': {
        'kein_risiko': False,
        # Risiko 1: Preisanpassung bei Neuvergabe (Option 4)
        # Eintrittswahrscheinlichkeit 40 %, Schadenshöhe 3.000 € → Risikowert 1.200 €
        'risiko1_schaden': 3000,
        'risiko1_wahrsch': 40,
        # Risiko 2: Nicht-Verfügbarkeit BWI-Kapazitäten (Option 3)
        # Eintrittswahrscheinlichkeit 25 %, Schadenshöhe 2.000 € → Risikowert 500 €
        'risiko2_schaden': 2000,
        'risiko2_wahrsch': 25,
    },

    'entscheidung': {
        'option_bezeichnung': (
            'Option 4: Leistungserbringung durch einen externen Dienstleister'
        ),
        'begruendung': (
            'Empfohlen wird Option 4 — Leistungserbringung durch einen externen '
            'Dienstleister. Die Gesamtkosten für den Betrachtungszeitraum '
            '01.07.–31.12.2026 betragen 25.200 € (ohne Risiko) bzw. 26.400 € '
            '(mit Risikobetrachtung: Risikowert 1.200 €) und sind damit um ca. '
            '1.100 € günstiger als Option 3 (BWI GmbH, 27.500 € inkl. Risiko). '
            'Die bestehende Markterfahrung mit externen IT-Dienstleistern und die '
            'Möglichkeit des Wettbewerbs bei der Neuvergabe sprechen zusätzlich '
            'für diese Option. Ein Vergabeverfahren gemäß UVgO ist einzuleiten. '
            '(siehe Anlage Marktrecherche, Nr. 1 und Nr. 3)'
        ),
    },

    'anlage': [
        {
            'nr':        '1',
            'produkt':   'IT-Helpdesk Managed Service für 50 Arbeitsplätze (Marktrecherche extern)',
            'preis':     '4.000–7.500 €/Monat (80–150 €/AP/Monat)',
            'url':       'https://www.juunit.com/blog/was-kostet-it-outsourcing',
            'bemerkung': 'Marktpreisrecherche IT-Outsourcing Deutschland 2026, Abruf 15.04.2026',
        },
        {
            'nr':        '2',
            'produkt':   'BWI GmbH User Help Desk (Inhousegesellschaft Bundeswehr)',
            'preis':     'ca. 90 €/AP/Monat (Schätzung, nicht öffentlich gelistet)',
            'url':       'https://www.bwi.de/magazin/artikel/user-help-desk-hier-wird-dem-nutzer-geholfen',
            'bemerkung': (
                'BWI betreibt UHD für >180.000 BW-Nutzer; Listenpreise intern; '
                'Schätzung auf Basis allg. Marktdaten, Abruf 15.04.2026'
            ),
        },
        {
            'nr':        '3',
            'produkt':   'Bechtle Service Desk (Referenz: laufender Vertrag BAIUDBw Bonn)',
            'preis':     '4.200 €/Monat (84 €/AP/Monat, 50 AP)',
            'url':       'https://www.bechtle.com/it-services/managed-services/service-desk',
            'bemerkung': (
                'Ist-Preis laufender Vertrag; bei Neuvergabe ggf. leicht höher; '
                'Abruf 15.04.2026'
            ),
        },
    ],
}


def main():
    filename = build_filename(
        wu_data['meta']['datum'],
        'IT-Helpdesk-Support',
        wu_data['meta']['dienststelle'],
    )
    outpath = os.path.join(OUTPUT_DIR, filename)

    print(f'Erzeuge WU-Dokument: {filename}')
    fill_template(wu_data, outpath)

    checkliste = erstelle_abschlusscheckliste_dienstleistung(wu_data, outpath)
    print(checkliste)

    return outpath


if __name__ == '__main__':
    main()
