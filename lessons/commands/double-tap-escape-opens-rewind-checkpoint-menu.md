---
id: double-tap-escape-opens-rewind-checkpoint-menu
created: 2026-09-01
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/andrew-codesmith/master-95-of-claude-code-in-15-mins-as-a-beginner_20260424.txt
  - transcripts/john-kim/how-i-use-claude-code-meta-staff-engineer-tips_20260307.txt
---

# Press Escape Twice to Open the Checkpoint/Rewind Menu

## TL;DR

Double-tapping Escape in Claude Code's terminal UI brings up a list of recent prompts/checkpoints you can rewind to, without typing a slash command.

If you pasted a lot of text into the prompt box and want to discard it, double-tap Escape to clear it instead of deleting manually.

With the input box empty, double-tapping Escape opens a rewind view where you can restore an earlier context point.

## Why it matters

The creator describes this as one of his three daily hacks: 'I press escape escape, and it shows me a load of prompts, or like checkpoints really... I can just tell Claude to forget the recent conversation history from then.'

John Kim calls this out as a handy shortcut he uses 'all the time' for exactly this situation (a big paste you decide not to send).

John Kim distinguishes this from the clear-input shortcut: on an empty prompt, the same double-Escape gesture surfaces the rewind/restore feature instead.

## How to apply

Mid-session, press Escape twice to bring up the checkpoint list, pick the point you want to rewind to, and tell Claude to forget everything after it, instead of letting a failed debugging detour keep bloating the context window.

With text in the input box, press Escape twice quickly to clear it.

Make sure the input box is empty, then press Escape twice to bring up the rewind menu and pick an earlier point to restore.

## Related

[[rewind-instead-of-arguing-with-stale-context]], [[rewind-can-recover-a-cleared-conversation]], [[directional-summarize-rewind-menu]]
