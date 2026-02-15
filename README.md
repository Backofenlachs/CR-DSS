# Credit Risk Decision Support System (CR-DSS)

Ein modular aufgebautes Entscheidungsunterstützungssystem zur Bewertung von Konsumentenkreditanträgen auf Basis finanzwirtschaftlicher Kennzahlen und eines strukturierten Scoring-Modells.



**Ziel des Projekts**

Das CR-DSS simuliert einen vereinfachten Kreditprüfungsprozess im Retailbanking.

Das System berechnet:
  - die monatliche Kreditrate (Annuität)
  - die Debt-to-Income-Ratio (DTI)
  - den monatlichen Haushaltsüberschuss
  - einen strukturierten Gesamtrisikoscore

Das Projekt demonstriert:
  - saubere Architekturprinzipien
  - Trennung von Fachlogik und Anwendungsschicht
  - finanzmathematische Modellierung
  - testgetriebene Entwicklung (TDD)
  - versionierte Architekturentscheidungen (ADR)
  - Erweiterbarkeit durch das Strategy Pattern



## Architekturübersicht

Das System ist schichtbasiert aufgebaut:

  - **Domain**
    Zentrale Fachobjekte (Applicant, Loan, ScoreResult)

  - **Services**
    Fachlogik wie Annuitätenberechnung und Scoring
  
  - **Application**
    Orchestrierung der Anwendungslogik
  
  - **CLI (main.py)**
    Benutzerschnittstelle zur Interaktion

Die Architektur folgt dem Prinzip der klaren Verantwortlichkeitstrennung (Separation of Concerns).



## Implementierte Funktionen (Version 1.0)

  - Annuitätendarlehen (konstante Monatsrate)
  - Berechnung der Debt-to-Income-Ratio
  - Ermittlung des Haushaltsüberschusses
  - Punktbasiertes Risikoscoring
  - Unit-Tests für die Domain-Schicht



## Tests

Tests werden mit pytest ausgeführt:

pytest -v


Optional mit Coverage-Analyse:

pytest --cov=.



## Dokumentation

Architektur- und Fachentscheidungen sind dokumentiert unter:

docs/architecture/

Enthalten sind:
  - Systemarchitektur (v1.0)
  - Scoring-Modell
  - Architecture Decision Records (ADR)



## Version

Aktuelle Version: 1.0

Geplante Erweiterungen:

  - Unterstützung weiterer Kreditmodelle (Strategy Pattern)
  - Erweiterung des Scoring-Modells
  - Persistenzschicht
  - API-Schnittstelle


# To Do
- annuity mathematisch herleiten doc erstellen
- anfangen zu coden anfangen mit domain layer

programmier reinfolge:
  - Alle datenclassen in Domainlayer machen
  - annuity calculator
  - scoring service
  - application layer
  - CLI
    core anwendung fertig dannach:
  - input validation
  - neue erweiterungen implementieren und planen

### Autor: Perseus Palma Jacobs

