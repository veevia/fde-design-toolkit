# FDE Design Toolkit v0.76 Scope

## TL;DR

v0.76 consolidates 68 v0.75 skills into 12 workflow-owned skills for field discovery, product framing, AI experience specification, experiment architecture, UX/UI prototyping, validation, and handoff.

## Status

**Yellow: structural draft.** The v0.75 folder inventory has been reviewed and every named skill has one disposition in `validation/v075-skill-review.csv`. Content-level and runtime validation cannot be claimed until every source `SKILL.md`, fixture, and validator is readable and executable.

## Falsifiable hypothesis

An FDE design toolkit needs a capability only when it directly produces or verifies one of these artifacts:

1. Field evidence brief
2. Product opportunity frame
3. AI experience design spec
4. Experiment plan and evidence decision
5. UX/UI prototype and delivery handoff

If a removed skill is required to create or verify one of those artifacts and no retained skill owns that requirement, the trim is wrong.

## Inclusion test

A core skill must pass all five checks:

1. **FDE-owned:** a field product or design practitioner can lead the work.
2. **Artifact-producing:** the skill creates or verifies a named workflow artifact.
3. **Decision-bearing:** its output changes scope, experience, experiment, or handoff decisions.
4. **Non-duplicative:** one skill owns the capability in v0.76.
5. **Tool-agnostic:** the procedure remains useful without a specific code framework or vendor integration.

## Exclusion rules

- Software implementation, code quality, security, performance, observability, and deployment route to engineering handoffs.
- Thin routers are removed; the workflow selects the next skill explicitly.
- Format-specific renderers and vendor integrations are optional adapters rather than core skills.
- Agent infrastructure is represented only at the product and experience-contract level in the AI design spec.

## Core skills

| Stage | Skill | Owned output |
|---|---|---|
| Discover | `fde-intake` | Field brief and unknowns register |
| Discover | `field-research-synthesis` | Evidence brief and current-state model |
| Frame | `problem-opportunity-frame` | Problem and opportunity frame |
| Frame | `concept-prioritization` | Selected concept and scope boundary |
| Decide | `decision-log` | Evidence-linked decision record |
| Specify | `ai-experience-spec` | Testable AI experience design spec |
| Experiment | `experiment-architecture` | Smallest decisive experiment |
| Design | `experience-architecture` | IA, content model, and design-system contract |
| Prototype | `ui-prototyping` | Inspectable UX/UI prototype |
| Validate | `prototype-validation` | UX/UI verification report |
| Learn | `field-feedback` | Structured user evidence |
| Handoff | `delivery-handoff` | Delivery-ready design contract |

## Structural target

- Source inventory: 68 skills
- Consolidated core: 12 skills
- Source capabilities merged into core: 46
- Explicit external handoffs: 14
- Routers or format adapters removed: 8
- Skill-count reduction: 82.4%

These numbers are structural facts from the attached v0.75 inventory. They are not evidence that the 12 skill bodies pass behavioral evaluation.
