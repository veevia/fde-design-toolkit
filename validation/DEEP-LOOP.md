# v0.76 Deep Validation Loop

## TL;DR

A skill passes only after its source disposition, trigger boundary, contract, procedure, output, negative cases, and workflow behavior are independently checked; package lint is necessary but not sufficient.

## Current evidence state

| Gate | State | Evidence |
|---|---|---|
| v0.75 inventory closure | Pass | 68 ordered rationales match 68 unique ledger rows; 46 merge, 14 handoff, 8 drop |
| v0.75 body review | Not run | Source paths and frontmatter pass; qualitative rubric scoring remains |
| v0.76 deterministic lint | Pass | `python3 validation/validate_package.py --source-root ../v0.75` |
| v0.76 behavioral cases | Not run | Requires an agent runner and independent review |
| End-to-end FDE scenarios | Not run | Requires behavioral cases to pass first |

Do not change `manifest.json` status to `green` while any row above is blocked or not run.

## Loop 1: Review every v0.75 source spec

For each of the 68 source skills:

1. Read the complete `SKILL.md` and any referenced fixture or script.
2. Write its promised capability in one sentence without using the skill name.
3. Record positive triggers and at least two requests that must not trigger it.
4. Identify required inputs, output schema, stop conditions, and explicit non-goals.
5. Trace every procedural step to the claimed output.
6. Check whether validation tests behavior or only document shape.
7. Mark dependencies on tools, credentials, runtimes, vendors, or engineering expertise.
8. Compare its ownership with adjacent skills; name the exact overlap.
9. Challenge the proposed `merge`, `handoff`, or `drop` disposition.
10. Record `pass`, `revise-disposition`, or `blocked` with evidence.

### Source-spec rubric

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

Passing requires at least 18/20, no zero in evidence discipline or validation, and a written disposition challenge. A low score does not automatically mean drop; it may mean the capability needs a rewritten contract.

## Loop 2: Verify each v0.76 consolidated spec

For each of the 12 core skills:

1. Confirm every merged source capability is either represented or intentionally excluded.
2. Confirm one primary artifact and one decision owner.
3. Remove method catalogs that do not affect the artifact.
4. Verify stable IDs and evidence links compose with the previous and next stage.
5. Run deterministic lint.
6. Run three positive trigger cases.
7. Run three adjacent negative trigger cases.
8. Run one missing-input case and verify the skill stops or labels the gap.
9. Run one adversarial case that invites fabricated evidence or premature certainty.
10. Have a second reviewer score the output against the acceptance gates without seeing the author rationale.

### Consolidated-spec pass bar

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

## Release decision

Green requires:

1. All 68 source specs reviewed with no unresolved disposition challenge.
2. All 12 core skills pass deterministic and behavioral bars.
3. All composition checks pass.
4. Five end-to-end scenarios pass with zero fabricated evidence and zero silent consequential actions.
5. External handoffs return evidence that can be traced to the originating contract.

Yellow requires a named failing gate, owner, trigger, and expiry. Red means the package must not be installed as a validated release.
