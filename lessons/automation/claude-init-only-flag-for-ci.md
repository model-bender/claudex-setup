---
id: claude-init-only-flag-for-ci
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
---

# Run `claude --init-only` to Fire the Init Hook Without Starting a Session, for CI/CD

## TL;DR

`claude --init-only` runs the same init hook as `claude --init` but skips actually launching a Claude Code session, which is useful when you just want the setup side effects (e.g. in a CI/CD pipeline) without an interactive agent.

## Why it matters

The transcript distinguishes this explicitly: 'if you want to do the same thing in headless mode instead, you can do init-only where it will basically run that hook, but not actually spin up a session of Claude Code. So that can be handy if you're using it in CI/CD pipelines.'

## How to apply

In a CI/CD step that only needs your onboarding/setup hook's side effects (installing deps, seeding config, etc.) and not an actual agent conversation, invoke `claude --init-only` instead of `claude --init`.
