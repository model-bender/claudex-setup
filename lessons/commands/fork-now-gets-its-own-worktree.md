---
id: fork-now-gets-its-own-worktree
created: 2026-08-07
status: active
supersedes: null
category: commands
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Stop Hand-Isolating Forked Sessions: /fork Now Creates Its Own Worktree

## TL;DR

As of 2.1.221, a session forked with `/fork` creates a new worktree of its own instead of working in the original session's checkout, so it is safe to run alongside continued foreground work in the same repo.

## Why it matters

Before this, a forked background session could edit files and run git commands in the very checkout your foreground session was using, so the two could clobber each other with no warning. Anyone who worked around that by manually creating a worktree first can drop the ceremony.

## How to apply

On 2.1.221 or later, just `/fork` and keep working; the isolation is automatic. Remember this is separate from the earlier naming change, where `/fork` became a background session and `/subtask` took over the in-session forked-subagent role.

> "Changed sessions forked with `/fork` to create a new worktree of their own instead of working in the original session's checkout", Claude Code CHANGELOG 2.1.221

## Related

[[fork-is-now-a-background-session-subtask-is-the-in-session-fork]]
