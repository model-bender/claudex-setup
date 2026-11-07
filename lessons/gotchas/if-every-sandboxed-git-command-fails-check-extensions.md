---
id: if-every-sandboxed-git-command-fails-check-extensions
created: 2026-08-22
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# If Every Sandboxed Git Command Fails, Check extensions.worktreeConfig

## TL;DR

On Linux, a repo with `extensions.worktreeConfig` set had every sandboxed git command fail before 2.1.239, because the sandbox made the not-yet-created `.git/config.worktree` unreadable.

## Why it matters

The symptom (all git commands failing only inside the sandbox, only in some repos) points at sandbox permissions or the repo, not at a git config extension that a worktree workflow may have enabled without you noticing, an easy hour to lose in exactly the worktree-heavy setups agent teams use.

## How to apply

Check `git config --get extensions.worktreeConfig` in the failing repo and upgrade to 2.1.239+; as a stopgap, create an empty `.git/config.worktree` or unset the extension.

> "Fixed the Linux sandbox making a nonexistent `.git/config.worktree` unreadable, which broke every sandboxed git command in repos with `extensions.worktreeConfig` set", canonical: Claude Code CHANGELOG 2.1.239
