---
id: auto-mode-not-run-row-means-the-classifier-failed-not-a-denial
created: 2026-10-19
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1x7ix85/the_permission_system_is_exhausting/ph4ledl/
---

# A Dim "Not run" Row in Auto Mode Means the Classifier Failed: Retry, Don't Write a Rule

## TL;DR

Since 2.1.296, a tool call that auto mode skipped because its check returned no usable answer shows as a dim `Not run · auto mode's check had no usable answer` row; that is a classifier or server failure, not a judgement about your command, so allow rules and environment entries cannot fix it.

## Why it matters

A blocked call and an unjudged call look similar at a glance, and the natural response to either is to add an allow rule or an `autoMode.environment` entry. For a "Not run" row that tuning does nothing, and on Amazon Bedrock or with a custom classifier model the real cause (a model your account or provider cannot serve) stays hidden while you edit rules.

## How to apply

Read the line under a blocked call before touching settings. A real denial calls for a rule or environment entry; a dim "Not run" calls for the errors page's fix: retry after a few seconds (Claude usually retries on its own), carry on with read-only work if it keeps failing, and if it repeats on every retry check that your provider serves the model named in the message or in `CLAUDE_CODE_AUTO_MODE_MODEL`. Press `Ctrl+O` to read the full message in the transcript viewer. Checked against the Claude Code error reference and the changelog's 2.1.296 entry, which reads "a tool call that wasn't run because auto mode's check had no usable answer now shows as a dim "Not run" row instead of a red error"; the 2.1.303 binary carries the "no usable answer" string.

> "If the message under a blocked call is a dim "Not run · auto mode's check had no usable answer", that's the classifier failing to answer, not a judgment about your command, and the fix is different (the errors page has an entry for it).", u/kuroudo_ai on r/ClaudeCode

## Related

[[run-auto-mode-setup-to-draft-environment-entries-before-skipping-permissions]], [[auto-mode-pauses-after-repeated-blocks-headless-runs-skip-the-action]]
