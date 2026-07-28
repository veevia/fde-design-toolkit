---
name: problem-opportunity-frame
description: Turn traceable field findings into one bounded problem and a small set of evidence-linked opportunities. Use when the team must agree on the user, blocked outcome, context, and cause before comparing concepts or writing an AI product specification.
---

# Problem Opportunity Frame

## When to use

Use when an evidence brief passes Gate G1 but stakeholders describe the problem differently, jump to requested features, or need a committed design point of view. The skill closes problem definition, not solution selection.

## Inputs

Required:

- Field brief
- Evidence brief with `EVD-*` and `FND-*` IDs
- Decision the frame must support

Optional:

- Existing problem statement, POV, JTBD, or HMW statements
- Business or policy constraints
- Prior decision records

If there is no traceable evidence for the claimed user problem, create an assumption-led frame and require an experiment to validate it. Do not label it evidence-backed.

## Output

Produce one opportunity frame:

```text
TL;DR
Problem: [user] cannot [outcome] when [context] because [evidence-backed cause]
Consequence: user | business | operational
Evidence: FND-* and EVD-*
Current workaround
Job or progress sought
Opportunity set: OPP-* | how might we | evidence | boundary | success signal
Assumptions and contradictions
Constraints
Non-goals
Decision this frame enables
```

The problem statement is singular. Opportunities may vary, but each must address the same committed problem.

## Procedure

1. Extract the user, context, blocked outcome, and likely cause from the evidence brief. Cite finding IDs for each claim.
2. Separate symptom from cause. Ask what evidence would remain true if the requested feature disappeared.
3. Draft the problem without a product, interface, model, or implementation choice. Reject verbs such as "needs a dashboard" unless the dashboard itself is the evidenced job.
4. State the user consequence and any business or operational consequence separately. Do not use business urgency as user evidence.
5. Capture the current workaround and progress sought. Use a JTBD form only if it clarifies motivation beyond the workflow steps.
6. Generate two to four `OPP-*` directions. Phrase each broadly enough for different concepts but narrowly enough to trace to the problem.
7. Give each opportunity a boundary and observable success signal. Mark unsupported causal beliefs as assumptions.
8. Stress-test the frame against contradictions, excluded segments, and a null explanation such as training, policy, or data quality.
9. Write non-goals and name the concept decision this frame will enable.

## Acceptance gates

- One primary user, context, blocked outcome, and cause are explicit.
- Every problem clause links to `FND-*` or is tagged `assumed`.
- The statement contains no embedded solution or vendor.
- User, business, and operational consequences are distinguishable.
- Each `OPP-*` has evidence, a boundary, and a success signal.
- At least one alternative explanation has been considered.
- Non-goals are non-empty.
- A reader can name the next decision after ten seconds.

## Do not use

- Do not use to prioritize or select a concept; use `concept-prioritization` next.
- Do not turn every pain point into a separate problem statement.
- Do not use an HMW statement to hide weak evidence or an undefined user.
- Do not frame technical feasibility, model quality, or integration effort without evidence from the appropriate specialist.