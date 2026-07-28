---
name: prototype-validation
description: Verify a UX/UI prototype against approved requirements, states, experiment scope, visual quality, responsive behavior, accessibility, and AI trust semantics. Use before field testing or handoff to separate contract defects from known simulation limits and implementation engineering issues.
---

# Prototype Validation

## When to use

Use when a prototype claims to be ready for an experiment, stakeholder decision, or delivery handoff. Trigger after substantive prototype changes and before participant exposure. This skill validates the experience contract; it routes code quality, production security, and performance remediation to specialists.

## Inputs

Required:

- Runnable or clickable prototype
- Approved AI experience spec
- Experience architecture contract
- `REQ/AC/STATE` trace map
- `EXP-*` target path and viewports

Optional:

- Design-system source
- Automated accessibility or browser results
- Known deviations
- Prior validation findings

If the prototype cannot be rendered or interacted with, report validation as blocked. Static source inspection cannot prove rendered behavior.

## Output

Produce one verification report:

```text
TL;DR and release recommendation
Environment and viewports
Coverage: ID | expected | observed | result
Findings: VAL-* | severity | type | evidence | affected IDs | reproduction | owner
Primary-task result
State and recovery result
AI trust-semantics result
Visual and content review
Responsive review
Accessibility review
Known deviations and experiment impact
Blocked engineering or security checks
Gate G6: pass | fail | blocked
```

Severity is based on decision impact: critical blocks or invalidates the target task; high materially changes behavior or interpretation; medium creates friction or inconsistency; low is contained polish.

## Procedure

1. Confirm the prototype version, environment, target viewports, experiment path, and approved contract versions. Reject stale trace maps.
2. Build a coverage checklist from in-scope `REQ-*`, `AC-*`, and `STATE-*` before inspecting the implementation.
3. Run the primary task from the defined start state. Record observed behavior and reproducible evidence; do not infer success from screen presence.
4. Exercise required boundary and recovery states, including empty, loading, error, stale, conflict, low-confidence, permission-denied, review, cancellation, and success where applicable.
5. Verify AI trust semantics at the decision point: source identity and freshness, grounded versus generated content, uncertainty reason, draft versus action, confirmation, and recovery.
6. Review information hierarchy, navigation, terminology, content clarity, control choice, density, consistency, and domain fit. Compare against the approved experience architecture rather than personal taste.
7. Inspect responsive layouts at all target viewports. Check overlap, clipping, reflow, truncation, fixed elements, touch targets, and preservation of essential actions.
8. Test keyboard navigation, visible focus, semantic names, headings, labels, status announcements, and contrast with available browser or accessibility tools. Record tool and method limits.
9. Separate experience-contract defects from implementation quality, security, or production performance concerns. Route the latter through external handoffs with affected IDs.
10. Record each `VAL-*` finding with severity, evidence, reproduction, affected contract IDs, experiment impact, and owner. A screenshot alone is insufficient for an interaction defect.
11. Re-run affected checks after fixes. Do not close a finding from an implementation claim without observed evidence.
12. Issue Gate G6 as pass, fail, or blocked and state whether known deviations could bias the planned experiment.

## Acceptance gates

- Every in-scope requirement, criterion, and state is pass, fail, or explicitly blocked.
- The primary task completes from the specified start state.
- No unresolved critical or experiment-invalidating issue remains.
- AI provenance, uncertainty, action status, and human commitment match the spec.
- Required recovery paths work and cannot be mistaken for success.
- Target desktop and mobile layouts contain no incoherent overlap or hidden required action.
- Keyboard and visible-focus paths complete the target task.
- Findings include evidence, reproduction, affected IDs, impact, and owner.
- Known simulations and deviations are assessed for experiment bias.
- Unperformed engineering or security checks are labeled blocked rather than passed.

## Do not use

- Do not certify production readiness, security, code quality, or performance.
- Do not replace participant evidence with expert design opinion.
- Do not approve behavior that looks polished but violates an acceptance criterion.
- Do not hide blocked checks in an overall pass percentage.
- Do not broaden review into unrelated prototype features outside the approved experiment scope.
