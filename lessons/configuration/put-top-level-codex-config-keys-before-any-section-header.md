---
id: put-top-level-codex-config-keys-before-any-section-header
created: 2026-08-31
status: active
supersedes: null
category: configuration
tool: codex
sources:
  - https://x.com/thsottiaux/status/2089082893804896524
---

# Put Top-Level config.toml Keys Before Any [section] Header or Codex Silently Ignores Them

## TL;DR

Keys like `model`, `model_context_window`, and `model_auto_compact_token_limit` must sit at the very top of `~/.codex/config.toml`, above any `[section]` header, or they are silently ignored with no error.

## Why it matters

A top-level key pasted below a `[section]` header stops being top-level, so the setting simply never takes effect and nothing warns you. That turns a working override into a silent no-op that is very hard to diagnose, because the file looks correct. Changes also only apply after restarting the client and starting a new session, which compounds the confusion.

## How to apply

Open `~/.codex/config.toml` and add or edit top-level settings before any `[section]` header, then restart the client and start a new session. To trial a setting without editing your defaults, pass it per-invocation instead, for example `codex -c model_context_window=1000000 -c model_auto_compact_token_limit=900000`.

## Related

[[raise-the-codex-context-window-to-1m-with-model-context-window]]
