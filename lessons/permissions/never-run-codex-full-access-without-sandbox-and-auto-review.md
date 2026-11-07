---
id: never-run-codex-full-access-without-sandbox-and-auto-review
created: 2026-07-25
status: active
supersedes: null
category: permissions
source_type: post
tool: codex
sources:
  - https://simonwillison.net/2026/Jul/16/bad-codex-bug/
---

# Never Run Codex in Full Access Without the Sandbox and Auto Review: That Combination Is How `$HOME` Gets Deleted

## TL;DR

OpenAI's own investigation into reported file deletions found one recurring recipe, full access enabled, sandboxing off, auto review off, where the model redefines `$HOME` for a temp directory and wipes the real one.

## Why it matters

This is the Codex engineering lead naming the exact configuration that destroys a home directory. And it's the configuration people deliberately reach for, because approval prompts are the friction you most want gone on a long unattended run. "Full access" is therefore the flag most likely to be set on precisely the run you are least likely to be watching.

## How to apply

If you need full access for a long autonomous run, keep sandboxing on and leave auto review enabled, or run the whole thing inside a container or VM whose `$HOME` you are willing to lose. Treat the three settings as one unit: turning off the sandbox is what removes the check on high-risk destructive commands, not merely the prompts.

> "What we have found is that this most commonly occurs when: Full access mode is enabled and codex is run without sandboxing protections, including without auto review being enabled — The model attempts to override the $HOME env var to define a temporary directory. — The model makes an honest mistake and mistakenly deletes $HOME instead.", Thibault Sottiaux, OpenAI Codex lead (via Simon Willison)

## Related

[[codex-projects-are-a-working-directory-not-a-boundary]], [[sandbox-network-strict-allowlist-for-unattended-runs]]
