# Bedarfsprognose — Dialog und Methode (Kap. 1.2)

**Quelle:** AR A-2400/62 Ziffer 1.2

---

## Überblick: Dialog-Logik

**Standard-Annahme:** Bedarf ist **konstant** über den Betrachtungszeitraum.

**Abweichung nur, wenn User explizit etwas anderes nennt.**

---

## Dialog-Entscheidungsbaum

```
START: Bedarfsprognose für Betrachtungszeitraum [X Jahre]
│
├─ FRAGE AN USER:
│  "Bleibt der Bedarf über den gesamten Betrachtungszeitraum 
│   [von JAHR bis JAHR] konstant oder ändert er sich?"
│
├─ ANTWORT: JA, konstant
│  └─ → FALL A (siehe unten)
│
└─ ANTWORT: NEIN, ändert sich
   └─ → FRAGE 2: "Wie ändert sich der Bedarf? 
      Nennen Sie bitte für jedes Jahr oder die Änderungsrate"
      └─ ERFASSE: Tabelle (Jahr | Bedarf | Grund)
      └─ → FRAGE 3: Quelle? (siehe FALL B/C unten)
```

---

## FALL A: Konstanter Bedarf (Standard)

### Dialog-Fragen
```
1. "Bleibt der Bedarf konstant?"
   → USER: "Ja"

2. "Wo kommt diese Annahme her?"
   → Standard-Antwort: "Aus der Ausgangslage (Kap. 2)"
```

### Satzmuster für Kap. 1.2

