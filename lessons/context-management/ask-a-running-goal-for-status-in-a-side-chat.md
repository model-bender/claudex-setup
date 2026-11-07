---
id: ask-a-running-goal-for-status-in-a-side-chat
created: 2026-10-19
status: active
supersedes: null
category: context-management
tool: codex
sources:
  - transcripts/john-kim/stop-using-codex-in-terminal-it-s-holding-you-back_yK9GnaE9rlY_20261017.txt
---

# Ask a Long-Running Goal for Its Status in a Side Chat, Then Steer the Fix Into the Main Thread

## TL;DR

To check on a goal that has run for hours without interrupting it, open a side chat (it inherits the thread's context), ask for status, and if the goal is stuck, add the fix to the main chat and steer it in.

## Why it matters

John Kim does this daily on long goals. In the app the side chat and main thread are visible together, whereas he says in the CLI the side conversation takes over the window you are in.

## How to apply

1. Open a side chat (the /side command in the Codex terminal, or the app's side-chat control or hotkey). 2. Ask 'tell me about the status of the goal'. 3. If it is blocked, send the fix in the main chat so the goal continues. Checked: codex-cli 0.163.0 vendored binary contains the string 'side conversation' (23 hits) and '/side' (6 hits); the CLI-versus-app window behaviour is the speaker's claim.

## Related

[[select-text-then-ask-in-side-chat-to-seed-the-fork]]
