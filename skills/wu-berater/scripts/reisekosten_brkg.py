"""
Reisekostenkalkulation nach Bundesreisekostengesetz (BRKG)
§ 5 Wegstreckenentschädigung, § 6 Tagegeld, § 7 Übernachtungsgeld
"""

def berechne_reisekosten(
    entfernung_km: float = 400,
    reisetage_pro_jahr: int = 10,
    uebernachtungen_pro_reisetag: float = 1.0,
    anreise_abreise_rate: float = 0.5,
    beschreibung: str = ""
) -> dict:
    """
    Berechnet jährliche Reisekosten nach BRKG für einen Mitarbeiter.

    Args:
        entfernung_km: Strecke zwischen Reiseorten in km (default: 400 km)
        reisetage_pro_jahr: Anzahl Reisetage pro Jahr (default: 10)
        uebernachtungen_pro_reisetag: Durchschn. Übernachtungen pro Reisetag (default: 1.0)
        anreise_abreise_rate: Anteil der Reisetage, die Anreise/Abreise sind (default: 0.5 = 50%)
        beschreibung: Begründung für die Annahmen

    Returns:
        dict mit Kostenaufschlüsselung und Begründung
    """

    # § 5 BRKG: Wegstreckenentschädigung
    satz_pro_km = 0.20  # EUR/km
    max_wegstrecke = 130.0  # EUR pro Reisetag

    # Berechnung: 0,20 € × km, aber max. 130 €
    wegstreckenkosten_pro_tag = min(satz_pro_km * entfernung_km, max_wegstrecke)

    # § 6 BRKG: Tagegeld
    tagegeld_anreise_abreise = 14.0  # EUR pro Tag
    tagegeld_volle_reisetage = 28.0  # EUR pro Tag

    # Berechnung: Anteil Anreise/Abreise vs. volle Reisetage
    anreise_abreise_tage = reisetage_pro_jahr * anreise_abreise_rate
    volle_reisetage = reisetage_pro_jahr * (1 - anreise_abreise_rate)

    tagegeldkosten_pro_jahr = (
        anreise_abreise_tage * tagegeld_anreise_abreise +
        volle_reisetage * tagegeld_volle_reisetage
    )

    # § 7 BRKG: Übernachtungsgeld
    uebernachtungsgeld_pro_nacht = 70.0  # EUR ohne Frühstück
    uebernachtungen_pro_jahr = reisetage_pro_jahr * uebernachtungen_pro_reisetag
    uebernachtungskosten_pro_jahr = uebernachtungen_pro_jahr * uebernachtungsgeld_pro_nacht

    # Wegstreckenentschädigung pro Jahr
    wegstreckenkosten_pro_jahr = reisetage_pro_jahr * wegstreckenkosten_pro_tag

    # Summe
    gesamtkosten_pro_jahr = (
        wegstreckenkosten_pro_jahr +
        tagegeldkosten_pro_jahr +
        uebernachtungskosten_pro_jahr
    )

    return {
        'wegstrecke': {
            'berechnung': f"{reisetage_pro_jahr} Reisetage × {entfernung_km} km × {satz_pro_km} €/km (max. {max_wegstrecke} €/Tag)",
            'pro_tag': round(wegstreckenkosten_pro_tag, 2),
            'pro_jahr': round(wegstreckenkosten_pro_jahr, 2),
        },
        'tagegeld': {
            'berechnung': f"{anreise_abreise_tage:.1f} Tage × {tagegeld_anreise_abreise} € + {volle_reisetage:.1f} Tage × {tagegeld_volle_reisetage} €",
            'anreise_abreise_tage': anreise_abreise_tage,
            'volle_reisetage': volle_reisetage,
            'pro_jahr': round(tagegeldkosten_pro_jahr, 2),
        },
        'uebernachtung': {
            'berechnung': f"{uebernachtungen_pro_jahr:.1f} Übernachtungen × {uebernachtungsgeld_pro_nacht} €",
            'uebernachtungen': uebernachtungen_pro_jahr,
            'pro_jahr': round(uebernachtungskosten_pro_jahr, 2),
        },
        'summe_pro_jahr': round(gesamtkosten_pro_jahr, 2),
        'beschreibung': beschreibung,
    }


def erkenne_reiseausloeser(optionsbeschreibung: str) -> bool:
    """
    Erkennt automatisch, ob eine Option Fahrtätigkeiten/Reisen enthält.

    Args:
        optionsbeschreibung: Text der Optionsbeschreibung (Kap. 3.1 oder 3.3)

    Returns:
        True, wenn Reisekosten wahrscheinlich anfallen
    """

    ausloeser = [
        # Fahrtätigkeiten
        'fahrt', 'dienstreise', 'reisen', 'mobile', 'unterwegs',
        'fahrzeug', 'dienstwagen', 'tour', 'einsatz',
        # Mehrere Standorte/Liegenschaften
        'standort', 'liegenschaft', 'bundesweit', 'dezentral',
        'mehrere orte', 'mehreren orten', 'verteilt',
        # Besuchstätigkeiten
        'besuch', 'inspektion', 'kontrolle', 'vor ort',
        'vor-ort', 'außendienst', 'außeneinsatz',
    ]

    beschreibung_lower = optionsbeschreibung.lower()
    erkannt = any(ausloeser_wort in beschreibung_lower for ausloeser_wort in ausloeser)

    return erkannt


def generiere_reisekostentext(reisekosten_dict: dict, entfernung_km: float, reisetage: int) -> str:
    """
    Generiert Fließtext für Kap. 3.3.x.3 (Personalkosten) mit Reisekosten.

    Returns:
        Formatted text snippet for inclusion in WU document
    """

    rk = reisekosten_dict

    # Datenschutz-Begründung für 400 km default
    datenschutz_hinweis = ""
    if entfernung_km == 400:
        datenschutz_hinweis = " Aus Gründen des Datenschutzes wird eine durchschnittliche Entfernung von 400 km angenommen."

    text = f"""Zu den Personalkosten hinzu kommen Reisekosten nach Bundesreisekostengesetz (BRKG).
Die monatlichen Reiseeinsätze erfordern durchschnittlich {reisetage} Reisetage pro Jahr mit einer Fahrtentfernung von {entfernung_km} km zwischen den Reiseorten.{datenschutz_hinweis}

Die Reisekosten setzen sich wie folgt zusammen:
- Wegstreckenentschädigung (§ 5 BRKG): {rk['wegstrecke']['berechnung']} = {rk['wegstrecke']['pro_jahr']:.2f} EUR/Jahr
- Tagegeld (§ 6 BRKG): {rk['tagegeld']['berechnung']} = {rk['tagegeld']['pro_jahr']:.2f} EUR/Jahr
- Übernachtungsgeld (§ 7 BRKG): {rk['uebernachtung']['berechnung']} = {rk['uebernachtung']['pro_jahr']:.2f} EUR/Jahr

Gesamtjährliche Reisekosten: {rk['summe_pro_jahr']:.2f} EUR"""

    return text
