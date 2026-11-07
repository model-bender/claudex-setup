---
id: auto-mode-can-block-a-subagent-spawn-but-only-warns-on-return
created: 2026-09-13
status: active
supersedes: null
category: permissions
source_type: post
tool: claude-code
sources:
  - https://www.anthropic.com/engineering/claude-code-auto-mode
---

# Review What a Subagent Hands Back: Auto Mode Can Block the Spawn but Only Warns on Return

## TL;DR

Auto mode runs the same classifier pipeline recursively for subagents, but the delegation-side classifier can deny while the return-side one only warns.

## Why it matters

The safety net is asymmetric, tight going in and loose coming back, which is the opposite of the intuition that a permitted subagent is a supervised one. Anything a subagent read from untrusted content lands in your main session with a warning at most.

## How to apply

Do not treat "the subagent was allowed to run" as licence to skip reading what it returns, especially for any subagent that touched untrusted input. Review the handed-back output yourself.

> "Subagents run the same pipeline recursively, with handoff classifiers at delegation (can deny) and at return (warns only).", Anthropic Engineering

## Related

[[auto-mode-is-not-injection-containment-isolate-the-session]]
