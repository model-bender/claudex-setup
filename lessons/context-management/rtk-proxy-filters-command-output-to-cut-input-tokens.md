---
id: rtk-proxy-filters-command-output-to-cut-input-tokens
created: 2026-07-10
status: active
supersedes: null
category: context-management
sources:
  - transcripts/sean-kochel/7-claude-code-tools-to-stop-wasting-tokens_bhB57Meachc_20260703.txt
---

# Proxy Verbose Command Output Through RTK to Stop Burning Input Tokens

## TL;DR

Install RTK as a hook between the shell and Claude Code so noisy command output (git diff/status/log, ls, file reads, test runs) is filtered, aggregated, truncated, and deduplicated before it ever enters the context window.

## Why it matters

A large share of input-token waste comes from Claude reading raw command output it doesn't need, a git-heavy session (a messy merge with repeated status/diff/log calls) can silently consume 150k+ tokens of boilerplate, whitespace, and repeated error lines.

## How to apply

`brew install rtk`; it registers a hook so commands like git status/diff/log route through rtk, applying four strategies, smart filtering (drop whitespace/boilerplate/comments), aggregation (collapse a repeated error into one line + count), truncation (cut long/redundant descriptions), and deduplication (repeated log lines shown once with a count), while staying overridable when Claude actually needs the full output; run `rtk gain` to see tokens saved, and add custom command rewrites for anything it doesn't cover.
