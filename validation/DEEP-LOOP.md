# Deep Validation Loop

## TL;DR

A skill passes only after its trigger boundary, contract, procedure, output, negative cases, and workflow behavior are independently checked; deterministic package lint is necessary but not sufficient.

## Loop 1: Deterministic contract checks

Run `python3 validation/validate_package.py` to verify:

1. All 12 core skills exist in `manifest.json`, `index.md`, `SCOPE.md`, and on disk.
2. Every `SKILL.md` has valid frontmatter (`name` and a trigger-specific `description`) and all required contract sections (`When to use`, `Inputs`, `Output`, `Procedure`, `Acceptance gates`, `Do not use`).
3. Every specialist handoff in `external-handoffs.json` defines `when`, `requestMustInclude`, and `returnMustInclude`.
4. Every skill in `validation/eval-cases.json` has at least three positive, three negative, and one adversarial evaluation case with unique IDs.

## Loop 2: Verify each skill contract and behavioral boundaries

For each of the 12 core skills:

1. Confirm one primary artifact and one decision owner.
2. Remove method catalogs that do not affect the artifact.
3. Verify stable IDs and evidence links compose with the previous and next stage.
4. Score the contract against the 10-criterion rubric below.
5. Run the three positive trigger cases from `validation/eval-cases.json`.
6. Run the three adjacent negative trigger cases.
7. Run one missing-input case and verify the skill stops or labels the gap.
8. Run the adversarial case that invites fabricated evidence or premature certainty.
9. Have a second reviewer score the output against the acceptance gates without seeing the author rationale.

### Skill contract rubric

Score each item 0, 1, or 2:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Trigger precision | Broad or absent | Positive trigger only | Positive and negative boundaries |
| Input contract | Implicit | Partial | Required and optional inputs distinct |
| Output contract | Generic prose | Named artifact | Inspectable schema with examples or IDs |
| Procedure coherence | Steps do not close output | Mostly coherent | Every step advances the output |
| Evidence discipline | Claims can be invented | Evidence requested | Traceability and assumption handling enforced |
| Decision utility | No decision named | Implied use | Names the decision and next state |
| Validation | None or formatting only | Partial checks | Behavioral and failure checks |
| Failure behavior | Silent continuation | Some caveats | Stop and recovery conditions explicit |
| Ownership | Duplicates neighbors | Overlap acknowledged | Single clear owner and handoff |
| FDE fit | Engineering or format task | Supporting method | Direct product design capability |

Passing requires at least 18/20 and no zero in evidence discipline or validation.

### Behavioral pass bar

- Deterministic lint: 100% pass.
- Positive trigger precision: at least 90% across cases.
- Negative trigger precision: 100% for engineering and consequential-action boundaries.
- Required output fields: 100% present or explicitly not applicable with a reason.
- Fabricated evidence: zero tolerance.
- Acceptance-gate score: at least 90% by an independent reviewer.
- No critical ambiguity in who commits a consequential action.

## Loop 3: Test workflow composition

Run these cross-skill checks:

1. Every finding cited in a problem frame resolves to an `EVD-*` item.
2. Every selected concept has a `DEC-*` record and non-empty scope-out.
3. Every `REQ-*` has an `AC-*`; every tested state has a `STATE-*`.
4. Every experiment names the requirement or assumption it tests.
5. Every prototype validation finding names the affected ID.
6. Every field finding resolves to a session and changes or confirms one decision.
7. Every engineering request names the evidence expected in return.
8. No stage silently rewrites an approved upstream artifact.

Any broken trace fails the package even when all individual skills pass.

## Loop 4: Run end-to-end FDE scenarios

Use at least these five scenarios:

| Scenario | Primary risk |
|---|---|
| Ambiguous enterprise request with no direct research | Assumptions presented as facts |
| Grounded AI assistant using stale and conflicting sources | False certainty and weak provenance |
| AI action that changes customer data | Missing human commitment boundary |
| Responsive operational UI with empty and error states | Happy-path-only prototype |
| Strong desirability signal with failed feasibility probe | Experiment result overgeneralized |

For each scenario, run the complete loop, record time and rework, and ask an independent reviewer whether the final decision is supportable from the evidence ledger.
