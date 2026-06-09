# CR-DSS — Scoring Model v0.2.0

## Goal

Second deterministic credit risk scoring model.

Focus:

- simple
- explainable
- deterministic
- evolvable

This version extends v0.1.0 with reserve coverage and stress testing while remaining suitable for the Python prototype.

---

# Applicant

## Input Fields

- `monthly_net_income`
- `monthly_fixed_costs`
- `existing_monthly_debt_payments`
- `cash_reserve`
- `employment_months`
- `age`

---

# Loan Request

## Input Fields

- `loan_amount`
- `annual_interest_rate`
- `term_months`

---

# Calculation Context

## Input Fields

- `stress`

Example:

```text
{
    "annual_interest_rate_addition": 0.03
}
```

The stress object is passed through the complete CalculationPlan.

Metrics may use the stress configuration if required.

Currently only the `MonthlyAnnuityMetric` consumes the stress value directly.

---

# Derived Metrics

## Monthly Annuity

Standard annuity formula for monthly loan payment.
File: `docs/math/annuity_derivation.md`


If no stress is used:

$$
\text{effective\_annual\_interest\_rate}
=
\text{annual\_interest\_rate}
$$

If stress is used:

$$
\text{effective\_annual\_interest\_rate}
=
\text{annual\_interest\_rate}
+
\text{stress.annual\_interest\_rate\_addition}
$$

---

## TotalDtiMetric

$$
\text{total\_dti}
=
\frac{
\text{existing\_monthly\_debt\_payments}
+
\text{monthly\_annuity}
}{
\text{monthly\_net\_income}
}
$$

Measures debt pressure relative to income.

---

## ResidualIncomeAfterLoanMetric

$
\text{residual\_income\_after\_loan} =
\text{monthly\_net\_income} -
\text{monthly\_fixed\_costs} -
\text{existing\_monthly\_debt\_payments} -
\text{monthly\_annuity}
$

Measures remaining income after all obligations.

---

## ReserveCoverageMonthsMetric

$$
\text{reserve\_coverage\_months}
=
\frac{
\text{cash\_reserve}
}{
\text{monthly\_fixed\_costs}
+
\text{existing\_monthly\_debt\_payments}
+
\text{monthly\_annuity}
}
$$

Measures how long the applicant could survive from savings.

---

# Risk Score

The final risk score combines:

- calculated metrics
- applicant attributes

Each factor contributes risk points.

---

## DTI Risk

| Value | Points |
|---------|---------:|
| $\text{total\_dti} \leq 0.30$ | 0 |
| $\text{total\_dti} \leq 0.40$ | 10 |
| $\text{total\_dti} \leq 0.50$ | 25 |
| $\text{total\_dti} > 0.50$ | 50 |

---

## Residual Income Risk

| Value | Points |
|---------|---------:|
| $\text{residual\_income\_after\_loan} \geq 800$ | 0 |
| $\text{residual\_income\_after\_loan} \geq 500$ | 10 |
| $\text{residual\_income\_after\_loan} \geq 250$ | 25 |
| $\text{residual\_income\_after\_loan} < 250$ | 50 |

---

## Reserve Coverage Risk

| Value | Points |
|---------|---------:|
| $\text{reserve\_coverage\_months} \geq 6$ | 0 |
| $\text{reserve\_coverage\_months} \geq 3$ | 10 |
| $\text{reserve\_coverage\_months} \geq 1$ | 25 |
| $\text{reserve\_coverage\_months} < 1$ | 50 |

---

## Employment Stability Risk

| Value | Points |
|---------|---------:|
| $\text{employment\_months} \geq 24$ | 0 |
| $\text{employment\_months} \geq 12$ | 10 |
| $\text{employment\_months} \geq 6$ | 25 |
| $\text{employment\_months} < 6$ | 40 |

---

## Age Risk

| Value | Points |
|---------|---------:|
| $25 \leq \text{age} \leq 60$ | 0 |
| $18 \leq \text{age} \leq 24$ | 10 |
| $61 \leq \text{age} \leq 70$ | 15 |
| $\text{age} > 70$ | 30 |

---

# Decision Logic

## APPROVE

- $\text{risk\_score} \leq 50$
- $\text{total\_dti} \leq 0.40$
- $\text{residual\_income\_after\_loan} \geq 500$

---

## REVIEW

- $\text{risk\_score} \leq 120$
- $\text{residual\_income\_after\_loan} \geq 250$

Manual review required.

---

## DECLINE

Everything outside the limits above.

---

# Required Metrics

- `monthly_annuity`
- `total_dti`
- `residual_income_after_loan`
- `reserve_coverage_months`

---

# Calculation Modes

## Base Run

```python
stress = null
```

## Stress Run

```python
stress.annual_interest_rate_addition = 0.03
```

The same CalculationPlan is executed again.

Only the `MonthlyAnnuityMetric` changes directly.

All dependent metrics automatically receive stressed values through the dependency chain.

---

# Why v0.2.0?

Compared to v0.1.0 this model adds:

- reserve coverage
- employment stability
- age consideration
- calculation stress support
- weighted risk evaluation
- explainable risk score

while remaining simple enough for the Python prototype and future dependency-based calculation planning.