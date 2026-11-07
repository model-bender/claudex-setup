---
id: search-past-prompts-with-ctrl-r-then-widen-the-scope
created: 2026-09-12
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Search Every Prompt You Have Written With Ctrl+R, Then Widen the Scope

## TL;DR

Ctrl+R opens a search over the prompts in the current session. Pressing Ctrl+S inside that search widens it to the whole project, and again to every project on the machine.

## Why it matters

Up-arrow history only reaches the current session, so a prompt you tuned three weeks ago in another repo gets rewritten from scratch. In the demo, typing 'credit' pulled back a prompt about the API credit pricing controversy and typing 'PDF' pulled back a slide-deck prompt, both from history rather than memory.

## How to apply

Press Ctrl+R at the input and type any word from the old prompt. Press Ctrl+S once to widen the search to this project and again to reach every project on the machine, then select the match to reinsert it.

## Related

[[session-resume-keyboard-shortcuts]], [[search-cross-project-session-history-in-natural-language]]
