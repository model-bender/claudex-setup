---
id: claude-w-flag-for-built-in-worktree-scoped-sessions
created: 2026-09-01
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
  - transcripts/simon-scrapes/every-claude-code-concept-explained-for-normal-people_20260307.txt
  - transcripts/simon-scrapes/every-claude-code-workflow-explained-u0026-when-to-use-each_20260424.txt
---

# Use `claude -w <name>` to Launch a Session in Its Own Built-In Worktree

## TL;DR

The `-w` flag (e.g. `claude -w feature-1`) starts a session scoped to its own git worktree, useful specifically when two features being built in parallel touch overlapping parts of the codebase.

Running `claude --worktree <name>` (or `-w <name>`) uses that single name for both the new isolated working directory and the git branch it creates.

The -w flag takes a short text description, creates a new git worktree named after it, and drops you directly into a Claude Code session inside that worktree in one command.

## Why it matters

Without a worktree, if one parallel session refactors or moves a file another session expected to be in a certain shape or location, the second session's plan silently goes stale. A worktree holds the codebase static per feature until it's merged.

Knowing the flag sets two things from one value avoids surprise branch names when you only expected a folder name, or vice versa.

The transcript demonstrates this as the mechanism behind the Operator pattern: 'claude-w important new onboarding flow... claude-w checkout bug... claude-wesign user settings' each opens a separate isolated worktree/session pair without manual git worktree add steps.

## How to apply

Run `claude -w feature-1` and `claude -w feature-2` for two features that are likely to touch the same files. Skip worktrees when the parallel changes are in clearly distinct areas of the codebase (e.g. backend API vs. homepage copy) that won't collide.

Launch with `claude --worktree feature-auth` (or `-w feature-auth`) to get an isolated directory named feature-auth on a branch also named feature-auth.

Run `claude -w "short task description"` per independent task from your project root; Claude Code creates the worktree (visible under your project's worktrees) and starts the session there, so open one such command per terminal for tasks that don't depend on each other.

## Related

[[worktrees-for-parallel-independent-tasks]]
