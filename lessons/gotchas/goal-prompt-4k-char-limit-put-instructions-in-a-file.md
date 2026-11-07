---
id: goal-prompt-4k-char-limit-put-instructions-in-a-file
created: 2026-07-12
status: active
supersedes: null
category: gotchas
sources:
  - transcripts/nate-herk-ai-automation/fable-5-just-built-me-a-business-with-one-prompt_R0qF17BVl9w_20260710.txt
---

# Beat /goal's ~4,000-Char Limit by Putting the Full Instruction Set in a File

## TL;DR

/goal silently caps around 4,000 characters, so for a long autonomous mission put the whole spec (mission, guardrails, phase arc, deliverables, definition-of-done, never-ask rule) in a file and make the /goal prompt just 'read this file and execute everything below the divider line as your goal.'

## Why it matters

A rich self-running multi-agent goal needs far more than 4k chars of instruction, but pasting it straight into /goal gets truncated; a referenced file has no limit, keeps the goal prompt tiny, and lets the model re-read the full contract as it works.

## How to apply

Write the spec to e.g. MASTER_PROMPT.md with a horizontal divider, then run: '/goal Read <file> and execute everything below the divider line as your goal. Follow it exactly including the never-ask rule. Do not report back until the definition of done is met. Start now.' Bake in 'make every call yourself and write down why' so it stays autonomous, and a subjective done-check (a stranger can open the recap HTML and run/understand the result).
