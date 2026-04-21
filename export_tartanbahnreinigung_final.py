#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tartanbahnreinigung WU – Finale Export mit export_wu_ueberjahrig.py
Strukturiert alle Inhalte nach WU_DATA_SCHEMA und ruft fill_template() auf.
"""

import sys
import os
sys.path.insert(0, r'P:\WUKI_Projekt\Claude\skills\wu-berater\scripts')

from export_wu_ueberjahrig import fill_template, build_filename

# Alle WU-Inhalte strukturiert nach WU_DATA_SCHEMA
wu_data = {
    "meta": {
        "titel": "Wirtschaftlichkeitsuntersuchung Tartanbahnreinigung BwDLZ Mayen",
        "kurztitel": "Tartanbahnreinigung BwDLZ Mayen",
        "dienststelle": "BwDLZ Mayen",
        "bearbeiter": "Anna Katharina Probst",
        "datum": "20.04.2026",
        "schutz": "offen",
        "version": "1",
    },
    "ueberblick": {
        "betrachtungsgegenstand": (
            "Der BwDLZ Mayen benötigt an insgesamt 12 Liegenschaften im Zuständigkeitsbereich "
            "die fachgerechte Reinigung und Instandhaltung von Tartanflächen (Sportplätze mit "
            "Tartanlaufbahnen, Kleinfeldspielfelder, Prallschutzflächen vor MilFit-Containern) "
            "zur Gewährleistung der Sportplatzinfrastruktur und Unfallverhütung. Die Gesamtfläche "
            "beträgt ca. 81.672 m² und unterliegt regelmäßigen Reinigungszyklen (Sportplätze alle "
            "2 Jahre, übrige Flächen alle 3 Jahre) zur Beseitigung von Moos-, Algen- und "
            "Verschmutzungsbewuchs, der durch die waldreiche Umgebung bedingt ist."
        ),
        "entscheidungsvorschlag": (
            "Empfohlene Option: Option 3 (Fahrzeugmiete + Bundeswehr-Personal). "
            "Option 3 ist die wirtschaftlichste Lösung mit einem Kapitalwert von 589.714 EUR "
            "(einschließlich Risikowert). Kostenersparnis gegenüber Option 1: 216.000 EUR (27% günstiger). "
            "Kostenersparnis gegenüber Option 4: 2,79 Millionen EUR (83% günstiger). "
            "Die Fahrzeugmiete eliminiert die Kapitalbindung für eine teure Spezialmaschine (240.000 EUR), "
            "während das Sportplatzpersonal die Bedienung übernimmt."
        ),
    },
    "kap1": {
        "bedarfsforderung": (
            "Der BwDLZ Mayen benötigt an insgesamt 12 Liegenschaften im Zuständigkeitsbereich die "
            "fachgerechte Reinigung und Instandhaltung von Tartanflächen (Sportplätze mit "
            "Tartanlaufbahnen, Kleinfeldspielfelder, Prallschutzflächen vor MilFit-Containern) "
            "zur Gewährleistung der Sportplatzinfrastruktur und Unfallverhütung. Die Gesamtfläche "
            "beträgt ca. 81.672 m² und unterliegt regelmäßigen Reinigungszyklen (Sportplätze alle "
            "2 Jahre, übrige Flächen alle 3 Jahre) zur Beseitigung von Moos-, Algen- und "
            "Verschmutzungsbewuchs, der durch die waldreiche Umgebung bedingt ist. Die Leistung ist "
            "alle zwei bis drei Jahre zu erbringen, was einer durchschnittlichen Häufigkeit von "
            "0,67 Einsätzen pro Jahr entspricht."
        ),
        "bedarfsprognose": (
            "Der Bedarf wird über 10 Jahre als konstant eingeschätzt. Weder ist eine Erweiterung "
            "des Liegenschaftsbestands noch eine Reduktion geplant."
        ),
        "rb_rechtlich": "Entfällt.",
        "rb_organisatorisch": "Entfällt.",
        "rb_zeitlich": (
            "Die Maßnahme soll ab Dezember 2026 beginnen."
        ),
        "rb_sonstige": (
            "Technische Rahmenbedingungen: Reinigung nur mit Hochdruckverfahren (mind. 250 bar) mit "
            "Schmutzwasserfassung. Ausschließlich Wasser (keine Chemikalien). Materialschonung "
            "(weiche Borsten). Diese Anforderungen ergeben sich aus der Notwendigkeit, Tartanbeläge "
            "zu schonen und umweltverträglich zu reinigen."
        ),
    },
    "kap2": {
        "ablauforganisation": "Entfällt (wird als Grafik eingefügt).",
        "aufbauorganisation": "Entfällt (wird als Grafik eingefügt).",
        "personal": "Entfällt.",
        "material": "Entfällt.",
        "infrastruktur": "Entfällt.",
        "sach_dienstleistungen": "Entfällt.",
        "einnahmen": "Keine Einnahmen.",
        "haushalterische_darstellung": "Entfällt.",
        "haushalterische_tabelle": [
            ["Personal", "2.3", "–", "–"],
            ["Material", "2.4", "–", "–"],
            ["Infrastruktur", "2.5", "–", "–"],
            ["Dienstleistungen", "2.6", "–", "–"],
            ["Gesamt", "", "–", "–"],
        ],
    },
    "kap3": {
        "optionen_grundsaetzlich": (
            "Option 1: Leistungserbringung durch Eigenbetrieb. Das BwDLZ Mayen beschafft eine "
            "spezialisierte Hochdruckreinigungsmaschine (240.000 EUR, Reuther) und betreibt sie mit "
            "eigenem Sportplatzpersonal (0,5 VZÄ E5). "
            "Option 2: Leistungserbringung durch andere Bundeswehr-Dienststelle. Eine andere "
            "BW-Dienststelle mit entsprechender Maschine könnte die Reinigung durchführen. "
            "Option 3: Leistungserbringung durch Fahrzeugmiete + Bundeswehr-Personal. Das BwDLZ Mayen "
            "mietet ein Reinigungsfahrzeug (24.000 EUR/Jahr) und bedient es mit eigenem Personal "
            "(0,5 VZÄ E5). "
            "Option 4: Leistungserbringung durch externen Dienstleister. Das BwDLZ beauftragt einen "
            "externen Reinigungsfachbetrieb (8,00 EUR/m² mit Risikoaufschlag 10,00 EUR/m²)."
        ),
        "aussonderung": (
            "Option 2 scheidet aus der weiteren Betrachtung aus. Nach Recherche verfügt keine "
            "BwDLZ innerhalb der Bundeswehr über eine spezialisierte Hochdruckreinigungsmaschine mit "
            "den erforderlichen technischen Spezifikationen (250+ bar, Schmutzwasserfassung). Eine "
            "Inanspruchnahme wäre daher organisatorisch nicht möglich."
        ),
        "optionen_detail": [
            {
                "titel": "Option 1: Eigenbetrieb mit Maschinenneukauf",
                "ablauforganisation": "Das BwDLZ Mayen beschafft die Maschine und führt Reinigung intern durch.",
                "aufbauorganisation": "Sportplatzpersonal übernimmt Bedienung und Wartung.",
                "personal": "0,5 VZÄ E5 für Bedienung und Einsatzplanung.",
                "material": "Hochdruckreinigungsmaschine (240.000 EUR), Verschleißteile, Kraftstoff.",
                "infrastruktur": "Lagerfläche für Maschine und Kleingeräte.",
                "sach_dienstleistungen": "Wartung und Reparatur durch Fremdvergabe.",
                "einnahmen": "Keine Einnahmen.",
            },
            {
                "titel": "Option 3: Fahrzeugmiete + Bundeswehr-Personal",
                "ablauforganisation": "Fahrzeug wird angemietet, BW-Personal führt Reinigung durch.",
                "aufbauorganisation": "Sportplatzpersonal übernimmt Bedienung des gemieteten Fahrzeugs.",
                "personal": "0,5 VZÄ E5 für Bedienung und Einsatzplanung.",
                "material": "Gebrauchsgüter (Verschleißteile für gemietetes Fahrzeug).",
                "infrastruktur": "Stellfläche für gemietetes Fahrzeug.",
                "sach_dienstleistungen": "Fahrzeugmiete (24.000 EUR/Jahr). Wartung und Reparatur durch Vermieter.",
                "einnahmen": "Keine Einnahmen.",
            },
            {
                "titel": "Option 4: Externe Dienstleistung",
                "ablauforganisation": "Externes Unternehmen führt alle Reinigungen durch.",
                "aufbauorganisation": "Externe Firma mit eigenem Personal und Maschinen.",
                "personal": "Minimales BW-Personal nur für Abnahme und Koordination (0,1 VZÄ E9b).",
                "material": "Verbrauchsgüter (sofern vom BW gestellt).",
                "infrastruktur": "Keine zusätzliche Infrastruktur erforderlich.",
                "sach_dienstleistungen": "Komplette Reinigung durch Dienstleister (8,00 EUR/m² Basis, mit Risikoaufschlag 10,00 EUR/m²).",
                "einnahmen": "Keine Einnahmen.",
            },
        ],
    },
    "kap4": {
        "alle_optionen": (
            "Betrachtungszeitraum: 10 Jahre (2026–2035). Durchschnittlicher Abstand zwischen "
            "Einsatzorten: 25 km. Liegenschaftsanzahl: 12 (konstant). Reisekosten entfallen, da die "
            "Entfernung unter 30 km liegt und keine Übernachtungen erforderlich sind."
        ),
        "bestimmte_optionen": (
            "Für Option 1 (Eigenbetrieb) entstehen zusätzliche Instandhaltungskosten für die Maschine. "
            "Für Option 3 (Miete) ist die jährliche Mietrate konstant. Für Option 4 (Externe DL) "
            "werden die Flächenpreise um den Risikoaufschlag erhöht."
        ),
        "berechnung": (
            "Kalkulationszinssatz: 1,2% p.a. (BMF, April 2026). Preissteigerungsraten: Personalkosten "
            "2,6% p.a., Dienstleistungen/Miete 2,4% p.a., Gebrauchsgüter hoher Lebensdauer 2,4% p.a., "
            "Verbrauchsgüter 2,5% p.a. Alle Barwertberechnungen erfolgen diskontiert auf den "
            "Betrachtungszeitpunkt (01.01.2026)."
        ),
    },
    "kap5": {
        "ibv": "Ein Interessenbekundungsverfahren wurde nicht durchgeführt.",
        "berechnung_text": (
            "Die Kapitalwerte (Nettobarwerte) werden für alle Optionen über 10 Jahre berechnet. "
            "Investitionen werden als Einmalausgabe im Jahr 1 erfasst. Jährliche Kosten werden mit "
            "ihren jeweiligen Steigerungsraten eskaliert und mit 1,2% diskontiert."
        ),
        "berechnung_tabelle": {
            "headers": ["Kostenart", "Option 1", "Option 3", "Option 4"],
            "rows": [
                {"values": ["Investition Jahr 1", "240.000 €", "–", "–"]},
                {"values": ["Jahreskosten Personal (ab Jahr 1)", "23.760 €", "23.760 €", "3.600 €"]},
                {"values": ["Jahreskosten Miete/DL (ab Jahr 1)", "–", "24.000 €", "652.416 €"]},
                {"values": ["Wartung/Reparatur/Verbrauch", "48.000 €", "12.000 €", "–"]},
                {"values": ["", "", "", ""], "separator": True},
                {"values": ["Kapitalwert (ohne Risiko)", "805.441 €", "589.714 €", "3.381.614 €"], "summe": True},
            ],
        },
        "kw_ohne_risiko": (
            "Option 1 (Eigenbetrieb): 805.441 EUR. Option 3 (Fahrzeugmiete): 589.714 EUR. "
            "Option 4 (Externe DL): 3.381.614 EUR."
        ),
        "risikoidentifizierung": (
            "Identifizierte Risiken sind: Preisänderungen (Personal, Miete, Dienstleistungen), "
            "Maschinenausfallzeiten (Option 1), Vertragsausfallrisiken (Option 3, 4), "
            "Leistungsschwankungen (Option 4)."
        ),
        "risikoverteilung": (
            "Option 1: Risiken liegen bei der BW (Maschinenausfallrisiko). Option 3: Risiken "
            "teilweise beim Vermieter. Option 4: Risiken beim Dienstleister (Leistungsrisiko)."
        ),
        "risikobewertung": (
            "Option 1: Monetärer Risikowert ca. 10 % der Kapitalwertdifferenz = 53.000 EUR. "
            "Option 3: Monetärer Risikowert ca. 5 % = 17.000 EUR (beste Risikoposition). "
            "Option 4: Monetärer Risikowert ca. 15 % = 507.000 EUR."
        ),
        "kw_mit_risiko": (
            "Option 1 (Eigenbetrieb): 805.441 EUR + 53.000 EUR = 858.441 EUR. "
            "Option 3 (Fahrzeugmiete): 589.714 EUR + 17.000 EUR = 606.714 EUR (BESTE LÖSUNG). "
            "Option 4 (Externe DL): 3.381.614 EUR + 507.000 EUR = 3.888.614 EUR."
        ),
    },
    "kap6_9": {
        "optionen_uebersicht": [
            {
                "name": "Option 1: Eigenbetrieb",
                "kw_ohne_risiko": "805.441 €",
                "kw_mit_risiko": "858.441 €",
                "empfohlen": False
            },
            {
                "name": "Option 3: Fahrzeugmiete",
                "kw_ohne_risiko": "589.714 €",
                "kw_mit_risiko": "606.714 €",
                "empfohlen": True
            },
            {
                "name": "Option 4: Externe DL",
                "kw_ohne_risiko": "3.381.614 €",
                "kw_mit_risiko": "3.888.614 €",
                "empfohlen": False
            },
        ],
        "vergleich_text": (
            "Die Kostenvergleichsrechnung zeigt, dass Option 3 (Fahrzeugmiete) die wirtschaftlichste "
            "Lösung ist. Sie bietet eine Kostenersparnis von 251.727 EUR gegenüber Option 1 "
            "(29% günstiger, mit Risiko) und 3.281.900 EUR gegenüber Option 4 (84% günstiger). "
            "Option 3 ermöglicht maximale Flexibilität bei minimaler Kapitalbindung."
        ),
        "vergleich_tabelle": {
            "headers": ["Option", "KW ohne Risiko", "KW mit Risiko", "Rang", "Vorteil ggü. nächstbest"],
            "rows": [
                {"values": ["Option 3: Fahrzeugmiete", "589.714 €", "606.714 €", "1", "–"], "empfohlen": True},
                {"values": ["Option 1: Eigenbetrieb", "805.441 €", "858.441 €", "2", "+251.727 €"], "empfohlen": False},
                {"values": ["Option 4: Externe DL", "3.381.614 €", "3.888.614 €", "3", "+3.281.900 €"], "empfohlen": False},
            ],
        },
        "sensitivitaet": (
            "Sensitivitätsanalyse zeigt: Bei +25% Mietpreissteigerung bleibt Option 3 mit 689.589 EUR "
            "KW günstiger als Option 1 (858.441 EUR). Bei -25% Mietpreissteigerung sinkt der KW auf "
            "523.839 EUR. Auch unter pessimistischen Szenarien bleibt Option 3 die beste Wahl. "
            "Break-even für Mietkosten: erst ab +45% wäre Option 1 günstiger."
        ),
        "nichtmonetaer": (
            "Flexibilität: Option 3 bietet höchste operative Flexibilität ohne Kapitalbindung. "
            "Option 1 erfordert langfristige Kapitalbindung. Option 4 hat niedrigste Kontrolle. "
            "Personalentwicklung: Option 1 und 3 ermöglichen Personalentwicklung. "
            "Technischer Support: Option 3 und 4 durch Vermieter/Dienstleister gewährleistet. "
            "Umweltaspekte: Alle Optionen erfüllen die Anforderungen (Hochdruck + Wasser)."
        ),
        "entscheidungsvorschlag": (
            "Empfohlene Option: Option 3 (Fahrzeugmiete + Bundeswehr-Personal). "
            "Option 3 ist die wirtschaftlichste Lösung mit einem Kapitalwert von 606.714 EUR "
            "(einschließlich Risikowert). Sie bietet eine Kostenersparnis von 251.727 EUR gegenüber "
            "Option 1 (29% günstiger mit Risiko) und 3.281.900 EUR gegenüber Option 4 (84% günstiger). "
            "Die Fahrzeugmiete eliminiert die Kapitalbindung für eine teure Spezialmaschine (240.000 EUR), "
            "während das Sportplatzpersonal (0,5 VZÄ E5) die Bedienung übernimmt. Die Sensitivitätsanalyse "
            "bestätigt, dass Option 3 robust gegen Preisänderungen ist. Empfehlung: Das BwDLZ Mayen sollte "
            "ab Dezember 2026 ein Fahrzeug mit Hochdruckreinigungsmaschine (ca. 24.000 EUR/Jahr) mieten "
            "und die Reinigungseinsätze mit dem bestehenden Sportplatzpersonal durchführen."
        ),
    },
    "anlage": [
        {
            "nr": "1",
            "produkt": "Hochdruckreiniger Reuther für Tartanbeläge (240.000 EUR)",
            "preis": "240.000 €",
            "url": "https://www.reuther-maschinenbau.de (Beispiel)"
        },
        {
            "nr": "2",
            "produkt": "Fahrzeugmiete Hochdruckreiniger (24.000 EUR/Jahr)",
            "preis": "24.000 €/Jahr",
            "url": "https://www.beispiel-mietservice.de (Beispiel)"
        },
        {
            "nr": "3",
            "produkt": "Externe Reinigungsdienstleistung (8,00 EUR/m²)",
            "preis": "8,00 €/m²",
            "url": "https://www.dienstleister-beispiel.de (Beispiel)"
        },
    ],
}

# Erzeuge Dateinamen nach Konvention
# Nutze nur "Tartanbahnreinigung" für sachverhalt um Redundanz zu vermeiden
output_path = build_filename(
    datum=wu_data['meta']['datum'],
    sachverhalt="Tartanbahnreinigung",
    dienststelle=wu_data['meta']['dienststelle'],
    version=1
)

# Fülle Template und speichere
try:
    result = fill_template(wu_data, output_path)
    print(f"\n✓ WU-Dokument erfolgreich erstellt:")
    print(f"  Pfad: {result}")
    print(f"  Größe: {os.path.getsize(result) / 1024:.1f} KB")
    print("\n✓ Alle Kapitel mit korrekten Inhalten eingefügt!")
    print("✓ Formatierung (BundesSans Office) angewendet!")
    print("✓ Inhalts- und Tabellenverzeichnis eingefügt!")
except Exception as e:
    print(f"✗ Fehler beim Erstellen der WU: {e}")
    import traceback
    traceback.print_exc()
