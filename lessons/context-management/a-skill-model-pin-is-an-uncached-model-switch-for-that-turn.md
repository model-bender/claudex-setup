---
id: a-skill-model-pin-is-an-uncached-model-switch-for-that-turn
created: 2026-10-02
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/prompt-caching
---

# Treat a skill or command with a `model:` frontmatter as an uncached model switch for that turn

## TL;DR

A skill that pins a different model re-reads the whole conversation uncached on the turn it runs.

## Why it matters

In a long session this is a full-price re-read hidden inside a slash command. Pinning a cheap model on a skill saves little if the history is large.

## How to apply

Set `model:` in skill or command frontmatter only for skills run early or in short sessions, or use `context: fork` so the forked subagent takes the model and the parent cache stays intact. The skills page says the session model resumes on the next prompt.

Verified: Read live docs prompt-caching.md and skills.md (frontmatter table, `model` row, same statements). `command grep -c -a -F PreModelSwitch` on 2.1.287 = 35, so the confirmation hook the page mentions exists. Library has prompt-cache-what-breaks-it (generic model switch) and gate-model-switches-with-a-premodelswitch-hook; neither mentions frontmatter-triggered switches.

> "When a skill or command's frontmatter names a [`model`](/docs/en/skills#frontmatter-reference) other than the session's current model, that turn is also a model switch: the next request reads the entire conversation history with no cache hits.", Claude Code docs (prompt caching)
