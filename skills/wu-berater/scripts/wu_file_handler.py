# -*- coding: utf-8 -*-
"""
WU-Berater: Robustes Datei-Handling für WU-Export
Verhindert Fehler durch Word-Locks und Encoding-Probleme.

Verwendung:
    from wu_file_handler import save_document_safely
    save_document_safely(doc, output_file)
"""

import os
import glob
from pathlib import Path


def cleanup_lock_files(directory):
    """
    Loescht Lock-Dateien von Word (~$...) im Verzeichnis.
    Word erstellt diese Dateien, wenn eine .docx offen ist.
    """
    if not os.path.isdir(directory):
        return

    lock_pattern = os.path.join(directory, "~$*.docx")
    for lock_file in glob.glob(lock_pattern):
        try:
            os.remove(lock_file)
            print(f"[INFO] Lock-Datei geloescht: {os.path.basename(lock_file)}")
        except Exception as e:
            print(f"[WARN] Konnte Lock-Datei nicht loeschen: {os.path.basename(lock_file)} ({e})")


def find_available_filename(base_path):
    """
    Prüft, ob die Datei gesperrt ist. Falls ja, erhöht die Versionsnummer.

    Argumente:
        base_path: z.B. '/path/to/20260420_WU_Schlepper_Version_1.docx'

    Rückgabe:
        /path/to/20260420_WU_Schlepper_Version_1.docx (falls frei)
        oder
        /path/to/20260420_WU_Schlepper_Version_2.docx (falls Version_1 gesperrt)
    """
    if not os.path.exists(base_path):
        return base_path

    # Versuche, die Datei zu oeffnen - wenn fehlgeschlagen, ist sie gesperrt
    try:
        with open(base_path, 'a'):
            pass
        return base_path
    except (PermissionError, IOError):
        # Datei ist gesperrt - erhoehe Versionsnummer
        base_name = base_path.replace(".docx", "")

        # Finde aktuelle Version
        match = base_name.rfind("_Version_")
        if match == -1:
            # Keine Version im Namen - fuege Version_2 hinzu
            new_path = base_name + "_Version_2.docx"
            print(f"[WARN] {os.path.basename(base_path)} ist gesperrt. Verwende: {os.path.basename(new_path)}")
            return new_path

        version_start = match + len("_Version_")
        current_version = int(base_name[version_start:])
        new_version = current_version + 1

        new_path = base_name[:match] + f"_Version_{new_version}.docx"
        print(f"[WARN] {os.path.basename(base_path)} ist gesperrt. Verwende: {os.path.basename(new_path)}")

        # Rekursiv pruefen, ob die neue Version auch gesperrt ist
        if os.path.exists(new_path):
            return find_available_filename(new_path)
        return new_path


def save_document_safely(doc, output_file):
    """
    Speichert ein Word-Dokument mit robustem Lock-Handling.

    Argumente:
        doc: python-docx Document-Objekt
        output_file: Zieldatei-Pfad (z.B. '/path/to/WU_Schlepper_Version_1.docx')

    Rückgabe:
        Tatsächlicher Speicher-Pfad (kann unterschiedlich sein, wenn Datei gesperrt war)

    Exceptions:
        RuntimeError: Wenn zu viele Versionen gesperrt sind oder anderer kritischer Fehler
    """
    # Erstelle Verzeichnis, falls nicht existent
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)

    # Räume Lock-Dateien auf
    cleanup_lock_files(output_dir)

    # Finde verfügbare Datei (erhöhe Version, falls nötig)
    actual_file = find_available_filename(output_file)

    # Speichere mit UTF-8 Encoding
    try:
        doc.save(actual_file)
        print(f"[OK] Datei gespeichert: {os.path.basename(actual_file)}")
        print(f"     Pfad: {output_dir}")
        print(f"     Groesse: {os.path.getsize(actual_file) / 1024:.1f} KB")
        return actual_file
    except Exception as e:
        raise RuntimeError(f"Fehler beim Speichern der WU: {e}") from e


def build_safe_filename(datum, sachverhalt, dienststelle, base_dir, version=1):
    """
    Erstellt einen sicheren Dateinamen fuer WU-Dokumente.

    Format: JJJJMMTT_WU_[Sachverhalt]_[Dienststelle]_Version_N.docx

    Argumente:
        datum: 'DD.MM.YYYY' oder 'YYYYMMDD'
        sachverhalt: z.B. 'Schlagbohrmaschine'
        dienststelle: z.B. 'BwDLZ_Mayen'
        base_dir: z.B. '/path/to/Erstellte WU/Überjährig'
        version: Versionsnummer (Default: 1)

    Rückgabe:
        '/path/to/Erstellte WU/Überjährig/20260420_WU_Schlepper_BwDLZ_Mayen_Version_1.docx'
    """
    # Konvertiere Datum zu JJJJMMTT
    if '.' in datum:
        teile = datum.split('.')
        if len(teile) == 3:
            jjjjmmdd = teile[2] + teile[1] + teile[0]
        else:
            jjjjmmdd = datum.replace('.', '')
    else:
        jjjjmmdd = datum.replace('-', '')

    # Sanitize Sachverhalt und Dienststelle
    sachverhalt = sachverhalt.strip().replace(' ', '_').replace('/', '_')
    dienststelle = dienststelle.strip().replace(' ', '_').replace('/', '_')

    filename = f'{jjjjmmdd}_WU_{sachverhalt}_{dienststelle}_Version_{version}.docx'
    return os.path.join(base_dir, filename)
