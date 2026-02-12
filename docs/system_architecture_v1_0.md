system_architecture_v1_0.md
**System Architecture**
Credit Risk Decision Support System
Version 1.0

Stand: Februar
Autor: Perseus Palma Jacobs



**TechStack**
Programmiersprache:         Python3.11+
CLI:                        Standart input/output
Testing:                    pytest
Mathematische Funktionen:   math library
Versionisierung:            Git


**Zielsetzung**
Dieses Dokument beschreibt die technische Struktur des Credit Risk Decision Support Systems (CR-CSS).

Ziel ist eine:  -Modulare
                -wartbare
                -testbare
                -erweiterbare CLI-basierte Python-Anwendung



**Schichtmodell**
Deshalb ist das System als Schichtenarchitektur konzepiert.
 _______________________________________________________
│                  **CLI Interface**                    |
|                                                       |
|        (main.py)                                      |
|       -Eingabe der Nutzerdaten                        |
|       -Aufruf der Application Services                |
|       -Formatierte Ausgabeergebnisse                  |
|       -Keine RechenLogik!                             |
|_______________________________________________________|
│                 **Application Layer**                 |
|                                                       |
|       (credit_evaluation_service.py)                  |
|       -Dient als zentrales Koordinationssystem        |
|       -Erstellung von Domain-Objekten                 |
|       -Berechnung der Annuität                        |
|       -Durchführung des Scorings                      |
|       -Rückgabe des Ergebnisses                       |
|_______________________________________________________|
│                 **Domain / Business**                 |
|                                                       |
|       Enthält reine Geschäftsobjekte                  |
|                                                       |
|       (applicant.py)                                  |
|       -Repräsentiert den Antragsteller.               |
|       -name                                           |
|       -age                                            |
|       -monthly_income                                 |
|       -fixed_costs                                    |
|       -employment_years                               |
|                                                       |
|       (loan.py)                                       |
|       -Repräsentiert den beantragten Kredit           |
|       -principal                                      |
|       -interest_rate                                  |
|       -duration_months                                |
|                                                       |
|       (score_result.py)                               |
|       speichert:                                      |
|       -total_score                                    |
|       -risk_category                                  |
|       -detailed_breakdown                             |
|_______________________________________________________|
│              **Calculation / Services**               |
|                                                       |
|       Enthält Geschäftslogik                          |
|                                                       |
|       (annuity_calculator.py)                         |
|       -calculate_annuity()                            |
|       -calculate_totale_payment()                     |
|       -calculate_total_interest()                     |
|                                                       |
|       (scoring_service.py)                            |
|       -Berechnung DTI                                 |
|       -Haushaltsüberschuss                            |
|       -Punktevergabe je Faktor                        |
|       -Gesamtscoreberechnung                          |
|       -Risikoklassifizierung                          |
|_______________________________________________________|
|                  **Utility Layer**                    |
|                                                       |
|       (input_validation.py)                           |
|       -Typprüfung                                     |
|       -Wertebereichsprüfung                           |
|       -Sonderfallbehandlung (z.B Zinssatz = 0)        |
|_______________________________________________________|
│               **Persistence (opt.)**                  |
|_______________________________________________________|

Idee der Schichtenarchitektur:
    -Trennung von Fachlogik und Ein-/Ausgabe
    -Keine Geschäftslogik im CLI
    -Reine Funktionen für Berechnungen
    -Erweiterbarkeit für Web-API (v2.0)
    -Unit-Test-Fähigkeit



**Projekt Struktur**
credit_risk_system/
│
├── main.py
│
├── domain/
│   ├── applicant.py
│   ├── loan.py
│   └── score_result.py
│
├── services/
│   ├── annuity_calculator.py
│   ├── scoring_service.py
│
├── application/
│   └── credit_evaluation_service.py
│
├── utils/
│   └── input_validation.py
│
├── tests/
│
├── docs/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore



**Datenfluss**
1.CLI sammelt Eingaben
2.Application Layer erstellt Domain-Objekte
3.Annuity Calculator berechnet Kreditrate
4.ScoringService berechnet Score
5.ScoreResult wird zurückgegeben
6.CLI formatiert Ausgabe



**Roadmap**
Geplante Erweiterungen
    -JSON-Export der Ergebnisse
    -Speicherung in SQLite
    -Rest-API (FastAPI)
    -Web-Frontend
    -Erweiterte Risikomodelle