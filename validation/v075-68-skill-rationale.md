# v0.75: 68-Skill Rationale

## TL;DR

All 68 skills remain accounted for: 46 design capabilities are merged into 12 stronger end-to-end contracts, 14 specialist capabilities become explicit handoffs, and 8 routers or rendering adapters leave the core inventory.

## How to read this review

- **Merge** means the capability remains core, but not as an independently triggered skill.
- **Handoff** means the concern remains important to design, while execution or verification belongs to a specialist.
- **Drop** means the item is a router or output adapter rather than a durable FDE product-design capability. It may still be used as a tool.

This is a structural disposition based on the v0.75 inventory and available descriptions. The individual v0.75 skill bodies and fixtures still require the body-level review defined in `DEEP-LOOP.md`.

## 01 Understand

### 1. `analysis-report-formatter`

**Disposition: Merge into `field-research-synthesis`.** Formatting a research analysis is valuable, but it is the presentation layer of synthesis rather than a separate product decision. Keeping evidence, findings, limitations, and report structure under one owner reduces the risk of producing a polished narrative that is detached from source evidence.

### 2. `design-sprint-planner`

**Disposition: Handoff to `workshop-facilitation`.** Design sprints are relevant to design, but they are one optional collaboration method rather than a required artifact in every FDE engagement. The core loop names the decision and required output; a facilitation capability can design the workshop when group alignment is the chosen method.

### 3. `journey-mapping-creator`

**Disposition: Merge into `field-research-synthesis`.** A journey map is one way to represent sequence, emotions, barriers, and opportunities found in evidence. It should be generated only when sequence matters to the decision, not triggered as a default deliverable independently of the evidence ledger.

### 4. `jtbd-creator`

**Disposition: Merge into `field-research-synthesis`.** JTBD clarifies the progress a user is trying to make and is strongly relevant to product thinking. It becomes a synthesis view because the job must be derived from observed or reported evidence and should not become an isolated statement with weaker traceability.

### 5. `persona-archetype-creator`

**Disposition: Merge into `field-research-synthesis`.** Behavioral archetypes can clarify stable differences between user groups, but personas are often overproduced or fictionalized. Consolidation requires the archetype to be evidence-backed and useful to the current decision instead of an automatic standalone artifact.

### 6. `socratic-intake`

**Disposition: Merge into `fde-intake`.** Clarifying ambiguity through disciplined questions is the essential entry behavior for an FDE engagement. It remains core, while its output is strengthened into a bounded field brief, evidence inventory, ranked unknowns, non-goals, and first decision.

### 7. `survey-analytics`

**Disposition: Merge into `field-research-synthesis`.** Survey results are one evidence type and need the same source, sampling, contradiction, and inference limits as interviews or observations. A separate skill could encourage quantitative-looking claims without integrating them with the rest of the evidence base.

### 8. `survey-creator`

**Disposition: Merge into `fde-intake`.** Survey design remains available as a discovery method, but method selection should follow the unknown and decision rather than exist as an independent destination. Intake determines whether a survey can resolve the highest-impact unknown and records its sampling and inference limits.

### 9. `uxr-assist`

**Disposition: Drop as a standalone router.** Its role is to choose an Understand-phase method rather than produce or verify a durable artifact. The v0.76 workflow performs this routing explicitly from the missing gate, making another trigger layer unnecessary.

## 02 Identify

### 10. `concept-creator`

**Disposition: Merge into `concept-prioritization`.** Concept creation is core design work, but concepts gain decision value only when they can be compared against evidence and meaningful alternatives. Combining generation and selection prevents a favored idea from being authored separately and treated as the inevitable winner.

### 11. `design-decision-articulator`

**Disposition: Merge into `decision-log`.** Explaining a design choice is essential, but the rationale belongs with evidence, alternatives, dissent, status, scope, and reopening conditions. One decision contract avoids parallel formats for product, design, and experiment commitments.

### 12. `design-pov-author`

