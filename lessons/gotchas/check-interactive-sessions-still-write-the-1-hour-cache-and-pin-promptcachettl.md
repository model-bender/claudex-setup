---
id: check-interactive-sessions-still-write-the-1-hour-cache-and-pin-promptcachettl
created: 2026-10-19
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/101685
  - https://github.com/anthropics/claude-code/issues/102276
---

# On a Max or Team Seat, Check That Interactive Sessions Still Write the 1-Hour Cache, and Pin promptCacheTtl "1h" If They Do Not

## TL;DR

Reporters saw interactive sessions silently drop to 5-minute cache writes from 2026-10-12 while headless runs kept 1 hour, and setting `"promptCacheTtl": "1h"` restored 1-hour writes on the next turn.

## Why it matters

A 5-minute write means any pause over 5 minutes rewrites the whole context, which burns usage, and it contradicts the expectation that a subscription gets 1 hour by default. The issue is open with no maintainer reply, so the cause is the reporters' own tracing.

## How to apply

Sum `message.usage.cache_creation.ephemeral_5m_input_tokens` against `ephemeral_1h_input_tokens` over non-sidechain rows in `~/.claude/projects/<project>/<session>.jsonl`. If the 5m column is non-zero for interactive sessions, add `"promptCacheTtl": "1h"` to settings.json. Checked: `promptCacheTtl` 5 hits in the 2.1.303 binary. Not reproduced on this hub's machine on 2026-10-19: 12 recent sessions, interactive and headless, wrote only 1-hour cache.

> "Since 2026-10-12 at about 18:18 UTC, every newly started **interactive** session writes its main-conversation prompt cache under the **5-minute** TTL.", GitHub issue #101685

## Related

[[prompt-cache-is-one-hour-on-subscription]], [[opt-into-the-1-hour-prompt-cache-with-promptcachettl-on-api-billing]]
