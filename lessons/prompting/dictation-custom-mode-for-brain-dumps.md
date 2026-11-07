---
id: dictation-custom-mode-for-brain-dumps
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: [claude-code, codex]
sources:
  - transcripts/edmund-yong/i-coded-another-profitable-app-from-scratch-everything-i-did-no-bs-step-by-step_kPVsX6lov_I_20260910.txt
---

# Add a Dictation Custom Mode That Turns Brain Dumps Into Instructions

## TL;DR

Voice tools support per-mode instructions applied to every dictation. A 'coding mode' that rewrites unstructured speech into clear actionable instructions means you can ramble at the agent and it still receives a structured prompt.

## Why it matters

The reason dictated prompts work is that speaking aloud tends to include the why behind the request, which is context typing usually drops. The custom mode keeps that context while removing the rambling shape, so you get the benefit without hand-editing the transcript. The same tool's replacements feature expands a short phrase into a whole prompt template.

## How to apply

In your dictation tool, create a mode with instructions like 'turn this into clear, actionable instructions for a coding agent, keep all reasoning about why', bind it to a hotkey, and add replacements for prompt boilerplate you retype. Run the models locally if you want dictation offline and off third-party services.

## Related

[[voice-dictation-for-longer-richer-prompts]], [[voice-to-text-word-remapping-glossary]]
