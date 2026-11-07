---
id: auto-mode-pauses-after-repeated-blocks-headless-runs-skip-the-action
created: 2026-08-29
status: active
supersedes: null
category: permissions
source_type: canonical
tool: claude-code
sources:
  - https://code.claude.com/docs/en/permission-modes
---

# Auto Mode Pauses After 3 Consecutive Blocks, and a -p Run Just Skips the Action

## TL;DR

Auto mode is not a stable ceiling for unattended work: after 3 consecutive or 20 total classifier blocks it pauses and resumes prompting, and in a non-interactive `-p` run with no `--permission-prompt-tool` the blocked actions are simply skipped while Claude carries on.

## Why it matters

A headless auto-mode run that hits the classifier does not fail loudly, it degrades: work silently does not happen and the final report can still read as success. The docs state the thresholds are not configurable, so you cannot tune around them.

## How to apply

Give headless runs a `--permission-prompt-tool` so there is somewhere to fall back to, or pre-approve (allow-rule) the specific commands the classifier keeps blocking. The docs on the thresholds: "if the classifier blocks an action 3 times in a row or 20 times total, auto mode pauses and Claude Code resumes prompting".

> "Sessions that can't prompt: a non-interactive -p run without a --permission-prompt-tool has no prompt to fall back to. When repeated blocks reach a threshold, the action doesn't run and Claude keeps working.", Claude Code docs, permission modes

## Related

[[headless-mode-for-batch-automation]], [[stop-hook-8-block-cap]]
