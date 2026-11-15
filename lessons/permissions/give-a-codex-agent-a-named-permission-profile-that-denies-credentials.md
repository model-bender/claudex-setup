---
id: give-a-codex-agent-a-named-permission-profile-that-denies-credentials
created: 2026-11-15
status: active
supersedes: null
category: permissions
tool: codex
source_type: canonical
sources:
  - https://developers.openai.com/blog/securing-persistent-agents-like-openclaw-at-openai
---

# Give a Codex agent a named permission profile that denies ~/.ssh and writes only its own workspace

## TL;DR

In config.toml set default_permissions = "openclaw", then under [permissions.openclaw.filesystem] grant ":minimal" = "read", the agent's workspace = "write", a managed read-only dir = "read", and "/home/dev-user/.ssh" = "deny"; under [permissions.openclaw.network] keep allow_upstream_proxy, allow_local_binding, enable_socks5, dangerously_allow_all_unix_sockets and dangerously_allow_non_loopback_proxy all false.

## Why it matters

A path-level allow/deny profile bounds an unattended agent better than prompt-by-prompt approvals, and it is OpenAI's own configuration for hundreds of internal agents.

## How to apply

Copy the profile shape, replace the workspace and read-only paths, and pair it with the requirements.toml ceiling.

Checked: `default_permissions` has 19 hits on codex-cli 0.169.0. Not from the post: on this hub's own setup, any profile with deny entries made Codex run git inside the sandbox, where git writes fail (openai/codex#38318), so try a commit after switching.

> "# Prevent access to SSH credentials.", OpenAI developer blog, Securing persistent agents

## Related

[[use-codex-requirements-toml-as-the-ceiling-for-a-persistent-agent]], [[strip-tokens-from-codex-commands-with-shell-environment-policy-exclude]], [[make-a-test-commit-after-adding-deny-entries-to-a-codex-permission-profile]]
