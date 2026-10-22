# FDE Design Toolkit

A gated design workflow for forward-deployed engineers (FDEs) and product designers. Twelve [Agent Skills](https://agentskills.io) (`SKILL.md`) turn an ambiguous field request into a testable AI experience specification, a decisive experiment, and a delivery-ready UX/UI contract.

![The FDE design loop as an animated diagram in five stage columns. A field request enters Discover: fde-intake (gate G0) and field-research-synthesis (G1). Frame: problem-opportunity-frame, concept-prioritization and decision-log (G2). Specify: ai-experience-spec and experience-architecture in parallel (G3), then experiment-architecture (G4). Prototype: ui-prototyping (G5) and prototype-validation (G6), which can send work back to fix. Learn: field-feedback, decision-log again (G7) and delivery-handoff (G8), which outputs a design contract. Dotted lines send the spec, the experiment and the handoff to specialist handoffs; a dashed rail returns work from the Learn decision to the earliest stage that new evidence invalidates.](docs/images/fde-design-loop.gif)

<sub>Static diagram: [docs/images/fde-design-loop.png](docs/images/fde-design-loop.png)</sub>

## Why this toolkit

Frontier models can generate a polished UI or PRD from a vague prompt in seconds. In field engineering, that speed creates a new risk: **plausible output gets mistaken for validated product decisions.**

Without guardrails, ambiguous sponsor escalations become premature AI builds, assumptions get restated as user findings, prototypes only demo the happy path, and critical AI trust states (stale sources, conflicting records, uncertainty, and human-commit boundaries) are improvised during implementation.

This toolkit gives coding and design agents an explicit operating contract:

- **One loop, no routers.** Five stages (`Discover`, `Frame`, `Specify`, `Prototype`, `Learn`) and one artifact owner per stage. The workflow names the next skill directly.
- **Nine evidence gates (`G0`–`G8`).** Work advances only when its artifact passes the gate—from a bounded request (`G0`) to change-controlled handoff (`G8`).
- **Traceable IDs end to end.** Evidence (`EVD-*`), unknowns (`UNK-*`), findings (`FND-*`), opportunities (`OPP-*`), decisions (`DEC-*`), requirements (`REQ-*`), acceptance criteria (`AC-*`), states (`STATE-*`), and experiments (`EXP-*`) travel forward without silent drops.
- **Engineering stays with engineers.** Runtime implementation, security, performance, and rollout route through six typed specialist handoffs that specify what evidence must return.

### How it differs from other agent skills and frameworks

| Category on GitHub | Primary focus | What it leaves unsolved | How FDE Design Toolkit fits |
|---|---|---|---|
| **UI & visual design skills** | Fast screen generation, styling, design tokens, Figma-to-code | Assumes the prompt's feature is right; defaults to happy-path demos | Supplies the upstream problem frame, non-happy `STATE-*` rules, and task architecture before UI is built |
| **Generic PRD / ideation prompts** | Brainstorming personas, JTBD, or feature specs in one shot | Blends assumptions with facts; no traceability across turns | Enforces `observed`/`reported`/`assumed` tags, non-AI baselines, and stable IDs (`EVD-*` → `DEC-*` → `REQ-*`) |
| **Agentic engineering SDLCs** *(e.g., RPI / spec-to-code)* | Codebase research, implementation plans, testing, and security rules | Assumes requirements and AI trust behavior are already validated | Operates **upstream (`G0`–`G8`)** to validate *what* to build and hands off a frozen `REQ/AC/STATE` contract to engineering |

## Quickstart

### 1. Install

```bash
npx skills add veevia/fde-design-toolkit                       # install all 12 skills
npx skills add veevia/fde-design-toolkit --skill fde-intake    # install a single skill
```

Or clone this repository and point your agent at the stage folders. Every skill is a self-contained `SKILL.md`.

### 2. Enter at the right gate

Start with [`fde-intake`](01-discover/fde-intake/SKILL.md) when a request is ambiguous. Skip a stage only when its required input artifact already exists and passes that stage's gate:

- **New field escalation → [`fde-intake`](01-discover/fde-intake/SKILL.md)**
  > *"Sales asks for an AI renewal copilot before next quarter, but we have no baseline or agreed user moment. Bound the brief and rank the unknowns."*
- **Approved concept → [`ai-experience-spec`](03-specify/ai-experience-spec/SKILL.md)**
  > *"Using `DEC-02`, specify the testable `REQ-*`, `AC-*`, and `STATE-*` contract for our grounded account assistant, including stale CRM fallback and human approval."*
- **Validated prototype → [`delivery-handoff`](05-learn/delivery-handoff/SKILL.md)**
  > *"Package our Green decision, prototype trace map, and open specialist questions into a change-controlled engineering handoff."*

## How the loop works

Follow [`workflows/fde-design-loop.md`](workflows/fde-design-loop.md) stage by stage. [`index.md`](index.md) provides a quick lookup of triggers, outputs, and next steps.

| Stage | Skill | Use when | Produces | Gate to pass |
|---|---|---|---|---|
| **01 Discover** | [`fde-intake`](01-discover/fde-intake/SKILL.md) | Request is ambiguous or unbounded | Field brief & unknowns (`EVD-*`, `UNK-*`) | **G0 Bounded request:** One target user and consequential moment named; observable outcome, constraints, non-goals, and ranked unknowns explicit. |
| **01 Discover** | [`field-research-synthesis`](01-discover/field-research-synthesis/SKILL.md) | Field evidence exists but is not decision-ready | Evidence brief & current-state model (`FND-*`) | **G1 Traceable evidence:** Every finding links to `EVD-*`; `observed` and `reported` stay distinct from `assumed`; contradictions and sample limits visible. |
| **02 Frame** | [`problem-opportunity-frame`](02-frame/problem-opportunity-frame/SKILL.md) | Findings exist but problem definitions conflict | Problem & opportunity frame (`OPP-*`) | Feeds **G2**: Names one user, blocked outcome, context, and evidence-backed cause without embedding a solution. |
| **02 Frame** | [`concept-prioritization`](02-frame/concept-prioritization/SKILL.md) | Multiple solution directions compete | Selected concept & scope boundary | Feeds **G2**: Compares at least two materially different options (including a non-AI baseline where plausible) with sensitivity checks. |
| **02 Frame** | [`decision-log`](02-frame/decision-log/SKILL.md) | A consequential choice must commit or stop work | Evidence-linked decision record (`DEC-*`) | **G2 Committed direction:** Decision is `Green`, or `Yellow` with owner, trigger, expiry, and interim behavior (`Red` stops or returns to discovery). |
| **03 Specify** | [`ai-experience-spec`](03-specify/ai-experience-spec/SKILL.md) | Selected concept has AI-visible behavior or action | Testable AI experience spec (`REQ-*`, `AC-*`, `STATE-*`) | **G3 Testable design contract** *(with `experience-architecture`)*: Required states covered; AI claims define source freshness, provenance, uncertainty, and human commitment boundaries. |
| **03 Specify** | [`experience-architecture`](03-specify/experience-architecture/SKILL.md) | Required behavior lacks task structure or vocabulary | IA, content model & design-system contract | **G3 Testable design contract** *(with `ai-experience-spec`)*: Navigation and content use one controlled vocabulary and map to `REQ-*` / `STATE-*`. |
| **03 Specify** | [`experiment-architecture`](03-specify/experiment-architecture/SKILL.md) | A risky assumption must change a decision | Smallest decisive experiment (`EXP-*`) | **G4 Decision-capable experiment:** Names the decision it changes; precommits one primary threshold, guardrails, and pass/iterate/stop/inconclusive rules. |
| **04 Prototype** | [`ui-prototyping`](04-prototype/ui-prototyping/SKILL.md) | Approved experiment needs inspectable UX/UI | Inspectable prototype & trace map | **G5 Inspectable experience:** User can complete the target task; every tested screen and state traces to `REQ-*`, `AC-*`, or `STATE-*`. |
| **04 Prototype** | [`prototype-validation`](04-prototype/prototype-validation/SKILL.md) | Prototype claims test or handoff readiness | UX/UI verification report (`VAL-*`) | **G6 Test-ready prototype:** No critical conformance or task-blocking defect remains; keyboard path works; required states render and recover. |
| **05 Learn** | [`field-feedback`](05-learn/field-feedback/SKILL.md) | Validated experience needs direct user evidence | Session evidence packet (`SES-*`) | Feeds **G7** (then re-run [`decision-log`](02-frame/decision-log/SKILL.md)): Observations stay separate from interpretation; findings cite sessions and compare against precommitted thresholds to ship, iterate, or stop. |
| **05 Learn** | [`delivery-handoff`](05-learn/delivery-handoff/SKILL.md) | Green decision authorizes implementation | Change-controlled design contract | **G8 No silent redefinition:** Intent and behavior are frozen by approved IDs; open items have an owner; any behavior change reopens `DEC-*`. |

### Traceability & iteration

```text
Field Request
  └─► EVD-* (Evidence) & UNK-* (Unknowns)          [01 Discover]
        └─► FND-* (Findings) ──► OPP-* ──► DEC-*   [02 Frame]
              └─► REQ-* / AC-* / STATE-* / EXP-*   [03 Specify]
                    └─► Trace Map & VAL-*          [04 Prototype]
                          └─► SES-* ──► DEC-*      [05 Learn & Handoff]
```

When new evidence invalidates an upstream assumption, **return to the earliest stage it invalidates** rather than restarting the loop from scratch. A failed keyboard check returns to `ui-prototyping`; a falsified user need returns to `field-research-synthesis` or `problem-opportunity-frame`.

## Specialist handoffs

The toolkit owns the product question and required evidence; receiving specialists own implementation and return findings against that contract. See [`external-handoffs.json`](external-handoffs.json) for request and return schemas.

| Handoff | When to use |
|---|---|
| `workshop-facilitation` | A multi-person workshop is chosen over an individual FDE workflow. |
| `agent-development` | The approved AI experience spec requires prompt packaging, runtime orchestration, tools, or protocol implementation. |
| `engineering-review` | Prototype or production code needs correctness, maintainability, debugging, performance, or code-level test review. |
| `design-tool-integration` | Approved tokens, components, or frames must cross a vendor-specific design-tool boundary. |
| `security-review` | The concept handles sensitive data, identity, permissions, consequential actions, or untrusted model/tool output. |
| `engineering-delivery` | An approved experience is moving from validated prototype to staged production delivery. |

## Validation & project map

Run deterministic package checks with the Python standard library:

```bash
python3 validation/validate_package.py
```

This verifies manifest paths, skill frontmatter, required contract sections, handoff schemas, and the 84 evaluation cases in [`validation/eval-cases.json`](validation/eval-cases.json). See [`validation/DEEP-LOOP.md`](validation/DEEP-LOOP.md) for the full behavioral evaluation protocol and [`SCOPE.md`](SCOPE.md) for skill inclusion rules.

```text
01-discover/ … 05-learn/       The 12 core skills (one SKILL.md each)
workflows/fde-design-loop.md   Stages, gates G0–G8, and iteration rules
index.md                       Skill triggers, outputs, and next steps
manifest.json                  Package skill inventory
external-handoffs.json         Specialist handoff contracts
SCOPE.md                       Capability inclusion test and exclusion rules
validation/                    Package validator, eval cases, and validation protocol
docs/images/                   Animated loop overview and static reference diagram
```

## License

[MIT](LICENSE)
