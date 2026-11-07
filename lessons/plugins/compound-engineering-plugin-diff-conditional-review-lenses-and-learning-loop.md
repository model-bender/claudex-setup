---
id: compound-engineering-plugin-diff-conditional-review-lenses-and-learning-loop
created: 2026-07-10
status: active
supersedes: null
category: plugins
sources:
  - transcripts/sean-kochel/the-claude-code-plugin-you-ll-wish-you-found-sooner_PMm_vRk7vfQ_20260703.txt
---

# Run the Compound Engineering Plugin for Diff-Conditional Review Lenses and a Solved-Bug Learning Loop

## TL;DR

Every's Compound Engineering plugin is a 6-skill pipeline (ideate -> brainstorm -> plan -> work -> review -> compound) whose review step fires only the reviewer personas relevant to what your diff touched (design lens on UI, security on auth, Rails/Python/TS/DB reviewers by stack - 17 conditional plus always-on correctness/testing/maintainability) and whose compound step writes each solved problem to solutions/best-practices/*.md with 'applies when' metadata so future related work auto-pulls the fix.

## Why it matters

A flat panel of review personas spreads attention thin and a session's hard-won bug fixes evaporate by the next session; conditioning reviewers on the actual change concentrates scrutiny where it matters, and compounding solved problems into conditionally-surfaced learning docs means you stop re-solving the same nasty bug and each build cycle gets faster.

## How to apply

Install the plugin; use CE:ideate (code-base-aware brainstorm -> adversarial filter to ~7 surviving ideas) when you don't know what to build, CE:brainstorm->plan to harden requirements (it runs an adversarial plan review before you build), CE:work to implement, CE:review (conditional lenses auto-fix or defer by severity), then CE:compound after resolving something painful to persist the learning; skip ideate/brainstorm and jump straight to CE:plan when the idea is already concrete.
