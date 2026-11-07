---
id: desktop-app-hides-sessionstart-hook-output
created: 2026-08-31
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/austin-marchese/17-tricks-to-build-10x-faster-with-claude_ZzHB2mPHb2g_20260724.txt
---

# Verify SessionStart Hook Output in the Terminal CLI: the Desktop App Hides It

## TL;DR

SessionStart hook messages only appear in terminal Claude Code; the desktop app hides the hook's output, so a session-open reminder silently does nothing there and you conclude the hook is broken.

## Why it matters

The failure is silent: the hook loads and runs, but its message never reaches you in the desktop app, so anything you rely on SessionStart output for simply never appears in desktop sessions. The natural misdiagnosis is that the hook itself is broken, which sends you debugging the wrong layer.

## How to apply

Test any SessionStart hook that prints or surfaces a message in terminal Claude Code, not the desktop app. If a session-open reminder or injected note matters to your workflow, run those sessions from the terminal where SessionStart output is actually displayed.

## Related

[[sessionstart-hook-day-of-week-reminders]]
