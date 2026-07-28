---
name: decision-log
description: Close a consequential product or design choice with evidence, options, named disagreement, and a Green, Yellow, or Red commitment. Use whenever field evidence, concept selection, experiment results, or delivery changes scope, behavior, trust boundaries, or the next workflow state.
---

# Decision Log

## When to use

Use for non-trivial decisions that affect user behavior, product scope, experiment direction, AI trust boundaries, or delivery interpretation. Invoke after concept selection, experiment review, major validation findings, or any proposed change to approved requirement IDs.

## Inputs

Required:

- Decision question
- Decider and affected owners
- Options considered
- Evidence and assumption IDs
- Named disagreements or an explicit record of who was consulted

Optional:

- Prior decision being superseded
- Experiment result
- Deadline or external constraint

If no decider exists, the output cannot be Green. Record the governance gap as Yellow or stop.

## Output

Produce one record:

```text
DEC-* | title | date | decider | status
Context and decision question
Evidence: EVD-* | FND-* | EXP-* | confidence and limits
Options considered
Decision
Rationale
Scope-in and scope-out
Named disagreement
Consequences and follow-on changes
Yellow only: trigger | owner | expiry | interim behavior
Red only: reason | reopen condition
Supersedes / superseded by
```

Status meanings:

- **Green:** committed; downstream work may rely on it.
- **Yellow:** conditional; the trigger, owner, expiry, and interim behavior are mandatory.
- **Red:** stopped or rejected; reopening evidence is explicit.

## Procedure

1. Phrase the decision as a choice, not a topic. Name the person with authority to commit it.
2. Link evidence and assumptions separately. Summarize confidence limits rather than citing a document without the relevant claim.
3. Record at least two options for a consequential choice, including stop or defer when relevant.
4. Capture stakeholder positions by name before writing the rationale. Do not rewrite disagreement as alignment.
5. State the decision in one sentence and assign exactly one status.
6. Write why this option wins under the current evidence and which tradeoff is knowingly accepted.
7. Define scope-in, non-empty scope-out, and downstream artifacts or IDs that must change.
8. For Yellow, specify an observable trigger, one owner, an expiry date or event, and safe interim behavior. Yellow without all four fields is invalid.
9. For Red, state what evidence could reopen the choice. For Green, state what class of new evidence would require a new decision rather than silent drift.
10. Link superseded records; never erase the earlier rationale.

## Acceptance gates

- One decision question and one accountable decider are named.
- Evidence and assumptions are distinguishable.
- Material options and tradeoffs are visible.
- Disagreement names people and positions or records who was consulted.
- Exactly one Green, Yellow, or Red status is present.
- Yellow has trigger, owner, expiry, and interim behavior.
- Scope-out is non-empty.
- Consequences name the artifacts and owners affected.
- A later reader can tell when and why to reopen the decision.

## Do not use

- Do not create records for trivial, reversible formatting choices.
- Do not use Green to imply certainty; it means commitment under current evidence.
- Do not use Yellow as a way to avoid a decider or deadline.
- Do not change an approved record in place when the choice changes; supersede it with a new `DEC-*` record.
