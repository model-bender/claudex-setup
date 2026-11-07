---
id: sessionstart-hook-day-of-week-reminders
created: 2026-07-25
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/austin-marchese/17-tricks-to-build-10x-faster-with-claude_ZzHB2mPHb2g_20260724.txt
---

# Put Recurring Reminders in a SessionStart Hook With Day-of-Week Logic

## TL;DR

A SessionStart hook fires the moment a session opens, so branch on the day of the week and surface the thing you meant to do, "It's Friday, want to run `/improve-system` before we begin?", inside the tool you're already in, rather than in a calendar you don't read.

## Why it matters

The creator's periodic maintenance skills (system-improvement passes, weekly reviews) kept getting skipped because the reminder lived somewhere other than the terminal he works in all day. SessionStart puts the prompt at the exact moment he can act on it, with zero context switch. The gotcha from the transcript: these messages only appear in the terminal CLI, the desktop app hides SessionStart hook output, so the reminder silently does nothing there and you conclude the hook is broken.

## How to apply

Add a SessionStart hook in `settings.json` whose command checks the current weekday and echoes the matching reminder, naming the exact skill or command to run. Keep one branch per cadence rather than printing a wall of text every session, a reminder you see daily stops registering. Verify it in terminal Claude Code, not the desktop app. Pairs with the SessionStart hook already used to catch plan archival on clear-context approvals.

## Related

[[desktop-app-hides-sessionstart-hook-output]]
