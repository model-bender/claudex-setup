---
id: script-claude-ultrareview-with-trust-workspace
created: 2026-10-25
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21309
---

# Pass --trust-workspace When You Script claude ultrareview

## TL;DR

Since 2.1.309 `claude ultrareview` needs workspace trust: it asks on a terminal and refuses otherwise, so a script or CI job must pass `--trust-workspace` (after the PR number or base branch) or set `CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK=1`.

## Why it matters

A non-interactive ultrareview call that worked on 2.1.308 now refuses, and because the flag takes no value, putting it before the PR number makes the number look like its argument.

## How to apply

Write the call as `claude ultrareview <pr-or-base> --trust-workspace`. Use the environment variable only on machines whose checkouts you control. Checked: `CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK` has 5 matches and `trust-workspace` 11 in the installed 2.1.310 binary.

> "Changed `claude ultrareview` to require workspace trust: it asks on a terminal, else refuses; scripts pass `--trust-workspace`, which takes no value (put a PR number or base branch before it), or set `CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK=1`", Claude Code CHANGELOG 2.1.309
