---
id: pay-down-cognitive-debt-with-an-animated-html-explainer-of-the
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/
---

# Pay down cognitive debt with an animated HTML explainer of the algorithm

## TL;DR

When a prose walkthrough still leaves an algorithm opaque, have the agent build a single-page animated visualisation of it, with pause, speed and frame-stepping controls.

## Why it matters

Willison's own escalation is the evidence: the agent's report ("Archimedean spiral placement with per-word random angular offset") explained nothing, a linear walkthrough explained the code structure but not the algorithm, and only the animation made the mechanism click. Cognitive debt behaves like technical debt, once the core is a black box you can no longer plan features against it confidently.

## How to apply

Feed the existing walkthrough in (`Fetch <raw-url> to /tmp using curl so you can read the whole thing`), then ask for a self-contained HTML page that animates the algorithm step by step, with a slider that can be paused, sped up, or stepped frame by frame, and input persisted in the URL `#fragment` so a link reproduces the state.

## Staleness

Current. The chapter names Claude Opus 4.6 as having "quite good taste when it comes to building explanatory animations", the model name is stale (Opus 5 is current) but the claim is not model-version-dependent. Distinct from [[generate-editable-architecture-diagram-to-orient-and-target-the-model]] and another lesson, which are static structure aids for review rather than dynamic explanations of a mechanism.

> "When we lose track of how code written by our agents works we take on cognitive debt.", Simon Willison

## Related

[[persist-artifact-state-in-the-url-fragment-so-a-link-reproduces-it]]
