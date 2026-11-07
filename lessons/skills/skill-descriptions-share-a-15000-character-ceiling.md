---
id: skill-descriptions-share-a-15000-character-ceiling
created: 2026-08-31
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/how-to-use-claude-code-skills-like-the-1-it-s-easy-actually_20260307.txt
  - transcripts/simon-scrapes/the-claude-code-skills-trap-most-people-fall-for-this_20260307.txt
  - transcripts/simon-scrapes/every-level-of-claude-code-skills-in-27-mins_20260424.txt
  - transcripts/ray-amjad/anthropic-just-dropped-their-internal-skills-strategy_20260424.txt
  - transcripts/simon-scrapes/the-easiest-way-to-get-ahead-with-claude-code_20260424.txt
  - transcripts/ray-amjad/better-than-mcps-claude-code-s-new-skills-feature_20260307.txt
---

# Budget Skill Descriptions Against a Shared Listing Budget and a Per-Skill Cap

## TL;DR

Skill descriptions share one listing budget, and each description has its own cap. On Claude Code 2.1.281 the budget is `skillListingBudgetFraction`, default 0.01 (1% of the context window, measured in characters), and the per-skill cap is `skillListingMaxDescChars`, default 1,536 characters; longer descriptions are cut off. Keep each description short, put the trigger words first, and prune marginal skills. (Corrected 2026-09-24: the source's ~15,000-character figure, and a later 2,048 and 0.02 correction, are both out of date. The id keeps its old name so links still resolve.)

## Why it matters

This is a hard ceiling, not just a soft context tax: an over-budget catalog cannot carry every skill's full description, so one bloated description or a pile of rarely-used skills degrades the routing surface for the rest. The general advice to keep skills lean does not tell you the budget is fixed and shared, which is what makes catalog curation a zero-sum decision.

## How to apply

Treat description length as a shared resource: when adding a skill, weigh its description against the listing budget (1% of the context window by default) and the 1,536-character per-skill cap, keep each description short, and prune marginal skills instead of letting the catalog grow. Prefer a few well-built skills whose descriptions carry their trigger language over many overlapping ones.

## Related

[[skill-md-under-200-lines-progressive-disclosure]]
