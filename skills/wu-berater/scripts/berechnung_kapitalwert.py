"""
WU-Berater: Kapitalwertberechnung gemäß § 7 BHO / AR A-2400/62

Berechnet Barwerte und Kapitalwerte für alle Optionen einer überjährigen WU
nach der Kapitalwertmethode mit Preissteigerung.

Verwendung:
    from berechnung_kapitalwert import berechne_kapitalwert, berechne_alle_optionen

Formel:
    KW = Investition + Σ(t=1..T) Kosten_t × (1+g)^t / (1+r)^t

    wobei:
        g = Preissteigerungsrate der Kostenart
        r = Kalkulationszinssatz
        T = Betrachtungszeitraum in Jahren
"""

from dataclasses import dataclass, field
from typing import List, Optional


# ── Standardwerte (aktuell, BMF April 2026) ────────────────────────────────────
ZINSSATZ_DEFAULT          = 0.012   # 1,2 %
PSR_PERSONAL              = 0.026   # 2,6 %
PSR_DIENSTLEISTUNGEN      = 0.024   # 2,4 %
PSR_GEBRAUCHSGUETER_HOCH  = 0.024   # 2,4 % (hohe Lebensdauer)
PSR_GEBRAUCHSGUETER_MITTEL = 0.027  # 2,7 %
PSR_VERBRAUCHSGUETER      = 0.025   # 2,5 %
PSR_ENERGIE               = 0.022   # 2,2 %
PSR_BAULEISTUNGEN         = 0.054   # 5,4 %


@dataclass
class Kostenposition:
    """Eine jährliche Kostenposition mit Preissteigerung."""
    bezeichnung: str
    jahresbetrag: float          # Betrag im ersten Jahr (Basisjahr)
    preissteigerung: float       # z.B. 0.026 für 2,6 %
    kategorie: str = ''          # z.B. 'Personal', 'Wartung', 'Leasing', 'Dienstleistung'


@dataclass
class Option:
    """Eine Bedarfsdeckungsoption mit ihren Kosten."""
    name: str
    investition: float = 0.0            # Einmalige Ausgabe in Jahr 0
    kostenpositionen: List[Kostenposition] = field(default_factory=list)
    residualwert: float = 0.0           # Restwert am Ende (als Einnahme, positiv)


def barwert_wachsende_annuitaet(
    jahresbetrag: float,
    preissteigerung: float,
    zinssatz: float,
    jahre: int
) -> float:
    """
    Berechnet den Barwert einer wachsenden Annuität.

    BW = C1 × Σ(t=1..T) ((1+g)/(1+r))^t

    :param jahresbetrag:   Ausgabe im ersten Jahr
    :param preissteigerung: Jährliche Preissteigerungsrate (z.B. 0.026)
    :param zinssatz:       Kalkulationszinssatz (z.B. 0.012)
    :param jahre:          Betrachtungszeitraum
    :return:               Barwert
    """
    if jahresbetrag == 0:
        return 0.0

    q = (1 + preissteigerung) / (1 + zinssatz)

    # Geometrische Summe: Σ(t=1..T) q^t = q × (q^T - 1) / (q - 1)
    if abs(q - 1) < 1e-10:
        # Sonderfall: q ≈ 1 (Zinssatz ≈ Preissteigerung)
        summe = jahre
    else:
        summe = q * (q ** jahre - 1) / (q - 1)

    return round(jahresbetrag * summe, 0)


