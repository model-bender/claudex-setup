---
id: pin-subagent-spawn-depth-the-default-flipped-twice
created: 2026-07-25
status: active
supersedes: null
category: agents
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Pin `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`: the Nesting Default Flipped Twice in Three Releases

## TL;DR

Nested subagent spawning was disabled by default in 2.1.217 and re-enabled to depth 3 in 2.1.219, so any workflow that depends on layered fan-out should set the depth explicitly rather than inherit whatever the current default happens to be.

## Why it matters

A layered-analysis pattern silently became a flat one on 2.1.217, and silently became three-deep, with the token multiplication that implies, on 2.1.219, both without the user changing anything. A default that has moved twice in three releases is not a default you can build a workflow on.

## How to apply

Set `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` in the settings `env` block to the depth you actually want, using `1` to disable nesting entirely. Its sibling knob `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` caps concurrency (20 by default), set both if an unattended fan-out's cost matters.

> "Subagents can now spawn nested subagents up to depth 3 by default (was 1); set CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1 to disable nesting", Claude Code CHANGELOG 2.1.219

## Related

[[max-budget-usd-now-halts-background-subagents]], [[supervisor-agent-unblocks-worker-agents-and-escalates-by-exception]], [[cap-parallel-subagent-concurrency-with-max-concurrent-subagents]]
