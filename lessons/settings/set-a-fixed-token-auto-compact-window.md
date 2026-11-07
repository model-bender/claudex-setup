---
id: set-a-fixed-token-auto-compact-window
created: 2026-08-29
status: active
supersedes: null
category: settings
tool: claude-code
sources:
  - transcripts/simon-scrapes/19-claude-code-mistakes_icM0ewXGvAw_20260824.txt
---

# Set the auto-compact window to a fixed token count: the percentage threshold is gone

## TL;DR

Auto-compaction no longer fires at ~95% of the window: with no auto-compact window limit set, Claude Code compacts only when the conversation reaches the model's context limit (with per-model exceptions), so set the auto-compact setting to a fixed token budget like 100K, because quality degrades long before the window is full.

## Why it matters

The old mental model (a percentage threshold you could override) is obsolete, and the new default is worse for quality: waiting until the hard model limit means you spend the whole late conversation in the degraded-retrieval zone. Anthropic's own long-context benchmark shows retrieval accuracy falling substantially as context grows, so a fixed budget well under the limit keeps the session in the range where the model still reliably finds its rules. A fixed token number is also predictable across models in a way a percentage never was.

## How to apply

Set the auto-compact window setting to a concrete figure, e.g. 50K or 100K tokens, instead of leaving it on automatic (CLAUDE_CODE_AUTO_COMPACT_WINDOW is the env-var form). Once the conversation hits that budget it auto-compacts, keeping the working set small. Pair it with CLAUDE.md compaction instructions naming what must survive the summary.

Corrected 2026-10-25: this lesson named the variable `CLAUDE_CODE_AUTOCOMPACT_WINDOW`, which has 0 occurrences in the installed 2.1.310 binary; `CLAUDE_CODE_AUTO_COMPACT_WINDOW` has 17. Before 2.1.304 a suffixed value such as `200k` silently set a 100K window (see [[auto-compact-window-suffix-values-silently-set-100k-before-2-1-304]]).

## Related

[[context-rot-prevention-compact-proactively]], [[steer-auto-compaction-from-claude-md]]
