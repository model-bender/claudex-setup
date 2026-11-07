---
id: include-a-why-in-every-subagent-system-prompt
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Add a CLAUDE.md Rule to Always Include a 'Why' in Subagent System Prompts

## TL;DR

Instruct Claude Code, at the user CLAUDE.md level, to always state the specific purpose behind a subagent it spawns, not just the task.

## Why it matters

Without a stated purpose, parallel subagents exploring the same area (e.g. 'how auth works') produce generic, overlapping summaries. With a why (e.g. 'how auth works for rate limiting because you're improving rate limiting'), the subagent filters signal from noise and results stop overlapping.

## How to apply

Add to your user-level CLAUDE.md: 'when spawning a subagent, include a why in the subagent system prompt because it will help it filter the signal from the noise.'
