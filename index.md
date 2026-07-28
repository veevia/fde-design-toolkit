# v0.76 Skill Index

## TL;DR

Twelve skills form one FDE design loop; use the stage gate to choose the next skill instead of invoking a router.

| Stage | Skill | Trigger | Output | Next |
|---|---|---|---|---|
| Discover | [fde-intake](01-discover/fde-intake/SKILL.md) | Request is ambiguous or unbounded | Field brief and unknowns | `field-research-synthesis` or evidence collection |
| Discover | [field-research-synthesis](01-discover/field-research-synthesis/SKILL.md) | Field evidence exists but is not decision-ready | Evidence brief and current-state model | `problem-opportunity-frame` |
| Frame | [problem-opportunity-frame](02-frame/problem-opportunity-frame/SKILL.md) | Findings exist but problem definitions conflict | Bounded problem and opportunities | `concept-prioritization` |
| Frame | [concept-prioritization](02-frame/concept-prioritization/SKILL.md) | Multiple solution directions compete | Selected concept and scope | `decision-log` |
| Frame | [decision-log](02-frame/decision-log/SKILL.md) | A consequential choice must commit or stop work | Green Yellow or Red decision | Stage named by decision |
| Specify | [ai-experience-spec](03-specify/ai-experience-spec/SKILL.md) | Selected concept has AI-visible behavior or action | Testable AI experience contract | `experiment-architecture` and prototype |
| Specify | [experiment-architecture](03-specify/experiment-architecture/SKILL.md) | A risky assumption must change a decision | Minimum decisive experiment | `ui-prototyping` or specialist POC |
| Specify | [experience-architecture](03-specify/experience-architecture/SKILL.md) | Required behavior lacks task structure or vocabulary | IA content and design-system contract | `ui-prototyping` |
| Prototype | [ui-prototyping](04-prototype/ui-prototyping/SKILL.md) | An approved experiment needs inspectable UX/UI | Prototype and trace map | `prototype-validation` |
| Prototype | [prototype-validation](04-prototype/prototype-validation/SKILL.md) | Prototype claims test or handoff readiness | Verification report | Fix or `field-feedback` |
| Learn | [field-feedback](05-learn/field-feedback/SKILL.md) | Validated experience needs direct user evidence | Session evidence packet | `decision-log` |
| Learn | [delivery-handoff](05-learn/delivery-handoff/SKILL.md) | Green decision authorizes implementation | Change-controlled design contract | Engineering delivery |

## Package contracts

- [Scope](SCOPE.md)
- [FDE design loop](workflows/fde-design-loop.md)
- [v0.75 review ledger](validation/v075-skill-review.csv)
- [Deep validation loop](validation/DEEP-LOOP.md)
- [Current validation results](validation/results.json)
- [External handoffs](external-handoffs.json)

## Selection rule

Use the earliest skill whose required input artifact is missing or fails its gate. When new evidence invalidates an upstream assumption, return to that stage rather than continuing downstream.
