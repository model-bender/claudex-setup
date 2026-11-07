---
id: stack-several-skills-in-one-prompt
created: 2026-09-12
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Name Several Skills in One Prompt and Let Them Compose

## TL;DR

Skills can be invoked together in a single request and nest up to five levels deep, so one prompt can produce a draft with one skill and route it through an editing skill on the way out.

## Why it matters

Building skills modularly is wasted if you only ever fire one at a time. The example asks for a UGC script and a long-form article and requires both to pass through a humanizer skill, and the same trick stacks a plain-English skill with an anti-slop skill to get both properties in one pass rather than two rounds of manual copy-paste.

## How to apply

Write the request as an explicit chain: 'create X and Y for my most recent video, and make sure they pass through <skill>'. Keep skill descriptions non-overlapping first, because near-identical descriptions are what stops the right ones activating.

## Related

[[chain-skills-with-condensed-handoff-summaries]], [[skills-complementary-not-overlapping]], [[skill-description-is-routing-logic-not-marketing]]
