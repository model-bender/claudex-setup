---
id: sandboxed-sessions-cannot-run-git-worktree-add
created: 2026-11-15
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Don't let a sandboxed session run git worktree add: create worktrees outside the sandbox or with EnterWorktree

## TL;DR

Inside the Bash sandbox, worktree management and commits into a worktree the session was not started in now fail.

## Why it matters

Orchestrator sessions that spawn per-task worktrees with raw `git worktree add` and commit into them will start failing under the sandbox. The failure reads as a read-only error. A related 2.1.323 line says worktree creation now refuses `.git` links and `cp -al` copies ("use a plain clone").

## How to apply

Start each session inside its worktree (`claude -w <name>` or `cd` first), use EnterWorktree, or create worktrees from outside the sandbox. Do not widen the sandbox to work around it.

> "Changed the sandbox on macOS and Linux: `git worktree add`, `move` and `remove` now fail read-only, as do commits in a worktree the session wasn't started in or given, even one inside the project", Claude Code CHANGELOG 2.1.323
