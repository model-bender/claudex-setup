---
id: use-arrow-keys-not-tab-for-tabbed-command-output
created: 2026-09-01
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# Use Arrow Keys, Not Tab, to Switch Between Tabs in Multi-Tab Command Output

## TL;DR

Commands with tabbed output (like /stats) are now navigated with the left/right arrow keys instead of repeatedly pressing Tab to cycle through them.

## Why it matters

Tab-cycling through several tabs to reach the one you want is slower than jumping directly with an arrow key, and using Tab there can conflict with its other use for triggering suggestions.

## How to apply

When a command's output has multiple tabs, press the left/right arrow keys to move between them directly instead of pressing Tab repeatedly.
