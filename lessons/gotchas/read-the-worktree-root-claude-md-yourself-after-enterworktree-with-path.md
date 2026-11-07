---
id: read-the-worktree-root-claude-md-yourself-after-enterworktree-with-path
created: 2026-10-11
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/99275
---

# After EnterWorktree With path:, Read the Worktree's Root CLAUDE.md and AGENTS.md Yourself

## TL;DR

An open issue reports that `EnterWorktree` with `path:` never loads the worktree's root CLAUDE.md or its `@AGENTS.md` import; only subdirectory CLAUDE.md files load.

## Why it matters

A session that follows a repo's own "work in a worktree" instruction silently loses that repo's main instructions.

## How to apply

After entering a worktree that way, have Claude Read `<worktree>/CLAUDE.md` and `AGENTS.md` explicitly, or wire a PostToolUse hook on `EnterWorktree` that adds a reminder to do so (the issue author's workaround). Checked: `EnterWorktree` has 20 hits in the 2.1.296 binary; the bug itself was not reproduced here.

> "After `EnterWorktree` with `path:` (launch directory = a parent folder containing the repo), the worktree's **root** `CLAUDE.md` (and its `@AGENTS.md` import) is never loaded into context.", anthropics/claude-code issue #99275
