---
id: gitignored-personal-claude-md-for-machine-specific-notes
created: 2026-09-01
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Keep a Gitignored Personal CLAUDE.md for Machine-Specific Notes Like 'You're Running in WSL'

## TL;DR

Alongside your committed root and project CLAUDE.md files, keep a personal-preferences file that stays only on your machine and is never committed, for environment facts like running under WSL.

## Why it matters

Different machines (e.g. Windows-via-WSL vs macOS) need different context, and that context is specific to you, not the team, so it shouldn't be checked in.

## How to apply

Create a local, gitignored file (e.g. local.md) alongside your CLAUDE.md hierarchy containing only machine-specific facts (e.g. 'you're running in WSL'), and reference or load it locally without committing it to the repo.

## Related

[[claude-md-hierarchy-keep-it-under-200-lines]]
