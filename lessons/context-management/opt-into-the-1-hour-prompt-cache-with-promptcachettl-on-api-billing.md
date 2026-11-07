---
id: opt-into-the-1-hour-prompt-cache-with-promptcachettl-on-api-billing
created: 2026-08-29
status: active
supersedes: null
category: context-management
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# On an API Key or Cloud Provider, Opt Into the 1-Hour Prompt Cache With promptCacheTtl

## TL;DR

The 1-hour cache window is not automatic off a subscription: API-key, Bedrock, Vertex, and Foundry users must set `promptCacheTtl` themselves, and can keep subagents on the cheaper 5-minute TTL separately via `subagentPromptCacheTtl`.

## Why it matters

Cache-window advice written for subscriptions silently does not apply on an API key, so long API-billed sessions pay full re-cache on every gap longer than 5 minutes. Splitting the main conversation from subagents matters because short-lived subagents gain nothing from an hour-long cache but are billed for it.

## How to apply

Set `promptCacheTtl: "1h"` and `subagentPromptCacheTtl: "5m"` in `settings.json` (added in 2.1.243). For a single long-running agent, 2.1.248 adds per-agent `experimental.cacheTtl` (`"5m"` or `"1h"`) in agent frontmatter, used when no subagent TTL setting is configured.

> "Added `promptCacheTtl` and `subagentPromptCacheTtl` settings so API-key and cloud-provider users can keep a 1-hour prompt cache on the main conversation while subagents stay at 5 minutes", Claude Code CHANGELOG 2.1.243

## Related

[[prompt-cache-is-one-hour-on-subscription]], [[compact-inside-the-cache-window-not-after-it-expires]]
