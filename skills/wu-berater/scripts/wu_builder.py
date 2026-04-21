"""
WU-Builder: Validierungs- und Hilfsfunktionen für Wirtschaftlichkeitsuntersuchungen

Verwendet für:
1. Validierung von wu_data Dictionaries gegen Schemata
2. Guard-Checks für unzulässige Aussonderungsgründe
3. Completeness-Checks vor Export
4. Safe-Export-Wrapper
"""

from typing import Dict, List, Tuple, Optional, Any
import json


class WuValidator:
    """Validator für WU-Datenstrukturen."""

    INVALID_EXCLUSION_REASONS = {
        'missing_budget': 'fehlende Haushaltsmittel',
        'missing_personnel': 'fehlendes Personal',
        'missing_posts': 'fehlende Dienstposten',
        'insufficient_infrastructure': 'nicht ausreichend vorhandene Infrastruktur',
        'no_money': 'kein Geld',
        'no_staff': 'kein Personal',
        'no_posts': 'keine Dienstposten',
        'not_enough_infrastructure': 'unzureichende Infrastruktur',
    }

    # Schema für unterjährige WU
    SCHEMA_UNTERJAHRIG = {
        'meta': {
            'dienststelle': str,
            'bearbeiter': str,
            'datum': str,
            'beginn_massnahme': str,
            'schutz': str,
            'version': str,
        },
        'inhalt': {
            'bedarfsforderung': str,
            'haken': dict,
            'eigenleistung_begruendung': str,
            'miete_begruendung': str,
            'ausgaben': (int, float),
        },
        'anlage': list,
    }

    # Schema für überjährige / Dienstleistungs-WU
    SCHEMA_UBERJAHRIG = {
        'meta': {
            'dienststelle': str,
            'bearbeiter': str,
            'datum': str,
            'schutz': str,
            'version': str,
        },
        'ueberblick': {
            'betrachtungsgegenstand': str,
            'entscheidungsvorschlag': str,
        },
        'kap1': dict,
        'kap2': dict,
        'kap3': dict,
        'kap4': dict,
        'kap5': dict,
        'kap6_9': dict,
        'anlage': list,
    }

    def __init__(self, wu_type: str = 'unterjahrig'):
        """
        Initialize validator.

        Args:
            wu_type: 'unterjahrig', 'uberjahrig', or 'dienstleistung'
        """
        self.wu_type = wu_type
        self.schema = self.SCHEMA_UNTERJAHRIG if wu_type == 'unterjahrig' else self.SCHEMA_UBERJAHRIG
        self.errors = []
        self.warnings = []

    def validate(self, wu_data: Dict) -> Tuple[bool, List[str], List[str]]:
        """
        Vollständige Validierung.

        Returns:
            (is_valid, errors, warnings)
        """
        self.errors = []
        self.warnings = []

        self._validate_structure(wu_data)
        self._validate_completeness(wu_data)
        self._validate_guards(wu_data)
        self._validate_references(wu_data)

        return len(self.errors) == 0, self.errors, self.warnings

    def _validate_structure(self, wu_data: Dict) -> None:
        """Prüft gegen grundlegende Struktur."""
        for key, expected_type in self.schema.items():
            if key not in wu_data:
                self.errors.append(f"Pflichtfeld fehlt: '{key}'")
            elif isinstance(expected_type, dict):
                if not isinstance(wu_data[key], dict):
                    self.errors.append(f"'{key}' muss ein Dictionary sein, nicht {type(wu_data[key])}")
            elif isinstance(expected_type, list):
                if not isinstance(wu_data[key], list):
                    self.errors.append(f"'{key}' muss eine Liste sein, nicht {type(wu_data[key])}")

    def _validate_completeness(self, wu_data: Dict) -> None:
        """Prüft auf fehlende wichtige Felder."""
        meta = wu_data.get('meta', {})

        # Kopfdaten
        if not meta.get('dienststelle'):
            self.warnings.append("meta.dienststelle ist leer")
        if not meta.get('bearbeiter'):
            self.warnings.append("meta.bearbeiter ist leer (kann später manuell ergänzt werden)")
        if not meta.get('datum'):
            self.errors.append("meta.datum ist erforderlich (TT.MM.JJJJ)")
        if not meta.get('schutz'):
            self.warnings.append("meta.schutz nicht gesetzt (Standard: 'offen')")

        # WU-spezifische Felder
        if self.wu_type == 'unterjahrig':
            inhalt = wu_data.get('inhalt', {})
            if not inhalt.get('bedarfsforderung'):
                self.warnings.append("Bedarfsforderung ist leer")
            if inhalt.get('ausgaben') is None or inhalt.get('ausgaben') == 0:
                self.warnings.append("Ausgaben nicht gesetzt (0 EUR?)")
            if not inhalt.get('haken'):
                self.warnings.append("Häkchen nicht gesetzt")
        else:
            # Überjährig / Dienstleistung
            ueberblick = wu_data.get('ueberblick', {})
            if not ueberblick.get('betrachtungsgegenstand'):
                self.warnings.append("Überblick: Betrachtungsgegenstand ist leer")
            if not ueberblick.get('entscheidungsvorschlag'):
                self.warnings.append("Überblick: Entscheidungsvorschlag ist leer")

            kap5 = wu_data.get('kap5', {})
            if not kap5.get('kw_mit_risiko') and not kap5.get('kw_ohne_risiko'):
                self.warnings.append("Kapitalwertberechnung (5.2/5.3) fehlt")

    def _validate_guards(self, wu_data: Dict) -> None:
        """Prüft auf unzulässige Aussonderungsgründe."""
        # Textuelle Suche nach verdächtigen Ausdrücken
        suspicious_texts = [
            ('Haushaltsmittel', 'fehlende Haushaltsmittel'),
            ('Personal', 'fehlendes Personal'),
            ('Dienstposten', 'fehlende Dienstposten'),
            ('Infrastruktur', 'mangelnde Infrastruktur'),
        ]

        # In allen Aussonderungs-Texten suchen
        for key, section in wu_data.items():
            if not isinstance(section, dict):
                continue

            aussonderung_fields = [
                section.get('aussonderung'),
                section.get('rb_rechtlich'),
                section.get('rb_organisatorisch'),
                section.get('rb_zeitlich'),
            ]

            for field_text in aussonderung_fields:
                if not field_text or not isinstance(field_text, str):
                    continue

                for keyword, full_reason in suspicious_texts:
                    if keyword in field_text and 'nicht möglich' not in field_text:
                        self.warnings.append(
                            f"⚠ GUARD CHECK: Möglicherweise unzulässiger Aussonderungsgrund "
                            f"('{full_reason}') in {key}. "
                            f"Prüfen ob zeitliche Rahmenbedingung + Nachweis verfügbar ist."
                        )

    def _validate_references(self, wu_data: Dict) -> None:
        """Prüft auf Quellenangaben und fehlende Verlinkungen."""
        anlage = wu_data.get('anlage', [])

        if not anlage:
            self.warnings.append("Anlage Marktrecherche ist leer")
            return

        # Zähle Einträge
        if len(anlage) == 0:
            self.warnings.append("Keine Marktrecherche-Einträge vorhanden")

        # Prüfe auf fehlende Felder in Anlage
        required_fields = ['nr', 'produkt', 'preis', 'url']
        for i, eintrag in enumerate(anlage):
            for field in required_fields:
                if not eintrag.get(field):
                    self.warnings.append(f"Anlage Nr. {i+1}: Feld '{field}' ist leer")

    def get_missing_fields(self, wu_data: Dict) -> List[str]:
        """Gibt Liste der Felder zurück, die noch befüllt werden müssen."""
        missing = []

        meta = wu_data.get('meta', {})
        if not meta.get('bearbeiter'):
            missing.append('meta.bearbeiter')

        if self.wu_type == 'unterjahrig':
            inhalt = wu_data.get('inhalt', {})
            if not inhalt.get('bedarfsforderung'):
                missing.append('inhalt.bedarfsforderung')
            if not inhalt.get('eigenleistung_begruendung'):
                missing.append('inhalt.eigenleistung_begruendung')
            if not inhalt.get('miete_begruendung'):
                missing.append('inhalt.miete_begruendung')
        else:
            kap1 = wu_data.get('kap1', {})
            if not kap1.get('bedarfsforderung'):
                missing.append('kap1.bedarfsforderung')

            kap5 = wu_data.get('kap5', {})
            if not kap5.get('kw_mit_risiko') and not kap5.get('kw_ohne_risiko'):
                missing.append('kap5.kw_mit_risiko (oder kw_ohne_risiko)')

        return missing

    def export_safe(self, wu_data: Dict, fill_template_fn, build_filename_fn,
                    output_template_name: str) -> Tuple[bool, str, str]:
        """
        Sicherer Export-Wrapper.

        Args:
            wu_data: WU-Datenstruktur
            fill_template_fn: Funktion zum Füllen des Templates
            build_filename_fn: Funktion zum Erstellen des Dateinamens
            output_template_name: Name für Ausgabedatei

        Returns:
            (success, output_path, summary)
        """
        is_valid, errors, warnings = self.validate(wu_data)

        summary = ""

        if errors:
            summary = "❌ FEHLER - Export nicht möglich:\n"
            for err in errors:
                summary += f"  • {err}\n"
            return False, "", summary

        if warnings:
            summary = "⚠️  WARNUNGEN (Export trotzdem durchgeführt):\n"
            for warn in warnings:
                summary += f"  • {warn}\n"
            summary += "\n"

        try:
            meta = wu_data.get('meta', {})
            outpath = build_filename_fn(
                meta.get('datum', ''),
                output_template_name,
                meta.get('dienststelle', '')
            )
            fill_template_fn(wu_data, outpath)

            summary += f"✅ Export erfolgreich: {outpath}\n"
            return True, outpath, summary

        except Exception as e:
            summary += f"❌ Export fehlgeschlagen: {str(e)}\n"
            return False, "", summary


