---
id: write-the-handoff-as-a-prompt-for-the-next-session
created: 2026-09-12
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Write the Session Handoff as a Prompt for the Next Session, Not a Summary for You

## TL;DR

Instead of 'summarize our progress', ask Claude to write the next instructions as a prompt for the next session. Paste that straight into a fresh window.

## Why it matters

A human-readable summary ('the refactor was good, some issues remain') is useless the next morning, because it describes work rather than directing it. A prompt naturally does the right things: it points at exact files and folders instead of describing them, it names what was tried and did not work, and it opens with where to start. The example produced a full continuation brief for a homepage redesign, with the file list and the task breakdown, in place of a paragraph of narration.

## How to apply

End the session with 'write the next instructions as a prompt for the next session, not a summary for a human', add anything it does not know, then open a fresh session with that text as the first message.

## Related

[[build-a-session-handoff-skill-for-manual-context-clearing]], [[tell-fresh-session-not-to-act-until-instructed-after-handoff]]
