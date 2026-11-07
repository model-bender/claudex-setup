---
id: output-styles-don-t-reach-subagents-use-a-fork-when-the-style
created: 2026-08-22
status: active
supersedes: null
category: agents
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/output-styles
---

# Output Styles Don't Reach Subagents: Use a Fork When the Style Must Hold

## TL;DR

A subagent ignores your output style because it builds its own system prompt; a `subagent_type: "fork"` inherits the parent's full system prompt and therefore the style.

## Why it matters

Delegating the write-up half of a task to a subagent silently reverts the voice/format you configured, which is exactly the work where the style mattered; the fix is a spawn-type choice, not more prompt text.

## How to apply

For delegated work whose output goes to the user, spawn with `subagent_type: "fork"` (or restate the style in the subagent's own definition); keep plain subagents for work whose output you rewrite yourself.

> "Output styles apply to the main conversation only: a subagent runs its own system prompt, so styles don't change how subagents respond. A fork is the exception, because it inherits the parent's full system prompt.", canonical: Claude Code docs — Output styles