def quick_validate(wu_data: Dict, wu_type: str = 'unterjahrig') -> str:
    """
    Schnelle Validierung mit Textausgabe.

    Returns:
        Formatierte Validierungs-Summary
    """
    validator = WuValidator(wu_type)
    is_valid, errors, warnings = validator.validate(wu_data)

    output = ""

    if is_valid and not warnings:
        output += "✅ Alle Checks bestanden!\n"
    elif is_valid and warnings:
        output += f"⚠️  {len(warnings)} Warnungen:\n"
        for warn in warnings:
            output += f"  • {warn}\n"
    else:
        output += f"❌ {len(errors)} Fehler:\n"
        for err in errors:
            output += f"  • {err}\n"
        if warnings:
            output += f"\n⚠️  Zusätzlich {len(warnings)} Warnungen:\n"
            for warn in warnings:
                output += f"  • {warn}\n"

    return output


def create_empty_template(wu_type: str = 'unterjahrig') -> Dict:
    """Erstellt ein leeres wu_data Template."""
    if wu_type == 'unterjahrig':
        return {
            'meta': {
                'dienststelle': '',
                'bearbeiter': '',
                'datum': '',
                'beginn_massnahme': '',
                'schutz': 'offen',
                'version': '1',
            },
            'inhalt': {
                'bedarfsforderung': '',
                'haken': {},
                'eigenleistung_begruendung': '',
                'miete_begruendung': '',
                'ausgaben': 0,
            },
            'anlage': [],
        }
    else:
        return {
            'meta': {
                'dienststelle': '',
                'bearbeiter': '',
                'datum': '',
                'schutz': 'offen',
                'version': '1',
            },
            'ueberblick': {
                'betrachtungsgegenstand': '',
                'entscheidungsvorschlag': '',
            },
            'kap1': {},
            'kap2': {},
            'kap3': {},
            'kap4': {},
            'kap5': {},
            'kap6_9': {},
            'anlage': [],
        }


