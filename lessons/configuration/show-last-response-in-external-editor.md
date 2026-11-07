---
id: show-last-response-in-external-editor
created: 2026-09-12
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Turn On 'Show Last Response in External Editor' So Ctrl+G Carries Claude's Answer Too

## TL;DR

By default Ctrl+G opens only your own prompt in the external editor. Flip the /config toggle and it opens your most recent prompt plus Claude's last response, so you can write the next prompt underneath the answer.

## Why it matters

Reading a long answer through the terminal's collapsible window while composing a reply to it is the friction this removes. With the response in the editor you can quote it, react to it inline, and keep the full context of what was said in front of you.

## How to apply

Stash the current prompt, run /config, type 'show' to filter, set 'show last response in external editor' to true, then press Ctrl+G at the input.

## Related

[[edit-plan-in-editor-ctrl-g]]
