---
id: move-repeated-prompt-constraints-into-agents-md
created: 2026-08-31
status: active
supersedes: null
category: configuration
tool: codex
sources:
  - transcripts/john-kim/complete-beginner-s-guide-to-openai-s-codex-app_20260424.txt
---

# Move Constraints You Keep Retyping Into AGENTS.md, Repetition Is the Signal

## TL;DR

When the same constraint (framework, architecture, anything not apparent from the code) shows up in prompt after prompt, stop restating it and put it in AGENTS.md so every run inherits it.

## Why it matters

Constraints repeated by hand are constraints you will eventually forget to include, and the run that misses one goes off in a direction the constraint existed to prevent. AGENTS.md applies them to every session automatically, and catching yourself retyping a line is the reliable trigger for when a constraint has earned a place there.

## How to apply

As you write the constraints section of a Codex prompt, watch for lines you have written before. Move any repeat into AGENTS.md and drop it from your prompts from then on.

## Related

[[done-when-prompt-scaffold-for-codex]]