**Disposition: Merge into `problem-opportunity-frame`.** A design POV commits to a user, need, and insight, so it is part of the problem-framing decision. It should not float separately from the evidence-backed cause, consequences, boundaries, and opportunities it is supposed to govern.

### 13. `flywheel-mapper`

**Disposition: Merge into `concept-prioritization`.** Compounding effects can be a useful strategic criterion for comparing concepts. They are not required for every FDE problem, so flywheel logic becomes an optional concept test instead of an always-visible standalone skill.

### 14. `hmw-opportunity-generator`

**Disposition: Merge into `problem-opportunity-frame`.** HMW statements are useful intermediate reframes, not final evidence or decisions. Keeping them in the frame ensures each opportunity remains linked to a specific user problem, boundary, and success signal instead of becoming unconstrained ideation prompts.

### 15. `hypothesis-creator`

**Disposition: Merge into `experiment-architecture`.** A falsifiable hypothesis is indispensable, but by itself it does not define a valid experiment. It must travel with the decision, method, minimum scope, threshold, guardrails, disconfirming evidence, stop rules, and result matrix.

### 16. `known-unknown-mapper`

**Disposition: Merge into `fde-intake`.** Known and unknown mapping is most useful before selecting discovery or experiment work. Consolidation makes unknowns ranked by decision impact and connects each one to a resolution method rather than preserving a static quadrant artifact.

### 17. `pain-point-mapper`

**Disposition: Merge into `field-research-synthesis`.** Pain points remain central to product thinking, but their role, frequency, consequence, and confidence must stay linked to evidence. Housing them in synthesis prevents a pain inventory from being mistaken for a prioritized opportunity without supporting data.

### 18. `pathfinder-prioritizer`

**Disposition: Merge into `concept-prioritization`.** Explicit prioritization is a core product-design capability. It belongs with concept criteria, evidence notes, sensitivity analysis, scope boundaries, and the riskiest assumption so scoring cannot masquerade as an independent objective answer.

### 19. `prd-author`

**Disposition: Merge into `ai-experience-spec`.** Goals, non-goals, requirements, measures, and scope remain core. For an AI product, however, they must be joined to states, source use, uncertainty, provenance, human control, and acceptance criteria in one user-visible behavior contract.

### 20. `prioritization-alignment-assist`

**Disposition: Drop as a standalone router.** It selects among prioritization and alignment methods but does not own the resulting commitment. `concept-prioritization` and `decision-log` now expose criteria, disagreement, authority, and status directly.

### 21. `problem-definition-assist`

**Disposition: Drop as a standalone router.** It routes among problem-framing techniques rather than producing a single authoritative problem artifact. `problem-opportunity-frame` owns that artifact and may use POV, HMW, or problem-statement techniques internally when appropriate.

### 22. `problem-statement-builder`

**Disposition: Merge into `problem-opportunity-frame`.** A crisp problem statement is the nucleus of the frame and remains required. It gains stronger boundaries by linking every clause to findings or assumptions and sitting beside consequences, alternatives, opportunities, constraints, and non-goals.

### 23. `spec-driven-development`

**Disposition: Merge its product contract into `ai-experience-spec`.** Stable requirements, states, acceptance criteria, and traceability are essential to design-to-build continuity. Software-development execution does not enter the core; v0.76 retains the behavior specification and hands implementation to engineering.

### 24. `strategy-assist`

**Disposition: Drop as a standalone router.** It chooses among strategic methods without owning one decision artifact. Strategy considerations such as compounding value, uncertainty, and prioritization are applied inside framing and concept selection when they affect the chosen direction.

### 25. `traffic-light-decider`

**Disposition: Merge into `decision-log`.** Green, Yellow, and Red are commitment semantics, not a separate workstream. Every consequential decision now carries exactly one status, with mandatory trigger, owner, expiry, and interim behavior for Yellow.

## 03 Execute

### 26. `agent-skills-creator`

