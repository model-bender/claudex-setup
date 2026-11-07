---
id: compact-inside-the-cache-window-not-after-it-expires
created: 2026-08-22
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/sean-kochel/anthropic_LWx5jp7eoBE_20260820.txt
---

# If You Use /compact, Run It Inside the Cache Window, Not After the Session Has Gone Cold

## TL;DR

Compacting more than an hour after your last message means the cache is gone and the model must reprocess the entire conversation just to produce the summary, so compact regularly during active work or clear instead.

## Why it matters

The compaction step is itself a model call over the whole conversation. While the cache is warm that call is cheap, because the prefix is already stored and does not have to be re-sent and reprocessed. Once the session has been idle past the cache TTL, running /compact forces a full re-read of everything before it can summarise, which is the most expensive possible moment to compact and exactly when people reach for it (coming back to a stale session). The creator's own preference is to avoid the problem entirely by using /clear between tasks, and he attributes never hitting plan limits on Max largely to clearing aggressively, noting that spec-driven tools make this easy because each stage is written to an artifact that carries the context forward.

## How to apply

If /compact is part of your workflow, run it during active work rather than on return to a cold session, keeping each compaction inside the cache window. Better, structure work so there is nothing to compact: persist the state you need into a file or artifact and /clear between distinct tasks, so the next task starts from a written handoff rather than a summarised transcript. When you come back to a session that has been idle for hours, prefer a fresh session seeded from your notes over compacting the stale one.
