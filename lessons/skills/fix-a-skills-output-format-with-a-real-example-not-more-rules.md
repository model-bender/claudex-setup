---
id: fix-a-skills-output-format-with-a-real-example-not-more-rules
created: 2026-11-22
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everyone-ignore-these-claude-concepts-but-they-change-everything_6VjeXzvpoJo_20261120.txt
---

# Fix a skill's output format with a real example, not more rules

## TL;DR

When a skill keeps getting the layout slightly wrong, stop adding instructions and show an example of what good looks like.

## Why it matters

Anthropic's prompting guide calls examples one of the most reliable ways to steer output and suggests three to five.

## How to apply

Reference at least one real example of the finished output in the SKILL.md body, or put three to five examples in a separate reference file that the skill points to.

Checked: Platform prompting guide says to include three to five examples for best results (live docs fetched 2026-11-22). Correction: the transcript's 72% to 90% accuracy figure comes from Anthropic's 'advanced tool use' post, where it describes tool use examples on complex parameter handling, not examples in prompts or skills, so it is left out of the claim.

## Related

[[personalize-a-single-installed-skill-in-15-minutes]], [[delete-examples-and-negative-constraints-from-claude-md]]
