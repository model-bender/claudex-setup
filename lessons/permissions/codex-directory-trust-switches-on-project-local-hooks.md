---
id: codex-directory-trust-switches-on-project-local-hooks
created: 2026-08-16
status: active
supersedes: null
category: permissions
tool: codex
source_type: canonical
sources:
  - https://github.com/openai/codex/pull/36960
---

# Answer Codex's Directory-Trust Prompt Deliberately - Trust Switches On Project-Local Hooks

## TL;DR

Codex 0.147.0 adds a trust screen to TUI onboarding for any project whose trust level is unset, and saying yes is what activates that repo's local config, hooks, and exec policies. It is a permission grant, not a convenience dialog.

## Why it matters

Trust is the switch behind project-local hooks and exec policies - precisely the surface a malicious or compromised repo would use, since a hook is arbitrary code bound to tool events.

The non-obvious part: trust applies to the **git repository root** even when you launch Codex from a subdirectory. Trusting one nested folder trusts the whole repo, including parts you have not looked at.

## How to apply

Treat the trust prompt as a review gate. In an unfamiliar clone, read `.codex/` config, hooks, and exec policies *before* trusting it. For repos you have already vetted, set an explicit trust level in config to skip the prompt. Remote workspaces skip it automatically.

> "Trusting a directory enables project-local config, hooks, and exec policies, which can increase exposure to prompt injection. Require an explicit decision instead of automatically trusting projects whose trust level is unset.", openai/codex#36960

## Related

[[nested-repos-no-longer-inherit-parent-trust]], [[codex-projects-are-a-working-directory-not-a-boundary]], [[contain-agents-at-environment-layer-not-permission-prompts]]
