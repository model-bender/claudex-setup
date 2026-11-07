---
id: restate-critical-rules-in-subagent-prompts-explore-and-plan-skip-claude-md
created: 2026-08-29
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/simon-scrapes/19-claude-code-mistakes_icM0ewXGvAw_20260824.txt
---

# Restate critical rules in subagent prompts: built-in Explore and Plan agents skip CLAUDE.md

## TL;DR

A subagent receives only its own system prompt, your task text, and usually the CLAUDE.md hierarchy, never conversation history, output style, auto-memory, or files already read; and the built-in Explore and Plan agents that Claude auto-delegates to skip CLAUDE.md entirely, so constraints that must hold have to be restated in the delegation prompt itself.

## Why it matters

The dangerous case is the one you didn't choose: Claude spins out Explore/Plan subagents on its own during normal work, and those receive none of your CLAUDE.md rules, so a hard constraint like "never touch the migrations folder" or "all queries go through the repository layer" simply doesn't exist for them. There is no setting that fixes this; the only reliable channel into a subagent is the instruction text you (or the delegating prompt) pass it. For side tasks that genuinely need the full accumulated context, forking the conversation inherits everything and sidesteps the problem.

## How to apply

Keep a short list of your genuinely critical constraints and paste them into any subagent task prompt whose work they govern, including telling the main session to forward them if it delegates further. When the task needs conversation nuance rather than just rules, fork the conversation instead of spawning a fresh subagent. Assume anything not restated is unknown to the subagent: history, output style, auto-memory, and previously read files all stay behind.

## Related

[[output-styles-don-t-reach-subagents-use-a-fork-when-the-style]], [[subagents-for-noisy-tool-calls-not-large-edits]]
