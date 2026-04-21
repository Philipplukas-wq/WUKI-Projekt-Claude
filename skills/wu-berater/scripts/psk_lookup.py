"""
WU-Berater: PSK-Lookup (Personal- und Sachkosten, BMF 2024)
Liefert Vollkostensätze je Besoldungs-/Entgeltgruppe für Wirtschaftlichkeitsuntersuchungen.

Verwendung:
    from psk_lookup import vollkosten, stundensatz, vza_kosten

Quelle: BMF-Rundschreiben II A 3 – H 1012/00236/007/015, Stand 23. Juni 2025
        (PSK 2024, nachgeordnete Bundesbehörden)
"""

# ── PSK 2024 – Nachgeordnete Bundesbehörden ────────────────────────────────────
# Struktur: {Gruppe: (Brutto, Personalnebenkosten)}
# Alle Werte in EUR/Jahr
_ARBEITNEHMER = {
    'E1':  (None,   None),
    'E2':  (38090,  10275),
    'E3':  (40963,  10317),
    'E4':  (41636,  10606),
    'E5':  (44202,  11499),
    'E6':  (45527,  11800),
    'E7':  (48957,  13087),
    'E8':  (51354,  13577),
    'E9a': (54266,  13987),
    'E9b': (60027,  15241),
    'E9c': (59337,  14970),
    'E10': (62811,  15755),
    'E11': (68312,  16996),
    'E12': (77273,  18763),
    'E13': (71672,  17590),
    'E14': (83209,  19757),
    'E15': (96151,  21079),
}

_BEAMTE = {
    'A3':  (32959,  None),
    'A4':  (40802,  None),
    'A5e': (41992,  None),
    'A6e': (43223,  None),
    'A5m': (None,   None),
    'A6m': (40396,  None),
    'A7':  (40391,  None),
    'A8':  (48750,  None),
    'A9m': (54758,  None),
    'A9mZ':(60043,  None),
    'A9g': (46547,  None),
    'A10': (56982,  None),
    'A11': (66039,  None),
    'A12': (72234,  None),
    'A13g':(80441,  None),
    'A14': (83201,  None),
    'A15': (95558,  None),
    'A16': (106949, None),
}

# Gemeinkostenzuschlag nachgeordnete Bundesbehörden
GEMEINKOSTENSATZ = 0.294   # 29,4 %

# Sonstige Personalnebenkosten (Arbeitnehmer, pauschal, nachgeordnete Beh.)
_SONST_PNK_ARBEITNEHMER = 4150  # EUR/Jahr (Fürsorge 3.400 + UV 350 + Trennungsgeld 150 + Vermischt 250)

# Arbeitsstunden pro Monat (Arbeitnehmer, PSK 2024)
ARBEITSSTUNDEN_MONAT = 136
ARBEITSSTUNDEN_JAHR  = ARBEITSSTUNDEN_MONAT * 12  # 1.632


def _berechne_vollkosten(brutto: float, pnk: float, sonst_pnk: float = 0) -> float:
    """Vollkosten = (Brutto + PNK + sonstige PNK) × (1 + Gemeinkostensatz)"""
    personaleinzelkosten = brutto + (pnk or 0) + sonst_pnk
    return round(personaleinzelkosten * (1 + GEMEINKOSTENSATZ), 0)


