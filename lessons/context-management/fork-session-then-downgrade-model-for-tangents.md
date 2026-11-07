---
id: fork-session-then-downgrade-model-for-tangents
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/ray-amjad/my-claude-code-workflow-for-2026_20260307.txt
---

# Downgrade the Model Inside a Forked Tangent Session

## TL;DR

When you fork a session to ask a tangent question about why the agent chose a particular approach, also switch that forked session to a cheaper model (e.g. Sonnet), since a tangent Q&A doesn't need the main session's model.

## Why it matters

The tangent session's job is explaining reasoning and pulling in outside information, not doing the main work, so it doesn't need the full-power model the main session is running.

## How to apply

After running the fork-session flow to branch off a tangent, switch the model in that new session to something cheaper before asking your follow-up questions.

## Related

[[fork-session-for-deep-dive-questions-without-context-pollution]], [[spawn-a-subagent-instead-of-switching-model-mid-session]]