**Disposition: Handoff to `agent-development`.** Authoring reusable agent skills is tooling and runtime capability development rather than FDE product-design work. The FDE design spec supplies behavior, acceptance, context, and trust requirements; an agent specialist packages and implements the skill.

### 27. `agentic-trust-architecture`

**Disposition: Merge product-level concerns into `ai-experience-spec`.** Trust is central to AI experience design and cannot be removed. The spec owns what users see and control across confidence, provenance, grounding, and human commitment; implementation and security verification remain specialist work.

### 28. `confidence-calibrator`

**Disposition: Merge into `ai-experience-spec`.** Confidence affects interpretation, reliance, and recovery, so it is user-facing product behavior. Consolidation emphasizes explainable reasons such as missing, stale, or conflicting evidence instead of allowing an isolated numeric confidence mechanism.

### 29. `content-designer`

**Disposition: Merge into `experience-architecture`.** Content structure, labels, state messages, actions, and recovery language are inseparable from navigation and task comprehension. The combined contract gives every content type a source, owner, freshness rule, and role in the user journey.

### 30. `context-engineer`

**Disposition: Merge the product policy into `ai-experience-spec`.** What context the AI uses, retains, retrieves, or forgets directly affects relevance, privacy, and user expectations. Runtime token management and retrieval implementation are not retained as FDE responsibilities.

### 31. `data-integration-designer`

**Disposition: Merge product-facing source contracts into `ai-experience-spec`.** Designers must define why a source is used, its access boundary, freshness expectation, permitted claim types, and fallback. Connectors, schemas, and runtime integration remain engineering work requested through a handoff.

### 32. `design-system-author`

**Disposition: Merge into `experience-architecture`.** Tokens, component roles, accessibility semantics, responsive rules, and justified deviations are core UX infrastructure. They belong beside information and content architecture so the system expresses the task rather than becoming an isolated styling exercise.

### 33. `diff-reviewer`

**Disposition: Handoff to `engineering-review`.** Reviewing code or implementation diffs for regressions and correctness requires engineering ownership. The design toolkit provides affected requirement IDs and acceptance behavior, then consumes the specialist's findings as evidence.

### 34. `excalidraw-diagramming`

**Disposition: Drop from core and retain as an optional visual adapter.** Diagramming can communicate journeys, architecture, and decisions effectively, but the canvas format does not define the underlying design capability. Any core artifact may use Excalidraw after its content contract is settled.

### 35. `experiment-planner`

**Disposition: Merge into `experiment-architecture`.** Experiment planning is a core FDE capability and remains central in v0.76. It becomes the owner of the complete decision experiment rather than one planning step among separate hypothesis, scope, POC, and evaluation skills.

### 36. `figma-mcp-harness`

**Disposition: Handoff to `design-tool-integration`.** Figma retrieval and MCP transport are vendor-specific infrastructure. The FDE contract names required nodes, assets, tokens, versions, and destination mappings; the integration capability returns those artifacts and missing-item evidence.

### 37. `grounding-critic-designer`

**Disposition: Merge product requirements into `ai-experience-spec`.** The experience must define which claims require support, how conflicts appear, and when the system abstains. Building the second-pass critic or evaluation runtime is an agent-development responsibility.

### 38. `harness-builder`

**Disposition: Handoff to `agent-development`.** Wiring prompts, tools, context, data, and execution loops is implementation work. V0.76 supplies testable requirements, tool and data contracts, human boundaries, and golden cases for the runtime owner to implement and verify.

### 39. `hitl-boundary-designer`

**Disposition: Merge product behavior into `ai-experience-spec`.** Whether AI suggests, drafts, previews, or commits an action is a fundamental user-experience decision. The spec owns visibility, confirmation, cancellation, reversibility, and recovery; enforcement mechanisms are specialist-built.

### 40. `html-report-generator`

**Disposition: Drop from core and retain as an optional visual adapter.** HTML can be an excellent delivery format, but rendering does not independently produce validated analysis or design reasoning. Core skills define the artifact; an HTML adapter may present it afterward.

