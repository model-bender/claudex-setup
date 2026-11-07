---
id: codex-steers-mid-response-by-default-drop-the-instant-interrupt-override
created: 2026-10-19
status: active
supersedes: null
category: configuration
tool: codex
source_type: canonical
sources:
  - https://developers.openai.com/codex/changelog
  - https://github.com/openai/codex/pull/51812
---

# Drop the instant_interrupt Override on Codex 0.163.0 and Later: Steering Mid-Response Is Now the Default

## TL;DR

Since 0.163.0 a follow-up typed while Codex is responding steers the running turn without any opt-in, and an interrupt also stops active Code Mode cells and their nested tool calls.

## Why it matters

The 0.159.0 advice to opt in with `instant_interrupt = true` is stale: PR #51812 turned the feature on by default while keeping it marked as under development. A leftover config line now does nothing, and turning the behaviour off needs an explicit `false`.

## How to apply

Delete any `instant_interrupt = true` line from `config.toml`; set `instant_interrupt = false` only if you want queueing back. The queue-versus-steer Enter behaviour still decides what Enter does. Checked on codex-cli 0.163.0: `codex features list` shows `instant_interrupt under development true` and `code_mode_interrupt stable true`, and a copy of a config without the line still lists `instant_interrupt` as true.

> "Send a follow-up while Codex is responding to steer it immediately. Interrupting a turn also stops active Code Mode cells and their nested tool calls.", OpenAI Codex changelog, CLI 0.163.0

