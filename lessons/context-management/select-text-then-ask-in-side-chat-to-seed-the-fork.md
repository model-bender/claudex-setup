---
id: select-text-then-ask-in-side-chat-to-seed-the-fork
created: 2026-07-25
status: active
supersedes: null
category: context-management
source_type: post
tool: codex
sources:
  - https://developers.openai.com/blog/mastering-codex-remote-for-engineering
---

# Select the Text First, Then "Ask in Side Chat": the Selection Becomes the Side Chat's Starting Context

## TL;DR

Beyond `/side` and `/side <prompt>`, selecting a passage in the transcript and choosing "Ask in side chat" seeds the fork with that exact excerpt.

## Why it matters

A bare `/side` inherits the whole thread snapshot and leaves the side chat to guess which part of it you meant, so you end up re-describing the error or diff you were looking at. Nothing in the UI advertises that a text selection is a valid entry point, which is why this stays undiscovered.

## How to apply

Highlight the error message or code block in the transcript, choose "Ask in side chat", and ask your question against it, reserving plain `/side` for questions about the thread as a whole.

> "Even better, select text in the transcript and choose Ask in side chat. The selected passage becomes the starting context for the new conversation.", Thomas Ricouard, OpenAI

