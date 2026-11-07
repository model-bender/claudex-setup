---
id: cap-parallel-subagent-concurrency-with-max-concurrent-subagents
created: 2026-08-31
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Cap Parallel Subagent Concurrency With CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS (Default 20)

## TL;DR

CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS caps how many subagents run at once (20 by default); set it in the settings env block whenever an unattended fan-out's cost or machine load matters.

## Why it matters

Concurrency is a separate knob from spawn depth, and it is the one that directly bounds how much token burn and load a fan-out generates at any moment. Other lessons advise limiting concurrency only generically (step through a plan, bound spend explicitly), so the actual env var stays invisible to anyone scanning titles. Given that the sibling nesting default has already flipped twice, an explicit pin beats inheriting whatever the current default happens to be.

## How to apply

Add CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS to the settings env block with the ceiling you want; the default is 20. For unattended fan-outs where cost matters, set it together with CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH so both the breadth and the depth of the fan-out are pinned.

## Related

[[pin-subagent-spawn-depth-the-default-flipped-twice]]
