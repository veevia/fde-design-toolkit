---
name: experiment-architecture
description: Design the smallest experiment that can change a named product decision, with a falsifiable hypothesis, precommitted measures, thresholds, guardrails, and stop rules. Use when a selected concept or AI design spec contains a risky desirability, usability, behavior-quality, trust, or feasibility assumption.
---

# Experiment Architecture

## When to use

Use after a concept decision and before investing in a full prototype or build. Trigger when the team can name a choice but cannot support its riskiest assumption, or when an AI behavior needs evidence from users, golden cases, a Wizard-of-Oz simulation, or a specialist feasibility probe.

## Inputs

Required:

- `DEC-*` decision the experiment may change
- Riskiest assumption or uncertain `REQ-*`
- Target population and consequential moment
- Current alternative or baseline

Optional:

- Prior evidence and expected effect
- Available prototype or data
- Recruitment, time, policy, or technical constraints
- Specialist feasibility estimates

If the team cannot name the decision that a result will change, stop. Data collection without a decision is not an experiment architecture.

## Output

Produce one precommitted experiment contract:

```text
EXP-* | owner | decision | status
Assumption under test
Hypothesis: For [population], if [intervention], then [effect and threshold], because [mechanism]
Disconfirming result
Experiment type and fidelity
Minimum decisive scope
Population and sample rationale
Protocol and comparison
Primary measure and threshold
Diagnostic measures
Guardrails
Evidence capture and provenance
Biases and confounds
Stop rules
Result matrix: pass | iterate | stop | inconclusive
Required engineering or research handoffs
```

The output is a decision contract, not a research backlog or implementation plan.

## Procedure

1. Name one decision and one assumption with the highest combination of impact and uncertainty. Split compound assumptions before continuing.
2. Write a falsifiable hypothesis that names population, intervention, expected effect, threshold, and causal rationale. Also write the result that would disconfirm it.
3. Choose the cheapest valid evidence method:
   - Comprehension or task test for findability and usability
   - Wizard-of-Oz or fixed-response simulation for AI interaction and trust
   - Concierge test for workflow value
   - Golden-case evaluation for defined behavior quality
   - Specialist POC for technical feasibility
   - Limited field pilot for behavior in context
4. Hold everything outside the assumption stable. If live model variability is not under test, use deterministic responses and disclose the simulation.
5. Define minimum decisive scope: the smallest scenario, population, states, and fidelity that expose the risk. Remove anything that cannot affect the decision.
6. Select one primary measure. Define its unit, collection method, baseline or comparison, and threshold before seeing results. Add diagnostic measures only when they explain why the primary result moved.
7. Set guardrails for trust, accessibility, harm, privacy, time, or operational burden. A guardrail failure can override a primary-metric pass.
8. Justify the sample from the evidence needed. Do not use an arbitrary participant count as a universal standard; state what the sample can and cannot support.
9. Write the protocol, counterbalancing or comparison where relevant, evidence capture, source IDs, and known confounds.
10. Precommit stop rules and a result matrix for pass, iterate, stop, and inconclusive. Each outcome must map to a next decision.
11. Route technical probes to the relevant external handoff with the acceptance evidence required in return.
12. Have the decider approve the contract before running the experiment. Changes after data appears must be logged as deviations.

## Acceptance gates

- One `EXP-*` tests one primary assumption and names one decision.
- The hypothesis is falsifiable and includes a precommitted threshold.
- Disconfirming evidence is explicit.
- Method and fidelity are the minimum capable of exposing the risk.
- The primary measure is observable and not a vanity metric.
- Guardrails can override a misleading pass.
- Sample rationale states inference limits.
- Simulation and live behavior are distinguishable to the team and participants where disclosure is required.
- Pass, iterate, stop, and inconclusive outcomes each have a next action.
- Technical feasibility claims require returned specialist evidence.
- Protocol changes after launch are recorded rather than silently normalized.

## Do not use

- Do not use to justify a concept already treated as irreversible.
- Do not combine desirability, usability, model quality, and production feasibility into one untraceable test.
- Do not choose a full MVP when a prototype, concierge flow, or POC can answer the decision.
- Do not infer population prevalence from a small qualitative sample.
- Do not move thresholds after seeing results without marking the experiment invalid or exploratory.
