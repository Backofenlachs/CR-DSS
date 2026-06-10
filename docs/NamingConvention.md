## Uppercase Pipeline Artifacts

In CR-DSS, uppercase local variables represent finalized pipeline artifacts.

Pipeline artifacts are produced by one processing stage and consumed by the next. Once created, they should be treated as immutable and must not be modified by downstream components.

Examples:

* APPLICANT_DATA
* DEPENDENCY_PLAN
* CALCULATION_RESULT
* SCORE_RESULT
* APPLICANT_RESULT

Mutable runtime variables and temporary calculation data should remain lowercase.

Uppercase parameters indicate immutable pipeline artifacts
received from a previous processing stage.