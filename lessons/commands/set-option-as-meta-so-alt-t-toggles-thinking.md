---
id: set-option-as-meta-so-alt-t-toggles-thinking
created: 2026-08-31
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-connected-claude-code-to-your-browser_20260307.txt
  - transcripts/john-kim/his-claude-code-workflow-is-insane_20260307.txt
  - transcripts/john-kim/new-claude-code-updates-are-so-cool_20260424.txt
  - transcripts/john-kim/how-i-use-claude-code-meta-staff-engineer-tips_20260307.txt
  - transcripts/andrew-codesmith/900-hours-of-learning-claude-code-cursor-in-10-minutes_20260307.txt
  - transcripts/ray-amjad/my-claude-code-workflow-for-2026_20260307.txt
  - transcripts/simon-scrapes/the-only-claude-code-updates-you-need-to-know-apr-2026_20260424.txt
---

# Set 'Left Option Key Is Meta' So Alt+T Toggles Thinking Mid-Session

## TL;DR

In your terminal preferences, set the left Option key to act as Meta; Alt+T then toggles Claude Code's thinking mode mid-session, no restart or re-prompt needed.

## Why it matters

Flipping thinking mode per step is useful, but on many terminals the shortcut is unreachable because Option emits special characters instead of Meta, so the toggle silently never works. Extended thinking is a per-prompt decision more than a per-session one: some prompts benefit from deeper reasoning while others just pay its cost, and a working keybinding makes switching cheap enough that you actually do it at the moment of prompting.

## How to apply

Open your terminal's preferences and enable 'left Option key is Meta' (or your terminal's equivalent). From then on, press Alt+T inside a Claude Code session to switch thinking mode on or off mid-session, flipping it on before prompts that need deeper reasoning and off again for quick iterations.

## Related

[[chrome-extension-for-browser-testing]], [[voice-dictation-for-longer-richer-prompts]]
