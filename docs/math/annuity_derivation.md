# Herleitung der Annuitätenformel

## Ziel

Herleitung der Formel für die konstante Annuität $A$, mit der ein Kredit vollständig getilgt wird.

Gegeben:

- Anfangsdarlehen: $K_0$
- Zinssatz pro Periode: $i$
- Laufzeit: $n$ Perioden

Gesucht:

- Konstante Rate $A$

---

## 1. Grundprinzip: Barwertgleichheit

Ein Kredit entspricht dem Barwert aller zukünftigen Ratenzahlungen.


$K_0 = \text{Barwert aller Annuitäten}$


Jede Zahlung $A$, die in Periode $k$ erfolgt, wird abgezinst:


$\frac{A}{(1+i)^k}$


Damit ergibt sich:

$
K_0 =
\frac{A}{1+i}
+
\frac{A}{(1+i)^2}
+
\dots
+
\frac{A}{(1+i)^n}
$

---

## 2. Ausklammern von A

$
K_0 =
A \cdot
\left(
\frac{1}{1+i}
+
\frac{1}{(1+i)^2}
+
\dots
+
\frac{1}{(1+i)^n}
\right)
$

Der Klammerausdruck ist eine geometrische Reihe.

---

## 3. Geometrische Reihe

Allgemeine Formel:


$
\sum_{k=1}^{n} q^k = \frac{q(1-q^n)}{1-q}
$


Hier gilt:

$
q = \frac{1}{1+i}
$

---

## 4. Einsetzen

$
K_0 =
A \cdot
\frac{\frac{1}{1+i} \left(1 - \left(\frac{1}{1+i}\right)^n\right)}
{1 - \frac{1}{1+i}}
$

---

## 5. Nenner vereinfachen

$
1 - \frac{1}{1+i} = \frac{i}{1+i}
$

---

## 6. Kürzen

Nach Kürzen ergibt sich:

$
K_0 = A \cdot \frac{1 - (1+i)^{-n}}{i}
$

---

## 7. Auflösen nach A

$
A = K_0 \cdot \frac{i}{1 - (1+i)^{-n}}
$

---

# Ergebnis: Annuitätenformel

$
A =
K_0 \cdot
\frac{i}{1 - (1+i)^{-n}}
$

---

## Alternative Darstellung mit q

Setzt man

$
q = 1 + i
$

ergibt sich äquivalent:

$
A =
K_0 \cdot
\frac{q^n (q-1)}{q^n - 1}
$

Beide Darstellungen sind mathematisch identisch.

---

## Abgrenzung
### Numerische und modelltheoretische Wahl der i-Darstellung

Obwohl die Darstellung mit dem Aufzinsungsfaktor $q = 1+i$ algebraisch äquivalent ist, wird im Projekt bewusst die $i$-Form

$
A = K_0 \cdot \frac{i}{1 - (1+i)^{-n}}
$

verwendet. 

Gründe sind:

1. Der Zinssatz $i$ ist der ökonomisch primäre Modellparameter.
2. Die Darstellung verwendet direkt den ökonomischen Modellparameter i und entspricht unmittelbar der Herleitung der Barwertgleichheit.
3. Sensitivitäts- und Risikobetrachtungen erfolgen direkt in Bezug auf $i$.

Die Wahl ist somit sowohl mathematisch als auch modellarchitektonisch begründet.

für zukunft:
kann bei sehr kleinen zinssätzen instabil werden -> siehe taylor-aproximation, oder wie profesionelle finanzibliotheken das implementieren


## Interpretation

- Höherer Zinssatz → höhere Annuität
- Längere Laufzeit → geringere Annuität
- Bei $i = 0 \: \ A = \frac{K_0}{n}$

---

## Bedeutung für das Projekt

Die Annuitätenformel bildet die Grundlage für:

- Tilgungsplanberechnung
- Zins-/Tilgungsanteile pro Periode
- Restschuldformel
- Sensitivitätsanalysen
- Kreditrisikomodellierung

Sie ist eine direkte Anwendung der Barwertgleichheit und der geometrischen Reihe.


## Computer-optimierte Formel (Implementation)

Die mathematische Herleitung verwendet die Barwertform:

$
A = K_0 \cdot \frac{i}{1 - (1+i)^{-n}}
$

Für die Implementierung wird die algebraisch äquivalente Form

$
A =
K_0 \cdot
\frac{i(1+i)^n}{(1+i)^n - 1}
$

verwendet. Dadurch kann der Term $(1+i)^n$ einmal berechnet und wiederverwendet werden:

```python
term = (1 + i) ** n
monthly_annuity = K0 * ((i * term) / (term - 1))
```

### Benchmark (in c++)

| Variante                    | Laufzeit |
|-----------------------------|----------|
| Unoptimiert (`pow` zweimal) |   251 ms |
| Optimiert (`pow` einmal)    |   143 ms |
| Negative Exponentenform     |   144 ms |

### High-Precision-Gegenprüfung (in Python)

| Variante                           | Abweichung zur Referenz |
| ---------------------------------- | ----------------------: |
| Optimierte positive Exponentenform |      $0 \cdot 10^{-97}$ |
| Negative Exponentenform            |      $1 \cdot 10^{-97}$ |


---

Eine zusätzliche Prüfung in Pyhton `Decimal` (100 Stellen Präzision) zeigte, dass beide Formeln praktisch identische
Ergebniss liefern. Die positive Exponentenform lag dabei minimal näher am Referenzwert.


Für das Projekt wird daher die positive Exponentenform verwendet, da sie mathematisch äquivalent, leicht effizienter
und für typische Kreditparameter numerisch ausreichend stabil ist.

---
$$
A:(K0​,i,n)↦K0​⋅1−(1+i)−ni​
$$