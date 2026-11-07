---
id: persist-artifact-state-in-the-url-fragment-so-a-link-reproduces-it
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/
---

# Persist an Interactive Artifact's State in the URL Fragment So a Link Reproduces the Exact View

## TL;DR

Ask for every control on a generated artifact (step, speed, filters, per-item decisions) to serialise into the #fragment, so you can send or paste back the exact view instead of describing it.

## Why it matters

The archive recommends HTML artifacts for several jobs: audit decision lists, numbered before-and-after change sets, UI state matrices, algorithm animations. All of them share the same failure at the moment they become useful, which is when you want to discuss one specific item or frame and are back to screenshots and prose. Fragment-encoded state is what makes the artifact addressable, and it costs one clause in the prompt that generated it.

## How to apply

When prompting for an interactive artifact, require that every control writes into the URL fragment and restores from it on load. Then share the link at the state you mean, and paste that same link back to the agent when asking for a change, so it opens on the thing you are talking about.

## Related

[[pay-down-cognitive-debt-with-an-animated-html-explainer-of-the]]
