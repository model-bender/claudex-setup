---
id: slash-commands-and-skills-merged-internally
created: 2026-09-01
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
---

# Slash Commands and Skills Are Now the Same Mechanism Internally

## TL;DR

Your commands folder still works exactly as before, but Claude Code now treats slash commands and skills as the same underlying construct behind the scenes rather than two separate systems.

## Why it matters

The transcript states this plainly: 'they now merged slash commands and skills together. So you can still have the commands folder, for example, but behind the scenes in Claude Code, they are treated as the same thing.' This matters for anyone deciding whether to migrate legacy commands into the skills format, since the distinction is now cosmetic rather than functional.

## How to apply

Don't feel pressure to migrate an existing commands/ folder to skills/ purely for capability reasons; both are dispatched through the same internal mechanism now, so the choice between them can be based on convention/discoverability rather than feature parity.
