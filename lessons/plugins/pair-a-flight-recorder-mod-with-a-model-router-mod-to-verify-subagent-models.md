---
id: pair-a-flight-recorder-mod-with-a-model-router-mod-to-verify-subagent-models
created: 2026-10-11
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/mark-kashef/claude-code-now-has-mods-here-are-10-worth-stealing_uvIopT_2sY0_20261009.txt
---

# Verify a model-router mod took effect with a flight-recorder mod before trusting the savings

## TL;DR

Mark runs a router mod that forces cheaper models for subagents and a flight-recorder mod that shows each request's model and tools, so the router's effect is visible.

## Why it matters

His router mod (/router on, off, sonnet, haiku, both) was tested with a prompt asking for two parallel explore agents; the timeline view then showed 'sonnet number one, sonnet number two'. He says mixing mods lets you confirm changes are taking effect and that you are saving money, which matters on extra usage.

## How to apply

1. Install a request-timeline mod as a plugin (see the install lesson). 2. Install or build a router mod whose commands you define (he lists on, off, sonnet, haiku, both and says you can ask Claude Code for only two). 3. Send a prompt that spawns subagents and read the timeline for the model on each. 4. Optionally add a mod that reports money saved.

## Related

[[build-claude-code-mods-as-plugins-installed-at-user-scope]]
