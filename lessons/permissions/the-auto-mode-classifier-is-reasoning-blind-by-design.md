---
id: the-auto-mode-classifier-is-reasoning-blind-by-design
created: 2026-09-13
status: active
supersedes: null
category: permissions
source_type: post
tool: claude-code
sources:
  - https://www.anthropic.com/engineering/claude-code-auto-mode
---

# Put the Justification in Your Own Message: Auto Mode Never Reads Claude's Reasoning

## TL;DR

Auto mode's classifier sees only your messages and the literal tool calls; Claude's own chat text and tool outputs are stripped before it runs.

## Why it matters

When an action is blocked it is natural to assume Claude explained itself and the classifier disagreed. It structurally cannot have: no amount of Claude arguing that a command is safe reaches the thing deciding.

## How to apply

When an action might trip the classifier, state the reason in your own prompt ("these branches are all merged, delete them") rather than expecting Claude to justify it. Note this sits alongside the classifier reading CLAUDE.md rules: instruction files count, Claude's live reasoning does not.

> "The classifier sees only user messages and the agent's tool calls; we strip out Claude's own messages and tool outputs, making it reasoning-blind by design.", Anthropic Engineering

