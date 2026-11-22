---
id: tell-claude-to-write-a-script-and-not-open-the-big-file
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/everyone-ignore-these-claude-concepts-but-they-change-everything_6VjeXzvpoJo_20261120.txt
---

# For deterministic work on a big file, tell Claude to write a script and not to open the file

## TL;DR

When you only need totals, a move or a filter, keep the file on disk, have Claude write a script that reads it, and say in the prompt not to open it. Only the script's short output enters the chat.

## Why it matters

The video says a file handed to Claude is read in full, and read again if passed on, so a large spreadsheet or a meeting transcript costs tokens each time even when no reading is needed. It does not apply when you actually want a summary of the content.

## How to apply

Add a line such as: don't open this file, write a script that gives me the spend and the leads by month for this client, and show me only the report. Use it for moving files between systems or numeric analysis; skip it when you need Claude to understand the text.

Checked: No mechanism claim (prompt wording). Caveat checked 2026-11-22: the 150,000 to 2,000 token figure the video cites comes from Anthropic's 'Code execution with MCP' post, where it concerns loading tool definitions on demand, not reading spreadsheets, so that number is deliberately left out. The advice itself is this lesson's inference from the video and is untested here.
