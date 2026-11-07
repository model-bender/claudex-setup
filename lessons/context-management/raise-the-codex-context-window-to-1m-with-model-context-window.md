---
id: raise-the-codex-context-window-to-1m-with-model-context-window
created: 2026-08-22
status: active
supersedes: null
category: context-management
tool: codex
source_type: post
sources:
  - https://x.com/thsottiaux/status/2089082893804896524
---

# Raise the Codex context window to 1M with model_context_window in config.toml, and know you are overriding a tuned default

## TL;DR

The Codex lead documents the exact config.toml keys for a 1M-token window and warns that the shipped default was deliberately tuned for performance and cost, so the bigger window is a trade, not a free upgrade.

## Why it matters

The Codex context limit is not the model's limit, Codex ships a smaller tuned budget on purpose, which is invisible until someone tells you the override exists. The third key matters as much as the second: without raising model_auto_compact_token_limit, compaction still fires at the old threshold and the larger window buys nothing.

## How to apply

Put `model`, `model_context_window = 1000000`, and `model_auto_compact_token_limit = 900000` at the TOP level of `~/.codex/config.toml` (before any `[section]` header, or they are silently ignored), then restart the client and start a new session. To test without changing defaults: `codex -m gpt-5.6-sol -c model_context_window=1000000 -c model_auto_compact_token_limit=900000`.

> "Open ~/.codex/config.toml and add or update these settings at the top level, before any [section] headers: model = \"gpt-5.6-sol\" model_context_window = 1000000 model_auto_compact_token_limit = 900000", Thibault (Tibo) Sottiaux

## Related

[[put-top-level-codex-config-keys-before-any-section-header]]
