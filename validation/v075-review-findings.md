# v0.75 Review Findings

## TL;DR

The 68-skill inventory is too broad for an FDE design toolkit: product decisions are fragmented across many atomic skills while 22 entries are engineering handoffs, thin routers, or format adapters rather than core field-design capabilities.

## Evidence boundary

This is a structural review of the attached folder inventory and available workspace manifest descriptions. The source `SKILL.md` bodies, fixtures, and scripts were not readable in this session. Therefore these findings justify a curation hypothesis, not a claim that any individual v0.75 implementation is defective.

## Findings

### High: Product-level AI behavior has no single contract owner

The v0.75 inventory distributes user-visible AI behavior across `prd-author`, `spec-driven-development`, `agentic-trust-architecture`, `confidence-calibrator`, `context-engineer`, `data-integration-designer`, `grounding-critic-designer`, `hitl-boundary-designer`, `ontology-graph-designer`, `prompt-designer`, and `provenance-ledger-designer`.

That structure makes cross-cutting requirements easy to lose: a source can be defined without freshness behavior, a confidence rule without user-visible recovery, or a human boundary without the state and acceptance criterion that exercises it.

**v0.76 response:** `ai-experience-spec` is the single product-level owner. Runtime implementation remains an engineering handoff.

### High: The package mixes FDE design ownership with specialist engineering ownership

Fourteen source skills primarily concern workshop facilitation, runtime agent construction, protocol or vendor integration, implementation review, debugging, performance, security, tests, production instrumentation, or launch execution. Keeping them beside discovery and UX skills makes the toolkit promise expertise and validation authority it should request from specialists.

**v0.76 response:** retain the product question, affected requirement IDs, and required return evidence; route implementation through six typed handoffs in `external-handoffs.json`.

### High: Routers and output adapters inflate the trigger surface without owning decisions

Six thin assist/router skills and two format renderers appear as top-level choices. These entries select another method or presentation format but do not own a durable FDE decision artifact. Their presence creates avoidable trigger overlap with the actual work-producing skill.

**v0.76 response:** the gated workflow performs routing; format choices are optional adapters after the artifact contract is settled.

### Medium: Experiment ownership is split across hypothesis, planning, scope, POC, and eval skills

`hypothesis-creator`, `experiment-planner`, `mve-mvp-planner`, `poc-planner`, and `agentic-eval-harness` each represent part of one decision contract. Fragmentation can permit a hypothesis without a precommitted threshold, a minimum scope without a result matrix, or an eval without the product decision it changes.

**v0.76 response:** `experiment-architecture` owns the assumption, hypothesis, method, minimum decisive scope, threshold, guardrails, stop rules, and result-to-decision mapping. A technical POC is specialist-executed when required.

### Medium: Research representations can become deliverables by default

Analysis reports, personas, JTBD, journeys, survey analysis, and pain maps are separate skills. Without a common evidence owner, the package can encourage production of every representation even when only one helps the current decision.

**v0.76 response:** `field-research-synthesis` owns the evidence ledger and generates a journey, JTBD, or archetype only when it changes the target decision.

### Medium: UX structure and validation are distributed across adjacent skills

Information architecture, content, terminology, design systems, UI prototyping, prototype QA, browser checks, accessibility, and design review form two coherent contracts but appear as many independent entries.

**v0.76 response:** `experience-architecture` owns structure and vocabulary; `ui-prototyping` realizes the test path; `prototype-validation` owns rendered conformance and UX quality.

### Medium: Consolidation introduces a new risk of oversized skills

Reducing 46 source capabilities into 12 skills can create long procedures that agents partially execute. The largest risk is `ai-experience-spec`, which combines eleven source capability areas.

**Mitigation:** each consolidated skill has one primary artifact, stable IDs, required sections, acceptance gates, negative trigger cases, and a word-level contract validator. Behavioral evaluation must still show that agents complete every required section under realistic pressure.

## Inventory disposition

| Source phase | Skills | Merge | Handoff | Drop |
|---|---:|---:|---:|---:|
| 01-understand | 9 | 7 | 1 | 1 |
| 02-identify | 16 | 13 | 0 | 3 |
| 03-execute | 26 | 18 | 5 | 3 |
| 04-validate | 10 | 4 | 6 | 0 |
| 05-ship | 7 | 4 | 2 | 1 |
| **Total** | **68** | **46** | **14** | **8** |

Every source skill and rationale is listed in `v075-skill-review.csv`.

## Recommendation

Proceed with the 12-skill structure as a Yellow candidate. Do not graduate it until source-body disposition review, deterministic lint, 84 trigger-boundary cases, composition checks, and five end-to-end scenarios meet `DEEP-LOOP.md`.
