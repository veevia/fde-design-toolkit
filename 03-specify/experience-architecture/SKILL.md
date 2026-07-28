---
name: experience-architecture
description: Translate approved product requirements into a coherent task model, information architecture, content vocabulary, state content, and design-system contract. Use before UX/UI prototyping when users need predictable navigation, terminology, hierarchy, and responsive component rules across the specified experience.
---

# Experience Architecture

## When to use

Use in parallel with the AI experience spec or immediately after its core requirements stabilize. Trigger when the team knows what behavior is required but has not settled how users find, understand, compare, review, and recover across the experience.

## Inputs

Required:

- Approved concept and scope
- `REQ-*`, `STATE-*`, and target task flow
- User vocabulary from field evidence
- Existing product and design-system constraints

Optional:

- Current navigation or sitemap
- Content inventory
- Existing tokens and components
- Localization and accessibility requirements

If required behavior is still changing materially, produce a provisional architecture and label the affected branches. Do not make visual hierarchy compensate for an unresolved product decision.

## Output

Produce one experience architecture contract:

```text
Primary task and conceptual model
Object and action vocabulary: canonical term | synonyms | avoid | definition
Information architecture: location | purpose | contents | entry | exit
Navigation and task-flow map
Content model: content type | fields | source | owner | freshness
State content: STATE-* | heading | message | action | recovery
Hierarchy and disclosure rules
Design tokens and component roles
Responsive behavior
Accessibility semantics
REQ/STATE trace map
Open content or system decisions
```

This contract specifies structure and meaning. It may include low-fidelity diagrams but does not require polished screens.

## Procedure

1. Start from the primary task and list the objects users inspect or change, the actions they take, and the system states they must understand.
2. Reconcile field language, source-system labels, and product terms. Select one canonical user-facing term per concept; record synonyms and terms to avoid.
3. Build a conceptual model that reflects user work rather than database or organization structure. State relationships and status transitions.
4. Group content by task and decision need. Define each location's purpose, contents, entry paths, exits, and permission boundaries.
5. Draw the shortest complete path for the primary task, then add alternate entry, cancellation, interruption, and recovery paths.
6. Define a content model with fields, source, owner, freshness, and empty behavior. Do not use placeholder copy where comprehension is part of the experiment.
7. Write state content for every required `STATE-*`. Messages explain what happened, what is known, what is not, and the next safe action without blaming the user.
8. Set hierarchy and progressive-disclosure rules. Put consequential status, source freshness, and commitment controls at the point of decision.
9. Map existing design tokens and components by role. Add a new component only when existing patterns cannot express a required behavior.
10. Define responsive reflow, truncation, density, and stable dimensions for repeated operational elements. Do not hide essential actions solely because the viewport narrows.
11. Specify landmarks, headings, labels, focus order, status announcements, and accessible names before visual styling.
12. Trace every location, content type, and state to `REQ-*` or `STATE-*`; remove unsupported UI structure.

## Acceptance gates

- Users can predict where the primary object and action live.
- One canonical term represents each domain concept.
- Navigation mirrors the task rather than implementation boundaries.
- Every content type has a source, owner, freshness rule, and empty behavior.
- Required states include clear next and recovery actions.
- Consequential controls and source status appear at the decision point.
- Existing design-system patterns are preferred and deviations are justified.
- Responsive rules preserve required content and actions without overlap.
- Accessibility semantics and focus order are defined.
- Every structural element traces to an approved requirement or state.

## Do not use

- Do not use to add screens or navigation for hypothetical future scope.
- Do not treat source-system taxonomy as automatically user-centered.
- Do not solve unresolved permissions or policy through vague content.
- Do not select visual style, animation, or decorative layout before task hierarchy and state behavior are sound.
