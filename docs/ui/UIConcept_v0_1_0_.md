# UI Concept - Version 0.1.0

[Penpot Design](https://design.penpot.app/#/view?file-id=7cd71457-8d32-8044-8008-5507ba9522f4&page-id=7cd71457-8d32-8044-8008-5507ba9522f5&section=interactions&frame-id=569de593-e945-8045-8008-5507bf193eaf&index=0&share-id=7cd71457-8d32-8044-8008-5515db7761a3)

PDF: `/docs/ui/CR-DSS_UI_v0_1_0.pdf` 

This document defines the technical, buisness, and layout requirements for the first CR-DSS user interface.

## Purpose

UI v0.1.0 provides the minimum interface required to:

- collect loan application data
- send the application to the server
- receive and display the risk assessment result
- integrate the tool-based structure of UI-Engine v0.2.0

CR-DSS is designed as an internal work interface for employees processing loan applications. The UI should therefore be
functional, clean, modern, and minimalistic.

It should not include marketing-oriented UX, animations, bright colors, or unnecessary visual effects.

## Layout

UI v0.1.0 is a desktop-first single-page interface designed for Full HD displays at approximately `1920 x 1080px`.

Responsive layouts, smartphone support, and optimizations for significantly smaller or larger displays are outside the
scope of this version.

The interface consists of three main components:

- `HeaderTool`
  - CR-DSS title
  - Risk Engine version
  - Server version
  - UI version

- `ApplicantRequestTool`
  - positioned on the left
  - collects applicant and loan request data
  - submits the application

- `RiskAssessmentTool`
  - positioned on the right
  - displays the decision
  - displays calculated metrics and scoring results

## Summary

- Internal employee work interface
- Single-page desktop UI
- Target resolution: `1920 x 1080px`
- Build with UI-Engine v0.2.0
- Tool-based layout with tree components
- Input and result areas remain clearly separated
- Minimalistic and functional design
- No animations or marketing-oriented UX
- No responsive or mobile support in v0.1.0