### 41. `information-architecture-designer`

**Disposition: Merge into `experience-architecture`.** Navigation, conceptual models, locations, entry paths, exits, and task structure remain core UX work. Combining IA with terminology, content, and design-system rules creates one coherent structure for prototyping.

### 42. `mcp-integration-designer`

**Disposition: Handoff to `agent-development`.** Typed MCP contracts and protocol behavior are valuable engineering infrastructure, not the primary FDE product artifact. The AI experience spec identifies tool purpose, permissions, user-visible behavior, and required evidence; specialists define and implement the protocol.

### 43. `mve-mvp-planner`

**Disposition: Merge into `experiment-architecture`.** Choosing the smallest build that tests the riskiest assumption is central to FDE experimentation. It belongs with the hypothesis and decision threshold so minimum scope is determined by learning value rather than by a generic product milestone.

### 44. `ontology-graph-designer`

**Disposition: Merge product semantics into `ai-experience-spec`.** Domain entities, relationships, statuses, and user-facing meanings constrain what AI may infer and how users understand results. Database or graph implementation remains outside the core design toolkit.

### 45. `poc-planner`

**Disposition: Merge into `experiment-architecture`.** A POC is one experiment type used when technical feasibility is the riskiest assumption. The FDE defines the decision, minimum proof, acceptance evidence, and inference limits; engineering executes the technical probe.

### 46. `prompt-designer`

**Disposition: Merge product behavior into `ai-experience-spec`.** Prompt behavior influences clarification, response structure, refusal, tone, and user control, all of which need design requirements and examples. Hidden prompt strings, tuning, and runtime implementation are not treated as the product specification itself.

### 47. `prototype-qa`

**Disposition: Merge into `prototype-validation`.** Prototype conformance should be checked with rendered interaction, design, responsive, state, and accessibility behavior in one gate. A separate QA skill risks splitting requirement coverage from the actual user experience being tested.

### 48. `prototyping-assist`

**Disposition: Drop as a standalone router.** It selects a prototyping method but does not own the experiment or prototype artifact. `experiment-architecture` chooses the minimum valid fidelity, and `ui-prototyping` produces the resulting testable experience.

### 49. `provenance-ledger-designer`

**Disposition: Merge product semantics into `ai-experience-spec`.** Users need to know where claims came from, how fresh they are, and whether content is grounded or generated. The visible provenance contract remains core while storage and ledger implementation are handed off.

### 50. `terminology-taxonomy-designer`

**Disposition: Merge into `experience-architecture`.** Controlled vocabulary spans navigation, content, filters, statuses, and AI explanations. Keeping it with IA ensures one canonical user-facing term per concept rather than a taxonomy disconnected from the task flow.

### 51. `ui-creative-technologist`

**Disposition: Merge into `ui-prototyping`.** Building realistic, inspectable UX/UI remains a core capability. V0.76 narrows it to approved requirements and experiment fidelity so creative technology does not expand into unapproved features or production engineering.

## 04 Validate

### 52. `accessibility-verification`

**Disposition: Merge into `prototype-validation`.** Accessibility is a required UX acceptance gate, not optional polish. Keyboard, focus, semantics, labels, status announcements, contrast, and responsive access are tested alongside the exact task and states being validated.

### 53. `agentic-eval-harness`

**Disposition: Merge product-level evaluation design into `experiment-architecture`.** Golden cases, behavior measures, thresholds, guardrails, and decision rules belong in the experiment contract. Implementing and running a production evaluation harness remains agent-development or engineering work.

### 54. `browser-testing-with-devtools`

**Disposition: Merge into `prototype-validation`.** Live DOM, rendered state, viewport, console, and interaction evidence are methods used to verify the experience. DevTools is not a separate product-design outcome; it supports the unified validation report.

### 55. `code-review-and-quality`

