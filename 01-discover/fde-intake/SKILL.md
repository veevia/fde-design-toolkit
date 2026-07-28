---
name: fde-intake
description: Turn an ambiguous customer or field request into a bounded product brief and ranked unknowns register. Use when an FDE needs to clarify who is affected, which outcome matters, what evidence exists, and which decision must be made before research, specification, or prototyping begins.
---

# FDE Intake

## When to use

Use for a new customer request, escalation, opportunity, workflow complaint, or loosely stated AI idea that lacks a decision-ready brief. Trigger when the request mixes users, solutions, constraints, and desired outcomes or when the team is ready to build but cannot name the riskiest unknown.

## Inputs

Required:

- The request in the requester's own words
- Requester or sponsor
- Known affected role or customer
- Available source material

Optional:

- Current workflow and baseline
- Commercial, policy, time, or platform constraints
- Prior decisions and attempted solutions

If the requester, affected user, or desired outcome cannot be identified, stop after documenting the gap. Do not manufacture a complete brief.

## Output

Produce one field brief with this structure:

```text
TL;DR
Field situation
Target user and consequential moment
Desired outcome and current baseline
Evidence inventory: EVD-* | tag | source | date | relevance
Constraints
Non-goals
Unknowns: UNK-* | question | impact | certainty | resolution method
First decision to close
Recommended next stage
```

Evidence tags are `observed`, `reported`, or `assumed`. Use `unknown` for a missing value, never a plausible placeholder.

## Procedure

1. Preserve the original request before reframing it. Separate exact statements from your interpretation.
2. Name one primary user and one moment where the current experience blocks or risks an outcome. List other actors as stakeholders, not additional primary users.
3. Rewrite the desired outcome as an observable change. If no baseline exists, state that measurement is an unknown.
4. Inventory supplied evidence as `EVD-*`. Record source, date, and evidence tag; do not upgrade reported statements to observations.
5. Extract constraints and test each one: confirmed constraint, stakeholder preference, or assumption. Keep those classes distinct.
6. Write at least one non-goal that prevents the request from expanding silently.
7. Convert missing facts into `UNK-*` questions. Rank by decision impact first and certainty second.
8. Name the first decision that new evidence must support. Select the smallest next method capable of resolving the top unknown.
9. Route to `field-research-synthesis` when evidence exists, or to targeted collection before synthesis when it does not.

## Acceptance gates

- One primary user and one consequential moment are named.
- The outcome is observable without inventing a metric.
- Every factual claim has a source or an `assumed` tag.
- Constraints and preferences are not conflated.
- Non-goals are non-empty.
- Unknowns are questions and have impact-ranked resolution methods.
- The brief names one next decision, not a backlog of possible work.
- No UI, model, integration, or architecture choice is presented as settled unless cited to a prior decision.

## Do not use

- Do not use as a substitute for field research or synthesis.
- Do not use when an approved brief already passes Gate G0; continue from that artifact.
- Do not promise technical feasibility, delivery dates, or implementation effort. Request engineering evidence through the relevant handoff.
- Do not turn a sponsor's requested feature into a validated user need.
