---
id: author-golden-references-with-strongest-model-replicate-with-cheaper
created: 2026-07-10
status: active
supersedes: null
category: model-selection
sources:
  - transcripts/ray-amjad/cheap-fable-5-ends-this-week-here-s-where-it-actually-matters_B1sYKOWVHR0_20260705.txt
---

# Author Golden Reference Implementations With Your Strongest Model, Then Replicate With Cheaper Ones

## TL;DR

For tricky, repeated code with no good canonical example online (hosted-MCP wiring, websockets, complex concurrency), have your strongest model build one golden reference in a clean project, then point cheaper models at it to copy-adapt across every service or app that needs it.

## Why it matters

Models generate new code better than they edit existing code, and a strong-model-authored canonical example amortizes the premium model's judgment across many cheaper runs - the cheaper model just replicates a known-good pattern instead of re-deriving janky integration code from scratch each place it appears.

## How to apply

Ask the strong model to generate a canonical example of the pattern in a brand-new folder/project; keep it as a durable golden reference; then have cheaper (e.g. Opus 4.8) agents reapply it everywhere it matters - ideal when one app has many similar services or many apps share similar logic.
