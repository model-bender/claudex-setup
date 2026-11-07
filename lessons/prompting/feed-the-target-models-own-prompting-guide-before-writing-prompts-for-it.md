---
id: feed-the-target-models-own-prompting-guide-before-writing-prompts-for-it
created: 2026-08-22
status: active
supersedes: null
category: prompting
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/this-simple-ai-setup-replaces-your-higgsfield-subscription__VX6BZDKgrg_20260820.txt
---

# Give the Agent the Target Model's Own Docs Before It Writes Prompts for That Model

## TL;DR

When Claude Code or Codex is building something that prompts a *different* model (a video, image, or third-party LLM API), point it at that provider's API docs and model card first - every provider publishes its own prompting rules, and the agent's priors are not those rules.

## Why it matters

Model-specific prompting is real and documented: provider pages carry per-capability tips (video understanding, dialogue, text generation) and every model ships some form of system or model card explaining how to prompt it. An agent writing prompts from its own training data ignores all of that, and the parameter surface differs per model too - Mark Kashef shows bitrate disappearing as a parameter when switching from one video model to another, and one model accepting both a start frame and an end frame while others don't. Feeding the docs in is what lets a cheap workhorse model (he uses a fast Gemini tier) reliably expand a vague user prompt like 'a stunning drone view' into something tuned for the specific model being called, and it's what keeps the parameter list in your UI correct per model.

## How to apply

Find the provider's documentation page for the exact model and capability, view it as markdown, and paste the whole thing into Claude Code or Codex with the instruction to derive both the request structure and the prompting rules from it - then have it write the prompt-refinement layer against those rules rather than generic advice. Do the same for the model card's prompting section. Repeat per provider if you're routing across several. This is the same discipline as [[convert-docs-to-markdown-before-feeding-claude]] applied one level up: the docs aren't just reference for the integration, they're the source of the prompting policy.

## Related

[[convert-docs-to-markdown-before-feeding-claude]]