**Disposition: Handoff to `engineering-review`.** Correctness, readability, architecture, security, and performance of implementation require engineering expertise. Design supplies the behavioral contract and consumes severity-ranked findings without pretending to certify code quality.

### 56. `code-simplification`

**Disposition: Handoff to `engineering-review`.** Simplifying correct code is maintenance work that does not create a product-design decision artifact. It may support delivery quality, but it should not trigger as part of the FDE design loop.

### 57. `debugging-and-error-recovery`

**Disposition: Handoff to `engineering-review`.** Diagnosing implementation failures is engineering work. Design still owns the expected user-visible error and recovery behavior, while specialists reproduce and fix the runtime defect against those acceptance IDs.

### 58. `design-review`

**Disposition: Merge into `prototype-validation`.** Visual hierarchy, interaction clarity, design-system fidelity, content, state coverage, and domain fit are core UX review concerns. They gain stronger decision value when findings cite affected requirements and experiment impact.

### 59. `performance-optimization`

**Disposition: Handoff to `engineering-review`.** Designers can specify acceptable user-visible response and loading behavior, but profiling and remediating Core Web Vitals or runtime bottlenecks requires measured engineering evidence. The handoff returns findings against affected acceptance criteria.

### 60. `security-and-hardening`

**Disposition: Handoff to `security-review`.** Security deeply affects trust and design, but threat modeling, exploit analysis, and mitigation approval need specialist authority. The AI experience spec retains data classes, permissions, action boundaries, and abuse questions that the security review must verify.

### 61. `test-driven-development`

**Disposition: Handoff to `engineering-review`.** Code-level red-green-refactor practice belongs to implementation ownership. V0.76 preserves behavior-level acceptance criteria and experiments but does not prescribe or certify an engineering team's coding method.

## 05 Ship

### 62. `documentation-and-adrs`

**Disposition: Merge into `decision-log`.** The important design function is preserving why a choice was made, alternatives, evidence, consequences, and supersession. One decision history avoids a separate ADR process that can drift from product and experiment commitments.

### 63. `feedback-collector`

**Disposition: Merge into `field-feedback`.** Capturing raw feedback remains core, but it needs participant identity controls, method, prototype version, observed-versus-reported distinction, experiment links, and inference limits. The combined skill turns collection into decision-usable evidence.

### 64. `focus-group-planner`

**Disposition: Merge into `field-feedback`.** Focus groups remain available when shared language, attitudes, or group dynamics are the question. They are treated as one method with explicit limitations, not a default substitute for individual task observation.

### 65. `framework-handoff`

**Disposition: Merge into `delivery-handoff`.** Transitioning an approved product contract from design to delivery is core FDE work. The consolidated handoff freezes requirement IDs, preserves evidence and trust boundaries, requests specialist evidence, and prevents silent implementation redefinition.

### 66. `observability-and-instrumentation`

**Disposition: Handoff to `engineering-delivery`.** Design and experiment work define outcomes, guardrails, events of interest, and evidence needs. Production logging, metrics pipelines, privacy controls, and operational dashboards are implemented and verified by engineering.

### 67. `shipping-and-launch`

**Disposition: Handoff to `engineering-delivery`.** Staged rollout, deployment, monitoring, and rollback execution are delivery responsibilities. The FDE handoff supplies approved acceptance criteria, target population, guardrails, and rollback triggers without claiming production authority.

### 68. `uxr-feedback-assist`

**Disposition: Drop as a standalone router.** It chooses among Learn-phase feedback methods rather than producing evidence itself. `field-feedback` selects the method from the experiment question, and `decision-log` owns the resulting commitment.

## Accounting

| Disposition | Count | Meaning |
|---|---:|---|
| Merge | 46 | Capability remains inside one of the 12 core skills |
| Handoff | 14 | Concern remains, specialist executes or verifies it |
| Drop | 8 | Router or output adapter leaves the core skill inventory |
| **Total** | **68** | Every v0.75 skill has one disposition |