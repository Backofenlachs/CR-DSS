**Scoring-Modell**
Credit Risk Decision Support System
Version 1.0

Stand: Februar 2026
Autor: Perseus Palma Jacobs



**Zielsetzung:**
Das Scoring-Modell Version 1.0 dient der strukturierten, regelbasierten Bewertung der Kreditwürdigkeit eines Antragstellers.

Ziel ist es, auf Basis transparenter wirtschaftlicher Kennzahlen eine nachvollziehbare Risikoklassifizierung vorzunehmen.
Das Modell simuliert in vereinfachter Form Entscheidungslogiken aus dem Retail-Banking.

Das System ersetzt keine reale Bonitätsprüfung, sondern dient als konzeptionelles Entscheidungsunterstützungssystem.



**Modellübersicht:**
Das Modell basiert auf fünf unterschiedlich gewichteten Bewertungsfaktoren und die Maximal erreichbare Punktzahl ist 100.

| Bewertungsfaktor                         | Max. Punkte    | Gewichtung |
| ---------------------------------------- | -------------- | ---------- |
| Debt-to-Income Ratio (DTI)               | 30             | 30 %       |
| Haushaltsüberschuss                      | 25             | 25 %       |
| Beschäftigungsdauer                      | 15             | 15 %       |
| Alter                                    | 10             | 10 %       |
| Kreditbetrag im Verhältnis zum Einkommen | 20             | 20 %       |
| **Gesamt**                               | **100 Punkte** | 100 %      |



**Bewertungslogik:**
**Dept-To-Income Ratio (DTI)**
Definition: Gesammtbelastung / Einkommen
Bewertung:
| DTI         | Punkte |
| ----------- | ------ |
| < 20 %      | 30     |
| 20 % – 35 % | 20     |
| 35 % – 50 % | 10     |
| > 50 %      | 0      |

**Haushaltsüberschuss**
Definition: Einkommen - Fixkosten - bestehende_reditraten
Bewertung:
| DTI         | Punkte |
| ----------- | ------ |
| < 20 %      | 30     |
| 20 % – 35 % | 20     |
| 35 % – 50 % | 10     |
| > 50 %      | 0      |

**Beschäftigungsdauer**
Bewertung der wirtschaftliche Stabilität.
Bewertung:
| Dauer       | Punkte |
| ----------- | ------ |
| > 5 Jahre   | 15     |
| 2 – 5 Jahre | 10     |
| 1 – 2 Jahre | 5      |
| < 1 Jahr    | 0      |

**Alter**
Statistische Risikobewertung basierend auf Erwerbsalter.
Bewertung:
| Alter          | Punkte |
| -------------- | ------ |
| 25 – 55 Jahre  | 10     |
| 18 – 24 Jahre  | 5      |
| 56 – 65 Jahre  | 5      |
| < 18 oder > 65 | 0      |

**Kreditbetrag relativ zum Einkommen**
Definition: Verhältniss = Kredithöhe / (12 * einkommen)



**Gesamt Score:**
Score = Summe aller Teilwerte



**Risikoklassifizierung:**
| Scorebereich | Risikokategorie | Handlungsempfehlung                         |
| ------------ | --------------- | ------------------------------------------- |
| 80 – 100     | Niedrig         | Kredit empfehlenswert                       |
| 50 – 79      | Mittel          | manuelle Prüfung empfohlen                  |
| < 50         | Hoch            | Kredit nicht empfehlenswert                 |