def berechne_kapitalwert(
    option: Option,
    zinssatz: float = ZINSSATZ_DEFAULT,
    jahre: int = 10
) -> dict:
    """
    Berechnet den Kapitalwert einer Option.

    :param option:   Option-Objekt mit Investition und Kostenpositionen
    :param zinssatz: Kalkulationszinssatz
    :param jahre:    Betrachtungszeitraum
    :return:         Dict mit Einzelbarwerten und Gesamtkapitalwert
    """
    ergebnis = {
        'name':        option.name,
        'investition': option.investition,
        'positionen':  [],
        'summe_bw':    0.0,
        'kapitalwert': 0.0,
    }

    gesamt_bw = 0.0

    for pos in option.kostenpositionen:
        bw = barwert_wachsende_annuitaet(
            pos.jahresbetrag,
            pos.preissteigerung,
            zinssatz,
            jahre
        )
        ergebnis['positionen'].append({
            'bezeichnung':    pos.bezeichnung,
            'kategorie':      pos.kategorie,
            'jahresbetrag':   pos.jahresbetrag,
            'preissteigerung': pos.preissteigerung,
            'barwert':        bw,
        })
        gesamt_bw += bw

    # Residualwert abziehen (als Barwert diskontiert)
    residual_bw = 0.0
    if option.residualwert != 0:
        residual_bw = round(option.residualwert / (1 + zinssatz) ** jahre, 0)
        ergebnis['residualwert_bw'] = residual_bw

    ergebnis['summe_bw']    = round(gesamt_bw, 0)
    ergebnis['kapitalwert'] = round(option.investition + gesamt_bw - residual_bw, 0)

    return ergebnis


def berechne_alle_optionen(
    optionen: List[Option],
    zinssatz: float = ZINSSATZ_DEFAULT,
    jahre: int = 10
) -> List[dict]:
    """
    Berechnet die Kapitalwerte aller Optionen und gibt sie sortiert aus.

    :return: Liste von Ergebnis-Dicts, sortiert nach Kapitalwert (aufsteigend)
    """
    ergebnisse = [berechne_kapitalwert(opt, zinssatz, jahre) for opt in optionen]
    ergebnisse.sort(key=lambda x: x['kapitalwert'])
    return ergebnisse


def formatiere_eur(betrag: float) -> str:
    """Formatiert einen Betrag als EUR-String: 154.900 €"""
    return f"{betrag:,.0f} €".replace(',', '.')


def erstelle_tabellendaten(ergebnisse: List[dict]) -> dict:
    """
    Erzeugt die Tabellendaten für den Export in SKILL.md / wu_data['kap5'].

    :return: Dict mit 'headers' und 'rows' für export_wu_ueberjahrig.py
    """
    headers = ['Kostenart'] + [e['name'] for e in ergebnisse]
    rows = []

    # Alle Kostenarten sammeln
    alle_kategorien = []
    for e in ergebnisse:
        for pos in e['positionen']:
            if pos['bezeichnung'] not in alle_kategorien:
                alle_kategorien.append(pos['bezeichnung'])

    # Investitionszeilen
    inv_row = ['Investition (Jahr 0)']
    for e in ergebnisse:
        inv_row.append(formatiere_eur(e['investition']) if e['investition'] > 0 else '–')
    rows.append({'values': inv_row})

    # Jährliche Kostenzeilen
    for kat in alle_kategorien:
        zeile = [kat]
        for e in ergebnisse:
            gefunden = next((p for p in e['positionen'] if p['bezeichnung'] == kat), None)
            zeile.append(formatiere_eur(gefunden['jahresbetrag']) if gefunden else '–')
        rows.append({'values': zeile})

    # Trennzeile
    rows.append({'values': [''] * len(headers), 'separator': True})

    # Barwert-Zeilen
    for kat in alle_kategorien:
        zeile = [f'BW {kat}']
        for e in ergebnisse:
            gefunden = next((p for p in e['positionen'] if p['bezeichnung'] == kat), None)
            zeile.append(formatiere_eur(gefunden['barwert']) if gefunden else '–')
        rows.append({'values': zeile})

    # Kapitalwert-Summenzeile
    kw_zeile = ['Kapitalwert gesamt']
    for e in ergebnisse:
        kw_zeile.append(formatiere_eur(e['kapitalwert']))
    rows.append({'values': kw_zeile, 'summe': True})

    return {'headers': headers, 'rows': rows}


def erstelle_kw_uebersicht(ergebnisse: List[dict], risikowerte: dict = None) -> List[dict]:
    """
    Erzeugt die Übersichtstabelle (Entscheidungsvorschlag) für kap6_9.

    :param ergebnisse:  Ergebnisliste aus berechne_alle_optionen()
    :param risikowerte: Dict {option_name: risikowert_eur} (optional)
    :return: Liste für wu_data['kap6_9']['optionen_uebersicht']
    """
    if risikowerte is None:
        risikowerte = {}

    uebersicht = []
    for i, e in enumerate(ergebnisse):
        rv = risikowerte.get(e['name'], 0)
        kw_mit = e['kapitalwert'] + rv
        uebersicht.append({
            'name':           e['name'],
            'kw_ohne_risiko': formatiere_eur(e['kapitalwert']),
            'kw_mit_risiko':  formatiere_eur(kw_mit),
            'empfohlen':      (i == 0),   # günstigste Option
        })
    return uebersicht


