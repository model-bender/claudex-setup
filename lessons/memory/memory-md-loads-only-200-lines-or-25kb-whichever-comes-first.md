---
id: memory-md-loads-only-200-lines-or-25kb-whichever-comes-first
created: 2026-10-02
status: active
supersedes: null
category: memory
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/memory
---

# Keep MEMORY.md Under 25KB as Well as 200 Lines: Long Entries Hit the Byte Cap First

## TL;DR

Only the first 200 lines or the first 25KB of MEMORY.md load at session start, whichever comes first, so an index with long one-line entries can be cut off well before line 200.

## Why it matters

Long one-line entries can hit the 25KB cap before 200 lines, silently hiding the tail of the index.

## How to apply

Keep one short line per entry and push detail into topic files. Check `wc -c MEMORY.md` as well as the line count. A community issue (anthropics/claude-code#91188, not a staff statement) reports a compaction reminder near 17.1KB that cannot be configured.

Verified: Read live docs memory.md lines 31 and 542. Issue 91188 body confirms the 17.1KB compaction reminder and no setting to change it (community report, not staff). Library has configuration/auto-memory-and-autodream-for-session-continuity; grep for "25KB" found nothing.

> "The first 200 lines of `MEMORY.md`, or the first 25KB, whichever comes first, are loaded at the start of every conversation. Content beyond that threshold is not loaded at session start.", Claude Code docs (memory)

## Related

[[memory-index-keep-under-200-lines-autodream]]
