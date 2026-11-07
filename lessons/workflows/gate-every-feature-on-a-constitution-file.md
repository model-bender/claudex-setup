---
id: gate-every-feature-on-a-constitution-file
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/sean-kochel/why-your-agentic-workflows-don-t-work_ILKrUq_8aC4_20260820.txt
---

# Gate Every Feature on a Constitution File Rather Than Trusting Skills to Hold the Line

## TL;DR

Skills alone are not a build system; run them inside a spec-driven process where a constitution.md of project principles has to validate before planning proceeds, and the process refuses to continue when a feature violates it.

## Why it matters

The failure mode is relying on a pile of skills plus an orchestrating agent with no guardrails and no phase artifacts checking each other, which the creator flags as a guaranteed bad time for apps, agentic workflows and n8n-style automations alike. The special case worth naming is turning a video transcript into a skill: pasting someone's transcript into a model and asking it to build you their system is described as a terrible idea that will blow up in your face, because a transcript has no artifacts, no acceptance criteria and no integration checks. Spec Kit's constitution mechanism is the concrete alternative: principles about your app, its ethos and what things mean are generated into constitution.md, and planning a feature or generating tasks has to validate against that file, bouncing the work back to you with the violated principle when it does not pass. Its clarify stage then hunts ambiguity in the spec, which is what stops the model making an arbitrary call on something you never decided.

## How to apply

Adopt a spec-driven system rather than bare skills; the creator's two picks are OpenSpec (lighter, you can move between phases freely) and GitHub Spec Kit (more rigorous, strictly sequential gating). With Spec Kit, generate the constitution first and keep it current, then run specify, clarify, plan, tasks and implement, letting the constitution check block anything that violates your principles and letting the task breakdown mark which tasks can run in parallel versus in sequence. Add your own quality-gate checklists at the task stage. When a skill from a video looks useful, rebuild the idea through this process instead of asking a model to reconstruct the system from the transcript.

## Related

[[dont-build-a-skill-from-a-video-transcript]]
