# ADR-0003: Frontend Layered Architecture

**IN PROGRESS**

Date: 07.06.2026

Author: Perseus Palma Jacobs

## Context
This Document establishes the fundamental rules and decisions for the frontend structure.

Since the frontend is currently in progress and the first UI design, `/docs/ui/CR-DSS_UI_v0_1_0.md`, has already been
successfully implemented in combination with the native `/libs/ui-engine-v0_2_0`, a basic set of architectural rules is
required.
The goal is not only to create a working frontend, but also an understandable, scalable and stable foundation.

### Current State
The frontend is located in: `/frontend/`

### UI-Engine and TS implementation
Even though the JS UI engine itself is written in JavaScript, I decided to write the frontend in TypeScript. 

I do not consider this setup complex enough to require a separate ADR, but it is an important part of the frontend
architecture and therefore documented here.

Since the frontend is intended to be backend-driven, clear API contracts and data structures become increasingly
important.

```
Backend-driven frontend
    ↓
clear API contracts and data structures become imporant
    ↓
TypeScript interfaces/types are useful
```

TypeScript also provides:

- easy and clean handling of data structures through interfaces,
- reduces debugging time,
- self-documenting code,
- enhanced IDE support
- "safe" refactoring,
- a clear API definition for the UI-Engine

These are core conditions for me to write structured code in a minimal amount of time. 

At the moment, the UI-Engine TypeScript adapter is located in: 

`/frontend/types/ui-engine-v0_2_0.d.ts`

Future versions of the UI-Engine will come with native TypeScript support.

I will use a minimalistic setup:

`Vanilla typeScript` and additionally `browser-sync`, for easier and faster development, are installed via NPM:

`/frontend/package.json`

The `./dev.sh` script starts the TypeScript watch mode and the browser-sync plugin. 


## Problem
The current architectural requirements are defined as follows:

- Backend-Driven,
- mount/tool-driven approach following the native UI-Engine style,
- clean data handling,
- scalable and easy to understand,
- easy migration to modern frameworks like Vue or React,

## Decision
I will establish a closed layered architecture by default. 

However, in edge cases, for example small read-only lookup requests, Tools are allowed to bypass the Store layer and
call Services directly. The exact rules and limitations for these bypasses will be defined in a dedicated follow-up 
ADR (ADR-0004: Service Bypass Guidelines).

```
Tools: Controllers/Views -> UI-Engine
    ↓ 
Stores
    ↓
Services
    ↓
Backend
```

### Tool / View Layer
The Tools are mounted on the UI-Engine. These components handle the UI and presentation logic.

Every complex Tool should follow a Controller/View-based structure. A Model may be introduced when additional 
separation of logic is required.

`Adapter` -> `Controller` -> `View`

This is based on the UI-Engine documentation: `github.com/Backofenlachs/UI-Engine/docs`. 


### Adapter / Controller
The Adapter has to inherit from `BaseTool` in `/libs/ui-engine-v0_2_0/index.js"` to get access to the lifecycle. 

The Controller is responsible for event handling and orchestration. It can also activate or deactivate other Tools
through the runtime. At the current state, this should be minimized and mainly used for fast development and testing.


### Model
Models can contain logic to outsource logic from the Controller or Adapter.

Since we have established Stores, Models will normally not be necessary in most cases.

### View
Holds the HTML boilerplate.

---

The Tools are allowed to implement variations of these combinations, depending on the complexity of the tool.

Views should not manipulate or transform the data. They are only dumb UI elements.

- Tools must not access Services directly unless the access complies with an accepted bypass rule.

## Stores

Every Store holds global UI logic or global states for a specific domain or UI workflow.

The Tools, on the other hand, are responsible for local UI logic and local states.

Every Store should represent a business-important domain or workflow.

The tasks are:

Hold state, data, and business-important logic.

