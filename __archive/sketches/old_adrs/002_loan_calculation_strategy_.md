# ADR-002 Annuityalgorithmen Strategy pattern

## Status
**Proposed**

Datum: 2026-03-01

Autor: Perseus Palma Jacobs

---
Dieses Dokument ist noch nicht fertig und ist nur auf detusch eine zusammengeschriebene idee. 
Das finale englische version muss noch bearbeitet werden.
---

## Kontext
- Unterschiedliche Algorithmen sollen je nach loanstrategy benutzt werden.
- in v1_0 ist es nur die Annuity Calculation
- absehbar sind zb. FÄlligkeits darlehn., Volltilgerdarlehen. außer dem soll in späteren versionen auch mehrere Zusätzliche Berechnungsmodelle erstellt werden. siehe ADR-001

---
domain/
│
├── loan/
│   ├── __init__.py
│   ├── loan.py
│   ├── calculation/
│       ├── __init__.py
│       ├── strategy.py
│       ├── annuity_strategy.py
│       ├── tilgung_strategy.py
│       ├── calculator.py
│       └── parameters.py
│
├── applicant/
│   ├── __init__.py
│   └── applicant.py
│
├── scoring/
│   ├── __init__.py
│   ├── score_result.py
│   └── scoring_rules.py   (später)
│
└── __init__.py

und alles in src ordner tuen.


---
## Entscheidung
Strategy pattern + externe AnnuityParameters classe im domain layer. diese wird dann über das service layer mit hilfe der Loan daten gemapt.
auch das result soll dann in eine Value Object AnnuityReslt gespeichert werden.

---

## Alternativen

### Option A: Hard coden.
Verworfen weil:
- Fachlogick in Domain gehört nicht in SystemLayer
- Jedes Gerüst neu gebaut werden muss.

### Option B: Algorithmus in Domain ohne strategy pattern
Verworfen weil:
- dann muss jede rechenmethode später im system layer hardgecodet werden mit zb. if- else statements. 

---


