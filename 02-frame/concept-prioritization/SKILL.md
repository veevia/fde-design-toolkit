---
name: concept-prioritization
description: Define materially different product concepts and select one against explicit evidence, value, risk, and learning criteria. Use when an opportunity frame is approved but the team needs a defensible direction, bounded scope, and riskiest assumption before specification or experimentation.
---

# Concept Prioritization

## When to use

Use after Gate G1 and an approved problem-opportunity frame. Trigger when stakeholders favor different solutions, one requested feature is being treated as inevitable, or a team needs to choose which concept deserves specification and experiment investment.

## Inputs

Required:

- Approved problem and `OPP-*` set
- Linked findings and evidence confidence
- Confirmed constraints and non-goals
- Named decider

Optional:

- Existing concepts
- Feasibility evidence from engineering
- Commercial or policy criteria
- Prior failed approaches

Missing feasibility evidence is an uncertainty, not a low score invented by the facilitator.

## Output

Produce one concept decision packet:

```text
Decision question
Criteria: criterion | definition | weight | evidence required
Concepts: name | user change | mechanism | AI role | evidence | key risk
Comparison: concept | criterion score | evidence note | uncertainty
Sensitivity check
Selected concept and rationale
Scope-in
Scope-out
Riskiest assumption
Rejected options and conditions for reconsideration
Dissent
Required DEC-* record
```

A concept describes a before-and-after experience and mechanism. It is not a feature list or visual treatment.

## Procedure

1. Restate the decision as one question tied to the approved problem and target user.
2. Define three to five criteria before scoring. Include user outcome, evidence confidence, trust or consequence risk, and learning leverage. Include feasibility only when there is evidence or label it unknown.
3. Set criterion weights that total 100 and explain each weight. Use a small anchored scale such as 1, 3, and 5; define what each score means before applying it.
4. Create at least two materially different concepts. Include a simpler workflow or non-AI baseline when AI is not inherently required by the opportunity.
5. For each concept, state the user change, mechanism, role of AI, source evidence, riskiest assumption, and explicit exclusions.
6. Score collaboratively and attach an evidence note to every score. Do not average away named disagreement.
7. Run a sensitivity check by varying the largest uncertain score or weight. If the winner changes easily, the result is Yellow and the deciding uncertainty becomes the next experiment.
8. Select one concept, write scope-in and non-empty scope-out, and identify the smallest assumption that could invalidate the choice.
9. Preserve rejected options and the evidence that would reopen them. Route the commitment to `decision-log`.

## Acceptance gates

- The decision traces to one approved problem and opportunity.
- At least two concepts differ in mechanism, not only presentation.
- A simpler or non-AI baseline is considered where plausible.
- Criteria and scale anchors were set before scoring.
- Every score has evidence or is marked unknown.
- Sensitivity and named dissent are visible.
- Selected scope has explicit in and out boundaries.
- The riskiest assumption can be tested by `experiment-architecture`.
- The packet does not claim implementation feasibility without specialist evidence.

## Do not use

- Do not use for backlog ranking across unrelated problems.
- Do not use scores as objective measurement; they expose a comparative judgment.
- Do not select a concept through score alone when a hard trust, policy, or accessibility constraint fails.
- Do not proceed to specification without a `DEC-*` commitment or valid Yellow condition.
