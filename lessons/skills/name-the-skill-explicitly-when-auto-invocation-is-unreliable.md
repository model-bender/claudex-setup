---
id: name-the-skill-explicitly-when-auto-invocation-is-unreliable
created: 2026-09-12
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/sean-kochel/google-s-7-step-vibe-engineering-skill-is-incredible_4bfKyZ7hbsU_20260703.txt
---

# Name the Skill in the Prompt When You Cannot Trust It to Auto-Invoke

## TL;DR

When a framework ships a skill that should fire for this step but does not reliably, say 'use the front-end UI engineering skill' by name instead of trusting the model to choose it.

## Why it matters

Skill selection is a model judgement call, and a skill that silently fails to load produces plausible output built without the guidance you installed it for, which is invisible in the result. That makes it the class of failure review does not catch. It bites hardest with skill libraries you did not write, where you cannot see or tune the description that drives the trigger.

## How to apply

For each skill you actually depend on, run the step and check the transcript for the skill loading. Where it does not fire, name it explicitly in the prompt for that step. If you own the skill, fix its description trigger instead, so you are not naming it forever.

## Related

[[scope-phased-build-frameworks-to-one-phase-per-invocation]]
