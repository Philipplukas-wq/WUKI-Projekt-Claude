# WU File Handler — Robustes Speichern von WU-Dokumenten

## Problem, das gelöst wird

### 1. **Word-Lock-Dateien**
Word erstellt temporäre Lock-Dateien (`~$Dateiname.docx`), wenn ein Dokument offen ist. Diese verhindern, dass Python-Skripte die Datei überschreiben können.

**Fehler ohne Handler:**
```
PermissionError: [Errno 13] Permission denied: '.../20260420_WU_Tartanbahnreinigung_Version_1.docx'
```

### 2. **Automatische Versionierung**
Wenn eine Datei gesperrt ist (weil sie noch in Word offen ist), wird die Versionsnummer automatisch erhöht:
- `Version_1.docx` ist gesperrt → speichere als `Version_2.docx`
- `Version_2.docx` ist auch gesperrt → speichere als `Version_3.docx`

### 3. **Encoding-Probleme mit Umlauten**
Python-Strings mit Umlauten (ä, ö, ü) können bei fehlerhaftem Encoding beschädigt werden, was zu `SyntaxError` führt.

**Solution:** UTF-8 Encoding wird explizit behandelt.

---

## Verwendung

### **Für Word-Dokumente (.docx)**

```python
from wu_file_handler import save_document_safely

# Erstelle Dokument mit python-docx
from docx import Document
doc = Document()
# ... befülle doc ...

# Speichere mit robustem Handling
output_file = "/path/to/20260420_WU_Schlepper_Version_1.docx"
actual_file = save_document_safely(doc, output_file)

print(f"Gespeichert als: {actual_file}")
# Output: 
# [INFO] Lock-Datei geloescht: ~$260417_WU_Allradschlepper_Version_4.docx
# [OK] Datei gespeichert: 20260420_WU_Schlepper_Version_2.docx
#      Pfad: /path/to/...
#      Groesse: 62.5 KB
```

### **Für Excel-Dateien (.xlsm)**

```python
from wu_file_handler import cleanup_lock_files
import openpyxl

# Lade und befülle Workbook
wb = openpyxl.load_workbook('Template.xlsm', keep_vba=True)
# ... befülle wb ...

# Räume Lock-Dateien auf
output_dir = "/path/to/Erstellte WU/Unterjährig"
cleanup_lock_files(output_dir)

# Speichere normal
wb.save(output_path)
```

---

## Was der Handler macht

### `cleanup_lock_files(directory)`
Löscht alle Word-Lock-Dateien im Verzeichnis:
```python
from wu_file_handler import cleanup_lock_files
cleanup_lock_files("/path/to/Erstellte WU/Überjährig")
# Löscht: ~$260417_..., ~$260420_..., etc.
```

### `find_available_filename(base_path)`
Prüft, ob eine Datei gesperrt ist. Falls ja, erhöht die Versionsnummer:
```python
from wu_file_handler import find_available_filename

base = "/path/to/20260420_WU_Schlepper_Version_1.docx"
actual = find_available_filename(base)
# Falls Version_1 gesperrt:
# actual = "/path/to/20260420_WU_Schlepper_Version_2.docx"
```

### `save_document_safely(doc, output_file)`
**Alleinstellungsmerkmal:** Macht alles in einem Schritt:
1. Erstellt das Ausgabeverzeichnis
2. Räumt Lock-Dateien auf
3. Prüft ob die Zieldatei gesperrt ist
4. Erhöht Versionsnummer, falls nötig
5. Speichert das Dokument
6. Gibt Erfolgs-Feedback aus

```python
from wu_file_handler import save_document_safely

actual_file = save_document_safely(doc, "/path/to/WU_Version_1.docx")
# Rückgabe: tatsächlicher Pfad (kann Version_2, Version_3 sein, wenn nötig)
```

### `build_safe_filename(...)`
Erstellt sichere Dateinamen im Standard-Format:
```python
from wu_file_handler import build_safe_filename

filename = build_safe_filename(
    datum="20.04.2026",
    sachverhalt="Tartanbahnreinigung",
    dienststelle="BwDLZ Mayen",
    base_dir="/path/to/Erstellte WU/Überjährig",
    version=1
)
# Ergebnis: 
# /path/to/Erstellte WU/Überjährig/20260420_WU_Tartanbahnreinigung_BwDLZ_Mayen_Version_1.docx
```

