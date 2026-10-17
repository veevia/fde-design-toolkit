# FDE Design Toolkit

A gated design loop for forward-deployed engineers and designers. Twelve [Agent Skills](https://agentskills.io)
(`SKILL.md`) turn an ambiguous field request into a testable AI product experience, a decisive experiment, and a
delivery-ready UX/UI contract.

![The FDE design loop as an animated diagram in five stage columns. A field request enters Discover: fde-intake (gate G0) and field-research-synthesis (G1). Frame: problem-opportunity-frame, concept-prioritization and decision-log (G2). Specify: ai-experience-spec and experience-architecture in parallel (G3), then experiment-architecture (G4). Prototype: ui-prototyping (G5) and prototype-validation (G6), which can send work back to fix. Learn: field-feedback, decision-log again (G7) and delivery-handoff (G8), which outputs a design contract. Dotted lines send the spec, the experiment and the handoff to specialist handoffs; a dashed rail returns work from the Learn decision to the earliest stage that new evidence invalidates.](docs/images/fde-design-loop.gif)

<sub>A still version: [docs/images/fde-design-loop.png](docs/images/fde-design-loop.png).</sub>

- **One loop, no routers.** Five stages (Discover, Frame, Specify, Prototype, Learn) and one artifact owner per
  stage. The workflow names the next skill instead of a router guessing it.
- **Nine gates, G0 to G8.** Work moves on only when its artifact passes: a bounded request, traceable evidence,
  a committed direction, a testable design contract, a decision-capable experiment, an inspectable experience,
  a test-ready prototype, an evidence decision, and no silent redefinition.
- **IDs travel forward.** Evidence, unknowns, opportunities, decisions, requirements, acceptance criteria,
  states and experiments keep stable IDs (`EVD-*`, `UNK-*`, `OPP-*`, `DEC-*`, `REQ-*`, `AC-*`, `STATE-*`,
  `EXP-*`) from intake to handoff.
- **Engineering stays with engineers.** Implementation, security, performance and delivery go to six specialist
  handoffs that state the evidence they must return. The toolkit does not fabricate it.

> **Status: 0.76.0-draft, Yellow.** The inventory and the twelve skill contracts pass deterministic validation.
> Qualitative scoring of the skills and behavioral evaluation have not run, so this is not yet a validated
> release; [validation/DEEP-LOOP.md](validation/DEEP-LOOP.md) lists what must pass first.

## How it works

Start with `fde-intake` unless an approved field brief already exists, then follow
[`workflows/fde-design-loop.md`](workflows/fde-design-loop.md) stage by stage. Skip a stage only when its
artifact already exists and passes the same gate.

| Gate | After | Passes when |
|---|---|---|
| **G0** bounded request | `fde-intake` | One target user and one consequential moment are named, the outcome is observable, and constraints, non-goals and ranked unknowns are explicit. |
| **G1** traceable evidence | `field-research-synthesis` | Every finding links to evidence; observed and reported evidence stay distinct from assumptions; contradictions and sample limits are visible. |
| **G2** committed direction | `problem-opportunity-frame` → `concept-prioritization` → `decision-log` | The problem names a user, blocked outcome, context and evidence-backed cause; at least two options were considered; the decision is Green, or Yellow with a trigger and expiry. Red returns to discovery or stops the effort. |
| **G3** testable design contract | `ai-experience-spec` and `experience-architecture`, in parallel | Every requirement has a `REQ-*` ID and an `AC-*` criterion; required states are addressed; AI claims define source use, freshness, provenance, uncertainty and human commitment boundaries. |
| **G4** decision-capable experiment | `experiment-architecture` | The experiment names the decision it will change; one primary measure has a threshold set before data collection; pass, iterate, stop and inconclusive outcomes are precommitted. |
| **G5** inspectable experience | `ui-prototyping` | The primary user can complete the target task, and every tested screen and state traces to `REQ-*`, `AC-*` or `STATE-*` IDs. |
| **G6** test-ready prototype | `prototype-validation` | No critical conformance or task-blocking issue remains, the keyboard path works, and required states render and recover. |
| **G7** evidence decision | `field-feedback` → `decision-log` | Findings cite sessions and measures and are compared with the precommitted thresholds: ship to delivery, iterate one named assumption, run a new experiment, or stop. |
| **G8** no silent redefinition | `delivery-handoff` | Design intent and behavior are frozen by approved IDs, open items have an owner, and a change to user behavior reopens the design decision. |

**Iteration:** new evidence returns work to the earliest stage it invalidates, not to the start. A failed
accessibility check returns to the prototype; a falsified user need returns to synthesis or framing.

## The twelve skills

| Stage | Skill | Use when | Produces |
|---|---|---|---|
| Discover | [`fde-intake`](01-discover/fde-intake/SKILL.md) | The request is ambiguous or unbounded | Field brief and unknowns register |
| Discover | [`field-research-synthesis`](01-discover/field-research-synthesis/SKILL.md) | Field evidence exists but is not decision-ready | Evidence brief and current-state model |
| Frame | [`problem-opportunity-frame`](02-frame/problem-opportunity-frame/SKILL.md) | Findings exist but problem definitions conflict | Problem and opportunity frame |
| Frame | [`concept-prioritization`](02-frame/concept-prioritization/SKILL.md) | Multiple solution directions compete | Selected concept and scope boundary |
| Frame | [`decision-log`](02-frame/decision-log/SKILL.md) | A consequential choice must commit or stop work | Evidence-linked decision record |
| Specify | [`ai-experience-spec`](03-specify/ai-experience-spec/SKILL.md) | The selected concept has AI-visible behavior or action | Testable AI experience design spec |
| Specify | [`experiment-architecture`](03-specify/experiment-architecture/SKILL.md) | A risky assumption must change a decision | Smallest decisive experiment |
| Specify | [`experience-architecture`](03-specify/experience-architecture/SKILL.md) | Required behavior lacks task structure or vocabulary | IA, content model and design-system contract |
| Prototype | [`ui-prototyping`](04-prototype/ui-prototyping/SKILL.md) | An approved experiment needs inspectable UX/UI | Inspectable UX/UI prototype |
| Prototype | [`prototype-validation`](04-prototype/prototype-validation/SKILL.md) | A prototype claims test or handoff readiness | UX/UI verification report |
| Learn | [`field-feedback`](05-learn/field-feedback/SKILL.md) | A validated experience needs direct user evidence | Structured user evidence |
| Learn | [`delivery-handoff`](05-learn/delivery-handoff/SKILL.md) | A Green decision authorizes implementation | Delivery-ready design contract |

[`index.md`](index.md) adds the next step for each skill.

## Install

```bash
npx skills add veevia/fde-design-toolkit                       # all twelve skills
npx skills add veevia/fde-design-toolkit --skill fde-intake    # one skill
```

Or clone the repository and point your agent at the stage folders. Each skill is a plain `SKILL.md` in the
open Agent Skills format; the workflow, index and handoff contracts sit beside them.

## Specialist handoffs

The toolkit owns the product question and the evidence it needs; the receiving specialist owns implementation
and returns findings against that contract. [`external-handoffs.json`](external-handoffs.json) defines what each
request and each return must include.

| Handoff | When |
|---|---|
| Workshop facilitation | A multi-person workshop is the chosen method rather than an individual FDE workflow. |
| Agent development | The approved AI experience spec requires prompt packaging, runtime orchestration, tools, or protocol implementation. |
| Engineering review | Prototype or production code needs correctness, maintainability, debugging, performance, or code-level test review. |
| Design-tool integration | Approved tokens, components, or frames must cross a vendor-specific design-tool boundary. |
| Security review | The concept handles sensitive data, identity, permissions, consequential actions, or untrusted model and tool output. |
| Engineering delivery | An approved experience is moving from validated prototype to staged production delivery. |

## Validate the package

```bash
python3 validation/validate_package.py
```

The validator uses only the Python standard library. It checks inventory closure, unique ownership, handoff
targets, manifest paths, frontmatter, and the required sections of each skill contract, then prints
`PASS: v0.76 deterministic package checks`. Deterministic checks cannot certify skill quality: the behavioral
loops in [validation/DEEP-LOOP.md](validation/DEEP-LOOP.md) need an agent runner and a reviewer.

## Scope

v0.76 keeps a capability only when it directly produces or verifies one of five artifacts: a field evidence
brief, a product opportunity frame, an AI experience design spec, an experiment plan with its evidence decision,
or a UX/UI prototype and delivery handoff. It consolidates a 68-skill predecessor: 46 capabilities merged into the
twelve skills, 14 moved to specialist handoffs, and 8 routers or format adapters removed. [SCOPE.md](SCOPE.md) has
the inclusion test and exclusion rules, and [validation/](validation/) records the disposition of every
predecessor skill.

## Project map

```text
01-discover/ … 05-learn/       the twelve skills, one SKILL.md each
workflows/fde-design-loop.md   stages, gates G0-G8 and the iteration policy
index.md                       triggers, outputs and next steps for each skill
manifest.json                  package inventory
external-handoffs.json         specialist handoff contracts
SCOPE.md                       inclusion test and exclusion rules
validation/                    package validator, evaluation protocol and consolidation ledger
docs/images/                   the animated overview and a still version
```

## License

[MIT](LICENSE)
