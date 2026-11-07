---
id: rewrite-tool-input-in-a-function-hook
created: 2026-09-12
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Rewrite a Tool Call's Input in a Function Hook Instead of Blocking and Re-Prompting

## TL;DR

Shell hooks can only allow or block. A function hook wraps the tool call like Express middleware, so it can edit the arguments in flight, for example replacing npm with pnpm in every Bash command before it runs.

## Why it matters

Blocking a wrong command costs a turn: the model gets the rejection, reasons about it, and tries again, sometimes wrongly. Rewriting is silent and deterministic, so the convention holds without spending context arguing about it, and the same shape (match the tool, match a regex, then rewrite or let it pass) covers anything you keep correcting by hand.

## How to apply

In the hook, match on the tool name (Bash), test the command against a regex, return the modified input to proceed with, and fall through untouched otherwise. Generate it with /plugin-authoring rather than hand-writing the wiring.

## Related

[[enable-function-hooks-to-unlock-plugin-authoring]], [[hook-matchers-exact-match-not-substring]], [[pretooluse-hook-context-strings-brief-the-model]]
