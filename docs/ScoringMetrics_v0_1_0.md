# CR-DSS — Minimal Credit Risk Prototype Metrics

## Goal

Minimal first prototype for a basic credit risk / loan affordability evaluation.

Focus:
- simple
- understandable
- evolvable
- suitable for first Python CLI prototype

---

# Applicant

## Input Fields

- `monthly_net_income`
- `monthly_fixed_costs`
- `existing_monthly_debt_payments`

---

# Loan Request

## Input Fields

- `loan_amount`
- `annual_interest_rate`
- `term_months`

---

# Derived Metrics

## Monthly Annuity

Standard annuity formula for monthly loan payment.
File: `docs/math/annuity_derivation.md`


---

## Total DTI

Debt-To-Income ratio including the new loan.

$
\text{total\_dti} =
\frac{
\text{existing\_monthly\_debt\_payments}
+
\text{monthly\_annuity}
}{
\text{monthly\_net\_income}
}
$

Interpretation:
- lower is better
- measures debt pressure relative to income

---

## Residual Income After Loan

Remaining income after all obligations.

$
\text{residual\_income\_after\_loan} =
\text{monthly\_net\_income} -
\text{monthly\_fixed\_costs} -
\text{existing\_monthly\_debt\_payments} -
\text{monthly\_annuity}
$

Interpretation:
- measures practical survivability after loan obligations
- very intuitive metric for first prototype

---

# Basic Scoring Logic

## APPROVE

Conditions:

- `total_dti <= 0.35`
- `residual_income_after_loan >= 500`

---

## REVIEW

Conditions:

- `total_dti <= 0.45`
- `residual_income_after_loan >= 250`

Manual review required.

---

## DECLINE

Everything outside the limits above.

---

# Notes

## Why no affordability_ratio?

Currently unnecessary because:

- `total_dti`
- `residual_income_after_loan`

already describe affordability sufficiently for a minimal prototype.

Adding additional ratios too early would likely duplicate meaning and overcomplicate the first implementation.

---

# Prototype Scope

This is intentionally conservative and simplified.

The first Python CLI prototype should focus on:

- clean architecture
- deterministic calculations
- reproducibility
- traceable scoring logic
- extensibility for future risk engine evolution

Not on realistic banking-grade underwriting yet.

---

# Planned Evolution

Future versions may later include:

- credit score integration
- probabilistic risk scoring
- collateral handling
- employment stability
- behavioral scoring
- statistical calibration
- stress testing
- ML-assisted scoring
- dedicated C++ risk engine

Python is currently only the prototype layer.
The long-term architecture already plans a dedicated C++ risk engine.