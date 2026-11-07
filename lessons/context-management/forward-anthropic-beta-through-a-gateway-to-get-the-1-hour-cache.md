---
id: forward-anthropic-beta-through-a-gateway-to-get-the-1-hour-cache
created: 2026-10-20
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/prompt-caching#choose-the-ttl-yourself
  - https://code.claude.com/docs/en/llm-gateway-protocol#requests-and-defaults-by-connection-method
---

# Through an ANTHROPIC_BASE_URL Gateway, Forward the anthropic-beta Header Unchanged to Get the 1-Hour Cache, Then Check usage.cache_creation

## TL;DR

With `ANTHROPIC_BASE_URL` pointing at a gateway, Claude Code asks for the one-hour cache TTL through the `ttl` field in `cache_control` plus an `extended-cache-ttl` value in the `anthropic-beta` header, so a `promptCacheTtl: "1h"` you set depends on the gateway forwarding that header unchanged.

## Why it matters

Setting the TTL in Claude Code is not enough on its own: part of the one-hour request travels in the `anthropic-beta` header, and a gateway that drops that header, or allowlists only some of its values, loses it. This is specific to the Anthropic Messages format: the Bedrock and Agent Platform formats request the hour through the `ttl` field alone, and the Claude apps gateway does not offer the one-hour TTL at all.

## How to apply

Configure the gateway to forward `anthropic-beta` (and `anthropic-version`) unchanged. Then confirm with `claude -p "hello" --output-format json`: one-hour writes are reported under `usage.cache_creation.ephemeral_1h_input_tokens` and five-minute writes under `ephemeral_5m_input_tokens`. Checked on 2026-10-20 against the live prompt-caching and LLM gateway protocol docs and the 2.1.304 binary (`ephemeral_1h_input_tokens`: 16 hits, `extended-cache-ttl`: 2).

> "Through an LLM gateway you set with `ANTHROPIC_BASE_URL`, part of the one-hour request travels in the `anthropic-beta` header, so configure the gateway to forward that header unchanged.", Claude Code docs (Prompt caching, "Choose the TTL yourself")

## Related

- [[opt-into-the-1-hour-prompt-cache-with-promptcachettl-on-api-billing]]
- [[check-interactive-sessions-still-write-the-1-hour-cache-and-pin-promptcachettl]]
