---
id: keep-specs-fuzzy-let-code-review-catch-edge-cases
created: 2026-07-10
status: active
supersedes: null
category: workflows
sources:
  - transcripts/ray-amjad/i-spent-a-day-with-anthropic-engineers-here-s-their-real-workflow_hMgB1bjkI7o_20260705.txt
---

# Keep Specs Fuzzy and Let End-Stage Code Review Catch Edge Cases

## TL;DR

Over-specifying every edge case turns a spec into code-in-English and forces stronger models into worse deviations on contact with the real codebase; give only the goal plus hard 'don'ts', then run 2-3 rounds of end-stage /code-review to surface edge cases instead of pre-planning them.

## Why it matters

Anthropic engineers (per Ray Amjad's Code-with-Claude event report) don't use spec-driven frameworks like OpenSpec/SpecKit/BMAD - a rigid spec is 'the map, not the territory', so when the agent must deviate mid-build a strict spec produces worse results than trusting it to adapt, and this gets truer as models improve (observed sharply with Fable 5, where deleting CLAUDE.md/memory/skills and giving a bare prompt still landed ~95%).

## How to apply

Describe the feature goal plus a few hard constraints (e.g. rate limiting), let the model interview you and optionally mock up, plan, execute, then loop /code-review (medium for small changes, max for big features) 2-3 rounds - it catches edge cases a 'perfect' upfront spec would have missed, and sometimes reveals the change was architecturally wrong so you discard the PR and re-prompt for a root-cause fix. Cap the review loop (Codex once ran 12-13 rounds) with a round/blast-radius limit.
