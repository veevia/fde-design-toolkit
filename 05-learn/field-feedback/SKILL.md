---
name: field-feedback
description: Plan and capture user sessions as traceable observations, task measures, quotes, and interpretation limits tied to a precommitted experiment. Use when a validated prototype or field workflow is ready for usability testing, interviews, focus groups, or structured feedback without turning opinions into findings.
---

# Field Feedback

## When to use

Use after Gate G6 when direct user evidence is needed to evaluate an `EXP-*` contract. The method may be an individual task session, contextual interview, or focus group. Choose a group only for shared attitudes, language, or concept discussion; use individual sessions for task behavior and sensitive experience.

## Inputs

Required:

- Approved `EXP-*` contract and thresholds
- Validated prototype or current workflow
- Target participant criteria
- Research owner and evidence storage location

Optional:

- Recruitment list
- Consent and recording requirements
- Moderator and observer roles
- Prior session evidence

If consent, participant fit, or the tested prototype version is unknown, do not treat the session as valid experiment evidence.

## Output

Produce a field evidence packet:

```text
Session plan and neutral script
Participant criteria and actual role
Prototype/version and scenario
Session log: SES-* | date | method | participant code | consent | deviations
Observations: EVD-* | timestamp | observed/reported | exact note | task/AC ID
Measures: measure | value | collection rule | EXP threshold
Quotes with context
Observer debrief
Session-level interpretation
Cross-session result table
Limitations and missing segments
Decision inputs, not the decision itself
```

Store identity and consent data according to the applicable policy; use participant codes in the evidence packet.

## Procedure

1. Select the method from the experiment question. Do not use a focus group to measure individual task completion or an interview to claim observed behavior.
2. Recruit against explicit role, context, and experience criteria. Record mismatches rather than quietly broadening the population.
3. Write a neutral five-part session: welcome and consent, context, unaided task, targeted follow-up, and close. Avoid explaining the intended design before the task.
4. Define task start, completion, error, assistance, abandonment, and timing rules before sessions begin.
5. Pilot the script and prototype once. Fix protocol defects before collecting experiment data and record any resulting version change.
6. During the session, separate what the participant does, says, and what the observer infers. Capture timestamps and relevant `AC-*` or task IDs.
7. Ask open follow-ups after behavior: what they expected, what evidence they used, what felt uncertain, and what they would do next. Do not ask for feature approval.
8. For groups, prevent early speakers from anchoring everyone: collect individual reactions before discussion and preserve disagreement by participant code.
9. Run a short observer debrief immediately after each session. Record surprises and hypotheses separately from evidence.
10. Apply the precommitted collection rules and thresholds. Do not redefine completion or discard inconvenient sessions without documenting the exclusion rule.
11. Build a cross-session result table and preserve segment differences, outliers, protocol deviations, and sample limits.
12. Route the packet to `decision-log`, or to `field-research-synthesis` when a broader pattern analysis is required beyond the experiment.

## Acceptance gates

- Method matches the evidence question.
- Participant criteria, actual role, consent status, and prototype version are recorded.
- Tasks and measures follow the approved experiment rules.
- Observed behavior, reported opinion, and observer interpretation are distinguishable.
- Quotes retain participant code, context, and timestamp or location.
- Moderator wording does not reveal the desired answer before the task.
- Group disagreement and individual reactions remain visible.
- Exclusions and protocol deviations are explicit.
- Results are compared with precommitted thresholds without moving them.
- Limitations prevent claims beyond the sample and context.

## Do not use

- Do not invent participants, quotes, timestamps, measures, or consent.
- Do not count stakeholder reactions as target-user evidence unless they meet participant criteria.
- Do not use preference voting as proof of task value or usability.
- Do not decide ship or stop inside the evidence packet; the accountable decider uses `decision-log`.
- Do not merge personally identifying data into the shared evidence ledger without an approved need and policy.
