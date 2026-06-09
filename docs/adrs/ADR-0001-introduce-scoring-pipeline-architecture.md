# ADR-0001: Introduce Scoring Pipeline Architecture

## Status
**Accepted**

Date: 23.05.2026

Author: Perseus Palma Jacobs
---

## Context

At the beginning of the project, we want to define the minimal architectural foundation for the first
CR-DSS prototype.

The goal is not to prematurely build a large enterprise architecture, but to establish a small and
evolvable structure early enough so that future scoring models and calculation logic can grow without
rewriting the entire system.

At the moment, there exists only a very small prototype implementation (~100 lines of code) written
mainly to:

- Test the overall idea,
- validate the first calculation flow,
- experiment with naming and responsibilities,
- and define the first scoring metrics.

Current flow:

```text
loan-request.json
        ↓
basic calculations
        ↓
scoringModel_v0.1.0
        ↓
loan-result.json
```

Currently, most logic is implemented directly inside a single `main.py` file with only small helper functions.
The prototype currently behaves more like a simple script than a structured application.

---

## Problem

The current implementation contains multiple hardcoded dependencies and responsibilities inside one file.

Examples:

- Input handling,
- Mathematical calculations,
- Metric calculations,
- Scoring logic,
- Output generation,

are all mixed together.

This becomes problematic because the future architecture requires dynamic scoring behavior.

The intended future direction is:

```text
Input
    ↓
Calculation Metrics
    ↓
Scoring Model
    ↓
Output
```

However, the required calculations are not globally fixed.

Different scoring models may require:
- different metrics,
- different calculation orders,
- and later even different required inputs

This means:

- The selected `ScoringModel` determines which metrics are required,
- and the required metrics determine which inputs are required.
  
Additionally, later versions should support selecting the scoring model dynamically via loan request
configuration.

Without separation of responsibilities, every new scoring model would duplicate calculation logic and
increase coupling between input handling, calculations, and scoring behavior. 

---

## Decision

The application will be refactored into a small scoring pipeline architecture with separated responsibilities.

### Step 1 - Responsibility Separation

The system will be separated into three main layers:

#### IO Handlers
Responsible for:

- Reading input files,
- writing output files,
- and handling serialization/deserialization.

Examples:
```text
loan-request.json
loan-result.json
```

IO handlers must not contain scoring logic.

---

#### Calculation Metrics
Responsible for:

- calculation reusable financial metrics,
- and deriving values from the loan request input

Examples:

- monthly_annuity
- affordability_ratio
- debt_to_income

Calculation metrics are intended to become reusable building blocks for multiple scoring models.

---

#### Scoring Models

Responsible for:
- evaluating calculated metrics,
- and generating a scoring result.

In the first implementation stage, scoring models will only consume calculated metrics and will not directly 
access raw input values.

---

## Step 2 - Required Metrics Declaration

Scoring models will explicit declare which metrics they require.

Example:

```Python
required_metrics = [
    "monthly_annuity",
    "affordability_ratio"
]
```

Each calculation metric may later declare:

- required input fields,
- and required dependent metrics

Example:
 
```python
required_inputs=[
    "monthly_income"
]
```

This creates a controlled dependency direction:

```text
ScoringModel
        ↓
required_metrics
        ↓
CalculationMetrics
        ↓
required_inputs
        ↓
Input
```

---

#### Orchestration

For the current prototype stage, `main.py` will remain the main orchestrator of the domain pipeline.

The planned high-level flow is:

```text
read input
        ↓
select scoring model
        ↓
check required metrics
        ↓
calculate metrics
        ↓
execute scoring model
        ↓
write result
```

---

## Consequences

### Positive

- Clear separation of responsibilities
- Reusable metric calculations
- Reduced duplication between scoring models
- Easier future extension of scoring logic
- Easier introduction of multiple scoring models
- Better maintainability compared to a monolithic script
- Better foundation for future validation and testing

### Negative

- More files and structural complexity
- Additional orchestration logic required
- Dependency ordering between metrics must be handled carefully
- Slightly more abstraction than required for the current prototype size
- Early architectural decisions may still evolve during later project stages.
