---
id: rename-command-syncs-session-tab-and-input-bar-name
created: 2026-09-01
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# /rename Also Retitles the Terminal Tab and Input Bar, Not Just the Session List

## TL;DR

Running /rename doesn't just label the conversation in /resume; it also renames the terminal tab (e.g. in Warp) and the input bar, which helps when juggling many sessions side by side.

## Why it matters

With multiple sessions open, a synced tab/input-bar name makes it much faster to identify which window is which than relying on the default session title.

## How to apply

Run /rename and press enter for an automatic name based on the conversation, or /rename <name> for a custom one (e.g. 'MCP workers'). Expect this to also update the terminal tab title in terminals like Warp and the on-screen input bar label.
