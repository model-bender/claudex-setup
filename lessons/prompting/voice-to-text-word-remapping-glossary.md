---
id: voice-to-text-word-remapping-glossary
created: 2026-09-01
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/austin-marchese/17-tricks-to-build-10x-faster-with-claude_ZzHB2mPHb2g_20260724.txt
---

# Build a Word-Remapping Glossary in Your Voice-to-Text Tool for Terms It Keeps Mishearing

## TL;DR

If your voice-to-text tool consistently mishears a specific term you use often (product names, technical vocabulary), add a word-mapping entry in the tool itself so what reaches Claude matches what you actually said.

## Why it matters

The presenter's product 'buildpartner.ai' gets transcribed as 'boat partner' in his New York accent every time, creating 'an inherent mismatch in what you say and what is sent to Claude' so Claude thinks you mean two different things. This is silent and easy to miss because the transcript reads as plausible English.

## How to apply

In whatever voice-to-text tool you use (the presenter names Hex and Whisper Flow as options), find its custom-word or remapping/glossary setting and add an entry mapping the mis-heard phrase to the correct term for every word you notice going wrong.

## Related

[[voice-dictation-for-longer-richer-prompts]]
