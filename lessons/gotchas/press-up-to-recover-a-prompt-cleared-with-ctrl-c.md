---
id: press-up-to-recover-a-prompt-cleared-with-ctrl-c
created: 2026-10-11
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Press Up on the Empty Prompt to Recover a Draft You Cleared With Ctrl+C

## TL;DR

A long prompt wiped by Ctrl+C is not lost: pressing Up on the empty prompt brings the draft back, pasted text and images included.

## Why it matters

Clearing a half-written prompt by accident used to mean retyping it, including any pasted logs or screenshots. The draft is now kept.

## How to apply

After an accidental Ctrl+C, press Up before typing anything else. Do not press Ctrl+C a second time, since two presses exit the session. Shipped in 2.1.288; this is a hotkey behaviour, so there is no setting to check.

> "Added recovery for a prompt cleared with Ctrl+C: pressing Up on the empty prompt brings the draft back, including pasted text and images", Claude Code CHANGELOG 2.1.288

## Related

[[exit-claude-code-with-ctrl-c-twice]]
