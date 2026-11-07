---
id: cache-tool-results-in-the-function-hook-store
created: 2026-09-12
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Cache Expensive Tool Results in the Function Hook Store and Short-Circuit the Repeat Call

## TL;DR

Function hooks come with a store. Intercept WebFetch, look the URL up in the store, return the cached copy on a hit and let the call proceed on a miss. There is a per-session variable store and a separate store that survives restarts.

## Why it matters

Shell hooks have no memory, so nothing can be remembered across hooks, turns or sessions. With a store the hook stops being a filter and becomes a cache: repeat fetches of the same page cost nothing, and any other idempotent tool call can be memoised the same way.

## How to apply

Have the hook key on the tool's input, return the stored result to short-circuit, and write the result back on a miss. Use the per-session variable store for anything sensitive or short-lived and the persistent store only for data that is safe to keep on disk across sessions.

## Related

[[enable-function-hooks-to-unlock-plugin-authoring]], [[rewrite-tool-input-in-a-function-hook]]
