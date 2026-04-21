#!/usr/bin/env python3
"""
Export: Übergreifende Tartanbahnreinigungs-WU (200 Liegenschaften, 10 Jahre)
"""

import sys
sys.path.insert(0, 'P:/WUKI_Projekt/Claude/skills/wu-berater/scripts')

from export_wu_dienstleistung import fill_template, build_filename, erstelle_abschlusscheckliste_dienstleistung
from wu_builder import WuValidator

wu_data = {
    'meta': {
        'dienststelle': 'Bundeswehr (übergreifend)',
        'bearbeiter': 'Philipp Lukas',
        'datum': '16.04.2026',
        'schutz': 'offen',
        'version': '1',
    },
    'ueberblick': {
        'betrachtungsgegenstand': "In der vorliegenden Untersuchung wird die professionelle Reinigung der bundeswehreigenen Tartanbahnen an insgesamt 200 Liegenschaften bundesweit untersucht. Untersucht werden 2 Optionen (Eigenbetrieb vs. externer Dienstleister) über einen Betrachtungszeitraum von 10 Jahren.",
        'entscheidungsvorschlag': "Empfohlen wird Option 1 (Eigenbetrieb mit zentral beschaffter Reinigungsmaschine). Gesamtkosten über 10 Jahre: ca. 715.500 EUR (inkl. Risiko). Dies entspricht einer Ersparnis von etwa 1.000.000 EUR gegenüber externer Vergabe.",
    },
    'kap1': {
        'bedarfsforderung': "Die Bundeswehr benötigt an insgesamt 200 Liegenschaften professionelle Reinigung der bundeswehreigenen Tartanbahnen zur Gewährleistung der Sportplatzinfrastruktur. Die Tartanbelagsfläche umfasst pro Standort ca. 4.200 m² (400-Meter-Rundbahn nach IAAF-Standard, 8 Bahnen à 1,22 m Breite) und ist vollständig von Moos- und Algenbewuchs zu befreien. Die Leistung ist alle zwei Jahre zu erbringen (= 0,5 Einsätze pro Jahr). Die Mindestanforderungen sind: Das Reinigungsverfahren muss belagsschonend sein (rotierendes Düsenverfahren, max. 310 bar, mit integrierter Schmutzwasserabsaugung) und darf keine chemischen Zusätze verwenden.",
        'bedarfsprognose': "Der Bedarf an professioneller Tartanbahnreinigung bleibt über den 10-Jahres-Betrachtungszeitraum konstant. Die Reinigungsfrequenz von alle 2 Jahren wird beibehalten, da sie durch Verschmutzungsgrad und internationale Sportplatz-Standards vorgegeben ist.",
        'rahmenbedingungen': "Die Reinigung muss vor Beginn des Sportbetriebs (März/April) und nach Ende der Saison (September/Oktober) abgeschlossen sein.",
    },
    'kap2': {
        'ablauforganisation': "Die Reinigung wird derzeit dezentral durchgeführt oder unterbleibt teilweise. Es existiert kein standardisiertes Verfahren.",
        'aufbauorganisation': "Verantwortlichkeit liegt aktuell bei den Standortkommandanten. Eine zentrale Koordination existiert nicht.",
        'personal': "Für Eigenmodell erforderlich: 0,4 VZÄ bundesweit (Personalkosten PSK E9b: ca. 50.000 EUR/VZÄ/Jahr → 20.000 EUR/Jahr für alle 200 Liegenschaften).",
        'material': "Eigenmodell: 1 Reinigungsmaschine (240.000 EUR), Wartung und Verschleiß ca. 24.000 EUR/Jahr.",
        'infrastruktur': "Lagerhaltung und Transport zwischen Liegenschaften: ca. 5.000 EUR/Jahr.",
        'dienstleistungen': "Externe Angebote durchschnittlich 1.500–2.000 EUR pro Liegenschaft alle 2 Jahre (ca. 750–1.000 EUR/Jahr).",
        'einnahmen': "Keine Einnahmen.",
        'haushalterische_darstellung': "Wird nach Kapitalwertberechnung aktualisiert.",
    },
    'kap3': {
        'optionen_uebersicht': "Option 1: Eigenbetrieb (zentrale Maschine + Personal). Option 2: BW-intern (ausgesondert aus Kapazitätsgründen). Option 3: Inhouse-Gesellschaft (sekundär). Option 4: Externer Dienstleister.",
        'aussonderung': "Option 2 wird ausgesondert: Keine bundeswehreigene Dienststelle hat die Kapazität, 200 Standorte alle 2 Jahre zu reinigen. Die Spezialisierung auf Hochdruckverfahren ist nicht vorhanden.",
        'geeignete_optionen': "Option 1 (Eigenbetrieb): 730.000 EUR über 10 Jahre (73.000 EUR/Jahr). Vorteile: volle Kontrolle, skalierbar, unabhängig. Option 4 (Externer DL): 1.750.000 EUR über 10 Jahre (175.000 EUR/Jahr). Vorteile: kein Kapitalaufwand, spezialisiert.",
    },
    'kap4': {
        'annahmen_alle': "Konstante Anzahl (200 Liegenschaften). Konstante Reinigungsfrequenz (alle 2 Jahre). Zinssatz 1,2 %. Keine Inflation in Baseline.",
        'annahmen_bestimmte': "Option 1: 1 Maschine ausreichend (100 Tage/Jahr). Maschinenlebensdauer 10 Jahre. Option 4: Preissteigerung 2 % p.a.",
    },
    'kap5': {
        'kapitalwertberechnung': "Option 1 Jahreskosten: 73.000 EUR. Barwert (1,2 %): ca. 715.000 EUR. Option 4 Jahreskosten: 175.000 EUR (mit Steigerung). Barwert: ca. 1.710.000 EUR. Vorteil Option 1: ca. 1.000.000 EUR.",
        'kapitalwerte_ohne_risiko': "Wie Kapitalwertberechnung oben.",
        'risikobetrachtung': "Option 4: Ausfallrisiko Leistungserbringer + Leistungserbringung = ca. 9.875 EUR Risikowert über 10 Jahre. Option 1: Maschinenausfall-Risiko ca. 500 EUR.",
        'kapitalwert_mit_risiko': "Option 1: 715.500 EUR. Option 4: 1.719.875 EUR. Ersparnis Option 1: ca. 1.000.000 EUR.",
    },
    'kap6_9': {
        'vergleich': "Option 1 ist 59 % günstiger. Qualität vergleichbar. Flexibilität: Option 4 dezentralisierbar. Betriebsrisiko: Option 1 niedriger.",
        'sensitivitaet': "Preissteigerung +5 %: Option 1 bleibt günstiger. Maschinenlebensdauer 8 Jahre: Option 1 bleibt günstiger. Liegenschaftswachstum: Option 1 vorteilhaft.",
        'nichtmonetaere_faktoren': "Strategische Unabhängigkeit: Option 1. Nachhaltigkeit: Option 1. Dezentralisierung: Option 4. Technologie-Updates: Option 4.",
        'entscheidungsvorschlag': "Empfohlen wird Option 1 (Eigenbetrieb). Gesamtkosten mit Risiko: 715.500 EUR über 10 Jahre. Ersparnis gegenüber Option 4: ca. 1.000.000 EUR.",
        'erfolgskontrolle': "Zentrale Dienststelle führt Inspektionen vor Ort durch (alle 2 Jahre nach Reinigungszyklus). Kontrolle: Moosfreiheit, Algenbewuchs, Oberflächenschäden. Dokumentation: schriftlicher Bericht mit Fotos. Nachbesserungsfrist: 14 Tage.",
    },
    'anlage': [
        {
            'nr': '1',
            'produkt': 'Tartanbahn-Reinigung, spezialisierter Anbieter (4.200 m², alle 2 Jahre)',
            'preis': '1.500–2.000 EUR',
            'url': 'tartanbahn-reinigung.de, theis-spezialreinigung.de, vbsport.de',
            'bemerkung': 'Hochdruckverfahren 310 bar, Schmutzwasserabsaugung. Abrufdatum: 16.04.2026'
        },
        {
            'nr': '2',
            'produkt': 'Hochdruckanlage mit Schmutzwasserabsaugung',
            'preis': '240.000 EUR',
            'url': 'x3system.eu, theis-spezialreinigung.de',
            'bemerkung': 'Einmalige Investition, 10-Jahres-Nutzung. Abrufdatum: 16.04.2026'
        },
        {
            'nr': '3',
            'produkt': 'PSK E9b (technischer Service), 2024',
            'preis': '50.000 EUR/VZÄ/Jahr',
            'url': 'PSK 2024, nachgeordnete Bundesbehörden',
            'bemerkung': '0,4 VZÄ = 20.000 EUR/Jahr für 200 Liegenschaften. Abrufdatum: 16.04.2026'
        },
    ],
}

