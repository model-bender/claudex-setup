---
id: add-remove-all-mannered-prose-to-your-global-instructions
created: 2026-09-12
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-5-changed-prompting-forever-fix-yours-now_dfi3BsEPxic_20260910.txt
---

# Put 'Remove All Mannered Prose' in Your Global Instructions to Fix Fable 5.1's Density

## TL;DR

Fable 5.1 writes denser than Fable 5: longer sentences, fewer paragraph breaks. Anthropic's own name for it is mannered prose, and one line in your global instructions is the cheapest fix.

## Why it matters

Anthropic's own framing is the argument: mannered prose 'makes the reader work harder so the writer can perform.' Because the tendency is model-level rather than task-level, fixing it per prompt means repeating yourself forever and still missing the places you forget. Putting it in the instruction file that loads on every session fixes it in one place, and lets you delete the scattered per-prompt rules about jargon and sentence structure.

## How to apply

Add 'Please remove all mannered prose' to your CLAUDE.md (or the desktop app's project instructions). Then delete the ad hoc lines in individual prompts about marketing jargon, sentence length and structure, they were doing this job badly.

## Related

[[delete-formatting-bans-the-system-prompt-already-trims-them]], [[brand-voice-profile-reduces-ai-detection]], [[switch-to-the-built-in-concise-output-style-instead-of]]