---

## Integration in bestehende Skripte

### **Schnelle Migration (`doc.save()` → robustes Speichern)**

**Vorher:**
```python
doc.save(output_path)
print(f"Datei: {output_path}")
```

**Nachher:**
```python
from wu_file_handler import save_document_safely

actual_file = save_document_safely(doc, output_path)
# Keine weiteren Prints nötig — Handler gibt automatisch Feedback
```

### **In Export-Skripten (wu-berater/scripts)**

```python
# Am Anfang des Skripts:
from wu_file_handler import save_document_safely

# Am Ende, statt doc.save():
actual_file = save_document_safely(doc, output_path)
return actual_file  # Rückgabe des tatsächlichen Pfads
```

---

## Fehlerfälle & Handling

| Szenario | Verhalten | Lösung |
|----------|-----------|--------|
| Datei ist offen in Word | Erhöhe Versionsnummer automatisch | Keine Aktion nötig |
| Lock-Dateien vorhanden | Lösche sie automatisch | Keine Aktion nötig |
| Zu viele gesperrte Versionen (>10) | RuntimeError mit Nachricht | Schließe Word-Dateien |
| Verzeichnis existiert nicht | Erstelle es automatisch | Keine Aktion nötig |
| Encoding-Fehler | Python-Strings mit UTF-8 behandelt | Verwende `# -*- coding: utf-8 -*-` am Script-Anfang |

---

## Beispiel: Kompletter Workflow

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
from wu_file_handler import save_document_safely
import os

# === ERSTELLE DOKUMENT ===
doc = Document()
doc.add_heading("Wirtschaftlichkeitsuntersuchung", level=1)
doc.add_paragraph("Tartanbahnreinigung BwDLZ Mayen")

# === SPEICHERE SICHER ===
output_dir = "/path/to/Erstellte WU/Überjährig"
output_file = os.path.join(output_dir, "20260420_WU_Tartanbahnreinigung_BwDLZ_Mayen_Version_1.docx")

actual_file = save_document_safely(doc, output_file)

# Output:
# [OK] Datei gespeichert: 20260420_WU_Tartanbahnreinigung_BwDLZ_Mayen_Version_1.docx
#      Pfad: /path/to/Erstellte WU/Überjährig
#      Groesse: 15.2 KB
```

---

## Testing

Zum Testen der Lock-Handling-Logik:

1. Öffne eine existierende WU-Datei in Word
2. Starte das Export-Skript
3. Beobachte: Das Skript speichert unter einer neuen Versionsnummer, statt zu crashen

```bash
# Version_1.docx ist offen in Word
python build_wu_tartanbahnreinigung_final.py

# Output:
# [WARN] 20260420_WU_Tartanbahnreinigung_Version_1.docx ist gesperrt. Verwende: Version_2.docx
# [OK] Datei gespeichert: 20260420_WU_Tartanbahnreinigung_Version_2.docx
```

---

## Technische Details

- **Encoding:** UTF-8 (Python 3 default)
- **Lock-Pattern:** `~$*.docx` (Word-Standard)
- **Versions-Pattern:** `_Version_N` vor `.docx`
- **Max. Versionsprünge:** 10 (verhindert Endlosschleifen)
- **Timeout:** Keine (blockiert bis Datei frei ist)

---

## Zusammenfassung

| Punkt | Nutzen |
|-------|--------|
| **Zuverlässigkeit** | Keine PermissionErrors mehr durch Word-Locks |
| **Benutzerfreundlichkeit** | Automatische Versionierung — kein manueller Eingriff nötig |
| **Debugging** | Detailliertes Logging mit `[INFO]`, `[WARN]`, `[OK]` |
| **Wartbarkeit** | Zentrale Lösung für alle WU-Export-Skripte |
| **Zukunftssicherheit** | Neue Skripte können `save_document_safely()` direkt nutzen |

