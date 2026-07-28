---
name: field-research-synthesis
description: Convert interviews, observations, surveys, support signals, and prior research into traceable findings and a decision-relevant current-state model. Use when field evidence exists but the team needs patterns, contradictions, pains, jobs, or journey moments without overstating what the sample proves.
---

# Field Research Synthesis

## When to use

Use after evidence has been collected and before committing to a problem frame. It is appropriate for mixed qualitative and quantitative sources, including sparse enterprise field evidence, when the result must show what is supported, what conflicts, and what remains assumed.

## Inputs

Required:

- Approved field brief or equivalent scope
- Source artifacts with source identity and date
- Target decision or ranked unknowns

Optional:

- Interview or observation notes
- Survey responses and sampling details
- Product, support, sales, or operational signals
- Prior personas, journeys, or JTBD statements to revalidate

Do not synthesize inaccessible or summarized evidence as if the underlying source was inspected. Record the access limit.

## Output

Produce one evidence brief:

```text
TL;DR
Scope and sample limits
Evidence ledger: EVD-* | tag | source | date | participant/segment | excerpt/measure
Findings: FND-* | claim | evidence IDs | confidence | contradiction
Current-state model: stage | doing | thinking | feeling | pain | evidence IDs
Jobs or archetypes only when decision-relevant
Ranked pains: pain | role | impact evidence | frequency evidence | confidence
Contradictions and outliers
Evidence gaps
Implications for the next decision
```

Confidence is a judgment based on coverage, source linkage, consistency, and freshness. State those factors; do not convert them into a decorative percentage.

## Procedure

1. Normalize each source into an `EVD-*` item without removing context, speaker role, date, or evidence tag.
2. Separate direct observation, participant report, and analyst assumption. Keep interpretation out of the evidence excerpt.
3. Group evidence silently by repeated behavior, goal, barrier, workaround, trust signal, or failure point. Do not begin with desired feature categories.
4. Draft `FND-*` claims that are narrower than their evidence. Link every finding to evidence IDs.
5. Search deliberately for disconfirming evidence, segment differences, and outliers. Put contradictions beside the finding they qualify.
6. Build only the synthesis views needed for the decision. A journey explains sequence; JTBD explains progress sought; an archetype explains stable behavior differences. Do not produce all three by default.
7. Rank pain using evidenced consequence and recurrence. Label sponsor urgency separately from user impact.
8. Assess confidence from coverage, linkage, consistency, and freshness. State sample and access limitations.
9. End with implications and open questions, not solution recommendations disguised as findings.

## Acceptance gates

- Every finding resolves to one or more `EVD-*` entries.
- Every evidence entry preserves source, date, and tag.
- Sample, access, and freshness limits are visible near the claims they constrain.
- Contradictions and outliers are not deleted to simplify the narrative.
- Personas, journeys, and JTBD views are generated only when supported and decision-relevant.
- Pain rank distinguishes impact evidence from stakeholder preference.
- Assumptions are not counted as corroborating sources.
- The brief answers the intake decision or states why evidence is insufficient.

## Do not use

- Do not use to invent research participants, quotes, measures, or prevalence.
- Do not use to design a survey or interview plan; return to intake and select a collection method.
- Do not use to select a concept. Route supported findings to `problem-opportunity-frame`.
- Do not collapse conflicting customer segments into an average user.
