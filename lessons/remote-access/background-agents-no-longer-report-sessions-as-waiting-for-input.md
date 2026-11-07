---
id: background-agents-no-longer-report-sessions-as-waiting-for-input
created: 2026-09-13
status: active
supersedes: null
category: remote-access
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Update Any Idle-Detection Script That Keyed Off "Waiting for Your Input"

## TL;DR

Remote and headless sessions used to report themselves idle while background agents were still running; 2.1.269 fixes the status, and `CLAUDE_CODE_BG_TASKS_REPORT_RUNNING=0` restores the old behaviour.

## Why it matters

Any notification hook, dashboard or polling script that treated that string as a proxy for "nothing is happening" changes meaning on upgrade, and the failure is quiet: you get told a run finished while an agent is still working.

## How to apply

Update the script to account for background agents still running, or set `CLAUDE_CODE_BG_TASKS_REPORT_RUNNING=0` to keep the prior reporting. Verified present in the installed 2.1.270 binary (3 occurrences).

> "Fixed remote and headless sessions reporting "waiting for your input" while background agents were still running (set `CLAUDE_CODE_BG_TASKS_REPORT_RUNNING=0` to restore the old behavior)", Claude Code CHANGELOG 2.1.269
