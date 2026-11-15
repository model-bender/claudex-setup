---
id: make-a-test-commit-after-adding-deny-entries-to-a-codex-permission-profile
created: 2026-11-15
status: active
supersedes: null
category: gotchas
tool: codex
source_type: canonical
sources:
  - https://github.com/openai/codex/issues/38318
  - https://developers.openai.com/blog/securing-persistent-agents-like-openclaw-at-openai
---

# After Adding a Denied Path to a Codex Permission Profile, Make a Test Commit

## TL;DR

With any denied-read path configured, Codex's execpolicy allow rules silently stay sandboxed (openai/codex#38318), so a rule that runs git outside the sandbox stops working and every git write fails.

## Why it matters

A profile that looks correct breaks commits with no warning, and the failure only shows when the agent next tries to land work, far from the config change that caused it. This hub hit it with its own no-secrets profile.

## How to apply

After setting `default_permissions` to a profile with any deny entry, have Codex make a throwaway commit. If the git write fails, keep that profile opt-in until the issue is fixed, or (inference) make commits outside the agent.

> "Execpolicy allow rules silently stay sandboxed when any denied-read path is configured", openai/codex issue #38318 (open on 2026-11-15)

## Related

[[give-a-codex-agent-a-named-permission-profile-that-denies-credentials]]
