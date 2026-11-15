---
id: use-codex-requirements-toml-as-the-ceiling-for-a-persistent-agent
created: 2026-11-15
status: active
supersedes: null
category: permissions
tool: codex
source_type: canonical
sources:
  - https://developers.openai.com/blog/securing-persistent-agents-like-openclaw-at-openai
---

# Make Codex's managed requirements.toml the ceiling for a persistent agent, so user config cannot widen sandbox, search or network allowlist

## TL;DR

For an always-on Codex agent, put the hard limits in requirements.toml (allowed_sandbox_modes = ["read-only","workspace-write"], allowed_web_search_modes = ["cached"], experimental_network.managed_allowed_domains_only = true plus allowed_domains and denied_domains including metadata endpoints such as 169.254.169.254), and keep config.toml for the actual choices.

## Why it matters

requirements.toml restricts what options are available, config.toml only selects among them, so an agent that rewrites its own config cannot lift the limit. OpenAI says "Persistent agents can change their configuration and write arbitrary code to accomplish a goal."

## How to apply

Write the ceiling in requirements.toml (sandbox modes without danger-full-access, cached web search, managed network proxy with an explicit allowlist and denylist), then set default_permissions in config.toml to a named profile that stays inside it.

Checked: on codex-cli 0.169.0, `allowed_sandbox_modes` has 5 hits, `allowed_web_search_modes` 4, `managed_allowed_domains_only` 5 and `default_permissions` 19.

> "# Exclude unrestricted "danger-full-access" sandbox mode.", OpenAI developer blog, Securing persistent agents

## Related

[[keep-credentials-out-of-the-agent-sandbox]], [[give-a-codex-agent-a-named-permission-profile-that-denies-credentials]]
