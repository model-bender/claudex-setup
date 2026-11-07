---
id: retest-prompt-and-agent-hooks-written-as-instructions
created: 2026-10-11
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Re-test prompt and agent Hooks Written as Instructions: Before 2.1.294 They Could Allow What They Described Blocking

## TL;DR

A `prompt` or `agent` hook phrased as an instruction ("Block commands that...") could approve the very thing it named until 2.1.294; Stop and SubagentStop prompt hooks phrased that way also stopped Claude early.

## Why it matters

A hook judged "working" because it never fired a denial may have been permitting everything. That failure is indistinguishable from having nothing to block.

## How to apply

Run 2.1.294 or later, then fire each `prompt` and `agent` hook once with an input it should deny and confirm the denial. This is a behaviour fix, so there is no setting to check.

> "Fixed `prompt` and `agent` hooks written as instructions (such as "Block commands that...") allowing what they should block", Claude Code CHANGELOG 2.1.294

> "Improved how `prompt` hooks on Stop and SubagentStop written as instructions (such as "Carry on if the build is broken") are judged, so Claude is less likely to stop early", Claude Code CHANGELOG 2.1.294
