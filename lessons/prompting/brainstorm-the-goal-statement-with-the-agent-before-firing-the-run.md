---
id: brainstorm-the-goal-statement-with-the-agent-before-firing-the-run
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: codex
sources:
  - transcripts/ray-amjad/the-codex-feature-that-s-going-viral-right-now_20260603.txt
---

# Draft the Goal Statement With the Agent Before You Start a Multi-Hour Goal Run

## TL;DR

A vague goal like 'make this better' has no stopping condition and runs until you kill it, so sharpen the objective in conversation first, then fire it.

## Why it matters

A goal run is measured in hours and is expensive to get wrong, and its failure mode is silent: it keeps working because nothing in the objective tells it when it has won. The parent lesson answers which work suits /goal at all. Writing the objective is the separate discipline, and it is the step people skip precisely because starting the run looks cheap.

## How to apply

Before invoking /goal, ask the agent to critique your objective: is it observable, what exactly would count as done, what will it measure to know it is improving. Rewrite until the stopping condition is a number or a check it can run itself, then start. Pair it with a safety cap so even a badly framed goal terminates.

## Related

[[use-goal-for-unfolding-work-then-redo-it-from-a-distilled-spec]]
