---
id: fork-is-now-a-background-session-subtask-is-the-in-session-fork
created: 2026-07-25
status: active
supersedes: null
category: commands
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
  - https://x.com/dmwlff/status/2062273521603195078
---

# `/fork` Now Spawns a Background Session: the In-Session Forked Subagent Is `/subtask`

## TL;DR

`/fork` changed meaning: it now copies your conversation into a detached background session with its own row in `claude agents`, and the old behaviour, a forked subagent running inside your session, moved to `/subtask`.

## Why it matters

Existing guidance about forked subagents (they inherit the full conversation's nuance, and you shouldn't use them to review code they just wrote) now attaches to `/subtask`. Typing `/fork` out of habit gets you a different primitive with a different place for its output. Worse, this naming has churned inside a single quarter, a June announcement described `/fork` as a background agent with `/branch` holding the drivable-copy behaviour, and the July CHANGELOG describes the split as `/fork` vs `/subtask`. Treat the command names here as volatile.

## How to apply

Use `/subtask` for the in-session forked subagent that inherits conversation nuance; use `/fork` when you want a detached copy in `claude agents` while you keep working. **REVISIT: verify with `/help` before relying on either name**, the fork/branch/subtask split moved twice between June and July 2026, so a workflow or CLAUDE.md rule that hardcodes one of these should be re-checked on upgrade.

> "`/fork` now copies your conversation into a new background session (its own row in `claude agents`) while you keep working; the in-session subagent it used to launch is now `/subtask`", Claude Code CHANGELOG 2.1.212

## Related

[[set-background-false-on-forked-skills-you-need-inline]]
