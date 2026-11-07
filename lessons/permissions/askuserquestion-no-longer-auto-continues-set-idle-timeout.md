---
id: askuserquestion-no-longer-auto-continues-set-idle-timeout
created: 2026-07-17
status: active
supersedes: null
category: permissions
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# AskUserQuestion No Longer Auto-Continues: Set an Idle Timeout for Unattended Runs

## TL;DR

`AskUserQuestion` dialogs now wait indefinitely instead of auto-continuing; if a semi-autonomous or scheduled run relies on them advancing without you, opt into an idle timeout via `/config`.

## Why it matters

The old auto-continue could silently pick a default answer while you were away; blocking by default is safer interactively but will stall an unattended session the moment it hits a question with no human present, the run just hangs.

## How to apply

For unattended or scheduled runs, enable the AskUserQuestion idle-timeout option in `/config` so a question eventually advances instead of hanging. If you'd rather the agent never ask, deny the tool entirely (see [[deny-list-to-disable-interactive-question-tool]]), the idle timeout is the lighter-touch alternative when you still want questions when you're present.

> "Changed `AskUserQuestion` dialogs to no longer auto-continue by default; opt into an idle timeout via `/config`", Claude Code CHANGELOG 2.1.200

## Related

[[deny-list-to-disable-interactive-question-tool]]
