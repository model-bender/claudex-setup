---
id: dispatch-routes-tasks-by-type-desktop-must-stay-open
created: 2026-09-01
status: active
supersedes: null
category: remote-access
tool: claude-code
sources:
  - transcripts/simon-scrapes/the-only-claude-code-updates-you-need-to-know-apr-2026_20260424.txt
---

# Use Dispatch's One Persistent Thread to Auto-Route Tasks to Claude Code or Claude Co-work by Type

## TL;DR

Dispatch gives you a single ongoing conversation thread from your phone; describe a task and it decides whether it's a coding job (routed to Claude Code) or knowledge work (routed to Claude Co-work), running each independently and pushing a notification when done, but your desktop app must stay open the whole time or the session is lost.

## Why it matters

Unlike remote control (a window into one running session), Dispatch is an orchestrator that spins up the right kind of session for you, letting you fire off multiple parallel tasks from your phone without deciding tool-per-task yourself. The tradeoff documented in the same segment is that closing the laptop lid (not just letting it sleep) kills the session, so it only works for genuinely long-running desktop uptime.

## How to apply

Open Dispatch and send it a task description from your phone in plain language; don't specify which tool to use, it classifies code tasks to Claude Code and knowledge tasks to Claude Co-work itself. Keep your desktop machine's lid open and the app running for the duration; check back via push notification rather than polling.

## Related

[[remote-control-channels-for-phone-access]]
