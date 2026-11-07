---
id: generate-editable-architecture-diagram-to-orient-and-target-the-model
created: 2026-07-10
status: active
supersedes: null
category: workflows
sources:
  - transcripts/sean-kochel/5-new-vibe-coding-repos-you-haven-t-heard-of-yet_UnzD_bwylWs_20260703.txt
---

# Generate an Editable Whole-App Architecture Diagram to Orient Yourself and Point Claude at the Right Layer

## TL;DR

Use a draw.io/diagram skill to render an editable architecture diagram of your whole app (presentation → state → service → data → edge layers) so you build a real mental model and can point Claude at the exact layer a problem lives in instead of making it explore blindly.

## Why it matters

When you (especially as a non-engineer) don't know how your app's pieces connect, every fix means Claude burns tokens re-exploring the codebase and you can't sanity-check where a bug lives; a persistent architecture map both saves that exploration cost and turns each session into a learning loop, since you can only push these tools as far as your own understanding goes.

## How to apply

Install the draw.io CLI and its skill, invoke the skill with a natural-language request ('visualize the service layers in my repo'), and it explores the codebase and emits an editable diagram; use it to locate the right module before prompting (e.g. 'the chat-parsing logic lives in the resolver layer, audit there') so you don't send the model off reading irrelevant files, and re-run it to drill into specific service→DB connections as the app grows.
