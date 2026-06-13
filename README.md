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
- evolvalbility
- understanding systems deeply

than "using the newest framework".

---

# Project Background

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

CR-DSS is intentionally developed and divided into many smaller phases. This makes progress easier to track, allows
individual milestones to be completed incrementally, and helps the project evolve in a controlled manner over time.

## Phase 1 — Domain Exploration & Architecture

- Credit risk research
- Initial architecture design
- Technology evaluation

**Status:** Completed


## Phase 2 — UI-Engine

- Development of a standalone frontend architecture prototype
- Runtime and lifecycle concepts
- Modular UI composition
  
**Status:** Completed

repo: `https://github.com/Backofenlachs/UI-Engine.git`

## Phase 3 — Python Scoring Prototype

- Risk calculation pipline
- Scoring models
- Dependency resolution
- Calculation planning

**Status:** Completed

## Phase 4 — Validation & Robustness

- Input validation
- Error handling
- Testing
- Edge-case analysis

**Status:** In Progress

## Long-Term Direction

The long-term objective of CR-DSS is the impoementation of a dedicated C++ Risk Engine.

Planned target:
**Phase 12 — Initial C++ Risk Engine Implementation** 

Estimated timeline: 
**~1-1.5 years**

For a detailed roadmap and all project Phases, see:
`docs/ROADMAP.md`

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

# Disclamer

CR-DSS is an educational engineering project.

It is not a production banking system and not financial advice.

The main purpose is learning architecture, system integration and long-term software engineering.