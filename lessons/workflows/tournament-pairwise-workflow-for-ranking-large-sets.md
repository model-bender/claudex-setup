---
id: tournament-pairwise-workflow-for-ranking-large-sets
created: 2026-07-10
status: active
supersedes: null
category: workflows
sources:
  - transcripts/mark-kashef/master-all-6-claude-code-dynamic-workflows_g9b9G8dcS8Y_20260704.txt
---

# Rank Large Candidate Sets With a Pairwise Tournament Workflow, Not Cold Absolute Scoring

## TL;DR

For ranking many items (resumes, titles, product names), run a dynamic workflow of pairwise head-to-head comparisons in fresh-context agents with a deterministic loop holding the bracket - each round can carry its own rubric - instead of scoring each item cold in one session.

## Why it matters

Absolute scoring of hundreds of items in one context bloats it, drifts, and inherits self-preference bias, whereas models judge relative head-to-head comparisons far more reliably than cold numeric scores; a per-match fresh context keeps each decision unbiased and individually traceable. This is one of the six patterns from Anthropic's official dynamic-workflows masterclass.

## How to apply

Prompt: 'use a workflow to rank every X by running a tournament of pairwise comparisons against a rubric, where each head-to-head match is its own comparison agent and the deterministic loop holds the brackets so only the running order stays in context.' Give successive rounds different rubrics if you want to filter on different criteria as the bracket narrows.
