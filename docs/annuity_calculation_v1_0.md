📘 Annuitätenberechnung – Version 1.0
1. Ziel der Berechnung

Im Credit Risk Decision Support System (CR-DSS) wird die monatliche Kreditrate (Annuität) berechnet, um:

die monatliche Belastung des Antragstellers zu bestimmen

die Debt-to-Income-Ratio (DTI) zu berechnen

den Haushaltsüberschuss zu ermitteln

die Grundlage für das Scoring-Modell zu schaffen

Die Annuität ist eine konstante monatliche Rate, die sowohl Zins als auch Tilgungsanteil enthält.

2. Mathematische Definition

Gegeben:

𝐾
K = Kreditbetrag (Principal)

𝑝
p = nominaler Jahreszinssatz (in Prozent)

𝑖
i = monatlicher Zinssatz

𝑛
n = Laufzeit in Monaten

𝐴
A = monatliche Annuität

2.1 Umrechnung des Zinssatzes

Der Jahreszinssatz wird in einen monatlichen Zinssatz umgerechnet:

𝑖
=
𝑝
100
⋅
12
i=
100⋅12
p
	​

2.2 Annuitätenformel

Die monatliche Annuität ergibt sich aus:

𝐴
=
𝐾
⋅
𝑖
(
1
+
𝑖
)
𝑛
(
1
+
𝑖
)
𝑛
−
1
A=K⋅
(1+i)
n
−1
i(1+i)
n
	​

3. Sonderfall: Zinssatz = 0 %

Falls 
𝑖
=
0
i=0, würde die Formel zu einer Division durch Null führen.

In diesem Fall gilt:

𝐴
=
𝐾
𝑛
A=
n
K
	​


Das bedeutet:

keine Zinsen

lineare Rückzahlung

4. Interpretation der Formel

Die Formel basiert auf der finanzmathematischen Annahme einer konstanten Rate über die gesamte Laufzeit.

Die Rate setzt sich zusammen aus:

Zinsanteil (anfangs hoch)

Tilgungsanteil (anfangs niedrig)

Mit zunehmender Laufzeit:

sinkt der Zinsanteil

steigt der Tilgungsanteil

Die Gesamtzahlung ergibt sich aus:

𝐺
𝑒
𝑠
𝑎
𝑚
𝑡
𝑧
𝑎
ℎ
𝑙
𝑢
𝑛
𝑔
=
𝐴
⋅
𝑛
Gesamtzahlung=A⋅n
5. Bedeutung im CR-DSS

Die berechnete Annuität wird verwendet für:

Debt-to-Income-Ratio (DTI)

𝐷
𝑇
𝐼
=
𝐴
𝑚
𝑜
𝑛
𝑎
𝑡
𝑙
𝑖
𝑐
ℎ
𝑒
𝑠
𝐸
𝑖
𝑛
𝑘
𝑜
𝑚
𝑚
𝑒
𝑛
DTI=
monatlichesEinkommen
A
	​


Haushaltsüberschuss

𝑈
¨
𝑏
𝑒
𝑟
𝑠
𝑐
ℎ
𝑢
𝑠
𝑠
=
𝐸
𝑖
𝑛
𝑘
𝑜
𝑚
𝑚
𝑒
𝑛
−
𝐹
𝑖
𝑥
𝑘
𝑜
𝑠
𝑡
𝑒
𝑛
−
𝐴
U
¨
berschuss=Einkommen−Fixkosten−A

Diese Kennzahlen fließen in das Scoring-Modell Version 1.0 ein.

6. Fachliche Annahmen (Version 1.0)

Zinssatz ist fix über gesamte Laufzeit

Keine Sondertilgungen

Keine Restschuldversicherung

Keine Gebühren berücksichtigt

Monatliche Zahlung am Periodenende

7. Beispielrechnung

Gegeben:

Kreditbetrag: 10.000 €

Zinssatz: 5 %

Laufzeit: 36 Monate

Monatlicher Zinssatz:

𝑖
=
5
100
⋅
12
=
0,004167
i=
100⋅12
5
	​

=0,004167

Eingesetzt in die Formel ergibt sich eine monatliche Rate von ca.:

𝐴
≈
299
,
71
€
A≈299,71€