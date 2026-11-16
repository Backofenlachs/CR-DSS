# ADR-0005 Introduce Service Based Architecture

## Status

**IN PROGRESS**

Date: 01-11-2026

Autor: Perseus Palma Jacobs


## Context

CR-DSS is a long-term software architecture and learning playground focused on exploring diffrent technologies, architectural patterns, and system integration.

As the project has evolved, serveral components have been developed using diffrent programming languages and technologies:

- **Frontend** TypeScript, Vanilla JavaScript, and a custom UI-Engine
- **Api Layer** PHP with the Slim4 framework
- **Risk Engine:** Python-based risk calculations and scoring models
- **System Service:** C++ HTTP server build using the Linux Socket API (ADR-004)

The project already provides a working end-to-end risk assessment workflow. However, its components are currentyl integrated through a combination of HTTP communication and direct process execution.

With the introduction of the independent C++ System Service and the planned separation of the Python Risk Engine into its own service, the project requires a clearer architectural direction.

According to the project principles, (link to md file), the project will contain a few diffrent components.

## Decision

## Consequences

### Positive

### Negative

