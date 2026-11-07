---
id: pin-promptcachettl-1h-if-you-work-on-usage-credits
created: 2026-10-25
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1x745l9/your_claude_code_prompt_cache_drops_from_an_hour/
---

# Pin promptCacheTtl to 1h If You Keep Working on Usage Credits: the Main Conversation Drops to a 5-Minute Cache There

## TL;DR

On a subscription the main conversation gets the 1-hour prompt cache only while you are within plan usage; once Claude Code draws on usage credits it falls back to 5 minutes unless you set `promptCacheTtl` (or `CLAUDE_CODE_PROMPT_CACHE_TTL`) yourself.

## Why it matters

In the same session, any pause over 5 minutes after you cross the limit re-writes the whole context, now at billed rates. The existing cache lessons cover the 1-hour subscription default and opting in on API billing, not this switch mid-session.

## How to apply

If you often keep going on usage credits and take breaks longer than 5 minutes, set `"promptCacheTtl": "1h"` in settings.json or `CLAUDE_CODE_PROMPT_CACHE_TTL=1h`, accepting that 1-hour cache writes cost more. An explicit setting survives the fallback; a `1h` in agent frontmatter does not. Checked against the installed 2.1.310 binary: the TTL function returns 5 minutes when `isUsingOverage` is true and no TTL was chosen, after the env var and setting are read; the prompt-caching docs page says the same.

> "the moment you go past that limit and start drawing on usage credits, the main conversation drops to a five minute ttl.", u/virtualunc on r/ClaudeCode

## Related

[[check-interactive-sessions-still-write-the-1-hour-cache-and-pin-promptcachettl]], [[prompt-cache-is-one-hour-on-subscription]], [[opt-into-the-1-hour-prompt-cache-with-promptcachettl-on-api-billing]]