def merge_updates(base: Dict, updates: Dict) -> Dict:
    """
    Merged updates in base dictionary (deep merge).

    Beispiel:
        wu_data = create_empty_template('uberjahrig')
        wu_data = merge_updates(wu_data, {
            'meta': {'dienststelle': 'BAIUDBw'},
            'kap1': {'bedarfsforderung': 'Text...'}
        })
    """
    for key, value in updates.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            base[key] = merge_updates(base[key], value)
        else:
            base[key] = value
    return base


# ============================================================================
# QUALITÄTSPRÜFUNGEN FÜR INLINE-FEEDBACK IM GEFÜHRTEN DIALOG
# ============================================================================

class WuQualityChecker:
    """Prüft Textqualität und formulistische Anforderungen."""

    @staticmethod
    def check_demand_statement(text: str) -> Tuple[bool, str]:
        """
        Prüft Bedarfsforderung auf:
        - Mindestlänge (2-3 Sätze)
        - Lösungsneutralität (keine Produktnamen)
        - Quantitative Angaben (Menge, Häufigkeit)

        Returns:
            (is_ok, feedback)
        """
        if not text or len(text.strip()) < 50:
            return False, "❌ Bedarfsforderung zu kurz. Bitte 2-3 vollständige Sätze mit Menge/Häufigkeit."

        # Check für verdächtige Produktnamen
        suspicious_products = [
            'Dell', 'HP', 'Lenovo', 'MacBook', 'iPhone', 'Samsung', 'Sony',
            'CAT', 'JCB', 'Liebherr', 'Bosch', 'Makita', 'DeWalt',
            'BMW', 'Mercedes', 'VW', 'Audi', 'Toyota',
        ]

        for product in suspicious_products:
            if product.lower() in text.lower():
                return False, (
                    f"⚠️ Verdächtig konkret: '{product}' ist ein Produktname. "
                    f"Bitte funktional/lösungsneutral formulieren, z.B. 'Laptops mit Spezifikation [X]'."
                )

        # Check auf Quantifizierung
        has_quantity = any(word in text.lower() for word in ['stück', 'menge', 'anzahl', 'häufigkeit', 'einsatztage', 'pro', 'täglich', 'jährlich'])

        if not has_quantity:
            return False, "⚠️ Keine Quantifizierung erkannt. Bitte ergänzen: Stückzahl, Menge oder Häufigkeit der Einsätze."

        return True, "✅ Bedarfsforderung: funktional + lösungsneutral + quantifiziert"

    @staticmethod
    def check_exclusion_reason(text: str) -> Tuple[bool, str]:
        """
        Prüft Aussonderungsgründe auf unzulässige Formeln.

        Returns:
            (is_ok, feedback)
        """
        invalid_patterns = [
            ('haushaltsmittel', 'Haushaltsmittel'),
            ('kein geld', 'fehlende Mittel'),
            ('personal', 'fehlendes Personal'),
            ('dienstposten', 'fehlende Dienstposten'),
            ('infrastruktur', 'mangelnde Infrastruktur'),
        ]

        for pattern, label in invalid_patterns:
            if pattern in text.lower() and 'nicht möglich' not in text.lower():
                return False, (
                    f"❌ GUARD CHECK: '{label}' ist kein zulässiger Aussonderungsgrund. "
                    f"Nutzen Sie stattdessen eine **zeitliche Rahmenbedingung**:\n"
                    f"   ✅ 'Option X scheidet aus, da Personalgewinnung bis [Datum] nachweislich nicht möglich ist.'"
                )

        if 'scheidet aus' in text.lower() and ('nicht möglich' in text.lower() or 'nicht verfügbar' in text.lower()):
            # Check auf Anlage-Verweis (Belegpflicht)
            if 'anlage' not in text.lower():
                return True, (
                    "⚠️ Hinweis: Für zeitliche Rahmenbedingungen ist ein Beleg erforderlich. "
                    "Bitte verweisen Sie auf eine Anlage (z.B. Schreiben der Personalstelle)."
                )

        return True, "✅ Aussonderungsgrund: zulässig formuliert"

    @staticmethod
    def check_complete_sentences(text: str) -> Tuple[bool, str]:
        """
        Prüft auf vollständige, grammatikalisch korrekte Sätze.
        (Vereinfachte Heuristik)

        Returns:
            (is_ok, feedback)
        """
        if not text or len(text.strip()) < 30:
            return False, "❌ Abschnitt zu kurz (mindestens 2-3 Sätze)."

        sentences = text.split('.')
        if len(sentences) < 2:
            return False, "❌ Nur ein Satz. Bitte 2-3 vollständige Sätze im Behördenstil."

        # Check auf Stichpunkte statt Fließtext
        if text.count('\n-') > 0 or text.count('\n•') > 0:
            return False, "❌ Stichpunkte erkannt. Bitte als Fließtext formulieren."

        return True, "✅ Vollständige Sätze im Behördenstil"

    @staticmethod
    def check_source_reference(text: str) -> Tuple[bool, str]:
        """
        Prüft auf Quellenverweise zu Anlagen (Marktrecherche).

        Returns:
            (is_ok, feedback)
        """
        if 'anlage' not in text.lower() and 'siehe' not in text.lower():
            return True, (
                "ℹ️ Hinweis: Prüfen Sie, ob Sie einen Verweis auf die Anlage "
                "(z.B. '(siehe Anlage Marktrecherche, Nr. X)') ergänzen müssen."
            )

        return True, "✅ Quellenverweise vorhanden oder nicht erforderlich"


