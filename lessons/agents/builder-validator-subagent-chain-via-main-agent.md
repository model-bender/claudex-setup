---
id: builder-validator-subagent-chain-via-main-agent
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-workflow-explained-u0026-when-to-use-each_20260424.txt
---

# Chain a Builder Subagent Into a Reviewer Subagent Through the Main Agent

## TL;DR

Since subagents cannot message each other directly, get a free build-then-review quality gate by having one subagent build something, letting its output return to the main agent, then handing that output to a second reviewer subagent.

## Why it matters

The video calls this the 'builder-validator chain', one of the most powerful applications of the split-and-merge pattern: because sub-agents are hub-and-spoke (they can only report to the main agent, never to each other), the main agent has to be the one relaying builder output to the reviewer. Without realizing this constraint, someone might wrongly ask a builder and reviewer subagent to 'coordinate' directly and get silence.

## How to apply

Prompt Claude to (1) delegate a build task to a subagent, (2) once it returns, delegate the reviewer subagent with that build's output, and (3) synthesize the reviewer's findings back into the main conversation, all funneled through the main agent rather than expecting the two subagents to talk to each other.
