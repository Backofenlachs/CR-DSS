# ADR-001: 4-Layer-Architektur als Grundstruktur 

## Status
**Accepted** (planned for v1.0)

Datum: 2026-03-01

Autor: Perseus Palma Jacobs

---

## Kontext
Das Credit Risk Decicion Support System (CR-DSS) startet als CLI-Anwendung zur bewertung von Kreditanträgen (Rate --> Kennzahlen wie DTI --> Score/Risikoklasse)

Zu Projektbeginn ist absehbar, dass das System in späteren Version erweitert wird um:

- **Mehrere Interfaces** (CLI, Web-UI. ggf REST-API)
- **Zusätzliche Berechnungsmodelle** Weitere Kreditarten, Regeln, Strategien (Tilgungszins)
- **Weitere Use Cases** z. b.Erstellen von Darlehns-Plänen
- **Persistenz** für interne Datenspeicherung und abfrage
- **Data Science / ML-Komponenten** z.b. Deep-Learning-Modelle zur Risikoprognose
- **Externe Datenquellen** z. b. SCHUFA-Score oder ähnliche externe Scores, Daten aus Fremdsystemen

Aufgrund der zunehmenden Komplexität der Software in späteren Versionen wird eine Architektr benötigt, die:
- einfache **Erweiterbarkeit** fördert,
- **Testbakeit** sicherstellt,
- **Domänenlogik schüztz und separiert** (unabhängig vn UI/DB/externen Serevices.)

---

## Entscheidung
Das CR-DSS wird vo nanfang an in einer 4-Layer-Architektur strukturiert:

1. **Presentation Layer**: CLI/UI/API, Input/OUtput
2. **Application Layer**: Use-Case-Orchestrierung (z. b. "Evaluate Credit", später "Generate Loan Plan")
3. **Service Layer**: fachliche Services / Integrationskoordination (z. b. Scoring, Loan Calculation, spätere ML-Scoring, Data Enrichment)
4. **Domain Layer**: Domänenmodelle und Kernlogig (Entities, Value Objects, dataclasses, Strategien)

### Abhängigkeiten
von außen nach innen:
```text
Presentation --> Application --> Service --> Domain
```
**Domain** darf dabei keine Abhängigkeiten zu den anderen schichten, externen APIs oder Frameworks besitzen.

Persistence und externe Datenquellen werden als **Adapter außerhalb der Domain implementiert und über Schnittstellen eingebunden (z. B. Repository-Interfaces)

### Begründung
Die 4-Layer-Strucktur wurde gewählt, um golgenede Ziele zu erreichen:

- **Seperation of Concerns**: Use-Case-Orchestrierung, Services und Domänenmodell bleiben getrennt.
- **Austauschbarkeit der UIs**: CLI, Web-UI oder API können im Service Layer angebunden werden, ohne dass die Domain von ihnen abhängt.
- **Integrations exterternen Datenquellen**: Externe Score/Daten können im Service Layer angebunden werden, ohne das die Domain von ihnen abhängt.
- **Testbarkeit**: Domain und Application können isoliert getrennt und getestet werden
- **Vorbereitung auf ML/DL**: Modelle kann als Service gekapselt werden; Domain bleibt stabil, während sich ML-Implementierung ändern.

---

## Alternativen

### Option A: Keine Layering Struktur (alles in einem Modul)
Verworfen, weil:
- Hohe Vermischung von UI, Persistenz und Integration
- Schlechte Wartbarkeit bei wachsender Funktionalität
- Erschwerte Tests

### Option B: 3-Layer-Architektur (Presentation -> Application -> Domain)
Warum nicht gewählt?
- Application Layer würde fachlich überladen
- Integrationslogik würde direkt in Use Case landen
- Geringere strukturelle Klarheit

### Option C: Vollständige Clean/Hexagonal Architecture (Ports & Adapters)
Warum nicht gewählt?
- Höherer Initialer Struktur und Abstraktionsaufwand
- Für Projektstart überproportianale Komplexität
- Kann bei Bedarf später evolutiv eingeführt werden

---

## Konsequenzen

### Positive
- klare Verantwortlichkeiten pro Layer
- Gute Testbarkeit der Domain- und Application-Logik
- Austauschbarkeit von UIs (CLI --> Web/API)
- Vorbereitung auf ML-Integration und externe Datenquellen
- Gute langfristige Wartbarkeit

### Negative
- Mehr struktureller Aufwand zu Beginn
- Erfordert Disziplin bei der Einhaltung der Abhängigkeitsregel
- Potentielles Overengineering in frühen Versionen

---