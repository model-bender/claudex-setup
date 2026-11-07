---
id: skills-call-subagents-easily-the-reverse-rarely-works
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/ray-amjad/better-than-mcps-claude-code-s-new-skills-feature_20260307.txt
---

# A Skill Can Call a Subagent, But a Subagent Rarely Calls a Skill Back

## TL;DR

In practice a skill can chain into a subagent (e.g., a release-notes skill calling a release-notes-generator subagent), but the reverse direction is unreliable because the subagent's own system prompt doesn't mention that skills exist.

## Why it matters

Ray Amjad found this asymmetry in his own testing: 'I seem to be having a much harder time making a subagent call a skill instead... I think that's probably something to do with the system prompt of the subagent because it kind of forgets that skills are even a thing to begin with.'

## How to apply

Design compositions where the skill is the outer/calling layer and the subagent is the inner/called layer; don't rely on a subagent noticing and invoking a skill on its own unless you explicitly tell that subagent about the skill in its own prompt.

