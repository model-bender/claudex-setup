---
id: symlink-one-shared-rules-directory-into-every-repo
created: 2026-09-12
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Keep One Shared Rules Directory and Symlink It Into Every Repo

## TL;DR

The rules folder follows symlinks, so maintain a single rules directory above your projects and symlink it into each repo instead of copying the same standards into every one.

## Why it matters

Copied rule files drift: you fix a standard in one repo and the other five keep the old wording. One physical directory behind symlinks means every repo picks up the edit, while the glob front matter still decides which file loads when.

## How to apply

Put the shared rule files in one top-level directory, symlink it to .claude/rules inside each repo, and keep repo-specific rules as real files alongside it. Skills are not safe to symlink this way because their frontmatter is not portable across tools.

