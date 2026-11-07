---
id: skill-activation-rate-20-to-84-percent
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/how-to-use-claude-code-skills-like-the-1-it-s-easy-actually_20260307.txt
---

# Expect Skill Activation to Max Out Around 84% Even With a Well-Tuned Description

## TL;DR

An informal test found skills with a poor description activate as low as 20% of the time they should, and even with an optimized description plus supporting hooks, the measured ceiling was around 84%, not 100%.

## Why it matters

If a task's correctness depends on a skill firing every time it matches, budgeting for roughly 1-in-5 (or 1-in-6 at best) misses changes whether you rely on description-based auto-invocation or add an explicit trigger instead.

## How to apply

For a skill that must fire reliably, don't rely on description-based auto-invocation alone: tighten the description's trigger phrasing, and for safety- or correctness-critical tasks add an explicit slash command or hook trigger rather than trusting automatic activation.

## Related

[[skill-description-is-routing-logic-not-marketing]], [[run-a-skill-cold-to-verify-it-still-triggers]]
