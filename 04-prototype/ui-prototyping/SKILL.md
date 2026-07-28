---
name: ui-prototyping
description: Build an inspectable UX/UI prototype that exercises approved requirements, realistic content, AI states, and the exact experiment path without becoming a production engineering project. Use when a design spec and experiment contract are stable enough to test interaction, comprehension, trust, or workflow value.
---

# UI Prototyping

## When to use

Use after Gates G3 and G4. Trigger when the team needs a realistic interface to test an approved product behavior or communicate a delivery contract. The prototype may be clickable, coded, or operator-driven, but its fidelity must be chosen by the experiment rather than by presentation ambition.

## Inputs

Required:

- Approved AI experience spec with `REQ-*`, `AC-*`, and `STATE-*`
- Experience architecture contract
- `EXP-*` experiment and target task
- Design-system assets or explicit visual constraints

Optional:

- Representative content and data samples
- Existing product shell or starter
- Images, icons, and brand assets
- Operator script for Wizard-of-Oz behavior

Do not begin with generated UI when required content, assets, or states are missing. Record the blocker or use a clearly labeled test substitute.

## Output

Produce a prototype bundle:

```text
Runnable or clickable prototype
Primary scenario and start state
Representative data and content
REQ/AC/STATE-to-screen trace map
Interaction and transition inventory
Simulation disclosure and operator script where used
Desktop and mobile target viewports
Known deviations and excluded behavior
Run instructions
```

The first screen is the actual task experience, not a marketing page explaining the prototype.

## Procedure

1. Restate the experiment question and identify the minimum screens, states, and interactions required to answer it.
2. Choose fidelity deliberately. Use paper or wireframes for structure, clickable screens for flow and comprehension, coded UI for responsive or state behavior, and Wizard-of-Oz simulation for AI behavior that is not itself the feasibility test.
3. Gather representative content and assets before layout. Use specific data that exposes length, empty, conflict, uncertainty, and permission cases.
4. Establish visual direction from domain, audience, existing product, and design-system constraints. Operational products prioritize scanability, density, predictable navigation, and repeated action over decorative composition.
5. Build the primary flow end to end before secondary paths. Keep stable dimensions for controls, lists, grids, and repeated items so dynamic content does not shift the layout.
6. Implement the required `STATE-*` set, especially loading, empty, error, stale, conflicting, low-confidence, review, success, and recovery states relevant to the experiment.
7. Make AI status legible: source use, freshness, uncertainty, draft versus action, and the human commitment point appear where the user decides.
8. Use realistic controls and familiar icons for actions. Provide accessible names or tooltips for unfamiliar icon-only controls. Avoid nested cards and presentation-only containers that obscure task hierarchy.
9. Implement keyboard order, visible focus, headings, labels, and status semantics needed for the target task. Treat accessibility as prototype behavior, not polish.
10. Check desktop and mobile targets for overlap, clipping, hidden actions, unreadable content, and incoherent reflow.
11. Build the trace map while implementing. Every tested screen or state must cite an approved ID; every approved ID in experiment scope must be represented.
12. Document simulations, known deviations, excluded behavior, and run instructions. Route production code concerns to engineering review.

## Acceptance gates

- The target user can enter and complete the exact experiment task.
- Every in-scope `REQ-*`, `AC-*`, and `STATE-*` appears in the trace map.
- Content is realistic enough to test comprehension and trust.
- Simulated and live behavior are documented and do not invalidate the hypothesis.
- AI sources, uncertainty, and commitment boundaries are visible at the relevant moment.
- The primary path works with keyboard input and visible focus.
- Desktop and mobile targets have no overlapping text or controls and preserve required actions.
- Empty, error, boundary, and recovery states cannot be mistaken for success.
- Known deviations are visible to the test team before sessions begin.
- The prototype contains no production-readiness claim without specialist review.

## Do not use

- Do not build a landing page when the task requires an application or tool.
- Do not implement backend, deployment, security, or production architecture unless it is the approved feasibility experiment and specialist-owned.
- Do not add unapproved features to make the prototype feel complete.
- Do not use lorem ipsum or generic records when content meaning affects the result.
- Do not hide unsupported AI behavior behind a polished animation or simulated success state.