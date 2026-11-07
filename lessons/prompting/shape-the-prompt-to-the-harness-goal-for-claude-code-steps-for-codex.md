---
id: shape-the-prompt-to-the-harness-goal-for-claude-code-steps-for-codex
created: 2026-08-22
status: active
supersedes: null
category: prompting
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/i-made-codex-and-claude-code-build-the-same-app-one-clearly-won_WCrnS09vpfo_20260820.txt
---

# Give Claude Code the Goal, Give Codex the Steps: the Same Prompt Does Not Transfer

## TL;DR

An identical open-ended /goal prompt made Claude Code exercise scope restraint and made Codex sprawl, so hand Codex explicit phases and a cut list and reserve outcome-only prompts for Claude Code.

## Why it matters

Same prompt, same task (a production-ready Typeform alternative, orchestrate specialized agents through research, build and verify phases, do not stop at a prototype), wildly different execution. Claude Code: one orchestrator, 35 subagents, roughly 2,800 tool calls, 5.5 hours, about 800 dollars of equivalent API billing, 2 million output tokens. Codex: one orchestrator, 126 subagents, 32,500 tool calls, nearly 62 hours, about 3,000 dollars, 11 million output tokens, and 135 capabilities pursued "with less restraint", producing an editor the creator found overwhelming to use. Codex's own anonymized review of both sessions gave product judgment and scope to Claude Code for making clear must versus defer decisions. The creator's read matches his daily use: Claude Code responds to "this is what I want, this is what good looks like, this is when you stop", while Codex behaves like an obedient executor that needs step one, step two, step three.

## How to apply

When the prompt is outcome-shaped and the path is open ("build X, here is what good looks like, here is when to stop"), run it in Claude Code. When you hand the same work to Codex, convert it into explicit phases with a scope boundary and an explicit not-building list, otherwise it will keep finding capabilities to add. Independent of harness, insert a planning and mapping phase between research and build in any long autonomous prompt; the creator's own retrospective was that going research to build directly is what let both runs drift. Check the resulting scope early rather than at the end: a run that has already spawned a hundred subagents has already made the decision for you.

## Related

[[insert-a-planning-phase-between-research-and-build-in-autonomous-prompts]]
