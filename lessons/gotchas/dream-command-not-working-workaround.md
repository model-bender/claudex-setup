---
id: dream-command-not-working-workaround
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/the-only-claude-code-updates-you-need-to-know-apr-2026_20260424.txt
---

# If /dream Doesn't Trigger Memory Consolidation, Just Ask in Plain English

## TL;DR

The dedicated /dream (or similar) command for manually triggering auto-dream's memory consolidation is reported as unreliable; the workaround is to tell Claude directly, 'consolidate my memory files,' which runs the same cleanup process.

## Why it matters

Relying on a slash command that doesn't consistently fire means you might assume consolidation isn't available at all, when a natural-language instruction achieves the same outcome.

## How to apply

If the memory-consolidation slash command fails or does nothing, type the plain-English instruction 'consolidate my memory files' instead and Claude will run the same merge/prune/date-normalize pass.

## Related

[[auto-dream-memory-consolidation]]
