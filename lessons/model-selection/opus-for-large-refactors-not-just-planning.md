---
id: opus-for-large-refactors-not-just-planning
created: 2026-09-01
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/ray-amjad/my-claude-code-workflow-for-2026_20260307.txt
---

# Use Opus for Large-Scale Refactors, Not Only for Planning

## TL;DR

Use Opus for large-scale feature builds and multi-file refactors, not only for planning; it is reported as the primary implementation model for that class of work roughly 70-80% of the time.

## Why it matters

This runs counter to a simpler 'Opus plans, Sonnet executes' framing; the reported real usage pattern puts Opus in the execution seat for big changes because of its ability to change many files consistently and write clean, focused code.

## How to apply

When a change spans many files or is a large refactor, default to Opus for the actual implementation, not just for producing the plan.

## Related

[[model-selection-opus-sonnet-haiku-use-cases]]
