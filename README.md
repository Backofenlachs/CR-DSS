# CR-DSS

**Credit Risk Decision Support System.**

> Long-term architecture and system integration project.


---

# What is this?

CR-DSS is my long-term software engineering project.

The goal is not to build "yet another fintech app", but to slowly evolve a real technical system over multiple years while learning:

- architecture
- backend/frontend separation
- API design
- risk calculation logic
- system integration
- maintainability
- native engine development

I use this project mainly as a parctical engineering playground to explore how larger systems evolve over time.

- Not as a startup.
- Not as a tutorial clone.
- Not as a portfolio buzzword project.

More like:

> "What happens if  a motivated developer starts building a system step by step over many years?"

---

# Main Idea

The project simulates a simplified credit risk decision workflow.

Very simplified example:

```text
Applicant Data
      ⇓
Risk Calculations
      ⇓
Scoring Logic
      ⇓
Decision Output
```

The important part is not the business logic itself.

The important part is the architecture around it.

---

# Main Goals

This project exists to learn and explore:

- modular frontend architecture 
- API orchestration
- risk calculation pipelines
- clean system boundaries
- runtime/lifecycle concepts
- native engine integration later on

I intentionally want the project to evolve in phases instead of building everything at once.

---

# Engineering Philosophy

A lot of this project is built around a simple mindset:

- keep things understandable
- avoid fake complexity
- avoid overengineering
- evolve systems slowly
- document important decisions
- separate
- responsibilities clearly
- build foundations first

I care much more about:

- stable architecture
- clarity
- evolvability
- understanding systems deeply

than "using the newest framework".

---

# Planned System Architecture

```
Frontend (custom UI-Engine)
      ⇓
Slim4 API Layer
      ⇓
c++ Risk Engine
```

---

# Development Phases


## Phase 1 - UI-Engine

### Goal
Build a reusable frontend foundation

### What I built

- custom UI runtime
- mounting engine
- lifecycle system
- declarative layouts
- modular tool architecture
- architecture documentation
- ADRs
- PlantUML diagrams

### Tech 

- vanilla JavaScript
- jQuery
- custom architecture

### Status

**Completed** Engine v0.2.0 

repo: `https://github.com/Backofenlachs/UI-Engine.git`

This phase was mainly about refreshing my knowledge about frontend architecture and runtime concepts.

---

## Phase 2 - Python CLI Prototype

### Goal

Build the first actual risk calculation prototype.

### Architecture

```
input.json
      ⇓
python prototype
      ⇓
output.json
```

### Current Focus

- annuity calculations
- basic economic indicators calculations
- basic scoring logic
- deterministic outputs
- clean data structures

### Why Python?

Because right now speed of iteration matters more than performance.

Python is intentionally treated as a prototype layer.

### Status

**Current Phase**

---

## Phase 3 - Slim4 API Layer

### Goal 

Introduce a real backend safety and security layer between frontend and risk engine.

### Focus

- Rest API design
- DTOs
- validation 
- orchestration
- stateless communication
- frontend/backend separation
- security
- future persistence/database integration

### Status
**Planned**

---

## Phase 4 - C++ Risk Engine

### Goal

Replace the Python prototype with dedicated engine.


### Why C++

The C++ engine is not a "maybe later" idea.

It is already part of the planned long-term architecture and mainly exists to explore:
- system design
- lower-level engineering
- performance-oriented computation
- long-term engine evolution

### Status

**Planned**

---

# Documentation Strategy

This project contains a lot of documentation on purpose.

Including:

- ADRs
- architecture sketches
- PlantUML diagrams
- implementation notes
- runtime concepts

I treat documentation as part of the engineering process itself.

---
# About Me

I'm mainly interested in:

- software architecture
- runtime systems
- backend/frontend integration
- long-term engineering
- understanding how systems evolve over time

Before CR-DSS I spent years experimenting with:
- Unity/C# game development
- OpenGL and C++
- custom tooling and runtime systems
- neural network experiments
- architecture sketches and technical documentation

CR-DSS is the long-term continuation of that technical exploration.

# Disclamer

CR-DSS is an educational engineering project.

It is not a production banking system and not financial advice.

The main purpose is learning architecture, system integration and long-term software engineering.