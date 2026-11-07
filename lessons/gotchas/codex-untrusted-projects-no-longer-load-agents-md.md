---
id: codex-untrusted-projects-no-longer-load-agents-md
created: 2026-08-29
status: active
supersedes: null
category: gotchas
source_type: canonical
tool: codex
sources:
  - https://developers.openai.com/codex/changelog
---

# If Codex Ignores Your AGENTS.md, Check Directory Trust: Untrusted Projects No Longer Load It

## TL;DR

As of Codex CLI 0.150.0, an untrusted project's AGENTS.md is silently not loaded, so instruction-following failures in fresh checkouts are often a trust problem, not a prompt problem.

## Why it matters

The failure mode is invisible: Codex runs fine but without your project rules, which looks exactly like the model ignoring instructions. Fresh clones, CI containers, and worktrees that never got a trust answer are the likely victims.

## How to apply

Answer the directory-trust prompt (or pre-trust the path in Codex's trusted-projects config) before debugging AGENTS.md content; verify with a canary instruction in AGENTS.md that the file actually loaded.

> "Untrusted projects no longer supply project-level AGENTS.md instructions, and managed deny-read rules remain enforced after permission changes.", Codex changelog, CLI 0.150.0

## Related

[[codex-directory-trust-switches-on-project-local-hooks]]
