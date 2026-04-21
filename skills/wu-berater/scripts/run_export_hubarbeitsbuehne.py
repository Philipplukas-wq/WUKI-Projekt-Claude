import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, 'P:/WUKI_Projekt/Claude/skills/wu-berater/scripts')

from berechnung_kapitalwert import (
    Option, Kostenposition, berechne_alle_optionen,
    erstelle_tabellendaten, erstelle_kw_uebersicht, erstelle_sensitivitaet,
    PSR_PERSONAL, PSR_DIENSTLEISTUNGEN
)
from export_wu_ueberjahrig import fill_template, build_filename, erstelle_abschlusscheckliste

optionen = [
    Option('Option 2 - Kauf', investition=6683, kostenpositionen=[
        Kostenposition('Personal', 6500, PSR_PERSONAL),
        Kostenposition('Wartung/Pruefung', 400, PSR_DIENSTLEISTUNGEN),
    ]),
    Option('Option 3 - Miete', investition=0, kostenpositionen=[
        Kostenposition('Personal', 6500, PSR_PERSONAL),
        Kostenposition('Mietkosten', 4272, PSR_DIENSTLEISTUNGEN),
    ]),
    Option('Option 4 - Fremdbezug', investition=0, kostenpositionen=[
        Kostenposition('Personal (Koordination)', 1100, PSR_PERSONAL),
        Kostenposition('Dienstleistung extern', 13200, PSR_DIENSTLEISTUNGEN),
    ]),
]

ergebnisse = berechne_alle_optionen(optionen, zinssatz=0.012, jahre=10)
tbl_daten = erstelle_tabellendaten(ergebnisse)
risikowerte = {
    'Option 2 - Kauf': 1600,
    'Option 3 - Miete': 2500,
    'Option 4 - Fremdbezug': 5500,
}
uebersicht = erstelle_kw_uebersicht(ergebnisse, risikowerte)
sens = erstelle_sensitivitaet(optionen, ergebnisse, risikowerte, zinssatz=0.012, jahre=10)

