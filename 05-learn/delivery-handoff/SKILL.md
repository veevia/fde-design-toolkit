---
name: delivery-handoff
description: Transfer an approved and validated product experience to engineering without redefining behavior, evidence, trust boundaries, or acceptance criteria. Use after a Green delivery decision when requirements, prototype states, assets, known deviations, and specialist evidence requests must become one change-controlled contract.
---

# Delivery Handoff

## When to use

Use when the experiment decision authorizes implementation or a validated prototype needs a formal feasibility handoff. Trigger before estimation or build planning so engineering questions can challenge the contract without silently changing user behavior.

## Inputs

Required:

- Green `DEC-*` delivery decision
- Versioned AI experience spec
- Experience architecture and prototype
- Passing or explicitly bounded validation report
- `REQ/AC/STATE` trace map

Optional:

- Field evidence packet
- Design assets and tokens
- Returned feasibility, security, or integration evidence
- Rollout or instrumentation questions

If the decision is Yellow, produce only a conditional handoff that names the trigger, expiry, excluded work, and safe interim scope. Do not present it as approved delivery scope.

## Output

Produce one handoff contract:

```text
Authority: DEC-* | owner | version | date
Outcome, target user, and evidence links
Scope-in, scope-out, and non-goals
Primary and alternate flows
REQ/AC/STATE trace matrix
AI source, uncertainty, provenance, and human-action rules
Information, content, token, component, and asset references
Responsive and accessibility requirements
Known deviations and accepted tradeoffs
Engineering/security requests and evidence expected back
Open decisions: owner | due condition | blocked IDs
Acceptance and review plan
Change-control rule
```

Reference canonical artifacts by path and version. Do not duplicate their prose into a second source of truth.

## Procedure

1. Verify decision authority, version, and status. Confirm scope-in and non-empty scope-out still match the approved concept and experiment result.
2. Freeze the delivery set of `REQ-*`, `AC-*`, and `STATE-*` IDs. Record later changes through version history and a new decision when behavior changes.
3. Audit traceability backward to evidence and forward to prototype screens, validation results, and acceptance checks. Resolve or label every broken link.
4. Package canonical links for flows, content, tokens, components, assets, responsive rules, and accessibility semantics. Identify owner and freshness for externally maintained assets.
5. Highlight AI-specific obligations at their decision points: sources, freshness, uncertainty, provenance, permissions, draft versus action, human confirmation, cancellation, and recovery.
6. Separate known prototype simulation from required delivered behavior. State which implementation choices remain open to engineering.
7. Convert unknown technical claims into handoff requests. Include affected IDs, question, constraints, acceptance evidence, and the decision that the answer may reopen.
8. Walk through the primary flow and failure states with design, product, and engineering owners. Capture disagreement by name and close it through `decision-log`.
9. Agree how acceptance will be demonstrated: environment, owner, evidence, required viewports, data cases, and who can approve each requirement.
10. Set change control. Clarifications may annotate the contract; changes to user-visible behavior, scope, trust boundaries, or acceptance thresholds require a new decision and version.
11. Keep open decisions visible with one owner and due condition. Block affected IDs rather than letting teams assume a default.
12. Record returned specialist evidence against the originating request and update only the artifacts it resolves.

## Acceptance gates

- A valid Green decision or fully bounded Yellow condition authorizes the handoff.
- Scope-in, scope-out, and non-goals match the approved decision.
- Every delivered ID traces to evidence, prototype behavior, and acceptance evidence.
- Canonical artifacts have one owner, path, and version.
- AI trust and human commitment boundaries are prominent and testable.
- Prototype simulations are not mistaken for production requirements already met.
- Open technical questions request specific evidence and identify affected decisions.
- Known deviations and accepted tradeoffs are explicit.
- Acceptance owners, environments, data cases, and viewports are named.
- User-visible changes cannot enter through an informal implementation default.

## Do not use

- Do not use as an engineering architecture, sprint plan, estimate, security approval, or deployment plan.
- Do not hand off a failing prototype as if implementation will resolve an undefined behavior.
- Do not duplicate canonical specs into disconnected tickets without stable IDs and links.
- Do not let technical convenience silently change user outcomes, source semantics, or action boundaries.
- Do not close specialist requests until their required evidence has been inspected.