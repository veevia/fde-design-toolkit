# FDE Design Toolkit v0.76

> A trimmed design toolkit for turning field ambiguity into a testable AI product experience, a decisive experiment, and a delivery-ready UX/UI contract.

## Release status

**0.76.0-draft / Yellow.** The package structure and all 68 v0.75 dispositions pass deterministic validation. Qualitative source-body scoring and behavioral evaluation are not yet run, so this folder is not a validated release candidate.

## What is core

The toolkit keeps four capability pillars:

1. **FDE product thinking** - field intake, evidence synthesis, problem framing, concept choice, and decision history.
2. **AI design specification** - user-visible behavior, context, grounding, confidence, provenance, human control, states, and acceptance criteria.
3. **Experiment architecture** - falsifiable hypotheses, minimum decisive scope, measures, thresholds, stop rules, and evidence decisions.
4. **UX/UI** - information and content architecture, design-system constraints, prototyping, accessibility, design review, and field feedback.

Software implementation, code maintenance, security engineering, production observability, deployment, and vendor-specific integrations are explicit handoffs.

## The loop

```text
FIELD REQUEST
    |
    v
INTAKE -> SYNTHESIZE -> FRAME -> DECIDE
                               |
                               v
                  AI EXPERIENCE SPEC
                    |              |
                    v              v
             EXPERIMENT       EXPERIENCE ARCHITECTURE
                    \              /
                     v            v
                       PROTOTYPE
                           |
                           v
                  VALIDATE -> FIELD FEEDBACK
                           |
                           v
                    DECIDE -> HANDOFF / ITERATE / STOP
```

The complete stage and gate contract is in `workflows/fde-design-loop.md`.

## Core inventory

| Stage | Skills |
|---|---|
| Discover | `fde-intake`, `field-research-synthesis` |
| Frame | `problem-opportunity-frame`, `concept-prioritization`, `decision-log` |
| Specify | `ai-experience-spec`, `experiment-architecture`, `experience-architecture` |
| Prototype | `ui-prototyping`, `prototype-validation` |
| Learn | `field-feedback`, `delivery-handoff` |

## Use

1. Start with `fde-intake` unless an approved field brief already exists.
2. Follow `workflows/fde-design-loop.md`; do not select skills through a router.
3. Carry evidence IDs, requirement IDs, and decision IDs forward rather than copying prose.
4. Invoke engineering handoffs from `external-handoffs.json` when a decision requires implementation evidence.
5. Do not call the package validated until every gate in `validation/DEEP-LOOP.md` passes.

## Validation

When a local command runner is available:

```bash
python3 validation/validate_package.py --source-root ../v0.75
```

That command checks inventory closure, unique ownership, handoff targets, manifest paths, frontmatter, and required skill-contract sections. Behavioral cases still require an agent runner and reviewer; deterministic lint alone cannot certify skill quality.

## Review evidence

- `SCOPE.md` defines the inclusion and exclusion tests.
- `validation/v075-review-findings.md` summarizes the structural review and consolidation risks.
- `validation/v075-68-skill-rationale.md` explains every v0.75 skill disposition one by one.
- `validation/v075-skill-review.csv` accounts for all 68 v0.75 skill folders.
- `validation/DEEP-LOOP.md` defines the spec-by-spec and workflow evaluation.
- `manifest.json` is the single package inventory.