def vollkosten(gruppe: str) -> float:
    """
    Gibt den Vollkostensatz (EUR/VZÄ/Jahr) für eine Besoldungs-/Entgeltgruppe zurück.

    :param gruppe: z.B. 'E5', 'A11', 'E9a'
    :return: Vollkosten in EUR/VZÄ/Jahr
    :raises ValueError: wenn Gruppe nicht bekannt
    """
    gruppe = gruppe.replace(' ', '')
    # Fallback: case-insensitive Suche (z. B. 'a9m' → 'A9m')
    alle_schluessel = list(_ARBEITNEHMER.keys()) + list(_BEAMTE.keys())
    if gruppe not in alle_schluessel:
        treffer = [k for k in alle_schluessel if k.upper() == gruppe.upper()]
        if treffer:
            gruppe = treffer[0]

    if gruppe in _ARBEITNEHMER:
        brutto, pnk = _ARBEITNEHMER[gruppe]
        if brutto is None:
            raise ValueError(f'Keine PSK-Daten für {gruppe} verfügbar.')
        return _berechne_vollkosten(brutto, pnk, _SONST_PNK_ARBEITNEHMER)

    if gruppe in _BEAMTE:
        brutto, _ = _BEAMTE[gruppe]
        if brutto is None:
            raise ValueError(f'Keine PSK-Daten für {gruppe} verfügbar.')
        # Für Beamte: Versorgung abhängig von Laufbahngruppe
        # Vereinfacht: mittlerer Dienst 29,3 %, gehobener 36,9 %, höherer 32,6 %
        if gruppe in ('A5m', 'A6m', 'A7', 'A8', 'A9m', 'A9mZ'):
            versorgung = 0.293
        elif gruppe in ('A9g', 'A10', 'A11', 'A12', 'A13g'):
            versorgung = 0.369
        else:
            versorgung = 0.326
        pnk_beamte = round(brutto * versorgung, 0)
        return _berechne_vollkosten(brutto, pnk_beamte)

    raise ValueError(f'Gruppe "{gruppe}" nicht in PSK-Tabelle. Bekannte Gruppen: '
                     f'{sorted(list(_ARBEITNEHMER.keys()) + list(_BEAMTE.keys()))}')


def stundensatz(gruppe: str) -> float:
    """
    Gibt den Vollkostenstundensatz (EUR/Std.) zurück.
    Basis: 136 Std./Monat × 12 = 1.632 Std./Jahr
    """
    return round(vollkosten(gruppe) / ARBEITSSTUNDEN_JAHR, 2)


def vza_kosten(gruppe: str, vza: float) -> float:
    """
    Gibt die Jahreskosten für einen anteiligen VZÄ-Einsatz zurück.

    :param gruppe: Besoldungs-/Entgeltgruppe
    :param vza:    Anteil VZÄ (z.B. 0.15 für 15 %)
    :return:       Jahreskosten in EUR (gerundet auf 100 €)
    """
    return round(vollkosten(gruppe) * vza / 100) * 100


def erklaere(gruppe: str) -> str:
    """Gibt eine lesbare Erklärung der PSK-Berechnung zurück."""
    vk = vollkosten(gruppe)
    sh = stundensatz(gruppe)
    return (
        f'PSK 2024 – {gruppe} (nachgeordnete Bundesbehörde):\n'
        f'  Vollkosten:   {vk:,.0f} €/VZÄ/Jahr\n'
        f'  Stundensatz:  {sh:.2f} €/Std.\n'
        f'  Basis:        {ARBEITSSTUNDEN_JAHR} Std./Jahr '
        f'({ARBEITSSTUNDEN_MONAT} Std./Monat × 12)'
    ).replace(',', '.')


# ── Schnellreferenz ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('PSK 2024 – Vollkostensätze (nachgeordnete Bundesbehörden)\n')
    for gruppe in ['E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9a', 'E10', 'E11', 'E12', 'E13']:
        try:
            print(f'  {gruppe:6s}: {vollkosten(gruppe):>10,.0f} EUR/VZA/Jahr  |  {stundensatz(gruppe):>7.2f} EUR/Std.'.replace(',', '.'))
        except ValueError:
            pass
    print()
    for gruppe in ['A7', 'A8', 'A9m', 'A10', 'A11', 'A12', 'A13g', 'A14']:
        try:
            print(f'  {gruppe:6s}: {vollkosten(gruppe):>10,.0f} EUR/VZA/Jahr  |  {stundensatz(gruppe):>7.2f} EUR/Std.'.replace(',', '.'))
        except ValueError:
            pass
