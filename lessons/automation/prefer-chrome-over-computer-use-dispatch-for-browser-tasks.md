---
id: prefer-chrome-over-computer-use-dispatch-for-browser-tasks
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/john-kim/new-claude-code-updates-are-so-cool_20260424.txt
---

# Prefer /chrome Over Full Computer-Use Dispatch for Anything Browser-Based

## TL;DR

For web tasks, /chrome is faster and higher-fidelity than dispatching a full computer-use agent to click around the screen; reserve computer-use dispatch for desktop programs that have no browser or API path at all.

## Why it matters

Computer-use dispatch works by taking screenshots and clicking based on vision, which the speaker found slow and largely not useful for tasks he already had another way to do (bash, /chrome). It only earns its keep for software with literally no other access route.

## How to apply

Default to /chrome for any task involving a website. Only reach for full computer-use/dispatch when the target is a native desktop application (e.g. Final Cut Pro, Logic Pro) with no API or browser-based alternative, and expect it to be noticeably slower.

## Related

[[chrome-extension-for-browser-testing]]
