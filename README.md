# CR-DSS

**Credit Risk Decision Support System.**

> A creative Long-term architecture and system integration project.


---

# What is this?

CR-DSS is a polyglot software project that originated from my interest in finance.

The goal is not to build production-ready software, but to experiment with new ideas, explore different architectural styles and patterns, and gain experience with industry-relevant technologies and tech stacks beyond game development in C#.

Above all, it's a personal learning project developed in my free time. Where the project will eventually go is intentionally left open.

---

# Main Idea

The project simulates a simplified credit risk decision workflow.

Simplified example:

```text
Applicant Data
      ⇓
Risk Calculations
      ⇓
Scoring Logic
      ⇓
Decision Output
```

---

# Engineering Philosophy

A lot of this project is built around a simple mindset:

- Iterative development
- Intentional software design
- Technical depth

---

# Planned System Architecture

```
Frontend (custom UI-Engine)
      ⇓
Slim4 API Layer
      ⇓
mixed Risk Engine (in python and c++)
```

---

# Development Phases

CR-DSS is intentionally developed and divided into many smaller phases. This makes progress easier to track, allows
individual milestones to be completed incrementally, and helps the project evolve in a controlled manner over time.
      
      Full roadmap: `docs/ROADMAP.md`

## UI-Engine (Vanilla JS) — Completed
Standalone frontend architecture prototype
  
repo: `https://github.com/Backofenlachs/UI-Engine.git`

## Current State — Phase 5
first fully working pipeline 

```
Applicant Form (TypeScript)
          ↓
RiskAssessmentService
          ↓
Slim4 REST API (PHP)
          ↓
Python Risk Engine
          ↓
Scoring Result
          ↓
Frontend Result View
```

## Long-Term — Phase 12
Implementation of a dedicated C++ Risk Engine.


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