For example: `RiskAssessmentStore` - responsible for the Risk Calculation Workflow, holding state and data for the
Tools (`ApplicantRequestTool` and `RiskResultTool`).

A tool may access any Store required for its responsibility, but Store dependencies should be kept minimal and
domain/workflow aligned.

- Stores must not access UI Tools and
- must not make basic request calls.

## Services

The Services are mainly responsible for the basic requests that the Stores require.

They are the API layer of the frontend and also transform the response data into the required frontend data models.

In the beginning, the incoming data and frontend data models will match. But with increasing complexity and more
features, this will become necessary.

Decision-relevant calculations and outcome-altering transformations must not be implemented above the Service boundary,
except for explicitly documented temporary implementations.

Mapping currently belongs to the service layer and may later be extracted into dedicated mappers when complexity
requires it.

- Services must not depend on Stores or Tools.
## Consequences

### Positive

- Clear separation of responsibilities between Tools, Stores, Services and Backend.
- Predictable and easy-to-follow data flow through the application.
- Reduced coupling between UI implementation and backend communication.
- Easier testing and debugging because responsibilities are located in clearly defined layers.
- Backend remains the authoritative source for decision-relevant calculations, reducing the risk of inconsistent 
    results between frontend and backend.
- UI-Engine-specific code is isolated inside the Tool/Adapter layer, making later migration to frameworks like Vue or
    React easier.
- The architecture can be extended to a feature-based file structure when multiple views or workflows are introduced.
- `app.js` can later become mainly responsible for routing and application composition instead of developing into a god
    object that holds and coordinates all Tools.
- Stores allow multiple Tools to share workflow state without directly depending on each other.
- DTO mapping inside the Service layer protects upper layers from future backend contract changes.
- Additional abstractions such as dedicated Mappers can be introduced later without changing the fundamental 
    architecture.
- The architecture remains relatively minimal while still providing clear boundaries for future growth.
- Defined bypasses allow simple edge cases, such as small read-only lookups, to remain minimal without introducing
    unnecessary Stores.

### Negative

- The architecture introduces additional rules for deciding when the default layer flow should be used and when a 
    bypass is justified.
- Stores can become too large if too much workflow or domain logic is placed inside a single Store.
- Incorrect responsibility boundaries between Controller, Model and Store can lead to duplicated or unclear logic.
- Changes that affect multiple layers may require updates in several places, for example Backend 
    `DTO → Service mapping → Store → Tool`.
- The architecture requires discipline to maintain. Bypassing layers or introducing unnecessary abstractions can reduce
    its benefits.
- Migration to another frontend framework is simplified by the separation of responsibilities, but it will still 
    require replacement or adaptation of the Tool/UI layer.

## Architecture Rules

- By default, every layer only communicates with the layer directly beneath it.

  `Tool → Store → Service → Backend`

- Defined exceptions to the default dependency flow are allowed for specific edge cases. The exact requirements and
    limitations for these bypasses are documented in further ADRs. Every bypass must strictly comply with the criteria
    defined in ADR-0004.
- Tools own presentation and local UI state only.
- Stores own shared domain/workflow state and workflow logic.
- Services own backend communication and DTO/domain mapping.
- Decision-relevant calculations remain authoritative in the Backend.
- Frontend layers must not perform outcome-altering transformations unless explicitly documented as temporary behaviour.
- UI-Engine-specific code must remain inside Tool/Adapter boundaries.
- Store dependencies should be minimal and aligned with domains/workflows.
- Abstractions are introduced only when required by actual complexity.

### Data Authorization

**UI Layer:**

- may format data
- may filter presentation
- may derive display values

**Store:**

- may orchestrate state/workflow
- may derive presentation/workflow state

**Service:**

- may map/normalize DTOs

**Backend:**

- owns decision-relevant calculations


### Reactivity

Store state changes may be propagated to interested Tools through a simple subscription/event mechanism.

The exact implementation and rules for frontend reactivity will be defined in a separate ADR.
