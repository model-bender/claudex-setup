---
id: retest-deny-rules-against-what-a-rewriting-pretooluse-hook-produces
created: 2026-10-11
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Re-test Deny Rules Against the Output of Any PreToolUse Hook That Rewrites Tool Input

## TL;DR

Before 2.1.290, some permission rules and safety checks were not applied to a tool call after a PreToolUse hook rewrote its input (`updatedInput`).

## Why it matters

If you run a hook that rewraps or redirects commands, the rewritten call may have bypassed your deny rules on older versions, and nothing in the transcript would show it.

## How to apply

Run 2.1.290 or later. For each rewriting hook, fire one call whose rewritten form should be denied and confirm it is. Checked: `updatedInput` has 132 hits in the 2.1.296 binary.

> "Fixed some permission rules and safety checks not being applied to a tool call after a PreToolUse hook rewrote its input", Claude Code CHANGELOG 2.1.290

