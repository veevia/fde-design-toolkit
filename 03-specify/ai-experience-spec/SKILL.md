---
name: ai-experience-spec
description: Specify a selected AI product concept as testable user-visible behavior, states, source use, grounding, uncertainty, provenance, and human control. Use after a concept decision and before experiment design or prototyping when AI output or action affects the user's task, trust, or consequences.
---

# AI Experience Spec

## When to use

Use when an approved concept includes generated, retrieved, classified, recommended, or agent-initiated behavior. The skill defines what the experience must do and how a user understands and controls it. It does not design model infrastructure, runtime orchestration, or code.

For a non-AI concept, use the same requirement and state sections but mark AI-only sections not applicable with a reason.

## Inputs

Required:

- Approved `DEC-*` concept decision
- Problem and opportunity frame
- Evidence brief and target user
- Scope-in, scope-out, and riskiest assumption

Optional:

- Data-source inventory
- Policy, privacy, or permission constraints
- Existing terminology and design-system rules
- Feasibility evidence from engineering or security

If a consequential source, permission, or action boundary is unknown, keep the affected behavior out of committed scope or make its resolution an experiment or specialist handoff.

## Output

Produce one versioned design spec:

```text
TL;DR and DEC-* authority
Target user, moment, outcome, and current alternative
Goals, non-goals, scope-in, scope-out
Primary scenario and task flow
Domain vocabulary and entity relationships
REQ-* behavioral requirements
STATE-* state model
Source and context contract
Grounding, provenance, and freshness policy
Uncertainty and confidence behavior
Human control and consequential-action matrix
Prompt and response behavior contract
Permissions, memory, and retention expectations
AC-* acceptance criteria and golden examples
Experiment hooks and measures
Engineering and security handoffs
Open decisions and change history
```

Each requirement uses this record:

```text
REQ-* | actor | trigger | required behavior | visible outcome | evidence | priority
AC-*  | given | when | then | failure signal
```

Each state uses this record:

```text
STATE-* | entry condition | visible content | allowed actions | blocked actions | recovery
```

## Procedure

1. **Anchor authority.** Cite the approved `DEC-*`, target evidence, and exact scope. Copy neither unsupported research claims nor implementation assumptions into requirements.
2. **Write the primary scenario.** Describe the user's starting context, intent, task steps, system responses, decision point, and end state. Keep AI as a mechanism serving the task rather than the protagonist.
3. **Set controlled vocabulary.** Name core entities, relationships, statuses, and user-facing terms. Record synonyms to avoid, especially where the source systems use conflicting labels.
4. **Author behavioral requirements.** Give every required behavior a `REQ-*` ID, actor, trigger, visible outcome, evidence link, and priority. State what is intentionally not required.
5. **Model states before screens.** Cover default, loading, partial, empty, error, low-confidence, conflicting-source, stale-source, permission-denied, action-review, success, and recovery states. Mark a state not applicable only with a reason.
6. **Specify context and sources.** For each source, state purpose, access boundary, freshness expectation, permitted claim types, and fallback when unavailable. Do not equate source access with permission to expose its contents.
7. **Define grounding and provenance.** State which claims require source support, how citations or source details appear, what happens when sources conflict, and when the system must abstain. Generated content must not look sourced when it is not.
8. **Define uncertainty behavior.** Specify what the user sees when evidence is incomplete or confidence is low. Prefer reasoned cues such as missing source, stale date, or conflicting records over an unexplained numeric confidence score.
9. **Set human control boundaries.** Classify each action as preview-only, reversible auto-action, human-review, or human-commit. Name consequence, reversibility, permission, confirmation, cancellation, and recovery. The user must know whether AI is suggesting, drafting, or acting.
10. **Specify interaction behavior.** Define request framing, editable context, response structure, refusal or clarification behavior, and examples of acceptable and unacceptable output. Treat prompts as behavioral examples, not hidden implementation strings.
11. **Address permissions and memory.** State whose data may be used, what is retained, what persists across sessions, what the user can inspect or delete, and which questions require security review.
12. **Write acceptance criteria.** Give each `REQ-*` at least one `AC-*` in observable Given/When/Then form. Include golden normal, boundary, and failure examples without inventing model performance.
13. **Expose experiment hooks.** Link the riskiest requirements and assumptions to measures that `experiment-architecture` can test. Separate user outcome, behavior quality, and guardrails.
14. **Request specialist evidence.** Route runtime, integration, feasibility, performance, and security questions through `external-handoffs.json`. State the evidence required in return.
15. **Review traceability.** Verify every requirement traces backward to evidence or an assumption and forward to an acceptance criterion, state, or experiment.

## Acceptance gates

- The spec cites one approved concept decision and preserves its scope-out.
- Every `REQ-*` has evidence or an explicit assumption and at least one `AC-*`.
- Required normal, boundary, trust, failure, and recovery states are covered.
- Every source has purpose, access, freshness, permitted use, and fallback.
- Grounded and generated claims are visibly distinguishable.
- Conflicting or insufficient evidence has defined abstain, clarify, or recovery behavior.
- Consequential actions require an explicit human commitment boundary.
- The interface distinguishes suggestion, draft, and completed action.
- User-facing uncertainty is interpretable rather than decorative.
- Permissions, memory, and retention expectations are explicit or handed off as blockers.
- Golden examples include success, boundary, and failure cases.
- Technical claims cite specialist evidence; unknown feasibility remains unknown.
- Non-goals and engineering handoffs are non-empty.

## Do not use

- Do not use to choose the product concept; return to `concept-prioritization`.
- Do not specify model vendors, orchestration code, MCP implementations, database schemas, or deployment architecture unless an approved constraint makes them user-visible.
- Do not promise accuracy, latency, cost, or feasibility without measured specialist evidence.
- Do not hide consequential actions behind generic consent or a global confidence threshold.
- Do not let an AI-generated spec approve itself. The product or design owner commits scope; specialists commit their technical evidence.