---
id: build-a-record-mode-mod-that-masks-sensitive-values-on-screen
created: 2026-10-11
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-code-mods-are-game-changers-set-up-these-5-now_9hetShMMp2s_20261009.txt
---

# Add a record-mode mod toggled by a slash command to mask emails and figures while screen recording

## TL;DR

A mod can swap real emails and financial figures for placeholders in the displayed chat when you turn on a recording toggle, while Claude still reads the real text.

## Why it matters

Nate records videos and does not want to show email addresses or financial figures. In his demo, pasted HTML with prices was blurred on screen but the doc was still correctly edited from 29 to 39.

## How to apply

Ask Claude to build a mod with a command (his is 'record' to enable and 'record off' to disable) that masks personal and financial values in the display. Mods are turned on and off through slash commands and live in local files.

Checked: Binary 2.1.296: mods plumbing is present (`command grep -c -a plugin_dev_mods` = 4, case-insensitive `mods` = 88); /plugin appears as a command string. Mod behavior itself is described only by the speaker; not tested.
