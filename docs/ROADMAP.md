# CR-DSS Roadmap

## Phase 1 — UI-Engine
Status: **Completed**

Estimated time: 6–8 weeks  
Actual time needed: 7 weeks

- [x] Create standalone UI-Engine prototype
- [x] Define AppShell structure
- [x] Implement MountingEngine
- [x] Standardize BaseTool lifecycle
- [x] Add LayoutConfig structure
- [x] Runtime management
- [x] Document UI-Engine architecture
- [x] Create UI-Engine v0.2.0 snapshot

---

## Phase 2 — Python Scoring Prototype
Status: **In Progress**

Estimated time: 4–6 weeks

- [x] Create first scoring prototype
- [x] Implement first scoring model
- [x] Create ADR-0001
- [x] Separate scoring pipeline
- [ ] Introduce `required_metrics` (to handle reverse dependencies)
- [ ] Add second scoring model
- [ ] Multiple scoring model selection
- [ ] Standardize scoring model interfaces
- [ ] Introduce model versioning

---

## Phase 3 — Validation & Robustness of the Scoring Prototype
Status: **Planned**

Estimated time: 4–6 weeks

- [ ] Input validation
- [ ] Missing input handling
- [ ] Unit testing
- [ ] Edge-case testing
- [ ] Regression testing
- [ ] Stable error responses

---

## Phase 4 — GUI Integration using the UI-Engine
Status: **Planned**

Estimated time: 1 week

- [ ] Extend existing MVC prototype
- [ ] Add scoring request input fields
- [ ] Connect frontend with backend requests
- [ ] Render scoring results in the UI

---

## Phase 5 — Introduce Slim4 as a Lightweight Server Layer
Status: **Planned**

Estimated time: 3 weeks

- [ ] Introduce API routing
- [ ] Connect GUI with scoring prototype
- [ ] Add request/response handling
- [ ] Separate frontend and domain execution flow

---

> **Milestone** — Ready for application purposes for Deutsche Bank

---

## Phase 6 — Introduce the Third Scoring Model
Status: **Planned**

- [ ] Implement first larger scoring matrix
- [ ] Introduce more complex evaluation logic
- [ ] Compare multiple scoring models

---

## Phase 7 — Frontend Stabilization & Multi-Model Support
Status: **Planned**

- [ ] Improve frontend stability
- [ ] Add support for selecting different scoring models
- [ ] Improve UI feedback and result rendering

---

## Phase 8 — Server Layer Stabilization
Status: **Planned**

- [ ] Improve API stability
- [ ] Improve error handling
- [ ] Refactor request flow
- [ ] Improve maintainability

---

## Phase 9 — Optional Advanced Scoring Methods
Status: **In Discussion**

- [ ] Introduce more complex scoring methods
- [ ] Experiment with combined scoring models
- [ ] Allow frontend selection of combined scoring configurations

Notes:

- Optional phase
- Only implemented if enough time is available

---

## Phase 10 — Preparation for the C++ Risk Engine
Status: **Planned**

- [ ] Ensure the Python prototype has a stable architecture foundation
- [ ] Prepare clean separation of domain logic
- [ ] Prepare architecture for later C++ migration

---

## Phase 11 — Initial C++ Risk Engine Implementation
Status: **Future Planned**

Planned start:

- Between 1 and 1.5 years from now

---

## Time Reference

Planned study start:

- In approximately 1.5 years

At that point, the C++ risk engine implementation should begin.

Planned weekly time investment for CR-DSS:

- Approximately 20 hours per week