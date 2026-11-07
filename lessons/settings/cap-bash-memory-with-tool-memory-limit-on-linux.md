---
id: cap-bash-memory-with-tool-memory-limit-on-linux
created: 2026-08-16
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Cap Bash Memory With `CLAUDE_CODE_TOOL_MEMORY_LIMIT` on Linux

## TL;DR

Linux sessions can put Bash tool commands in a memory cgroup, so a build or test run that balloons gets killed instead of taking the session or the machine down with it.

## Why it matters

Memory exhaustion is a known way to lose in-flight work - the corpus already carries the warning that spawning roughly six parallel subagents can OOM-crash Claude Code mid-task. This is the first per-command containment for the other half of the same problem: the runaway `make`, the test suite that leaks, the bundler that eats the box.

It is opt-in, so nobody gets it by default, and it is exactly the kind of protection you want configured *before* the overnight run rather than after losing one.

## How to apply

Add `"CLAUDE_CODE_TOOL_MEMORY_LIMIT": "<bytes>"` to the `env` block of `~/.claude/settings.json` on any Linux box that runs unattended or overnight sessions.

> "Added opt-in memory cgroup support for Bash tool commands on Linux (`CLAUDE_CODE_TOOL_MEMORY_LIMIT`) so a runaway build can't stall the session", Claude Code CHANGELOG 2.1.233

## Related

[[guard-unattended-agent-runs-with-a-stall-watchdog-and-bounded-retry]]
