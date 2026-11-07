---
id: audit-your-skills-for-routing-collisions
created: 2026-10-11
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/anthropic-just-released-13-new-skills-to-level-up-your-claude-setup_CNsP0mi1DLw_20261009.txt
---

# Audit Your Skill Library for Routing Collisions Where Two Skills Match the Same Request

## TL;DR

Austin warns that when two skills could trigger on near-identical phrases (his example: 'What should I post?' and 'What should we post this month?'), neither pointing to the other, the wrong one fires.

## Why it matters

He says it wastes tokens and triggers skills you did not want, and he found collisions in Anthropic's own small business plugin.

## How to apply

Review your skills' trigger descriptions for overlap, split strategic from operational duties, and make descriptions point to each other. Austin shows an on-screen prompt for finding overlaps; the wording is not in the transcript.

## Related

[[skills-complementary-not-overlapping]], [[disambiguate-tool-descriptions-with-do-not-use-clauses]]