**Standard (Quelle = Ausgangslage):**
> „Der Bedarf wird über den gesamten Betrachtungszeitraum von [X] Jahren 
> als **konstant** eingeschätzt. Es ist nicht mit einer wesentlichen Änderung 
> zu rechnen, da [Begründung aus Kap. 2, z.B. 'die Lagerwirtschaftsprozesse 
> stabilen strukturellen Aufgaben entsprechen']. Die jährliche Nutzung wird 
> auf [konkrete Menge/Einheit] geschätzt."

### Konkretbeispiel

**Ausgangslage dokumentiert:**
> Kap. 2.3: „Für die Leistungserbringung werden derzeit 250–280 Arbeitstage 
> pro Jahr mit einer Einsatzzeit von 4–5 Stunden täglich benötigt."

**Dann in Kap. 1.2:**
> „Der Bedarf wird über den gesamten Betrachtungszeitraum von 10 Jahren als 
> **konstant** eingeschätzt. Es ist nicht mit einer wesentlichen Änderung zu 
> rechnen, da die Lagerwirtschaftsprozesse stabilen strukturellen Aufgaben 
> entsprechen (siehe Kap. 2). Die jährliche Nutzung wird auf 250–280 Arbeitstage 
> mit 4–5 Betriebsstunden täglich = ca. 1.100–1.400 Betriebsstunden pro Jahr 
> geschätzt."

### Dokumentation der Quelle

**Im Text:**
```
Verweis auf Kap. 2: „siehe Kap. 2.3"
oder direkt formulieren: „wie in Kap. 2 dargestellt"
```

---

## FALL B: Variabeler Bedarf (User kennt Quelle)

### Dialog-Fragen
```
1. "Bleibt der Bedarf konstant?"
   → USER: "Nein, er steigt / fällt / ändert sich sprunghaft"

2. "Wie ändert sich der Bedarf?"
   → USER nennt für jedes Jahr oder Änderungsrate:
      Beispiel: "2026: 100 Personen, 2027: 110, 2028: 120, ..."
      oder: "Jährlich +10 Personen wegen Personalaufbau"

3. "Woher kommt diese Prognose?"
   → USER: [nennt Quelle, z.B. Stellungnahme Personalabteilung, 
      Beschluss vom 15.03.2026, Strategiedokument XYZ]
```

### Satzmuster für Kap. 1.2 (mit Tabelle)

**Einleitung:**
> „Der Bedarf wird sich über den Betrachtungszeitraum von [X] Jahren verändern. 
> Folgende Bedarfe werden für die einzelnen Kalenderjahre prognostiziert:"

**Dann Tabelle:**
```
| Kalenderjahr | Bedarf (Einheit) | Begründung |
|---|---|---|
| 2026 | 100 Personen | Startzustand |
| 2027 | 110 Personen | Personalaufbau gemäß Strategie |
| 2028 | 120 Personen | Fortsetzung Aufbau |
| 2029 | 130 Personen | Planung Ressourcenamt |
| 2030+ | 150 Personen | Zielgröße erreicht, danach konstant |
```

**Anschließender Fließtext:**
> „Die Bedarfssteigerung von 2026 bis 2029 ist begründet durch den geplanten 
> Personalaufbau zur Unterstützung der erweiterten Aufgaben (siehe Stellungnahme 
> Personalbereich vom 12.04.2026, Anlage [X]). Ab 2030 wird ein stabiler Bestand 
> von 150 Personen angenommen."

### Dokumentation der Quelle

**Im Text mit Verweis:**
```
„gemäß Stellungnahme [Dienststelle] vom [Datum] (vgl. Anlage [X])"
oder
„gemäß Beschluss [Name/Nummer] vom [Datum]"
oder
„gemäß Strategie [Name] des [Bereichs]"
```

**Anlage beifügen:** Die Quelle (Mail, Stellungnahme, Beschluss) muss unter 
„Anlagen" der WU dokumentiert sein.

### Konkretbeispiel

**User sagt:** „Der Bedarf steigt von 100 auf 150 Personen bis 2029, dann konstant. 
Quelle: E-Mail vom Personalbereich vom 20.04.2026"

**Dann in Kap. 1.2:**
```
Der Bedarf wird sich über den Betrachtungszeitraum von 10 Jahren (2026–2035) 
verändern. Folgende Bedarfe werden für die einzelnen Kalenderjahre prognostiziert:

| Kalenderjahr | Bedarf (VZÄ) | Begründung |
|---|---|---|
| 2026 | 100 | Ausgangslage |
| 2027 | 110 | Personalaufbau |
| 2028 | 120 | Personalaufbau |
| 2029 | 130 | Personalaufbau |
| 2030 | 150 | Zielgröße erreicht |
| 2031–2035 | 150 | Konstant auf Zielgröße |

Die Bedarfssteigerung von 2026 bis 2029 resultiert aus dem geplanten 
Personalaufbau, wie von der Personalbereich per E-Mail vom 20.04.2026 bestätigt 
(vgl. Anlage 5: Stellungnahme Personalbereich). Ab 2030 wird ein stabiler 
Personalbestand angenommen.
```

---

## FALL C: Variabeler Bedarf (User kennt KEINE Quelle)

### Situation
User kann keine konkrete Quelle nennen, weiß aber, dass Bedarf sich ändert.

### Mein Vorschlag (an User im Dialog)

> „Sie haben angegeben, dass sich der Bedarf ändert [wie: z.B. steigt um X pro Jahr]. 
> Für die Dokumentation in der WU benötigen wir eine Quelle. 
>
> **Mögliche Optionen:**
>
> 1. **Erfahrungswert eines Fachbereichs** (bevorzugt):
>    Beziehen Sie sich auf einen Erfahrungswert des zuständigen Fachbereichs. 
>    Beispiel: „Gemäß Aussage Fachbereich Travelmanagement (Herr Maier) vom 
>    23.04.2026 per E-Mail ist ein Bedarf von X pro Jahr anzunehmen, da […]"
>
> 2. **Historische Daten**:
>    Falls Sie historische Daten haben (z.B. Bedarfe 2020–2025), können Sie 
>    auf diese Basis verweisen und eine Trendfortschreibung begründen.
>
> 3. **Externe Prognosen**:
>    Falls es öffentliche Prognosen gibt (z.B. Bevölkerungsprognosen für 
>    Infrastruktur), zitieren Sie diese.
>
> **Welche Option passt zu Ihrer Situation?** 
> Wenn Sie sich auf einen Fachbereich beziehen, **bitte per E-Mail anfragen** 
> (nicht telefonisch), damit Sie direkt eine schriftliche Quelle haben."

### Satzmuster bei Fachbereich-Aussage (bevorzugt)

> „Der Bedarf wird sich über den Betrachtungszeitraum wie folgt entwickeln 
> [Tabelle]. Grundlage dieser Prognose ist eine Aussage des Fachbereichs 
> [Name], die in einer E-Mail vom [Datum] getroffen wurde (vgl. Anlage [X])."

**Konkretbeispiel:**
> „Der Bedarf wird sich über den Betrachtungszeitraum wie folgt entwickeln: 
> 2026: 50 Fahrtage, 2027: 60 Fahrtage, 2028–2035: 70 Fahrtage. Grundlage dieser 
> Prognose ist eine Aussage des Fachbereichs Travelmanagement (Herr Maier), 
> die in einer E-Mail vom 23.04.2026 getroffen wurde (vgl. Anlage 6: 
> E-Mail Travelmanagement)."

### Was dann in die Anlage gehört

**Anlage: E-Mail oder Schreiben des Fachbereichs**
- ✅ Von-Wem, Datum, Medium (E-Mail oder Schreiben)
- ✅ Was wurde ausgesagt (Bedarf für jedes Jahr oder Steigerungsrate)
- ✅ Begründung (warum sich der Bedarf so entwickelt)

---

## Checkliste: Was der User dokumentieren muss

**Für konstanten Bedarf:**
- [ ] User bejaht: Bedarf ist konstant
- [ ] Quelle dokumentieren: Verweis auf Kap. 2 (Ausgangslage)
- [ ] Satz schreiben: „Der Bedarf wird über […] als konstant eingeschätzt, da […]"

**Für variablen Bedarf (mit Quelle):**
- [ ] User nennt jährliche Bedarfe oder Änderungsrate
- [ ] User nennt Quelle (Beschluss, Strategie, Fachbereich, Stellungnahme)
- [ ] Tabelle erstellen: Jahr | Bedarf | Begründung
- [ ] Fließtext schreiben mit Quellenangabe
- [ ] Originalquelle als Anlage beifügen (idealerweise schriftlich)

**Für variablen Bedarf (ohne Quelle):**
- [ ] Vorschlag machen: Auf Fachbereich-Aussage beziehen
- [ ] User kontaktiert Fachbereich per E-Mail
- [ ] E-Mail erhalten und als Anlage eingefügt
- [ ] Tabelle und Fließtext wie oben

---

## Integration in Kapitalwertberechnung

**Wichtig:** Die Bedarfsprognose beeinflusst die **Kostenberechnung pro Jahr**:

```
Kostenberechnung pro Jahr = Bedarf(Jahr) × Kostensatz pro Einheit

Beispiel:
- 2026: 100 Personen × 65.000 EUR/VZÄ = 6.500.000 EUR
- 2027: 110 Personen × 65.000 EUR/VZÄ = 7.150.000 EUR
- ...

Diese jährlichen Kosten fließen dann in die Kapitalwertberechnung ein.
```

**Daher:** Prognose-Fehler wirken sich direkt auf Kapitalwert aus → 
Sensitivitätsanalyse sollte testen, wie empfindlich das Ergebnis 
gegenüber Prognose-Abweichungen ist.

---

## Zusammenfassung: Was in Kap. 1.2 MUSS stehen

✅ Betrachtungszeitraum (z.B. 10 Jahre von 2026–2035)
✅ Konstant oder variabel?
✅ Wenn konstant: Begründung (aus Kap. 2)
✅ Wenn variabel: Tabelle mit jährlichen Bedarfen
✅ Quelle der Prognose (Kap. 2, Fachbereich, Beschluss, etc.)
✅ Fließtext, der die Prognose erklärt

