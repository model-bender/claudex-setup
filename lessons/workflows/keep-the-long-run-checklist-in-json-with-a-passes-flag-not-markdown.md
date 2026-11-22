---
id: keep-the-long-run-checklist-in-json-with-a-passes-flag-not-markdown
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/simon-scrapes/everyone-ignore-these-claude-concepts-but-they-change-everything_6VjeXzvpoJo_20261120.txt
---

# Keep a long-run task checklist in JSON with a passes flag, not in Markdown

## TL;DR

For a multi-session job, store the task list as JSON where each item has passes: false and tell Claude it may only flip that field to true after testing. Anthropic reports the model is less likely to inappropriately change or overwrite JSON than Markdown.

## Why it matters

In a Markdown list, the video says, Claude may tidy up, merge two items or quietly drop one without you noticing. In JSON it treats the file as data and is more likely to leave it alone, and you can see at a glance what is done.

## How to apply

Have the first session write a JSON file with one object per requirement, each with a description, verification steps and passes: false. Instruct later sessions to edit the file only by changing passes after the item is verified, and never to remove or edit items. For a client report, each section (spend, leads, cost per lead, email) gets its own false entry. Pair it with a progress file the same sessions update.

Checked: Checked 2026-11-22: fetched Anthropic's engineering post 'Effective harnesses for long-running agents'; it shows a feature list with "passes": false, says agents edit it only by changing the passes field, and contains the sentence 'the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files'. No Claude Code flag involved.

## Related

[[make-delegated-workers-write-progress-back-to-the-plan]]