def validate_step(step_key: str, text: str, wu_type: str = 'unterjahrig') -> str:
    """
    Inline-Validierung für einen Dialog-Schritt.
    Gibt formatiertes Feedback aus.

    Args:
        step_key: 'bedarfsforderung', 'aussonderung', 'aussonderung_miete', etc.
        text: Der eingegebene Text
        wu_type: 'unterjahrig', 'uberjahrig', 'dienstleistung'

    Returns:
        Formatiertes Feedback mit ✅, ⚠️, oder ❌
    """
    checker = WuQualityChecker()
    feedback_lines = []

    # Allgemeine Sätze-Prüfung
    complete_ok, complete_msg = checker.check_complete_sentences(text)
    feedback_lines.append(complete_msg)

    # Schritt-spezifische Prüfungen
    if 'bedarfsforderung' in step_key.lower():
        demand_ok, demand_msg = checker.check_demand_statement(text)
        feedback_lines.append(demand_msg)

    elif 'aussonderung' in step_key.lower() or 'ausschluss' in step_key.lower():
        excl_ok, excl_msg = checker.check_exclusion_reason(text)
        feedback_lines.append(excl_msg)

    # Quellenverweise immer prüfen
    source_ok, source_msg = checker.check_source_reference(text)
    if source_msg.startswith('ℹ️'):
        feedback_lines.append(source_msg)

    return "\n".join(feedback_lines)
