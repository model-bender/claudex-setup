---
id: a-gateway-that-strips-cache-control-bills-every-turn-uncached
created: 2026-10-20
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/prompt-caching#where-the-cache-lives
  - https://code.claude.com/docs/en/llm-gateway-protocol#feature-pass-through
  - https://github.com/anthropics/claude-code/issues/78410#issuecomment-5312172222
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Make Your Gateway Forward cache_control Unchanged: One That Strips It Bills Every Turn Uncached, With No Error

## TL;DR

Behind a custom `ANTHROPIC_BASE_URL` or an LLM gateway, caching depends on what the gateway does with Claude Code's `cache_control` markers. A gateway that silently removes them bills the whole conversation as uncached input on every turn, and one that flattens block-form system content to a plain string drops the marker the same way.

## Why it matters

The stripping gateway returns success, so nothing in the session looks wrong: only the bill and the cache-read count show it. A gateway that rejects the marker on the mid-conversation system block with a `400` naming `cache_control` is the cheaper failure: Claude Code re-sends with that marker moved onto your last conversation message, keeps it there for the rest of the conversation, and only that block bills as uncached.

## How to apply

After pointing Claude Code at a gateway, watch the `Prompt cache (main):` line in `/cost` over a few turns (see [[verify-cache-folklore-with-the-cost-prompt-cache-line]]). If cache reads stay near zero, make the gateway forward `cache_control` unchanged wherever it appears and keep `system` and message content in block form. Since 2.1.212 the mid-conversation system block (file-change notices and similar) also caches behind gateways and custom base URLs; Claude Code marks it for caching on every provider and connection, and `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` sends it uncached. Checked on 2026-10-20 against the live prompt-caching docs and the 2.1.304 binary (`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`: 13 hits; `Prompt cache (main):` present).

> "Removes the markers while returning success: your entire conversation history bills as uncached input on every turn. A gateway that converts block-form system content to a plain string drops the marker the same way.", Claude Code docs (Prompt caching, "Where the cache lives")

> "Improved prompt caching: the mid-conversation system block now works behind LLM gateways and custom base URLs (Bedrock, Vertex, 1P)", Claude Code CHANGELOG 2.1.212

## Related

- [[set-claude-code-attribution-header-0-when-your-gateway-reshapes-the-system-prompt]]
