---
id: pretooluse-hook-context-strings-brief-the-model
created: 2026-08-31
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
  - transcripts/ray-amjad/anthropic-just-dropped-their-internal-skills-strategy_20260424.txt
  - transcripts/simon-scrapes/every-claude-code-memory-system-compared-so-you-don-t-have-to_20260424.txt
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
---

# Return Context Strings From a PreToolUse Hook to Brief the Model Before It Proceeds

## TL;DR

A PreToolUse hook is not only an allow/block gate: it can pass additional context strings back to the model, which reads them before proceeding with the tool call, for example injecting a memory index right before the action.

## Why it matters

Hooks are usually treated purely as guardrails, so this second capability stays invisible: a PreToolUse hook can deliver context deterministically at the exact lifecycle moment it is relevant, without spending CLAUDE.md lines or relying on the model to remember to fetch it. Injecting something like a memory index just before a tool runs puts the information in front of the model precisely when it acts.

## How to apply

Write a PreToolUse hook whose output returns the context string you want the model to see (a memory index, a per-tool reminder, freshly computed state); the model reads it before proceeding with the tool call. Define the hook in settings.json for global behavior or in skill/agent YAML frontmatter to scope the injection to one skill or agent.

## Related

[[hooks-for-automation-and-guardrails]]
