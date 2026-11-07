---
id: claude-md-rule-to-aggressively-offload-research-to-subagents-for-0-50-context
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Add a CLAUDE.md Rule to Aggressively Offload Research, Docs, and Log Analysis to Subagents

## TL;DR

Add a user-level CLAUDE.md instruction telling Claude Code to always push online research, doc lookups, codebase exploration, and log analysis into subagents (log-checking specifically to a Haiku subagent), to stay in the 0-50% context range.

## Why it matters

Outside plan mode, quick doc checks or log greps load their full output straight into the main context window, jumping usage from ~30% to ~55% in one step; deferring that work to subagents keeps the main session in what the speaker calls the optimal 0-50% range.

## How to apply

Add to your user-level CLAUDE.md: 'always and aggressively offload online research, e.g., docs, codebase exploration, and log analysis to subagents. When you're about to check logs, defer that to a Haiku subagent. For complex problems you're going around in circles with, get a fresh perspective by asking subagents.'

## Related

[[subagents-for-noisy-tool-calls-not-large-edits]]