# ── Sensitivitätsanalyse (Break-even) ─────────────────────────────────────────

def berechne_breakeven(
    option_basis: Option,
    option_vergleich: Option,
    variable_bezeichnung: str,
    variable_preissteigerung: float,
    zinssatz: float = ZINSSATZ_DEFAULT,
    jahre: int = 10,
    risikowert_basis: float = 0,
    risikowert_vergleich: float = 0,
) -> dict:
    """
    Berechnet den Break-even-Wert einer variablen Kostenposition.

    Fragestellung: Bei welchem Jahresbetrag der variablen Kostenposition in
    option_vergleich werden beide Optionen gleich wirtschaftlich?

    Methode:
        KW_basis + RW_basis = KW_vergleich_ohne_variable + variable_breakeven × PV-Faktor + RW_vergleich
        => variable_breakeven = (KW_basis + RW_basis - KW_vergleich_ohne_variable - RW_vergleich) / PV-Faktor

    :param option_basis:           Die wirtschaftlichere Option (z.B. Option 1: Kauf)
    :param option_vergleich:       Die zu vergleichende Option (z.B. Option 2: Leasing)
    :param variable_bezeichnung:   Name der variablen Kostenposition (z.B. 'Leasing')
    :param variable_preissteigerung: PSR der variablen Kostenposition
    :param risikowert_basis:       Monetärer Risikowert Option Basis
    :param risikowert_vergleich:   Monetärer Risikowert Option Vergleich
    :return: Dict mit Break-even-Jahresbetrag, aktueller Wert, Abweichung in % und Bewertung
    """
    # KW Basis (vollständig, inkl. Risiko)
    erg_basis = berechne_kapitalwert(option_basis, zinssatz, jahre)
    kw_basis  = erg_basis['kapitalwert'] + risikowert_basis

    # KW Vergleich OHNE die variable Kostenposition (inkl. Risiko)
    option_ohne_variable = Option(
        name=option_vergleich.name,
        investition=option_vergleich.investition,
        kostenpositionen=[
            p for p in option_vergleich.kostenpositionen
            if p.bezeichnung != variable_bezeichnung
        ],
        residualwert=option_vergleich.residualwert,
    )
    erg_ohne = berechne_kapitalwert(option_ohne_variable, zinssatz, jahre)
    kw_ohne  = erg_ohne['kapitalwert'] + risikowert_vergleich

    # PV-Faktor der variablen Kostenposition (Σ für eine 1-EUR-wachsende Annuität)
    pv_faktor = barwert_wachsende_annuitaet(1.0, variable_preissteigerung, zinssatz, jahre)

    # Break-even Jahresbetrag
    differenz = kw_basis - kw_ohne
    if abs(pv_faktor) < 1e-10:
        return {'fehler': 'PV-Faktor zu klein, Berechnung nicht möglich.'}

    breakeven_jahresbetrag = round(differenz / pv_faktor, 0)

    # Aktueller Wert der variablen Kostenposition
    aktueller_wert = next(
        (p.jahresbetrag for p in option_vergleich.kostenpositionen
         if p.bezeichnung == variable_bezeichnung),
        None
    )

    abweichung_pct = None
    if aktueller_wert and aktueller_wert != 0:
        abweichung_pct = round((breakeven_jahresbetrag - aktueller_wert) / aktueller_wert * 100, 1)

    # Bewertung: realistisch oder nicht?
    bewertung = _bewerte_breakeven(abweichung_pct)

    return {
        'option_basis':           option_basis.name,
        'option_vergleich':       option_vergleich.name,
        'variable':               variable_bezeichnung,
        'breakeven_jahresbetrag': breakeven_jahresbetrag,
        'aktueller_wert':         aktueller_wert,
        'abweichung_pct':         abweichung_pct,
        'bewertung':              bewertung,
        'pv_faktor':              round(pv_faktor, 4),
    }