wu_data = {
    'meta': {
        'titel': 'Wirtschaftlichkeitsuntersuchung zur Beschaffung einer Hubarbeitsbuehne fuer das LogZBw',
        'kurztitel': 'WU Hubarbeitsbuehne LogZBw',
        'dienststelle': 'LogZBw',
        'bearbeiter': 'Philipp Lukas',
        'datum': '15.04.2026',
        'schutz': 'offen',
        'version': '1',
    },
    'ueberblick': {
        'betrachtungsgegenstand': (
            'In der vorliegenden Untersuchung wird die Beschaffung einer '
            'Hubarbeitsbuehne fuer die Liegenschaft des LogZBw betrachtet. '
            'Untersucht werden 3 Optionen ueber 10 Jahre.'
        ),
        'entscheidungsvorschlag': (
            'Empfohlen wird Option 2 - Kauf einer Scherenarbeitsbuehne Snorkel S3010P '
            'mit einem Kapitalwert von 82.710 EUR (inkl. Risiko, '
            'siehe Anlage Marktrecherche, Nr. 1).'
        ),
    },
    'kap1': {
        'bedarfsforderung': (
            'Fuer die Liegenschaft des LogZBw ist die Durchfuehrung von '
            'Gebaeudinstandhaltungsarbeiten in Hoehen bis zu 5 Metern sicherzustellen. '
            'Die erforderlichen Arbeiten umfassen sowohl Innen- als auch Aussenbereiche. '
            'Der Bedarf besteht fuer mindestens 4 Einsaetze pro Monat mit einer '
            'durchschnittlichen Einsatzdauer von je 3 Stunden (ca. 48 Einsatzstunden/Jahr).'
        ),
        'bedarfsprognose': (
            'Der Bedarf an Arbeiten in Hoehen bis zu 5 Metern wird ueber den gesamten '
            'Betrachtungszeitraum von 10 Jahren als konstant eingeschaetzt. Eine '
            'Intensivierung ist moeglich, sofern der Instandhaltungsrueckstand in der '
            'Liegenschaft zunimmt oder zusaetzliche Gebaeude in die Betreuung des LogZBw '
            'uebernommen werden. Es wird daher von mindestens 48 Einsatzstunden pro Jahr '
            'ausgegangen.'
        ),
        'rb_rechtlich': 'Entfaellt.',
        'rb_organisatorisch': 'Entfaellt.',
        'rb_zeitlich': (
            'Die Loesung muss bis spaetestens Juni 2026 einsatzbereit sein, da ab diesem '
            'Zeitpunkt Instandhaltungsarbeiten geplant sind. Optionen, die diesen Termin '
            'nicht erfuellen koennen, scheiden aus.'
        ),
        'rb_sonstige': 'Entfaellt.',
    },
    'kap2': {
        'ablauforganisation': (
            'Zur Durchfuehrung von Gebaeudinstandhaltungsarbeiten in Hoehen bis zu 5 Metern '
            'werden beim LogZBw derzeit Leitern eingesetzt.'
        ),
        'aufbauorganisation': 'Keine besondere Aufbauorganisation vorhanden.',
        'personal': 'Eigenes Personal des LogZBw fuehrt die Arbeiten durch.',
        'material': (
            'Derzeit werden Leitern eingesetzt. Der weitere Einsatz von Leitern als '
            'Arbeitsplatz ist gemaess TRBS 2121 Teil 2 i. V. m. BetrSichV nicht mehr '
            'zulaessig. Die bisherige Loesung ist daher nicht aufrechtzuerhalten.'
        ),
        'infrastruktur': 'Keine besondere Infrastruktur vorhanden.',
        'sach_dienstleistungen': 'Entfaellt.',
        'einnahmen': 'Keine Einnahmen.',
        'haushalterische_darstellung': (
            'Die aktuelle Loesung verursacht lediglich Personalkosten. '
            'Da Leitern Eigenbestand sind, entstehen keine gesonderten Beschaffungs- '
            'oder Mietkosten.'
        ),
        'haushalterische_tabelle': [
            ['Personal', '2.3', 'vorhanden', '-'],
            ['Material', '2.4', 'Leitern (Eigenbestand)', '-'],
            ['Infrastruktur', '2.5', '-', '-'],
            ['Dienstleistungen', '2.6', '-', '-'],
            ['Gesamt', '', '-', '-'],
        ],
    },
    'kap3': {
        'optionen_grundsaetzlich': (
            'Option 1: Weiterbetrieb mit Leitern (Status quo). '
            'Option 2: Kauf einer Hubarbeitsbuehne. '
            'Option 3: Miete einer Hubarbeitsbuehne. '
            'Option 4: Fremdbezug (Dienstleistungsvergabe).'
        ),
        'aussonderung': (
            'Option 1 scheidet aus. Der Weiterbetrieb mit Leitern als Arbeitsplatz ist '
            'gemaess TRBS 2121 Teil 2 i. V. m. BetrSichV nicht mehr zulaessig. '
            'Die Optionen 2, 3 und 4 sind grundsaetzlich geeignet und werden '
            'gleichwertig untersucht.'
        ),
        'optionen_detail': [
            {
                'titel': 'Option 2: Kauf einer Hubarbeitsbuehne',
                'ablauforganisation': (
                    'Eigenes Personal des LogZBw fuehrt die Instandhaltungsarbeiten '
                    'mit der beschafften Hubarbeitsbuehne durch. Einsatz 4 x im Monat a 3 Stunden.'
                ),
                'aufbauorganisation': (
                    'Keine Aenderung erforderlich. Buehne wird vom vorhandenen Personal betrieben.'
                ),
                'personal': (
                    '1 Beschaeftigte/r, E5, 144 h/Jahr (0,08 VZAe). '
                    'Personalkosten: 6.500 EUR/Jahr (PSK 2024).'
                ),
                'material': (
                    'Scherenarbeitsbuehne Snorkel S3010P, 5 m Arbeitshoehe, Batteriebetrieb, '
                    'Innen-/Ausseneinsatz, Traglast 240 kg. '
                    'Kaufpreis: 6.683 EUR netto (siehe Anlage Marktrecherche, Nr. 1).'
                ),
                'infrastruktur': (
                    'Lagerplatz fuer die Hubarbeitsbuehne (ca. 750 x 1.800 mm) muss vorhanden sein. '
                    'Geeigneter Stauraum wird als verfuegbar vorausgesetzt.'
                ),
                'sach_dienstleistungen': (
                    'Jaehrliche Wartung und Pruefung (UVV-Pruefung) nach BetrSichV: ca. 400 EUR/Jahr.'
                ),
                'einnahmen': 'Keine Einnahmen.',
            },
            {
                'titel': 'Option 3: Miete einer Hubarbeitsbuehne',
                'ablauforganisation': (
                    'Eigenes Personal fuehrt Arbeiten durch. '
                    'Hubarbeitsbuehne wird bedarfsweise angemietet - 4 x im Monat fuer je einen Tag.'
                ),
                'aufbauorganisation': 'Keine Aenderung erforderlich.',
                'personal': (
                    '1 Beschaeftigte/r, E5, 144 h/Jahr (0,08 VZAe). '
                    'Personalkosten: 6.500 EUR/Jahr (PSK 2024).'
                ),
                'material': (
                    'Anmietung einer Scherenarbeitsbuehne (ca. 5 m Arbeitshoehe). '
                    'Mietpreis ab 89 EUR/Tag (siehe Anlage Marktrecherche, Nr. 2). '
                    'Jahreskosten Miete: 4.272 EUR/Jahr.'
                ),
                'infrastruktur': 'Kein dauerhafter Lagerplatz erforderlich.',
                'sach_dienstleistungen': (
                    'Wartung und Pruefung obliegen dem Vermieter. Keine zusaetzlichen Kosten.'
                ),
                'einnahmen': 'Keine Einnahmen.',
            },
            {
                'titel': 'Option 4: Fremdbezug (Dienstleistungsvergabe)',
                'ablauforganisation': (
                    'Gebaeudinstandhaltungsarbeiten werden vollstaendig an externes Unternehmen '
                    'vergeben. Eigenes Personal koordiniert die Einsaetze.'
                ),
                'aufbauorganisation': 'Keine Aenderung erforderlich.',
                'personal': (
                    '1 Beschaeftigte/r, E5, 24 h/Jahr (0,01 VZAe) fuer Koordination. '
                    'Personalkosten: 1.100 EUR/Jahr (PSK 2024).'
                ),
                'material': 'Kein eigenes Material erforderlich.',
                'infrastruktur': (
                    'Keine Anforderungen. Zugangsmoelichkeit fuer Auftragnehmer wird vorausgesetzt.'
                ),
                'sach_dienstleistungen': (
                    '48 Einsaetze x 3 h x 75 EUR/h + 50 EUR/Einsatz Anfahrt = '
                    '13.200 EUR/Jahr (siehe Anlage Marktrecherche, Nr. 3).'
                ),
                'einnahmen': 'Keine Einnahmen.',
            },
        ],
    },
    'kap4': {
        'alle_optionen': (
            'Betriebliche Annahmen:\n'
            '- Betrachtungszeitraum: 10 Jahre (2026-2035)\n'
            '- Einsatzhaeufigkeit: 4 Einsaetze/Monat a 3 Stunden = 48 Einsaetze/Jahr\n'
            '- Jahresarbeitsstunden: 1.720 h/VZAe\n'
            '- Personalkosten: PSK 2024, nachgeordnete Bundesbehoerden, E5 = 77.447 EUR/VZAe/Jahr\n\n'
            'Kalkulatorische Annahmen:\n'
            '- Kalkulationszinssatz: 1,2 % (BMF, April 2026)\n'
            '- Preissteigerung Personal: 2,6 %/Jahr\n'
            '- Preissteigerung Dienstleistungen: 2,4 %/Jahr\n'
            '- Preissteigerung Gebrauchsgueter: 2,4 %/Jahr'
        ),
        'bestimmte_optionen': (
            'Option 2 (Kauf): Kaufpreis Snorkel S3010P: 6.683 EUR netto '
            '(Jungheinrich PROFISHOP, April 2026; siehe Anlage Marktrecherche, Nr. 1). '
            'Wartung/Pruefung: 400 EUR/Jahr. Restwert nach 10 Jahren: 0 EUR.\n\n'
            'Option 3 (Miete): Tagesmiete 89 EUR (SYSTEM LIFT, April 2026; '
            'siehe Anlage Marktrecherche, Nr. 2). 48 Miettage/Jahr.\n\n'
            'Option 4 (Fremdbezug): Handwerkerstundensatz 75 EUR/h '
            '(Marktmittelwert Deutschland 2026; siehe Anlage Marktrecherche, Nr. 3). '
            'Anfahrtspauschale 50 EUR/Einsatz. 48 Einsaetze/Jahr a 3 h.'
        ),
        'berechnung': (
            'Kapitalwertberechnung mit Zinssatz 1,2 %, Betrachtungszeitraum 10 Jahre.'
        ),
    },
    'kap5': {
        'ibv': 'Entfaellt.',
        'berechnung_text': (
            'Die Kapitalwertberechnung erfolgt auf Basis der in Kapitel 4 festgelegten '
            'Annahmen mit einem Kalkulationszinssatz von 1,2 % ueber 10 Jahre.'
        ),
        'berechnung_tabelle': tbl_daten,
        'kw_ohne_risiko': (
            'Option 2 - Kauf: 81.110 EUR | '
            'Option 3 - Miete: 115.765 EUR | '
            'Option 4 - Fremdbezug: 152.795 EUR'
        ),
        'risikoidentifizierung': (
            'Risiken Option 2: Technischer Ausfall, hoehere Wartungskosten.\n'
            'Risiken Option 3: Nicht-Verfuegbarkeit, Mietpreiserhoehung.\n'
            'Risiken Option 4: Terminuntreue Auftragnehmer, Preiserhoehung, Auftragnehmerausfall.'
        ),
        'risikoverteilung': (
            'Das Risiko eines technischen Ausfalls und erhoehter Wartungskosten liegt bei '
            'Option 2 vollstaendig beim LogZBw. Bei Option 3 traegt der Vermieter das '
            'Geraeterisiko; das LogZBw traegt das Verfuegbarkeits- und Preisrisiko. '
            'Bei Option 4 liegt das Qualitaets- und Preisrisiko im Wesentlichen beim '
            'Auftragnehmer, verbleibt durch vertragliche Abhaengigkeit jedoch mittelbar '
            'beim LogZBw.'
        ),
        'risikobewertung': (
            'Option 2: Risikowert 1.600 EUR. '
            'Option 3: Risikowert 2.500 EUR. '
            'Option 4: Risikowert 5.500 EUR.'
        ),
        'kw_mit_risiko': (
            'Option 2 - Kauf: 82.710 EUR | '
            'Option 3 - Miete: 118.265 EUR | '
            'Option 4 - Fremdbezug: 158.295 EUR'
        ),
    },
    'kap6_9': {
        'optionen_uebersicht': uebersicht,
        'vergleich': (
            'Option 2 (Kauf) ist sowohl ohne als auch mit Risikobetrachtung die '
            'wirtschaftlichste Option. Kostenvorteil gegenueber Option 3: 35.555 EUR, '
            'gegenueber Option 4: 75.585 EUR.'
        ),
        'sensitivitaet': sens,
        'nichtmonetaer': (
            'Eine Nutzwertanalyse ist nicht erforderlich, da keine nichtmonetaeren Faktoren '
            'vorliegen, die eine Abweichung vom wirtschaftlichsten Ergebnis begruenden wuerden.'
        ),
        'entscheidungsvorschlag': (
            'Die Untersuchung ergibt, dass Option 2 - Kauf einer Hubarbeitsbuehne die '
            'wirtschaftlichste Loesung darstellt. Mit einem Kapitalwert von 82.710 EUR '
            '(inkl. Risiko) ist sie gegenueber Option 3 (118.265 EUR) um 35.555 EUR und '
            'gegenueber Option 4 (158.295 EUR) um 75.585 EUR vorteilhafter. Die '
            'Sensitivitaetsanalyse bestaetigt die Robustheit. Es wird empfohlen, eine '
            'Scherenarbeitsbuehne Snorkel S3010P zum Preis von 6.683 EUR (netto) zu '
            'beschaffen (siehe Anlage Marktrecherche, Nr. 1).'
        ),
    },
    'anlage': [
        {
            'nr': '1',
            'produkt': 'Snorkel Scherenarbeitsbuehne S3010P, max. 5 m Arbeitshoehe, Batteriebetrieb',
            'preis': '6.683,00 EUR (netto)',
            'url': 'https://www.jh-profishop.de/p/snorkel-scherenarbeitsbuehne-290323-241015/',
            'datum': '15.04.2026',
            'hinweis': 'Onlineshop Jungheinrich PROFISHOP',
        },
        {
            'nr': '2',
            'produkt': 'Scherenarbeitsbuehne Miete, ca. 5 m Arbeitshoehe',
            'preis': 'ab 89,00 EUR/Tag',
            'url': 'https://www.systemlift.de/mietpreise.html',
            'datum': '15.04.2026',
            'hinweis': 'SYSTEM LIFT, Startpreis',
        },
        {
            'nr': '3',
            'produkt': 'Handwerker Instandhaltung, Stundensatz Marktmittelwert Deutschland 2026',
            'preis': '75,00 EUR/h zzgl. 50,00 EUR/Einsatz Anfahrt',
            'url': 'https://www.handwerk.cloud/wissen/allgemein/handwerker-stundenlohn-kosten-2026',
            'datum': '15.04.2026',
            'hinweis': 'Marktueblicher Mittelwert',
        },
    ],
}

outpath = 'P:/WUKI_Projekt/Claude/' + build_filename('20260415', 'Hubarbeitsbuehne', 'LogZBw')
print('Ausgabepfad:', outpath)
fill_template(wu_data, outpath)
print('Export erfolgreich.')
checkliste = erstelle_abschlusscheckliste(wu_data, outpath)
print(checkliste)
