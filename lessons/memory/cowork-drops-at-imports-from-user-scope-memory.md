---
id: cowork-drops-at-imports-from-user-scope-memory
created: 2026-08-16
status: active
supersedes: null
category: memory
tool: claude-code
about: claude-cowork
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Cowork Sessions Drop `@`-Imports From User-Scope Memory - Inline Anything Load-Bearing

## TL;DR

If `~/.claude/CLAUDE.md` pulls in rules via `@path/to/file`, those files are no longer inlined in Cowork sessions as of 2.1.232: the pointer stays, the content does not arrive.

## Why it matters

The documented CLAUDE.md pattern is to keep the root file short and `@`-import the detail - which means the rules most likely to be imported are exactly the detailed, specific ones you most want enforced. In Cowork you end up with a memory file that still references them and a model that has never seen them, with no error and no missing-file warning.

## How to apply

Inline any rule that must hold in Cowork directly in `~/.claude/CLAUDE.md` (or the project CLAUDE.md) rather than behind an `@`-import. Confirm with `/context` inside a Cowork session that the content actually loaded, rather than assuming the import resolved.

> "Cowork sessions no longer inline external @-imports from user-scope memory files", Claude Code CHANGELOG 2.1.232

