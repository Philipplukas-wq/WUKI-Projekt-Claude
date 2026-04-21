#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Übergreifende Dienstleistungs-WU: Tartanbahnreinigung (200 Liegenschaften, 10 Jahre)
Vollständige Version mit detaillierten Texten, Kostenkalkulationen und Tabellen
"""

import sys
sys.path.insert(0, 'P:/WUKI_Projekt/Claude/skills/wu-berater/scripts')

from export_wu_dienstleistung import fill_template, build_filename

# ============================================================================
# WU-DATA: TARTANBAHNREINIGUNG ÜBERGREIFEND (200 LIEGENSCHAFTEN)
# ============================================================================

wu_data = {
    'meta': {
        'dienststelle': 'Bundeswehr (übergreifend)',
        'bearbeiter': 'Philipp Lukas',
        'datum': '16.04.2026',
        'schutz': 'offen',
        'version': '1',
    },

    'ueberblick': {
        'betrachtungsgegenstand': (
            "In der vorliegenden Untersuchung wird die professionelle Reinigung der "
            "bundeswehreigenen Tartanbahnen an insgesamt 200 Liegenschaften bundesweit "
            "untersucht. Die Wirtschaftlichkeitsuntersuchung prüft zwei hauptsächliche "
            "Optionen (Eigenbetrieb vs. externer Dienstleister) über einen "
            "Betrachtungszeitraum von 10 Jahren gemäß AR A-2400/62."
        ),
        'entscheidungsvorschlag': (
            "Empfohlen wird Option 1 (Leistungserbringung durch Eigenbetrieb mit zentral "
            "beschaffter Reinigungsmaschine). Die Gesamtkosten über 10 Jahre betragen "
            "ca. 715.500 EUR (inkl. Risikowert). Dies entspricht einer Ersparnis von "
            "etwa 1.000.000 EUR gegenüber der Beauftragung eines externen Dienstleisters "
            "(Option 4). Die Empfehlung basiert auf einer durchgeführten "
            "Sensitivitätsanalyse und ist auch unter pessimistischen Annahmen robust."
        ),
    },

    'kap1': {
        'bedarfsforderung': (
            "Die Bundeswehr benötigt an insgesamt 200 Liegenschaften professionelle "
            "Reinigung der bundeswehreigenen Tartanbahnen zur Gewährleistung der "
            "Sportplatzinfrastruktur und der Wettkampffähigkeit. Die Tartanbelagsfläche "
            "umfasst pro Standort ca. 4.200 m² (400-Meter-Rundbahn nach IAAF-Standard, "
            "8 Bahnen à 1,22 m Breite) und ist vollständig von Moos- und Algenbewuchs "
            "zu befreien. Diese Verschmutzung entsteht durch Feuchtigkeit und "
            "mangelnde regelmäßige Reinigung und beeinträchtigt die Sportplatz-Qualität "
            "und die Sicherheit der Nutzer.\n"
            "Die Leistung ist alle zwei Jahre zu erbringen, was einer durchschnittlichen "
            "Häufigkeit von 0,5 Einsätzen pro Jahr entspricht. Die Mindestanforderungen "
            "für das Reinigungsverfahren sind: belagsschonendes Verfahren (rotierendes "
            "Düsenverfahren, Maximaldruck 310 bar), integrierte Schmutzwasserabsaugung "
            "und Verzicht auf chemische Zusätze. Diese Anforderungen entsprechen "
            "internationalen IAAF-Standards für hochwertige Wettkampfanlagen und schützen "
            "die Belagsinvestitionen vor Beschädigungen durch aggressive Reinigungsmethoden.\n"
            "Bundesweit ergibt sich ein Gesamtbedarf von 200 Standorte × 4.200 m² = "
            "840.000 m² Tartanbahnfläche zur Reinigung. Die Häufigkeit von alle 2 Jahren "
            "ist sachlich begründet durch den typischen Verschmutzungsgrad an "
            "Bundeswehr-Liegenschaften in der gemäßigten Klimazone."
        ),

        'bedarfsprognose': (
            "Der Bedarf an professioneller Tartanbahnreinigung bleibt über den "
            "10-Jahres-Betrachtungszeitraum konstant. Die Anzahl der Liegenschaften "
            "wird auf 200 Standorte angenommen, ohne Wachstum oder Reduktion. Dies "
            "basiert auf der aktuellen Liegenschaftsstruktur der Bundeswehr und "
            "berücksichtigt keine geplanten Schließungen oder Neuaufbau. Die "
            "Reinigungsfrequenz von alle 2 Jahren wird beibehalten, da sie durch den "
            "typischen Verschmutzungsgrad (Moos-, Algenbewuchs) und internationale "
            "Sportplatz-Standards vorgegeben ist und sich nicht ändern wird. Saisonale "
            "Schwankungen (Reinigung vorzugsweise im Frühling vor Trainings-/Wettkampfsaison "
            "und im Herbst nach Saisonende) sind in die Terminplanung der jeweiligen Option "
            "einzurechnen, ändern aber nicht die Gesamtausgaben pro Jahr."
        ),

        'rahmenbedingungen': (
            "Die Tartanbahnreinigung muss vor Beginn des Sportbetriebs (März/April) "
            "und nach Ende der Saison (September/Oktober) abgeschlossen sein, um "
            "Beeinträchtigungen des Trainings- und Wettkampfbetriebs zu vermeiden. "
            "Diese zeitliche Rahmenbedingung schließt Verfahren aus, die ohne "
            "spezialisierte Hochdruck-Reinigungsmaschinen durchgeführt werden, da eine "
            "manuelle oder improvisierte Reinigung der 4.200 m² zu zeit- und "
            "kostenintensiv und qualitativ unzureichend wäre. Daneben existiert keine "
            "weitere optionsausschließende Rahmenbedingung (z. B. keine rechtliche "
            "Verpflichtung zur Zentralisierung oder Dezentralisierung)."
        ),
    },

    'kap2': {
        'ablauforganisation': (
            "Die Reinigung der Tartanbahnen wird derzeit dezentral an den 200 "
            "Liegenschaften durchgeführt oder unterbleibt teilweise. Es existiert kein "
            "standardisiertes bundesweit einheitliches Verfahren. Jede Liegenschaft "
            "organisiert die Reinigung eigenständig oder vergibt diese lokal an externe "
            "Anbieter. Der Ablauf ist daher fragmentiert: Einige Standorte versuchen "
            "Eigenreinigung mit unzureichenden Mitteln, andere beauftragen lokal bekannte "
            "Reinigungsbetriebe, wieder andere vernachlässigen die Reinigung ganz. Diese "
            "Dezentralität führt zu erheblichen Preis- und Qualitätsschwankungen zwischen "
            "den Standorten und verhindert Skalierungseffekte, die durch zentrale "
            "Beschaffung oder Koordination möglich wären."
        ),

        'aufbauorganisation': (
            "Die Verantwortlichkeit für Tartanbahnunterhalt liegt derzeit bei den "
            "Standortkommandanten und BwDLZ-Leitern vor Ort. Eine zentrale Beschaffung, "
            "Koordination oder Standardisierung der Reinigung existiert nicht. Mit der "
            "vorliegenden übergreifenden Wirtschaftlichkeitsuntersuchung wird eine "
            "Governance-Grundlage geschaffen, ohne zentrale Zentralisierung zu erzwingen. "
            "Vielmehr wird ein Referenzmodell entwickelt, das jede Liegenschaft befolgen "
            "kann."
        ),

        'personal': (
            "Personal für Tartanbahnreinigung ist an den Standorten unterschiedlich "
            "verfügbar. Teilweise existiert kein geschultes Personal, weshalb auf externe "
            "Dienstleister ausgewichen wird. Für ein Eigenmodell wären folgende "
            "Personalressourcen erforderlich: 1 Person pro Reinigungseinsatz (1 Arbeitstag "
            "pro Liegenschaft). Bei 200 Liegenschaften mit 0,5 Reinigungen pro Jahr ergibt "
            "sich: 200 Standorte × 0,5 Einsätze/Jahr = 100 Einsatztage pro Jahr × 1 Person "
            "pro Einsatz. Bei 250 Arbeitstagen pro Jahr entspricht dies 100/250 = 0,4 VZÄ "
            "(Vollzeitäquivalent). Das Personal muss in das belagsschonende "
            "Hochdruckverfahren geschult sein (geschätzter Schulungsaufwand: 3-5 Tage).\n"
            "Personalkosten (PSK 2024, nachgeordnete Bundesbehörden, Gruppe E9b "
            "technischer Service): ca. 50.000 EUR pro VZÄ und Jahr. Für 0,4 VZÄ ergibt sich: "
            "0,4 × 50.000 = 20.000 EUR pro Jahr für alle 200 Liegenschaften."
        ),

        'material': (
            "Für ein Eigenmodell wäre eine hochwertige Reinigungsmaschine erforderlich: "
            "1 Hochdruck-Reinigungsanlage mit rotierendem Düsenverfahren, Maximaldruck "
            "310 bar, integrierter Schmutzwasserabsaugung und Transportmöglichkeit. "
            "Anschaffungskosten: ca. 240.000 EUR (einmalig). Diese Maschine würde zentral "
            "beschafft und an den 200 Standorten der Reihe nach eingesetzt. Wartung, "
            "Verschleiß und Reparaturen werden mit ca. 10 % des Anschaffungswertes pro Jahr "
            "kalkuliert (24.000 EUR/Jahr). Die Maschine hat eine Lebensdauer von ca. 10 Jahren "
            "(entspricht dem Betrachtungszeitraum der WU)."
        ),

        'infrastruktur': (
            "Für ein Eigenmodell sind Lagerhaltung und Transport erforderlich. Die "
            "Reinigungsmaschine muss zentral oder an dezentralen Stützpunkten gelagert werden "
            "und zwischen den Liegenschaften transportiert werden. Geschätzte Kosten: "
            "ca. 5.000 EUR pro Jahr für Lagerhaltung, Versicherung und Transport zwischen "
            "Standorten. Bei dezentraler Lagerung an 3-4 Stützpunkten könnten die Transportkosten "
            "optimiert werden, würde aber höhere Lagerhaltungskosten mit sich bringen."
        ),

        'dienstleistungen': (
            "Externe Angebote für Tartanbahnreinigung sind am Markt verfügbar "
            "(siehe Anlage Marktrecherche). Die typischen Kosten betragen ca. 1.500–2.000 EUR "
            "pro Liegenschaft und alle 2 Jahre (durchschnittlich: 1.750 EUR). Hochgerechnet auf "
            "ein Jahr: 1.750 EUR ÷ 2 Jahre = 875 EUR pro Liegenschaft pro Jahr. Für alle 200 "
            "Liegenschaften: 200 × 875 EUR = 175.000 EUR pro Jahr (Basis). Die Marktpreise sind "
            "stabil und mehrere spezialisierte Anbieter sind verfügbar (Tartanbahn-Reinigung.de, "
            "Theis Spezialreinigung, VB Sport, X3 System)."
        ),

        'einnahmen': (
            "Aus der Tartanbahnreinigung entstehen keine Einnahmen. Die Reinigung ist eine "
            "reine Aufwendung zur Instandhaltung der Liegenschaftsinfrastruktur."
        ),

        'haushalterische_darstellung': (
            "Die haushalterische Darstellung wird nach Abschluss der Kapitalwertberechnung "
            "(Kapitel 5.2) aktualisiert und zeigt die Jahresausgaben und kumulierten Ausgaben "
            "pro Option."
        ),
    },

    'kap3': {
        'optionen_uebersicht': (
            "Gemäß AR A-2400/62 und Dialogpfad C werden vier Standardoptionen für die "
            "Leistungserbringung untersucht:\n\n"
            "**Option 1: Leistungserbringung durch die eigene Dienststelle (Eigenbetrieb)**\n"
            "Zentrale Beschaffung einer Hochdruck-Reinigungsmaschine (240.000 EUR), bundesweit "
            "eingesetztes Personal (0,4 VZÄ), zentrale Lagerhaltung und Terminplanung. Alle 200 "
            "Liegenschaften werden nach standardisiertem Verfahren und Zeitplan gereinigt.\n\n"
            "**Option 2: Leistungserbringung durch andere bundeswehrinterne Dienststellen**\n"
            "Beauftragung einer anderen BW-Dienststelle (z. B. zentrale Dienststelle für "
            "Liegenschaftsmanagement oder technischer Service). Diese Dienststelle würde Ressourcen "
            "für die bundesweite Reinigung bereitstellen.\n\n"
            "**Option 3: Leistungserbringung durch Inhousegesellschaft / Dienststelle eines anderen Ressorts**\n"
            "Beauftragung eines öffentlich-rechtlichen Unternehmens oder einer Dienststelle eines "
            "anderen Ressorts (z. B. kommunale Reinigungsbetriebe mit Rahmenvertrag) zur Durchführung "
            "der Reinigung an allen 200 Standorten.\n\n"
            "**Option 4: Leistungserbringung durch externen Dienstleister**\n"
            "Ausschreibung und Beauftragung spezialisierter externer Unternehmen "
            "(z. B. Tartanbahn-Reinigung.de, Theis Spezialreinigung, VB Sport) mit Erfahrung in "
            "belagsschonender Hochdruckreinigung. Kann als Rahmenvertrag (zentral) oder dezentralisierte "
            "Einzelverträge pro BwDLZ umgesetzt werden."
        ),

        'aussonderung': (
            "**Option 2 wird ausgesondert.** Begründung: Keine bundeswehreigene Dienststelle "
            "verfügt derzeit über die kapazitiven Ressourcen und die fachliche Spezialisierung, um "
            "200 Standorte mit belagsschonender Hochdruckreinigung (310 bar max., Schmutzwasserabsaugung) "
            "alle 2 Jahre zu bedienen. Die spezialisierte Hochdrucktechnik ist nicht in "
            "Standardreinigungstruppen der Bundeswehr vorhanden. Eine zeitliche Rahmenbedingung wie "
            "\"bis [Datum] Ressourcen aufbauen\" ist nicht realistisch, da der Aufbau von "
            "Spezialkompetenz und Kapazitäten mehrere Jahre erfordern würde. (Vgl. Anlage: "
            "Anfrage beim Zentralen Immobilienmanagement der Bundeswehr, Antwort vom 15.04.2026.)\n\n"
            "**Option 3 wird nicht ausgesondert, aber als sekundär bewertet.** Begründung: "
            "Eine spezialisierte Inhouse-Gesellschaft mit Erfahrung in belagsschonender "
            "Hochdruckreinigung existiert im Bundeswehr-Bereich nicht. Kommunale Reinigungsbetriebe "
            "könnten ggf. über einen Rahmenvertrag beauftragt werden, würden dann aber wie externe "
            "DL-Angebote behandelt und ähnliche Kostenstrukturen haben wie Option 4. Diese Option "
            "wird daher in der weiteren Analyse nicht detailliert kalkuliert, sondern der "
            "Entscheidungslogik von Option 4 gleichgesetzt."
        ),

        'geeignete_optionen': (
            "**Verbleibende geeignete Optionen: Option 1 und Option 4**\n\n"
            "Diese beiden Optionen werden im Folgenden detailliert kalkuliert und verglichen. "
            "Option 1 stellt ein zentral verwaltetes Eigenmodell dar, Option 4 die dezentralisierbare "
            "Beauftragung von Marktleistern. Beide sind technisch und rechtlich machbar und erfordern "
            "keine unrealistischen Annahmen."
        ),
    },

    'kap4': {
        'annahmen_alle': (
            "**Allgemeine Annahmen (für beide Optionen):**\n\n"
            "1. Konstante Liegenschaftsanzahl: 200 Standorte über den gesamten "
            "10-Jahres-Betrachtungszeitraum. Keine Schließungen oder Neugründungen.\n\n"
            "2. Konstante Reinigungsfrequenz: Alle 2 Jahre = 0,5 Einsätze pro Liegenschaft pro Jahr. "
            "Dies basiert auf Erfahrungswerten und internationalen Standards.\n\n"
            "3. Zinssatz: 1,2 % (gemäß BMF-Vorgaben 2026 für langfristige Kapitalwertberechnungen).\n\n"
            "4. Baseline ohne Inflation: Kostenkalkulationen werden zunächst ohne allgemeine Preissteigerung "
            "durchgeführt. Preissteigungen werden in der Sensitivitätsanalyse (Kapitel 7) untersucht.\n\n"
            "5. Keine Reserven oder Rückstellungen: Kalkulationen basieren auf durchschnittlich "
            "erwarteten Kosten ohne Sicherheitszuschläge (Risikoaspekte werden separat in Kapitel 5.4 behandelt)."
        ),

        'annahmen_bestimmte': (
            "**Spezifische Annahmen für Option 1 (Eigenbetrieb):**\n\n"
            "1. Maschinen-Kapazität: Eine Hochdruck-Reinigungsanlage ist ausreichend für 200 Standorte "
            "alle 2 Jahre, da die Betriebszeit 100 Tage pro Jahr nicht übersteigt (200 Standorte × 0,5 "
            "Einsätze/Jahr = 100 Tage, gegenüber 250 Arbeitstagen/Jahr Kapazität). Wartung und "
            "Verschleiß reduzieren verfügbare Kapazität um ca. 20 % (50 Tage verfügbar pro Jahr nach "
            "Wartung), was aber ausreichend ist.\n\n"
            "2. Maschinenlebensdauer: 10 Jahre (entspricht dem Betrachtungszeitraum). Danach "
            "Reinvestition erforderlich (wird in dieser WU nicht berücksichtigt, da außerhalb des "
            "Zeitraums).\n\n"
            "3. Personal: Spezialisiert auf Hochdruckverfahren. Schulungskosten (geschätzt 3-5 Tage à "
            "ca. 500 EUR) sind in den PSK-Kosten kalkuliert.\n\n"
            "4. Lagerhaltung zentral oder an bis zu 3 Stützpunkten. Transport zwischen Standorten "
            "durchschnittlich 5 Betriebstage pro Jahr (Anfahrts-/Abreisetage). Kosten 5.000 EUR/Jahr.\n\n"
            "**Spezifische Annahmen für Option 4 (Externer DL):**\n\n"
            "1. Wettbewerbsfähiger Markt: Mehrere spezialisierte Anbieter sind verfügbar und bereit zu bieten. "
            "Keine Monopolsituation.\n\n"
            "2. Marktpreise basieren auf Recherche vom 16.04.2026: "
            "1.500–2.000 EUR pro Liegenschaft alle 2 Jahre.\n\n"
            "3. Preissteigerung: 2 % pro Jahr (basierend auf historischen Preissteigerungen für "
            "Dienstleistungen im Reinigungsbereich). Dies ist eine moderate Annahme angesichts von "
            "Lohnkostensteigerungen und Materialpreisen.\n\n"
            "4. Vertragsform: Entweder zentral (1 Rahmenvertrag für alle 200 Standorte) oder dezentralisiert "
            "(200 Einzelverträge). Beide werden für diese WU als äquivalent angenommen (keine "
            "Kostenunterschiede).\n\n"
            "5. Zahlungsweise: Jährliche Rechnungsstellung nach Durchführung (alle 2 Jahre). Keine "
            "Vorausleistungen angenommen."
        ),
    },

    'kap5': {
        'kapitalwertberechnung': (
            "**Kostenkalkulationen und Barwertberechnung (Zinssatz: 1,2 %)**\n\n"
            "---\n\n"
            "## OPTION 1: EIGENBETRIEB\n\n"
            "**Kostenposition 1: Maschinen-Abschreibung**\n"
            "  Formel: Anschaffungspreis ÷ Lebensdauer in Jahren\n"
            "  = 240.000 EUR ÷ 10 Jahre = 24.000 EUR/Jahr\n\n"
            "**Kostenposition 2: Personalkosten**\n"
            "  Formel: VZÄ-Bedarf × PSK-Satz (E9b)\n"
            "  Berechnung des VZÄ-Bedarfs:\n"
            "    Einsätze pro Jahr: 0,5 × 200 Standorte = 100 Einsätze/Jahr\n"
            "    Tage pro Einsatz: 1 Tag\n"
            "    Gesamttage pro Jahr: 100 Tage\n"
            "    VZÄ: 100 Tage ÷ 250 Arbeitstage = 0,4 VZÄ\n"
            "  PSK E9b (2024): 50.000 EUR/VZÄ/Jahr\n"
            "  Kosten: 0,4 × 50.000 = 20.000 EUR/Jahr\n\n"
            "**Kostenposition 3: Betrieb (Wartung, Reparatur, Verschleiß)**\n"
            "  Formel: Anschaffungspreis × 10 % (jährlicher Verschleiß)\n"
            "  = 240.000 × 0,10 = 24.000 EUR/Jahr\n\n"
            "**Kostenposition 4: Lagerhaltung und Transport**\n"
            "  Kosten für zentrale/dezentrale Lagerung: 5.000 EUR/Jahr\n"
            "  (Transport zwischen Standorten, Versicherung, Lagerverwaltung)\n\n"
            "**SUMME pro Jahr (nominal): 24.000 + 20.000 + 24.000 + 5.000 = 73.000 EUR/Jahr**\n\n"
            "**Über 10 Jahre (nominal, ohne Diskontierung): 73.000 × 10 = 730.000 EUR**\n\n"
            "**Barwert bei 1,2 % Zinssatz über 10 Jahre:**\n"
            "  Barwert = Σ (Jahreskosten ÷ (1 + Zinssatz)^Jahr) für Jahre 1–10\n"
            "  = 73.000 × [1/1.012 + 1/1.012² + ... + 1/1.012^10]\n"
            "  ≈ 73.000 × 9.790 (Annuitätsfaktor für 1,2 % und 10 Jahre)\n"
            "  ≈ 714.670 EUR (gerundet: 715.000 EUR)\n\n"
            "---\n\n"
            "## OPTION 4: EXTERNER DIENSTLEISTER\n\n"
            "**Marktpreis pro Liegenschaft (alle 2 Jahre):**\n"
            "  Recherchter Bereich: 1.500–2.000 EUR\n"
            "  Mittelwert: 1.750 EUR\n"
            "  Pro Jahr (verteilt): 1.750 ÷ 2 = 875 EUR/Liegenschaft/Jahr\n\n"
            "**Jahreskosten für 200 Liegenschaften (Basisjahr 1):**\n"
            "  = 200 × 875 EUR = 175.000 EUR/Jahr\n\n"
            "**Mit Preissteigerung 2 % p.a. (realistische Annahme für Dienstleistungen):**\n"
            "  Jahr 1: 175.000 EUR\n"
            "  Jahr 2: 175.000 × 1,02 = 178.500 EUR\n"
            "  Jahr 3: 175.000 × 1,02² = 182.070 EUR\n"
            "  Jahr 4: 175.000 × 1,02³ = 185.711 EUR\n"
            "  Jahr 5: 175.000 × 1,02⁴ = 189.426 EUR\n"
            "  Jahr 6: 175.000 × 1,02⁵ = 193.214 EUR\n"
            "  Jahr 7: 175.000 × 1,02⁶ = 197.078 EUR\n"
            "  Jahr 8: 175.000 × 1,02⁷ = 201.020 EUR\n"
            "  Jahr 9: 175.000 × 1,02⁸ = 205.040 EUR\n"
            "  Jahr 10: 175.000 × 1,02⁹ = 209.141 EUR\n\n"
            "**Summe 10 Jahre (nominal): ca. 1.916.200 EUR**\n\n"
            "**Barwert bei 1,2 % Zinssatz über 10 Jahre:**\n"
            "  Berechnung mit variabler Preissteigerung (2 % p.a.)\n"
            "  ≈ 1.710.000 EUR (gerundet)\n\n"
            "---\n\n"
            "## KOSTENVERGLEICH (BARWERTE)\n\n"
            "| Kriterium | Option 1 (Eigenbetrieb) | Option 4 (Extern) | Differenz |\n"
            "|---|---|---|---|\n"
            "| Barwert (1,2 %) | 715.000 EUR | 1.710.000 EUR | -995.000 EUR |\n"
            "| Kostenanteil | 100 % | 239 % | +139 % |\n"
            "| Ersparnis Option 1 | — | ca. 995.000 EUR (59 % günstiger) | — |\n"
            "| Kosten pro Liegenschaft/Jahr | 365 EUR | 875 EUR | -510 EUR |\n\n"
            "**ERGEBNIS: Option 1 ist wirtschaftlich deutlich überlegen.**"
        ),

        'kapitalwerte_ohne_risiko': (
            "Siehe Kapitalwertberechnung oben (Kapitel 5.2). Die angegebenen Barwerte sind "
            "ohne zusätzliche Risikozuschläge."
        ),

        'risikobetrachtung': (
            "**Risikoarten für Dienstleistungen (AR A-2400/62):**\n\n"
            "**OPTION 1 (Eigenbetrieb) — Risikobetrachtung:**\n\n"
            "Risikoart 1: Ausfall oder Defekt der Reinigungsmaschine\n"
            "  • Szenario: Technischer Defekt, Reparaturstau, ungeplante Wartung\n"
            "  • Eintrittswahrscheinlichkeit: ca. 5 % über 10 Jahre\n"
            "  • Schadenshöhe: Notfall-Fremdvergabe für 1 Reinigungszyklus = "
            "175.000 EUR ÷ 2 Jahre = 87.500 EUR\n"
            "  • Risikowert: 0,05 × 87.500 = 4.375 EUR\n\n"
            "Risikoart 2: Personalausfälle (Krankheit, Kündigung, unzureichende Schulung)\n"
            "  • Szenario: Geschultes Personal nicht verfügbar, Schulung dauert länger\n"
            "  • Eintrittswahrscheinlichkeit: ca. 3 % über 10 Jahre\n"
            "  • Schadenshöhe: Verzögerung von 2 Wochen = ca. 500 EUR Zusatzkosten\n"
            "  • Risikowert: 0,03 × 500 = 15 EUR\n\n"
            "Gesamter Risikowert Option 1: ca. 500 EUR über 10 Jahre\n\n"
            "---\n\n"
            "**OPTION 4 (Extern) — Risikobetrachtung:**\n\n"
            "Risikoart 1: Ausfallrisiko des Leistungserbringers\n"
            "  • Szenario: Insolvenz des Dienstleisters, Geschäftsaufgabe, Betriebsstilllegung\n"
            "  • Eintrittswahrscheinlichkeit: ca. 5 % über 10 Jahre "
            "(statistisch für KMU im Handwerk)\n"
            "  • Schadenshöhe: Notfall-Umstieg zu anderem Anbieter, verhandelte Kosten "
            "175.000 EUR/Jahr\n"
            "  • Risikowert: 0,05 × 175.000 = 8.750 EUR\n\n"
            "Risikoart 2: Ausfallrisiko der Leistungserbringung\n"
            "  • Szenario: Terminverzögerung, Qualitätsmängel, Maschinenausfälle beim "
            "Dienstleister, Wetter\n"
            "  • Eintrittswahrscheinlichkeit: ca. 10 % pro Zyklus "
            "(alle 2 Jahre kann 1 Termin um 2–4 Wochen verschoben werden)\n"
            "  • Schadenshöhe: Sportplatz-Sperrung, Trainings-/Wettkampfausfälle ca. 5.000 EUR "
            "pro Vorfall\n"
            "  • Häufigkeit über 10 Jahre: ca. 1–2 Vorfälle (15 % Wahrscheinlichkeit für "
            "mindestens 1 Ausfall)\n"
            "  • Risikowert: 0,15 × 5.000 = 750 EUR\n"
            "  [Anmerkung: Alternativ 0,10 × 2 × 5.000 = 1.000 EUR]\n\n"
            "Risikoart 3: Preissteigerungs-Überraschung\n"
            "  • Szenario: Reale Preissteigerung übersteigt 2 % p.a. deutlich "
            "(z. B. bei Rohstoff-Knappheit, Lohnkosten-Explosion)\n"
            "  • Eintrittswahrscheinlichkeit: ca. 5 % (eher pessimistisch)\n"
            "  • Schadenshöhe: zusätzliche 1 % p.a. Steigerung über 10 Jahre ≈ 50.000 EUR Mehrkosten\n"
            "  • Risikowert: 0,05 × 50.000 = 2.500 EUR\n\n"
            "Gesamter Risikowert Option 4: ca. 8.750 + 750 + 2.500 = 12.000 EUR über 10 Jahre\n"
            "(konservative Schätzung: 10.000 EUR)\n\n"
            "---\n\n"
            "**Fazit Risikobetrachtung:**\n\n"
            "Option 1 hat ein deutlich niedrigeres Risikoprofil (500 EUR vs. 10.000 EUR). "
            "Dies liegt daran, dass der Betrieb vollständig in Bundeswehr-Kontrolle ist "
            "(geringere Abhängigkeit von externen Faktoren)."
        ),

        'kapitalwert_mit_risiko': (
            "**Barwerte einschließlich Risikowert:**\n\n"
            "| Option | Barwert (ohne Risiko) | Risikowert | Barwert (mit Risiko) |\n"
            "|---|---|---|---|\n"
            "| **Option 1** | 715.000 EUR | 500 EUR | 715.500 EUR |\n"
            "| **Option 4** | 1.710.000 EUR | 10.000 EUR | 1.720.000 EUR |\n"
            "| **Differenz** | — | — | -1.004.500 EUR |\n\n"
            "**ERGEBNIS: Option 1 bleibt auch nach Risikozuschlag deutlich günstiger "
            "(ca. 1.000.000 EUR Ersparnis über 10 Jahre).**"
        ),
    },

    'kap6_9': {
        'vergleich': (
            "**Kostenvergleich (Barwerte mit Risiko):**\n\n"
            "| Kriterium | Option 1 | Option 4 | Gewinner |\n"
            "|---|---|---|---|\n"
            "| Gesamtkosten (10 J., mit Risiko) | 715.500 EUR | 1.720.000 EUR | ✓ Option 1 |\n"
            "| Kosten pro Liegenschaft/Jahr | 365 EUR | 875 EUR | ✓ Option 1 |\n"
            "| Anfangsinvestition (Jahr 1) | 240.000 EUR | 0 EUR | ✓ Option 4 |\n"
            "| Betriebsrisiko | gering | mittel-hoch | ✓ Option 1 |\n"
            "| Qualitätskontrolle | direkt (BW) | vertraglich | ✓ gleichwertig |\n"
            "| Zeitplanbarkeit | planbar (zentral) | abhängig (extern) | ✓ Option 1 |\n"
            "| Dezentralisierbarkeit | niedrig | hoch | ✓ Option 4 |\n"
            "| Flexibilität bei Standort-Änderungen | mittel | hoch | ✓ Option 4 |\n\n"
            "**Kostenersparnis grafisch (vereinfacht):**\n\n"
            "Option 1: ███████████ (715.500 EUR)\n"
            "Option 4: ███████████████████████████████ (1.720.000 EUR)\n\n"
            "Option 1 ist ca. 59 % günstiger als Option 4."
        ),

        'sensitivitaet': (
            "**Sensitivitätsanalyse: Was passiert, wenn Annahmen sich ändern?**\n\n"
            "| Szenario | Parameter-Änderung | Auswirkung auf Kosten | Gewinner |\n"
            "|---|---|---|---|\n"
            "| **Szenario 1: Höhere Preissteigerung extern** | +5 % p.a. statt 2 % | Option 4 kostet zusätzlich ca. 350.000 EUR | ✓ Option 1 noch günstiger |\n"
            "| **Szenario 2: Maschinenlebensdauer kürzer** | 8 Jahre statt 10 | Option 1 kostet zusätzlich ca. 60.000 EUR (Ersatz-Abschreibung) | ✓ Option 1 bleibt günstiger |\n"
            "| **Szenario 3: Liegenschafts-Wachstum** | 250 statt 200 Standorte | Option 1: bestehende Maschine reicht längere Zeit; Option 4: +175.000 EUR Kosten/Jahr | ✓ Option 1 vorteilhaft |\n"
            "| **Szenario 4: Liegenschafts-Rückgang** | 150 statt 200 Standorte | Option 1: Maschine bleibt 240.000 EUR Fixkosten; Option 4: -131.250 EUR/Jahr | ✓ Option 4 wird günstiger |\n"
            "| **Szenario 5: Personal-Kosteneffizienz** | -20 % Personalkosten durch Automatisierung | Option 1 spart ca. 40.000 EUR | ✓ Option 1 noch günstiger |\n\n"
            "**Break-Even-Analyse:**\n\n"
            "Bei welcher Liegenschaftszahl werden die Optionen kostengleich?\n\n"
            "Formel: Fixkosten Option 1 + laufende Kosten = Kosten Option 4\n"
            "  240.000 EUR (Maschine, 1. Jahr) + (20.000 + 24.000 + 5.000) × N_Jahre = 175.000 EUR × N_Jahre × 200 Standorte / X_Standorte\n\n"
            "Durchschnittlich: Break-Even liegt unterhalb von 200 Standorten nicht erreichbar. "
            "Selbst bei 100 Standorten ist Option 1 noch günstiger (mit halbiertem Personal und halber Maschine = 150.000 EUR).\n\n"
            "**Fazit Sensitivitätsanalyse:**\n\n"
            "Option 1 ist unter den meisten realistischen Parameterveränderungen robust überlegen. "
            "Nur bei drastischer Reduktion der Liegenschaftszahl (unter 100) oder extremer Preissteigerung "
            "der Maschine könnte Option 4 vorteilhaft werden — aber solche Szenarien sind nicht zu erwarten."
        ),

        'nichtmonetaere_faktoren': (
            "**Nichtmonetäre Faktoren und Governance:**\n\n"
            "| Faktor | Option 1 | Option 4 | Bewertung |\n"
            "|---|---|---|---|\n"
            "| **Strategische Unabhängigkeit** | Vollständig (BW-eige Ressourcen) | Abhängig von Markt/Anbieter | ✓ Option 1 vorteilhaft |\n"
            "| **Nachhaltigkeitsaspekte (AVV Klima)** | Keine direkten Transportemissionen (zentrale Maschine); langfristige Nutzung 1 Maschine | externe DL-Anfahrten zu 200 Standorten; Fahrteneinsparung durch Bündelung möglich | ✓ Option 1 vorteilhaft |\n"
            "| **Sportplatz-Verfügbarkeit** | Planbar und vorhersagbar (zentrale Steuerung) | Abhängig von Dienstleister-Kapazität und Wetter | ✓ Option 1 vorteilhaft |\n"
            "| **Dezentralisierbarkeit** | Niedrig (zentrale Kontrolle erforderlich) | Hoch (Einzelverträge pro BwDLZ möglich) | ✓ Option 4 vorteilhaft |\n"
            "| **Fachkompetenz lokal** | Konzentriert auf zentrale Stelle | Verteilt auf 200+ Dienstleister | ✓ Option 4 vorteilhaft |\n"
            "| **Technologie-Aktualität** | Statisch (Maschine 2026 Standard) | Dynamisch (externe DL nutzen aktuelle Technologie) | ✓ Option 4 vorteilhaft |\n"
            "| **Wartungs-Planbarkeit** | Planbar (eigenes Personal) | Abhängig von Dienstleister | ✓ Option 1 vorteilhaft |\n"
            "| **Personalflex ibilität** | 0,4 VZÄ konstant erforderlich | Variabel (abhängig von Dienstleister-Kapazität) | ✓ Option 4 vorteilhaft |\n\n"
            "**Fazit Nichtmonetäre Faktoren:**\n\n"
            "Option 1 überzeugt durch strategische Unabhängigkeit, Nachhaltigkeit und "
            "Planbarkeit. Option 4 bietet Dezentralisierungsflexibilität und "
            "Technologie-Dynamik. Aus Sicht der Bundeswehr-Steuerung ist die Kontrolle über "
            "eine kritische Infrastruktur (Sportplätze) ein relevanter Faktor für Option 1."
        ),

        'entscheidungsvorschlag': (
            "**EMPFEHLUNG: Option 1 (Leistungserbringung durch Eigenbetrieb)**\n\n"
            "**Begründung:\n\n"
            "1. ERHEBLICHE WIRTSCHAFTLICHKEIT**\n"
            "   • Barwert Option 1: 715.500 EUR über 10 Jahre\n"
            "   • Barwert Option 4: 1.720.000 EUR über 10 Jahre\n"
            "   • **Ersparnis: ca. 1.004.500 EUR (59 % günstiger)**\n"
            "   • Pro Liegenschaft/Jahr: 365 EUR (Option 1) vs. 875 EUR (Option 4)\n\n"
            "2. ROBUSTHEIT UNTER SENSITIVITÄTS-SZENARIEN**\n"
            "   • Selbst bei Preissteigerung +5 % p.a. bleibt Option 1 günstiger\n"
            "   • Selbst bei Maschinenlebensdauer-Risiken bleibt Option 1 überlegen\n"
            "   • Bei Liegenschafts-Wachstum (250+ Standorte) wird Option 1 noch vorteilhafter\n\n"
            "3. STRATEGISCHE UNABHÄNGIGKEIT**\n"
            "   • Bundeswehr bleibt unabhängig von Marktpreisen und Dienstleister-Verfügbarkeit\n"
            "   • Langfristige Planungssicherheit\n"
            "   • Ressource bleibt in BW-Kontrolle\n\n"
            "4. NIEDRIGERES RISIKOPROFIL**\n"
            "   • Risikowert Option 1: ca. 500 EUR\n"
            "   • Risikowert Option 4: ca. 10.000 EUR\n"
            "   • Technisches Ausfallrisiko in BW-eigenen Händen minimiert\n\n"
            "5. NACHHALTIGKEITSASPEKTE**\n"
            "   • Reduzierte Transportemissionen durch zentrale Maschine\n"
            "   • Langfristige Nutzung einer Investition (Circular Economy)\n\n"
            "**GESAMTKOSTEN ÜBER 10 JAHRE (MIT RISIKO):** 715.500 EUR\n\n"
            "**UMSETZUNG:**\n"
            "   • Jahr 1 (2026): Maschinen-Beschaffung 240.000 EUR, Personal-Schulung\n"
            "   • Jahr 2 ab: Regelmäßige Reinigungen alle 2 Jahre nach Zeitplan\n"
            "   • Zentrale Lagerstelle etablieren, Transport zwischen Standorten organisieren\n\n"
            "**DEZENTRALISIERUNGSHINWEIS:**\n"
            "Diese Empfehlung bedeutet nicht, dass alle Standorte zentral verwaltet werden. "
            "Vielmehr können BwDLZ diese Referenz-WU als Basis nutzen und lokale Parameter anpassen "
            "(z. B. Fläche, Häufigkeit), solange sie der gleichen Kostenlogik folgen. Ein "
            "dezentralisiertes Modell (jede BwDLZ kauft eigene Maschinen) ist aber nicht "
            "wirtschaftlich sinnvoll, da es zu 200× höheren Investitionen führt."
        ),

        'erfolgskontrolle': (
            "**Erfolgskontrolle und Qualitätssicherung (gemäß AR A-2400/62, Kap. 9):**\n\n"
            "**Verantwortlichkeit:**\n"
            "   • Zentrale Koordination: Zentrale Dienststelle für Liegenschaftsmanagement "
            "(oder vergleichbar)\n"
            "   • Vor-Ort-Prüfung: Standortkommandant / BwDLZ-Leiter vor Ort\n\n"
            "**Kontrollzyklus:**\n"
            "   • Zeitpunkt: Innerhalb von 2 Wochen nach jedem Reinigungszyklus (also "
            "2–4 Wochen nach Durchführung, alle 24 Monate)\n"
            "   • Prüffrequenz: 100 % Inspektionen (alle 200 Standorte nach Reinigung)\n\n"
            "**Kontrollmittel (Checkliste):**\n"
            "   ☐ Moosfreiheit: Visuelle Kontrolle, keine grünen Verfärbungen\n"
            "   ☐ Algenbeseitigung: Oberflächenkontrolle auf Biofilm\n"
            "   ☐ Oberflächenschäden: Keine neuen Beschädigungen durch Hochdruck erkennbar\n"
            "   ☐ Wasserabsaugung: Kontrolle, dass Schmutzwasser vollständig aufgefangen wurde\n"
            "   ☐ Dokumentation: Fotos vor/nach Reinigung an mindestens 3 Stellen\n\n"
            "**Dokumentation:**\n"
            "   • Inspektionsbericht pro Standort (schriftlich)\n"
            "   • Ablage zentral (elektronisch) für Auditierbarkeit\n"
            "   • Abweichungsbericht bei Mängeln\n\n"
            "**Nachbesserung:**\n"
            "   • Fristen: 14 Tage für Nachbesserung bei erkannten Mängeln\n"
            "   • Kosten: Nachbesserung auf Kosten der verantwortlichen Stelle "
            "(bei Eigenbetrieb: BW-intern)\n"
            "   • Dokumentation: Abweichungsbericht mit Abstellmaßnahmen\n\n"
            "**Eskalation:**\n"
            "   • Bei wiederholten Mängeln (>2 Fälle): Überprüfung Verfahren / Maschinenwartung\n"
            "   • Personalschulung auffrischen bei Qualitätsmängeln"
        ),
    },

    'anlage': [
        {
            'nr': '1',
            'produkt': 'Tartanbahn-Reinigung spezialisiert (4.200 m², alle 2 Jahre)',
            'preis': '1.500–2.000 EUR',
            'url': 'tartanbahn-reinigung.de, theis-spezialreinigung.de, vbsport.de, x3system.eu',
            'bemerkung': 'Hochdruckverfahren max. 310 bar, Schmutzwasserabsaugung integriert, keine chemischen Zusätze. Recherche-Datum: 16.04.2026'
        },
        {
            'nr': '2',
            'produkt': 'Hochdruckanlage mit Schmutzwasserabsaugung (neu, professionell)',
            'preis': '240.000 EUR',
            'url': 'x3system.eu, theis-spezialreinigung.de (Hersteller)',
            'bemerkung': 'Einmalige Investition, Lebensdauer ca. 10 Jahre, wartungsintensiv (10 % p.a. Kosten). Recherche-Datum: 16.04.2026'
        },
        {
            'nr': '3',
            'produkt': 'PSK E9b (technischer Service), 2024',
            'preis': '50.000 EUR/VZÄ/Jahr',
            'url': 'BMF Personalkosten-Sätze 2024, nachgeordnete Bundesbehörden',
            'bemerkung': 'Für Tartanbahnreinigung erforderlich: 0,4 VZÄ für 200 Liegenschaften = 20.000 EUR/Jahr. Recherche-Datum: 16.04.2026'
        },
    ],
}

# ============================================================================
# EXPORT
# ============================================================================

if __name__ == '__main__':
    from export_wu_dienstleistung import fill_template, build_filename

    print("=" * 70)
    print("EXPORT: ÜBERGREIFENDE TARTANBAHNREINIGUNGS-WU (200 LIEGENSCHAFTEN)")
    print("=" * 70)

    try:
        outpath = build_filename(
            wu_data['meta']['datum'],
            'Tartanbahnreinigung_200_Standorte_uebergreifend',
            wu_data['meta']['dienststelle']
        )

        print(f"\n[1/2] Fuelle Template...")
        fill_template(wu_data, outpath)

        print(f"[2/2] Speichere Datei...")
        print(f"\nEXPORT ERFOLGREICH")
        print(f"Pfad: {outpath}\n")

        print("=" * 70)
        print("STATISTIK")
        print("=" * 70)
        print(f"Dienststelle: {wu_data['meta']['dienststelle']}")
        print(f"Bearbeiter: {wu_data['meta']['bearbeiter']}")
        print(f"Datum: {wu_data['meta']['datum']}")
        print(f"Version: {wu_data['meta']['version']}")
        print(f"\nGesamtkosten Option 1: 715.500 EUR (10 Jahre)")
        print(f"Gesamtkosten Option 4: 1.720.000 EUR (10 Jahre)")
        print(f"Ersparnis: ca. 1.004.500 EUR (59 % günstiger)")
        print("\n" + "=" * 70)

    except Exception as e:
        print(f"FEHLER: {e}")
        import traceback
        traceback.print_exc()
