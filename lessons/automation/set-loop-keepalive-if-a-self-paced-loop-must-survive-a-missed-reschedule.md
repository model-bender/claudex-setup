---
id: set-loop-keepalive-if-a-self-paced-loop-must-survive-a-missed-reschedule
created: 2026-11-15
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Set CLAUDE_CODE_LOOP_KEEPALIVE=1 if a self-paced /loop must survive a turn that forgets to reschedule

## TL;DR

A self-paced loop whose iteration neither reschedules nor stops now ends. It used to be rescued by a fallback wakeup.

## Why it matters

Long polling loops that relied on the silent fallback now die quietly after one bad iteration. The loop prompt has to say to reschedule or stop on every pass.

## How to apply

Write the loop prompt so every iteration ends with a ScheduleWakeup or an explicit stop. If you depend on the old rescue, export `CLAUDE_CODE_LOOP_KEEPALIVE=1`.

Checked: `CLAUDE_CODE_LOOP_KEEPALIVE` has 4 hits in the installed Claude Code 2.1.325 binary. The scheduled-tasks docs page still described the old fallback wakeup on 2026-11-15, so the changelog is the current word.

> "Changed self-paced `/loop` to end when a turn finishes without rescheduling, instead of scheduling a fallback wakeup; set `CLAUDE_CODE_LOOP_KEEPALIVE=1` to keep the old behavior", Claude Code CHANGELOG 2.1.319

## Related

[[loop-command-for-recurring-in-session-tasks]]