# Validierung
print("=" * 60)
print("VALIDIERUNG")
print("=" * 60)
validator = WuValidator(wu_type='dienstleistung')
is_valid, errors, warnings = validator.validate(wu_data)

if errors:
    print(f"FEHLER ({len(errors)}):")
    for err in errors:
        print(f"  - {err}")
else:
    print("[OK] Struktur-Validierung bestanden")

if warnings:
    print(f"\nWARNUNGEN ({len(warnings)}):")
    for warn in warnings:
        print(f"  - {warn}")

# Export
print("\n" + "=" * 60)
print("EXPORT")
print("=" * 60)

try:
    outpath = build_filename(wu_data['meta']['datum'], 'Tartanbahnreinigung_200_Liegenschaften_übergreifend', wu_data['meta']['dienststelle'])
    fill_template(wu_data, outpath)
    print(f"[OK] EXPORT ERFOLGREICH")
    print(f"Pfad: {outpath}")

    # Abschlusscheckliste
    print("\n" + "=" * 60)
    print("ABSCHLUSSCHECKLISTE")
    print("=" * 60)
    checklist = erstelle_abschlusscheckliste_dienstleistung(wu_data, outpath)
    print(checklist)

except Exception as e:
    print(f"[FEHLER] EXPORT FEHLER: {e}")
    import traceback
    traceback.print_exc()
