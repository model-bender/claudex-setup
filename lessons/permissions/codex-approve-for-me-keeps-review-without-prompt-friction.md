---
id: codex-approve-for-me-keeps-review-without-prompt-friction
created: 2026-08-07
status: active
supersedes: null
category: permissions
tool: codex
source_type: canonical
sources:
  - https://learn.chatgpt.com/docs/changelog
---

# Reach for Codex's --approve-for-me Instead of Full Access on Unattended Runs

## TL;DR

Codex CLI 0.147.0 adds `--approve-for-me`, which auto-approves actions but still routes each through automated review. It is the middle ground between per-action prompts and full access with no review.

## Why it matters

The destructive recipe is full access plus no sandbox plus no auto review, which OpenAI's own Codex lead has named as the combination behind reported `$HOME` deletions. People reach for it because prompt friction is the thing they actually want gone, not the review. This flag separates the two, so removing the friction no longer means removing the safety leg with it.

## How to apply

On unattended `codex exec` runs, add `--approve-for-me` rather than granting full access. Keep the sandbox on as well; the flag replaces interactive approval, not containment.

> "Enable automatically reviewed approvals with the new `--approve-for-me` CLI flag.", OpenAI Codex changelog, CLI 0.147.0

## Related

[[never-run-codex-full-access-without-sandbox-and-auto-review]], [[codex-full-auto-flag-removed-use-sandbox-workspace-write]]
