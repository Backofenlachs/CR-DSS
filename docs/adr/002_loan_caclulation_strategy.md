adr_load_calculation_strategy_v1_0.md
**Architektur Decision Report Strategy Pattern**
Credit Risk Decision Support System
Version 1.0

Stand: Februar
Autor: Perseus Palma Jacobs



**Zielsetzung**
Im CR-DSS muss eine monatliche Kreditrate berechnet werden, da sie Grundlage für die folgende Konzepte ist: DTI, Haushaltsüberschuss, Gesamtrisiko. 
Die wahl des Kreditmodells beeinflusst indirekt die Risikobewertung.



**Annuitäten Darlehn**
In Version 1_0 wird ausschließlich das Annitäten Darlehn verwendet da es:
    -Standart im Retailbanking ist
    -Konstante monatliche Rate:
    -Planbare Cashflows
    -Stabile DTI- Berechnung
    -Realitätsnah für Konsumkredite



**Technische Architekturentscheidung: Strategie Pattern**
    -austauschbare Berechnungslogik
    -Erweiterbarkeit ohne Code änderung
    -Einhalten des Open-Closed-Prinzips

**Gemeinsame Schnittstelle**
LoanCalculationStrategy
    calcularte_monthly_payment(loan)



**Konkrete Implementierungen:**
    AnnuityStrategy (Version 1.0)
    TilgungStrategy (geplante Erweiterung)
    Weitere Modelle (Version 2.0+)



**Zusammenfassung**
Für Version 1.0 wurde bewusst das Annuitätendarlehen gewählt, da es:
dem Standard im Privatkundengeschäft entspricht

-konstante Zahlungsströme liefert
-eine stabile Risikobewertung ermöglicht

Gleichzeitig wurde die Architektur so gestaltet, dass weitere Kreditmodelle mithilfe des Strategy Patterns problemlos ergänzt werden können.

Diese Entscheidung verbindet fachliche Realitätsnähe mit technischer Erweiterbarkeit.