---
id: precompact-hook-reinjects-context-to-survive-compaction
created: 2026-07-10
status: active
supersedes: null
category: hooks
sources:
  - transcripts/mark-kashef/master-all-7-levels-of-claude-code-memory_OMkdlwZxSt8_20260704.txt
---

# Re-Inject a Curated Context File on the PreCompact Hook So Key Facts Survive Compaction

## TL;DR

Wire a PreCompact hook that injects a hand-maintained _context.md (identity, current goal, key decisions) into the session right before compaction, so the lossy auto-summary can't drop what matters.

## Why it matters

Compaction is non-deterministic and routinely discards the exact details you need to keep going, and a CLAUDE.md/SessionStart read is only best-effort and doesn't fire at compaction time; a PreCompact hook fires deterministically at the one moment the window is about to be summarized, guaranteeing your must-keep facts carry across the boundary.

## How to apply

Maintain a small markdown file of the session's must-keep facts; add a PreCompact hook (tag @claude-code-guide to write the settings.json entry) that reads it into the compacted context every time. Pair it with a SessionStart hook that injects the same identity/priming file at the start of each fresh session so both the start and the compaction boundary are covered deterministically.
