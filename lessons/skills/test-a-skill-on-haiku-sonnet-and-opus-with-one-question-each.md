---
id: test-a-skill-on-haiku-sonnet-and-opus-with-one-question-each
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everything-you-know-about-skills-is-outdated_e7TY56-yIvM_20261002.txt
---

# Test a skill on every model you will run it with, asking one question per model

## TL;DR

A skill's result depends on the model under it. Run it on each model you use and ask Haiku: enough guidance? Sonnet: clear and efficient? Opus: does it avoid over-explaining?

## Why it matters

Simon Scrapes says most people write and test a skill on whichever model is newest that month. Newer higher-end reasoning models can do worse with older, more prescriptive instructions, while smaller models still need the detail. A script runs the same on every model, so a step one model skips is a candidate for a script.

## How to apply

Run your most used skill on the same task with Haiku, then Sonnet, then Opus. If Haiku misses a step, make that step clearer or turn it into a script. If Opus does worse with the skill than without it, cut instructions until it does better. If you share the skill, note the intended model in the frontmatter or description.

Verified: Anthropic skill best practices page, fetched 2026-10-02: section 'Test with all models you plan to use' lists the three per-model questions exactly. The advice to cut instructions when Opus does worse with the skill than without is the creator's reading, not stated in that section.

## Related

[[retune-skills-when-you-swap-model-or-harness]], [[simplify-a-skill-after-a-model-upgrade-instead-of-adding-detail]]
