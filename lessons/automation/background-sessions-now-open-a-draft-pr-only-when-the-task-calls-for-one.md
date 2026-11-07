---
id: background-sessions-now-open-a-draft-pr-only-when-the-task-calls-for-one
created: 2026-08-07
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Read the Background Session's Final Report, Because a Draft PR Is No Longer Guaranteed

## TL;DR

Background sessions still commit and push to preserve work, but as of 2.1.221 they open a draft PR only when the task calls for one, follow your CLAUDE.md git instructions, and always end by reporting where the work lives. The final report, not a PR, is the reliable signal.

## Why it matters

This supersedes the 2.1.198 behaviour, which opened a draft PR unconditionally when a background agent finished code work. Anyone still operating on "check my PR list to find what the background agents did" now has a review process with a hole in it: work that did not call for a PR is sitting on a pushed branch with nothing in the PR queue pointing at it.

## How to apply

Read each background session's closing report to find where the work landed, rather than watching the draft-PR list. Since these sessions now follow your CLAUDE.md git instructions, encode the convention you want there (branch naming, whether to open a PR, whether to push at all) instead of relying on a fixed built-in behaviour.

> "Changed background sessions to commit and push to preserve work, open a draft PR only when the task calls for one, follow your CLAUDE.md git instructions, and always end by reporting where the work lives", Claude Code CHANGELOG 2.1.221

## Related

[[fork-now-gets-its-own-worktree]]
