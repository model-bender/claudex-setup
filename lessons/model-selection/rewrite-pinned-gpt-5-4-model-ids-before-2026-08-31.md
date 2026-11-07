---
id: rewrite-pinned-gpt-5-4-model-ids-before-2026-08-31
created: 2026-08-16
status: active
supersedes: null
category: model-selection
tool: codex
source_type: canonical
sources:
  - https://learn.chatgpt.com/docs/changelog
---

# Rewrite Every Pinned `gpt-5.4` Model ID Before 31 August 2026

## TL;DR

GPT-5.4 and GPT-5.4 mini leave Codex for ChatGPT-authenticated sessions on **2026-08-31**; replace `gpt-5.4` with `gpt-5.6-terra` and `gpt-5.4-mini` with `gpt-5.6-luna` everywhere a model ID is written down, not just in the model picker.

## Why it matters

The retirement is scoped to ChatGPT sign-in - API-key sessions keep both models - so a config that works on one auth path breaks on the other, which is a confusing way to discover the deadline.

The failure surface is the places you never look at. Custom agents in `~/.codex/agents/*.toml`, scheduled automations, and managed workspace defaults all pin model IDs independently of the chat picker, so switching the picker fixes nothing for your unattended work.

## How to apply

Grep your Codex config for `gpt-5.4` before the cutoff, covering `~/.codex/config.toml`, `~/.codex/agents/*.toml`, any scheduled automations, and workspace-managed defaults. Swap to `gpt-5.6-terra` / `gpt-5.6-luna`.

> "Before the cutoff, update workspace defaults, saved model settings, managed configurations, custom agents, and scheduled tasks that use either model.", Codex changelog, 2026-07-31

## Related

[[codex-reasoning-dial-resets-to-extra-high]]