def _bewerte_breakeven(abweichung_pct: float) -> str:
    """Bewertet ob ein Break-even-Szenario realistisch ist."""
    if abweichung_pct is None:
        return 'nicht bewertbar'
    if abweichung_pct >= 0:
        return ('unrealistisch — der aktuelle Wert liegt bereits unter dem Break-even; '
                'Option ist schon jetzt nicht günstiger')
    abw = abs(abweichung_pct)
    if abw <= 5:
        return 'kritisch — sehr geringe Marge, Reihenfolge könnte sich schnell ändern'
    elif abw <= 20:
        return 'möglich — Szenario ist unter bestimmten Marktbedingungen denkbar'
    elif abw <= 40:
        return 'unwahrscheinlich — würde erhebliche Marktveränderung erfordern'
    else:
        return 'unrealistisch — Marktveränderung dieser Größenordnung nicht zu erwarten'


def erstelle_sensitivitaet(
    optionen: List[Option],
    ergebnisse: List[dict],
    risikowerte: dict = None,
    zinssatz: float = ZINSSATZ_DEFAULT,
    jahre: int = 10,
) -> str:
    """
    Erstellt den vollständigen Sensitivitätsanalyse-Text für Kapitel 7.

    Vergleicht die beste Option jeweils gegen alle anderen und berechnet
    automatisch den Break-even für die wichtigste variable Kostenposition.

    :param optionen:    Liste der Option-Objekte
    :param ergebnisse:  Ergebnisliste aus berechne_alle_optionen()
    :param risikowerte: Dict {option_name: risikowert_eur}
    :return:            Fertig formatierter Text für kap6_9['sensitivitaet']
    """
    if risikowerte is None:
        risikowerte = {}

    if len(ergebnisse) < 2:
        return 'Sensitivitätsanalyse nicht anwendbar (weniger als 2 Optionen).'

    beste_opt_name = ergebnisse[0]['name']
    beste_opt      = next(o for o in optionen if o.name == beste_opt_name)
    rv_beste       = risikowerte.get(beste_opt_name, 0)

    absaetze = []

    for e in ergebnisse[1:]:
        vergleich_opt = next(o for o in optionen if o.name == e['name'])
        rv_vergleich  = risikowerte.get(e['name'], 0)

        # Variable Kostenposition bestimmen: die größte unique Kostenposition in der Vergleichsoption
        basis_bezeichnungen = {p.bezeichnung for p in beste_opt.kostenpositionen}
        unique_positionen = [
            p for p in vergleich_opt.kostenpositionen
            if p.bezeichnung not in basis_bezeichnungen
        ]

        if not unique_positionen:
            # Fallback: größte Kostenposition verwenden
            unique_positionen = sorted(vergleich_opt.kostenpositionen,
                                       key=lambda p: p.jahresbetrag, reverse=True)

        if not unique_positionen:
            continue

        variable = max(unique_positionen, key=lambda p: p.jahresbetrag)

        be = berechne_breakeven(
            beste_opt, vergleich_opt,
            variable.bezeichnung, variable.preissteigerung,
            zinssatz, jahre,
            rv_beste, rv_vergleich,
        )

        if 'fehler' in be:
            continue

        kw_beste    = ergebnisse[0]['kapitalwert'] + rv_beste
        kw_vergleich = e['kapitalwert'] + rv_vergleich
        differenz   = kw_vergleich - kw_beste

        absatz = (
            f'Break-even {beste_opt_name} vs. {e["name"]}:\n'
            f'Kapitalwertdifferenz: {formatiere_eur(kw_vergleich)} − '
            f'{formatiere_eur(kw_beste)} = {formatiere_eur(differenz)}.\n'
            f'Damit {e["name"]} gleich wirtschaftlich wie {beste_opt_name} wird, '
            f'müsste {variable.bezeichnung} von '
            f'{formatiere_eur(variable.jahresbetrag)}/Jahr auf '
            f'ca. {formatiere_eur(be["breakeven_jahresbetrag"])}/Jahr sinken '
            f'({be["abweichung_pct"]:+.1f} %). '
            f'Bewertung: {be["bewertung"]}.'
        )
        absaetze.append(absatz)

    kw_beste_mit_risiko = ergebnisse[0]['kapitalwert'] + rv_beste
    # Gesamtfazit
    alle_unrealistisch = all(
        abs(b['abweichung_pct'] or 0) > 20
        for b in [
            berechne_breakeven(
                beste_opt,
                next(o for o in optionen if o.name == e['name']),
                max([p for p in next(o for o in optionen if o.name == e['name']).kostenpositionen
                     if p.bezeichnung not in {p2.bezeichnung for p2 in beste_opt.kostenpositionen}],
                    key=lambda p: p.jahresbetrag,
                    default=next(o for o in optionen if o.name == e['name']).kostenpositionen[0]
                ).bezeichnung,
                max([p for p in next(o for o in optionen if o.name == e['name']).kostenpositionen
                     if p.bezeichnung not in {p2.bezeichnung for p2 in beste_opt.kostenpositionen}],
                    key=lambda p: p.jahresbetrag,
                    default=next(o for o in optionen if o.name == e['name']).kostenpositionen[0]
                ).preissteigerung,
                zinssatz, jahre,
                risikowerte.get(beste_opt_name, 0),
                risikowerte.get(e['name'], 0),
            )
            for e in ergebnisse[1:]
        ]
    )

    fazit = (
        f'\nErgebnis: Die Vorteilhaftigkeit von {beste_opt_name} '
        f'(Kapitalwert {formatiere_eur(kw_beste_mit_risiko)} inkl. Risiko) ist '
        f'{"unter realistischen Marktbedingungen robust. Eine Änderung der Rangfolge ist nicht zu erwarten." if alle_unrealistisch else "eingeschränkt robust. Die Rangfolge könnte sich unter veränderten Marktbedingungen ändern — dies sollte bei der Entscheidung berücksichtigt werden."}'
    )
    absaetze.append(fazit)

    return '\n\n'.join(absaetze)


