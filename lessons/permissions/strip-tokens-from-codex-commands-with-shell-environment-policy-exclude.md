---
id: strip-tokens-from-codex-commands-with-shell-environment-policy-exclude
created: 2026-11-15
status: active
supersedes: null
category: permissions
tool: codex
source_type: canonical
sources:
  - https://developers.openai.com/blog/securing-persistent-agents-like-openclaw-at-openai
---

# Strip GitHub tokens from a Codex agent's command environment with shell_environment_policy.exclude, and remember it hides env vars only, not credential files

## TL;DR

Set [shell_environment_policy] ignore_default_excludes = false and exclude = ["GH_TOKEN","GITHUB_TOKEN", ...] so tokens never reach the agent's commands, and use the filesystem deny list for files like ~/.ssh.

## Why it matters

Env filtering and file deny rules cover different leaks; the post itself flags the gap and says secrets should go through a credential broker.

## How to apply

Add the exclude list for every token your shell exports, keep ignore_default_excludes false, and deny credential files separately in the permission profile.

Checked: `shell_environment_policy` has 17 hits and `ignore_default_excludes` 9 on codex-cli 0.169.0.

> "# Remove GitHub credentials from agent command environments.", OpenAI developer blog, Securing persistent agents

## Related

[[give-a-codex-agent-a-named-permission-profile-that-denies-credentials]]
