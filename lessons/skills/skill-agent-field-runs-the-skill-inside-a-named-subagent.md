---
id: skill-agent-field-runs-the-skill-inside-a-named-subagent
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# A Skill's agent: Frontmatter Field Launches It Inside a Named Subagent, Not Just a Fork

## TL;DR

Setting agent: in a skill's frontmatter (with context fork enabled) spins up that specific subagent, complete with its own system prompt, and then triggers the skill running inside that subagent's context.

## Why it matters

This is the opposite direction from listing skills in a subagent's own frontmatter; conflating the two means you either can't get a skill to inherit a subagent's persona and system prompt, or you accidentally expect a subagent to gain skills it was never granted.

## How to apply

Enable context-fork behavior on the skill and add agent: <subagent-name> to its frontmatter. Running the skill first spawns that named subagent (with its configured system prompt) and then executes the skill's steps inside it.

