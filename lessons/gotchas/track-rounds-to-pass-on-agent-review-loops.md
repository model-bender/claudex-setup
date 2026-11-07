---
id: track-rounds-to-pass-on-agent-review-loops
created: 2026-11-06
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# Track Rounds-to-Pass on Agent Review Loops: One PR Ran More Than 50 Rounds Overnight

## TL;DR

When an agent writes and an agent reviews, the loop can run unbounded: the Claude Code team saw one PR go through more than 50 review and fix rounds overnight, and a git blame on what the reviewer kept flagging found about 59% was code present since its first pass. Track rounds to pass beside recall, and after three rounds have the reviewer ask the author to rethink the approach.

## Why it matters

Nits cost more when the author is an agent, because each one becomes another commit and another round. Running several rounds by default was something the team made worse itself.

## How to apply

1. Track rounds to pass alongside recall.
2. After three rounds, have the reviewer ask the author to step back and reconsider the approach.
3. Drop style-only and cleanup-only findings.
4. Use more rounds only for risky changes.

