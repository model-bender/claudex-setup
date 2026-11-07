---
id: change-codex-reasoning-mid-thread-without-losing-the-cache
created: 2026-10-25
status: active
supersedes: null
category: model-selection
tool: codex
source_type: post
sources:
  - https://x.com/thsottiaux/status/2113770573994299544
---

# In Codex, Change the Reasoning Level Mid-Thread: It No Longer Invalidates the Cache

## TL;DR

Codex's engineering lead says changing the reasoning level in Codex mid-conversation no longer invalidates the prompt cache, so raising effort for one hard step and lowering it after is now cheap.

## Why it matters

Splitting a thread or starting fresh just to change effort was a way to avoid an uncached re-read; for Codex that cost is reported gone. This is one maintainer statement and says nothing about Claude Code.

## How to apply

Change the reasoning level inside a live Codex thread when a step gets harder or easier, instead of opening a new thread. Codex 0.164.0 also takes the effort inline as an argument to `/model`.

> "Day 19/ Small updates. Calls connect much faster for dots, changing reasoning in codex & work mid conversation does not invalidate cache anymore and a we've also updated the codex cli.", Tibo Sottiaux

## Related

[[per-message-effort-change-keeps-the-cache-on-fable-5-1]], [[spawn-a-subagent-instead-of-switching-model-mid-session]]
