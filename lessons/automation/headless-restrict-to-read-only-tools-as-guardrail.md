---
id: headless-restrict-to-read-only-tools-as-guardrail
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-workflow-explained-u0026-when-to-use-each_20260424.txt
---

# Restrict Unattended Headless Runs to Read-Only Tools as a Guardrail

## TL;DR

For a headless -p run you won't be watching step by step, pass an allowed-tools restriction limited to read-only tools so the run can't take destructive, hard-to-undo actions if something goes wrong.

## Why it matters

The transcript's central warning about the headless pattern is 'the big limitation in this is trust... you probably don't want to go headless on anything that's hard to undo, but you can actually put guard rails on this as well. If you want it to only read and not write... we can do --allowed tools.' This is the concrete mitigation for that trust gap.

## How to apply

When running `claude -p "..."` unattended (e.g. from cron or a scheduled job) for a task where the output only needs to be read, add an allowed-tools restriction that excludes write/edit/bash-mutation tools, keeping the run read-only even with full autonomy otherwise.

## Related

[[disallowed-tools-in-skill-frontmatter]], [[headless-mode-for-batch-automation]]
