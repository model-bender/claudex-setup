---
id: draw-a-live-status-row-from-a-function-hook
created: 2026-09-12
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Draw a Live Status Row in Claude Code From a Function Hook

## TL;DR

Function hooks can add UI. A hook that watches deploys can paint a row next to the prompt showing the current stage (queued, building, ready) and how long it has been running, with a button to hide and reshow it, and each hook gets a panel where its data updates live.

## Why it matters

This is the class of information you would otherwise alt-tab to a dashboard for, and the row only exists while the hook has something to say. In the demo the row tracked a Vercel deploy through to ready at 5 minutes 50 seconds without leaving the session, and stacked as new deploys arrived.

## How to apply

Describe the row to /plugin-authoring: what triggers it, what it shows, how long it stays after the event, and how new entries stack. Ask for prototypes before it writes the final version, because the layout is the part you will iterate on.

## Related

[[claude-code-statusline-shows-clickable-active-pr-link]], [[enable-function-hooks-to-unlock-plugin-authoring]]
