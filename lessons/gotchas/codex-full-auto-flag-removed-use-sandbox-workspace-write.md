---
id: codex-full-auto-flag-removed-use-sandbox-workspace-write
created: 2026-08-07
status: active
supersedes: null
category: gotchas
tool: codex
source_type: canonical
sources:
  - https://learn.chatgpt.com/docs/changelog
---

# Replace codex exec --full-auto With --sandbox workspace-write, Which Was Removed Outright

## TL;DR

Codex CLI 0.147.0 deletes the deprecated `codex exec --full-auto` flag rather than continuing to warn on it. Scripts, aliases, and CI jobs still passing it now fail.

## Why it matters

The failure mode selects for the wrong people: anyone who saw the deprecation warning and shrugged is the one whose automation breaks today, with no further grace period. Because the flag typically lives in CI config and shell aliases rather than in code under review, it is easy to miss until a job goes red.

## How to apply

Grep your scripts, CI config, and shell aliases for `--full-auto` and replace it with `--sandbox workspace-write`, the direct replacement named in the same changelog line.

> "Remove the deprecated `codex exec --full-auto` flag; use `--sandbox workspace-write` instead.", OpenAI Codex changelog, CLI 0.147.0

## Related

[[never-run-codex-full-access-without-sandbox-and-auto-review]], [[codex-approve-for-me-keeps-review-without-prompt-friction]]
