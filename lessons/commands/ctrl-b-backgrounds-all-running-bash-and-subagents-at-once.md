---
id: ctrl-b-backgrounds-all-running-bash-and-subagents-at-once
created: 2026-09-01
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# Press Ctrl+B to Move Every Running Bash Command and Subagent to Background at Once

## TL;DR

If you have multiple foreground bash commands or subagents running simultaneously (e.g. five parallel explore subagents), Ctrl+B backgrounds all of them in one keystroke so you can keep chatting with Claude Code.

## Why it matters

Backgrounding tool calls one at a time is slow when several are running together; a single keystroke that batches the operation removes the friction of doing it individually.

## How to apply

While multiple bash commands or subagents are running in the foreground, press Ctrl+B to send all of them to the background simultaneously.

