# Changelog

## 0.76.0-draft - 2026-07-27

### Scope

- Reframed the package around FDE product thinking, AI experience design specifications, experiment architecture, and UX/UI.
- Reduced the top-level skill inventory from 68 to 12 consolidated skills.
- Accounted for every v0.75 skill in a machine-readable disposition ledger.

### Consolidated

- Combined intake, method selection, and known-unknown mapping into `fde-intake`.
- Combined analysis reporting, survey analysis, pains, journeys, JTBD, and evidence-backed archetypes into `field-research-synthesis`.
- Combined problem statements, design POV, and HMW framing into `problem-opportunity-frame`.
- Combined concept generation, strategic comparison, and prioritization into `concept-prioritization`.
- Combined design decisions, Traffic Light commitment, and ADR history into `decision-log`.
- Combined PRD and behavioral spec work with product-level context, source, grounding, confidence, provenance, ontology, prompt behavior, and HITL contracts in `ai-experience-spec`.
- Combined hypothesis, MVE/MVP, POC, experiment planning, and product-level golden-case criteria into `experiment-architecture`.
- Combined IA, content, terminology, and design-system rules into `experience-architecture`.
- Combined prototype conformance, rendered checks, accessibility, and design review into `prototype-validation`.
- Combined feedback collection and focus-group planning into `field-feedback`.

### Removed from core

- Removed thin phase routers; the gated workflow now selects the next skill directly.
- Removed HTML and Excalidraw format adapters from the core inventory.
- Routed agent runtime, MCP, design-tool integration, code review, debugging, performance, security, observability, and launch implementation to explicit specialist handoffs.

### Contract changes

- Added stable evidence, finding, decision, requirement, state, acceptance, experiment, and validation IDs.
- Added explicit failure and recovery behavior to every core skill.
- Added source, freshness, uncertainty, provenance, and consequential-action requirements to the AI design spec.
- Added numeric or categorical precommitment thresholds and result matrices to experiment planning.
- Added cross-skill traceability and no-silent-redefinition gates.

### Validation state

- Added deterministic package validation and a four-loop behavioral evaluation protocol.
- Deterministic package validation passes, including all 68 source paths and frontmatter contracts.
- Qualitative source-body scoring and behavioral evaluation remain not run.
- The release remains `0.76.0-draft` and Yellow until the documented gates pass.
