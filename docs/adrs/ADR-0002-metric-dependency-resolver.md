# ADR-0002: Metric Dependency Resolver

## Status
**Accepted**

Date: 07.06.2026

Author: Perseus Palma Jacobs

---

## Context

At the current state, a `ScoringModel` depends on multiple calculation metrics (Kennzahlen) to evaluate an applicant
score.

Depending on the metrics defined in: `ScoringModel.REQUIRED_METRICS`

the CR-DSS must:

1. Resolve all required metrics.
2. Resolve all transitive metric dependencies.
3. Bring all metrics into a valid calculation order.
4. Gather all required user inputs.
5. Execute the calculations and provide the result to the `ScoringModel`.

Currently there is no dependency planning or topological sorting mechanism available.

Therefore, the `CalculationService` contains a hard-coded calculation sequence and is not able to adapt automatically
to different requirements of different ScoringModels.

As the number of ScoringModels grows, this approach becomes increasingly difficult to maintain.

---

## Decision

We introduce a dedicated component called:
`MetricDependencyResolver`

The resolver is responsible for exploring and resolving the complete metric dependency graph. Based on:

- the metrics required by the `ScoringModel`
- all registered metrics in the `MetricsRegistry`

the resolver:

1. Resolves all required metrics and dependencies.
2. Assigns dependency levels to every metric.
3. Collects all required inputs.
4. Generates a calculation plan.

The result of the resolution process is:
```py
{
    "levels": levels,
    "required_inputs": required_inputs,
    "processed_metrics": processed_metrics
}
```

The returned information serves different purposes:
- `levels` contains the generated calculation plan.
- `required_inputs` contains all inputs needed by the calculation process.
- `processed_metrics` contains debugging and tracking information about all discovered metrics and their
  assigned levels.

---

### Level Assignment

Metrics are categorized in to dependency levels.

The resulting structure is represented as:
```py
levels = [
    [], # Level N
    [], # Level N-1
    ...
    [] # Level 1
]
```
The resolver starts at the highest dependency level and continues recursively towards lower dependency levels.

Every discovered metric is registered inside:
```py
processed_metrics = {
    metric_name: level
}
```
and added to the corresponding level inside the `levels` structure.

If a metric is discovered again on a deeper dependency path and already exists inside `processed_metrics` the
metric is moved to the lower dependency level.

This guarantees that metrics are eventually assigned to the lowest valid dependency level discovered during
graph exploration.

---

### Calculation Plan Execution

The generated `levels` structure represent the final calculation plan.

The `CalculationService` executes this plan in reverse order.

This ensures that all required dependencies have already been calculated bevor a metric is evaluated.

---

### Design Decision

Dependency expansion and level assignment are intentionally combined into a single recursive traversal.

During graph exploration the resolver simultaneously:

- resolves dependency levels
- assign dependency levels
- collect required inputs
- builds the final calculation plan

This decision was made to keep the architecture simple, understandable and educational.

The disadvantages of this approach are accepted because the expected dependency depth within the CR-DSS domain is small
and limited by the business context.

---

## Consequences

### Advantages
- Supports multiple ScoringModels.
- Removes hard-coded calculation pipelines.
- Automatically resolves metric dependencies.
- Automatically gathers required inputs.
- Produces a deterministic calculation plan.
- Provides additional debugging and tracking information through `processed_metrics`

### Disadvantages
- Dependency resolution and level assignment are coupled.
- Recursive graph traversal may become harder to maintain for very large dependency graphs.
- The current implementation is optimized for simplicity and transparency rather than maximum scalability.

---


## Known Failure Scenarios

### Circular Dependencies

A circular dependency can lead to an endless resolution loop.

Example:
```
MetricA
 └─ MetricB
     └─ MetricA
```

Such a structure is considered invalid.

Since every metric represents the calculation of a single buisness metric (Kennzahl), a metric should never require
itself directly or indirectly.

---

### Missing Metric Registration

A metric dependency may reference a metric which is not registered inside the MetricsRegistry.

Problem causes:
- Missing metric registration.
- Typographical errors.
- Incorrect registry keys.
- Incorrect entries inside `REQUIRED_METRICS`.

In such cases the resolver must fail because the dependency graph cannot be completed.

---

### Extreme Dependency Depth

The maximum depth of the dependency graph is theoretically unknown.

Very deep dependency graphs could eventually cause problems due to recursion depth or excessive memory consumption.

Within the current CR-DSS domain this risk is considered negligible.

The system is not expected to contain thousands of dependency levels or thousands of calculation metrics.

Future simulation models are not expected to significantly affect this assumption because simulations are treated
as isolated calculation units in the same way as individual calculation metrics.