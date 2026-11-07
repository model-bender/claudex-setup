---
id: steer-auto-compaction-from-claude-md
created: 2026-08-16
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/best-practices
---

# Steer Auto-Compaction From CLAUDE.md Instead of Reaching Straight for a PreCompact Hook

## TL;DR

Auto-compaction reads instructions from CLAUDE.md, so you can name what must survive summarization without writing any hook at all.

## Why it matters

Auto-compact is the least controllable context event in a long session: it fires when it fires, and whatever the summarizer drops is gone. The corpus's current answer is the PreCompact hook, which means a script, a settings edit, and a maintained context file.

A documented, zero-setup lever that steers the summarizer itself is strictly cheaper for the common case - and most people do not know CLAUDE.md is consulted at compaction time at all.

## How to apply

Add a CLAUDE.md line naming what compaction must keep: the modified-file list, the verification commands, the path to the current plan file. Keep the PreCompact hook for facts that must be *re-injected* rather than merely preserved - the two are complementary, not competing.

> "Customize compaction behavior in CLAUDE.md with instructions like `\"When compacting, always preserve the full list of modified files and any test commands\"` to ensure critical context survives summarization", Claude Code docs, Best practices

## Related

[[precompact-hook-reinjects-context-to-survive-compaction]]
