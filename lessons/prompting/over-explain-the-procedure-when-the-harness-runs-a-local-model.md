---
id: over-explain-the-procedure-when-the-harness-runs-a-local-model
created: 2026-08-16
status: active
supersedes: null
category: prompting
tool:
  - claude-code
  - codex
about: local models
sources:
  - transcripts/mark-kashef/3d-websites-just-became-free-one-prompt_FSnubu4Lpz8_20260812.txt
---

# Write the Whole Procedure Out When the Harness Runs a Local Model

## TL;DR

The brevity you get away with in Claude Code and Codex is a frontier-model affordance - they decompose a task into subtasks at their own effort level. A local model will not, so supply the decomposition yourself, including precomputed numbers and a reminder of which capabilities it has.

## Why it matters

The asymmetry is direct: with local models you always have to over-explain, whereas with Codex and Claude you can be lazier because they are smart enough to work through their effort levels and break the task into subtasks.

The failure is quiet. A local model given the same terse prompt does not error - it produces the formulaic default, so the missing decomposition shows up as bland output rather than as a failure you can debug. Precomputing derived facts matters for the same reason: the creator had a model analyse the source video first, then pasted the resulting frame count into the prompt rather than expecting the local model to work it out mid-run.

## How to apply

Structure the prompt as an explicit procedure:

- name the skill to read first
- state the exact artifact wanted in one shot ("a scroll-scrubbed website for a private bank called Meridian, tagline wealth fortified")
- give the input file's exact path and describe what it contains
- paste in any number you can precompute elsewhere ("this gives you approximately 362 frames")
- spell out the ordered steps ("watch the footage first, extract six key frames and read them")
- explicitly remind it of capabilities it will not use unprompted ("this model has vision")
- finish with vibe, accents, voice, tone, structure, and any other skills it should pull in

Keep the same prompt short for a frontier harness, where the extra scaffolding buys nothing.

## Related

[[build-and-harden-a-local-harness-with-a-frontier-agent]], [[size-local-models-by-half-params-and-keep-a-quantization-floor-for-tool-use]], [[turn-reasoning-off-on-local-coding-models]]
