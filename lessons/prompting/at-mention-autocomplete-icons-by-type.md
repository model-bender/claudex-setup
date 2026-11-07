---
id: at-mention-autocomplete-icons-by-type
created: 2026-09-01
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
---

# @ Autocomplete Now Shows a Different Icon per Suggestion Type

## TL;DR

When typing @ to autocomplete a mention, Claude Code now shows distinct icons: a plus for files, an asterisk for agents, and a diamond for MCP server tools, making it easy to tell which kind of item you're about to reference.

## Why it matters

The transcript notes this small UI change directly: 'the @autocomplete now added icons for different types of suggestions. So doing @ and typing something, + basically refers to any files, * refers to any agents, and then diamond refers to any MCP server tools.'

## How to apply

When @-mentioning something in a prompt, glance at the icon in the autocomplete list before selecting: + = file, * = agent, diamond = MCP tool, to avoid picking the wrong item when names collide across categories.
