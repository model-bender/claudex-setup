---
id: keep-nested-claude-md-under-the-size-limit-or-only-its-start-loads
created: 2026-10-25
status: active
supersedes: null
category: configuration
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21309
---

# Keep Each Nested CLAUDE.md Under the Size Limit: an Oversized One Now Loads Only Its Start

## TL;DR

Since 2.1.309 a nested CLAUDE.md over the size limit loads only its start (before, reading files under it could make a session compact repeatedly), so rules near the end of a huge per-folder file are dropped.

## Why it matters

Nothing warns you that the tail of the file was cut, so instructions placed late in a large nested CLAUDE.md silently stop applying.

## How to apply

Keep nested CLAUDE.md files short, split a big one by folder, and put the rules that must hold at the top. The changelog does not state the limit.

> "Fixed sessions compacting repeatedly after reading files under a very large nested CLAUDE.md; a nested CLAUDE.md over the size limit now loads only its start", Claude Code CHANGELOG 2.1.309