# ── Beispielaufruf ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    optionen = [
        Option(
            name='Option 1: Kauf',
            investition=25000,
            kostenpositionen=[
                Kostenposition('Personal', 10800, PSR_PERSONAL, 'Personal'),
                Kostenposition('Wartung',   1200, PSR_DIENSTLEISTUNGEN, 'Wartung'),
            ]
        ),
        Option(
            name='Option 2: Leasing',
            kostenpositionen=[
                Kostenposition('Personal', 10800, PSR_PERSONAL, 'Personal'),
                Kostenposition('Leasing',   5500, PSR_DIENSTLEISTUNGEN, 'Leasing'),
            ]
        ),
        Option(
            name='Option 3: Dienstleistung',
            kostenpositionen=[
                Kostenposition('Personal',       3600, PSR_PERSONAL, 'Personal'),
                Kostenposition('Dienstleistung', 45000, PSR_DIENSTLEISTUNGEN, 'Dienstleistung'),
            ]
        ),
    ]

    ergebnisse = berechne_alle_optionen(optionen, zinssatz=0.012, jahre=10)

    print('\n=== Kapitalwertberechnung ===')
    for e in ergebnisse:
        print(f"\n{e['name']}")
        print(f"  Investition:   {formatiere_eur(e['investition'])}")
        for pos in e['positionen']:
            print(f"  BW {pos['bezeichnung']:20s}: {formatiere_eur(pos['barwert'])}")
        print(f"  Kapitalwert:   {formatiere_eur(e['kapitalwert'])}")

    risikowerte = {
        'Option 1: Kauf':          1800,
        'Option 2: Leasing':       1000,
        'Option 3: Dienstleistung': 20250,
    }
    uebersicht = erstelle_kw_uebersicht(ergebnisse, risikowerte)
    print('\n=== Kapitalwertübersicht (mit Risiko) ===')
    for u in uebersicht:
        stern = ' ← EMPFOHLEN' if u['empfohlen'] else ''
        print(f"  {u['name']:40s}  ohne Risiko: {u['kw_ohne_risiko']:>12}  mit Risiko: {u['kw_mit_risiko']:>12}{stern}")
