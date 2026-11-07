---
id: webfetch-reads-long-pages-in-chunks-ask-for-the-rest-with-offset
created: 2026-10-11
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Ask Claude to Keep Reading a Long Page With WebFetch offset, and Distrust Long Fetches From Before 2.1.290

## TL;DR

WebFetch used to drop page text past 100,000 characters without saying so. Since 2.1.290 it reports how much was unread and accepts an `offset` to continue.

## Why it matters

A long reference fetched on an older version may have been missing its tail, so conclusions drawn from it can be wrong with no sign of the gap. On current versions the rest is only read if the model actually continues.

## How to apply

For long docs, tell Claude to keep calling WebFetch with `offset` until nothing is unread. When the exact text matters, curl the page to a file instead. `offset` is a WebFetch tool parameter, so there is no setting to check.

> "Fixed WebFetch silently dropping page text past 100,000 characters; it now says how much was unread and takes an `offset` to read on", Claude Code CHANGELOG 2.1.290
