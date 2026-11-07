---
id: relay-through-notion-to-preserve-formatting-on-paste
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/simon-scrapes/you-re-using-claude-code-wrong-these-10-tips-will-change-everything_20260307.txt
---

# Relay Claude's Markdown Output Through a Notion Page When a Destination App Mangles It

## TL;DR

For platforms other than the one you can prompt for natively, paste Claude's markdown output into a fresh Notion page first, then copy out of Notion into the target app; Notion preserves the markdown and converts it on copy-out.

## Why it matters

The speaker's workaround for formatting loss when moving content between apps: 'if you're not working in LinkedIn... always post it into a new notion page. It will maintain that markdown formatting and then notion supposedly when you copy from notion will convert to the output format of whatever platform you're using.' He notes this specific relay 'doesn't seem to work very well for LinkedIn,' which is why LinkedIn gets the native-format-prompt workaround instead.

## How to apply

Paste Claude's raw markdown response into a new Notion page as an intermediate step, then copy from that Notion page and paste into your actual destination app. Use this for apps other than LinkedIn; for LinkedIn, prompt for native formatting instead.

## Related

[[copy-command-for-formatted-output]], [[request-platform-native-format-before-clipboard-paste]]
