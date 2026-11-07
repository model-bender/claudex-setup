---
id: set-claude-code-attribution-header-0-when-your-gateway-reshapes-the-system-prompt
created: 2026-10-20
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/llm-gateway-protocol#system-prompt-attribution-block
  - https://github.com/anthropics/claude-code/issues/50085
  - https://github.com/anthropics/claude-code/issues/68900
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Set CLAUDE_CODE_ATTRIBUTION_HEADER=0 When Your Gateway Reshapes the System Prompt: Omit the Block at the Client Rather Than Stripping It in the Gateway

## TL;DR

When the upstream is `api.anthropic.com`, Claude Code's attribution block stays out of the prompt and the cache key only if the gateway forwards the `system` array exactly as received (any other upstream always receives the block as part of the prompt), so a gateway that reorders, prepends to, merges or stringifies it needs `CLAUDE_CODE_ATTRIBUTION_HEADER=0` set on the Claude Code side.

## Why it matters

`api.anthropic.com` strips the block by position. Reshaping defeats the strip, so the block reaches the model and the prompt cache key. Merging is worse: when the merged entry starts with the attribution header, the endpoint treats the whole entry as attribution and drops everything merged into it, including the rest of the system prompt. Stripping or moving the block inside the gateway is the wrong fix, because Anthropic and the cloud providers' Claude endpoints read it.

## How to apply

If the gateway passes `system` through untouched, you no longer need the variable for caching: since 2.1.181 the block is stable for a whole conversation behind a custom base URL. The older advice in issue #50085, echoed in a comment on #68900 (set it to `0` because a per-request `cch` token changed the start of the system prompt on every request, so prefix caches never hit), applies only to versions before 2.1.181. If the gateway must rewrite system content, set `CLAUDE_CODE_ATTRIBUTION_HEADER=0` in the settings `env` block. Checked on 2026-10-20 against the live LLM gateway protocol and env-vars docs and the 2.1.304 binary (`CLAUDE_CODE_ATTRIBUTION_HEADER`: 5 hits).

> "If your gateway must reshape system content, set `CLAUDE_CODE_ATTRIBUTION_HEADER=0` so Claude Code omits the block.", Claude Code docs (LLM gateway protocol, "System prompt attribution block")

> "From Claude Code v2.1.181, the block is stable for the lifetime of a conversation when requests route through a custom base URL, so a gateway-side prompt cache keyed on the full request body works without disabling it, and any provider your gateway forwards to receives a stable prompt prefix.", Claude Code docs (LLM gateway protocol, "System prompt attribution block")

## Related

- [[a-gateway-that-strips-cache-control-bills-every-turn-uncached]]
- [[set-claude-code-disable-structured-outputs-behind-gateways-that-reject-them]]
