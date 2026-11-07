---
id: forked-subagents-share-main-session-prompt-cache
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-subagent-upgrade-yet_20260424.txt
---

# Forked Subagents Are Cheap Despite Full History Because They Share the Main Session's Prompt Cache

## TL;DR

A forked subagent inherits the entire prior conversation, but because it reuses the same prompt cache as the main session, sending that history again doesn't cost nearly as much as a fresh, uncached prompt of the same size would.

## Why it matters

This is why forking, not just prompt-summarizing into a normal subagent, is viable for tasks needing full nuance: without cache sharing, resending 180k+ tokens of history to every fork would be prohibitively expensive.

## How to apply

When deciding between a fresh subagent (compressed summary, cheaper prompt) and a forked subagent (full history, cache-shared), remember the fork's cost advantage comes from cache reuse, not from being inherently cheap to send.

## Related

[[keep-sibling-agent-prompt-prefixes-identical-to-share-the-cache]]
