# FDE Design Loop

## TL;DR

Move from a field request to a delivery decision through eight evidence gates; skip a stage only when its required artifact already exists and passes the same gate.

## Operating rules

- One artifact owner per stage.
- Evidence is tagged `observed`, `reported`, or `assumed`.
- Every consequential choice has one decision record.
- IDs travel forward: `EVD-*`, `UNK-*`, `OPP-*`, `DEC-*`, `REQ-*`, `AC-*`, `STATE-*`, and `EXP-*`.
- Assumptions may enter an experiment but may not be restated as findings.
- Human approval is required for consequential commitments defined in the AI experience spec.
- Engineering evidence is requested through a handoff; this toolkit does not fabricate it.

## Stage 0: Intake

**Run:** `fde-intake`

**Input:** field request, sponsor, affected users, known constraints, available evidence.

**Output:** field brief, current evidence inventory, unknowns register, first decision needed.

**Gate G0 - bounded request**

- One target user and one consequential moment are named.
- Desired outcome is observable.
- Constraints and non-goals are explicit.
- Unknowns are ranked by decision impact.

If G0 fails, remain in intake.

## Stage 1: Synthesize

**Run:** `field-research-synthesis`

**Input:** field brief plus interviews, observations, support data, surveys, or prior research.

**Output:** evidence ledger, patterns, current-state journey or JTBD where useful, ranked pains, contradictions, evidence gaps.

**Gate G1 - traceable evidence**

- Every finding links to at least one evidence item.
- Observed and reported evidence are distinguishable from assumptions.
- Contradictions and sample limits are visible.
- No persona, journey, or JTBD claim exceeds its evidence.

If direct evidence is unavailable, proceed only with an assumptions register and an experiment designed to replace it.

## Stage 2: Frame and decide

**Run:** `problem-opportunity-frame`, then `concept-prioritization`, then `decision-log`.

**Output:** committed problem frame, ranked options, selected concept, scope-in, scope-out, decision status.

**Gate G2 - committed direction**

- The problem names a user, blocked outcome, context, and evidence-backed cause.
- At least two materially different options were considered.
- Selection criteria and evidence confidence are explicit.
- The decision is Green or a valid Yellow with trigger and expiry.
- Scope-out is non-empty.

Red returns to discovery or stops the effort.

## Stage 3: Specify the experience

**Run in parallel where practical:** `ai-experience-spec` and `experience-architecture`.

**Output:** behavioral requirements, acceptance criteria, state model, source and trust policy, IA, content model, design tokens, and component constraints.

**Gate G3 - testable design contract**

- Each requirement has a stable `REQ-*` ID and at least one `AC-*` criterion.
- Loading, empty, error, low-confidence, stale-source, denied-action, and recovery states are addressed or marked not applicable with a reason.
- AI claims define source use, freshness, provenance, uncertainty, and human commitment boundaries.
- Navigation and content use one controlled vocabulary.
- Non-goals and engineering handoffs are explicit.

## Stage 4: Architect the experiment

**Run:** `experiment-architecture`

**Output:** falsifiable hypothesis, riskiest assumption, experiment type, minimum decisive scope, measures, thresholds, stop rules, and evidence plan.

**Gate G4 - decision-capable experiment**

- The experiment names the decision it will change.
- One primary measure has a numeric or categorical threshold set before data collection.
- Guardrails and disconfirming evidence are defined.
- The minimum scope exercises the riskiest assumption and no more.
- Pass, iterate, stop, and inconclusive outcomes are precommitted.

## Stage 5: Prototype

**Run:** `ui-prototyping`

**Output:** realistic prototype plus requirement trace map.

**Gate G5 - inspectable experience**

- The primary user can complete the target task.
- Every tested screen and state traces to `REQ-*`, `AC-*`, or `STATE-*` IDs.
- Content is realistic enough to test comprehension and trust.
- AI behavior is deterministic or operator-controlled where live behavior is not the hypothesis.
- Desktop and mobile layouts do not overlap or hide required actions.

## Stage 6: Validate

**Run:** `prototype-validation`

**Output:** conformance, design, accessibility, responsive, and interaction findings ordered by severity.

**Gate G6 - test-ready prototype**

- No unresolved critical conformance or task-blocking issue remains.
- Keyboard path and visible focus work for the target flow.
- Required states render and recover as specified.
- Known deviations are named and excluded from the test interpretation.

## Stage 7: Learn and decide

**Run:** `field-feedback`, then `decision-log`.

**Output:** evidence-linked findings and a Green, Yellow, or Red decision.

**Gate G7 - evidence decision**

- Observations are separated from interpretation.
- Findings cite sessions and experiment measures.
- The result is compared with precommitted thresholds.
- The decision is ship to delivery, iterate one named assumption, run a new experiment, or stop.

## Stage 8: Handoff

**Run:** `delivery-handoff`.

**Output:** approved contract, trace map, assets, open decisions, engineering requests, and acceptance plan.

**Gate G8 - no silent redefinition**

- Design intent and behavior are frozen by approved IDs.
- Open items have an owner and due condition.
- Engineering handoffs state the evidence required in return.
- A change to user behavior reopens the relevant design decision.

## Iteration policy

Return to the earliest stage invalidated by new evidence. Do not restart the whole loop by default. A failed accessibility implementation check returns to prototype; a falsified user need returns to synthesis or framing.