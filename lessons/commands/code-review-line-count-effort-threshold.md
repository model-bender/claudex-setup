---
id: code-review-line-count-effort-threshold
created: 2026-09-01
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Set a 100-Line Threshold in CLAUDE.md to Auto-Pick /code-review's Effort Level

## TL;DR

Write a CLAUDE.md rule that runs /code-review at medium effort for changes under 100 lines and high effort for anything bigger, so effort selection stops being a manual guess.

## Why it matters

The presenter adds exactly this rule to CLAUDE.md ('run /code review the skill at medium setting if it's a small change less than 100 lines and a high setting if it's a change that's bigger than that') so the task lifecycle picks the right cost/thoroughness tradeoff automatically instead of always defaulting to one setting.

## How to apply

Add a line to CLAUDE.md such as: 'Before verifying changes, run /code-review at medium effort in a sub agent for diffs under 100 lines, and high effort for diffs at or above 100 lines.'

## Related

[[default-to-code-review-low-it-spawns-no-agents]], [[code-review-reuses-your-last-effort-level]]
