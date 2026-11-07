---
id: update-brand-voice-file-on-every-manual-correction
created: 2026-09-01
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/simon-scrapes/the-only-claude-cowork-setup-busy-entrepreneurs-actually-need_BMEaJTl3Vo0_20260820.txt
---

# Fold Every Manual Brand-Voice Correction Back Into the Voice Profile File

## TL;DR

Whenever you find yourself manually adjusting Claude's output to match your actual style, update the brand-voice rule file with that correction immediately instead of just fixing the one output.

## Why it matters

Skipping the update means you'll make the identical correction again on the next output; the rule file only pays off if it captures what you've already learned works.

## How to apply

After editing an AI-drafted piece for tone, add the specific rule you applied (a phrase to avoid, a structure you prefer) to the core brand-voice file or its per-platform companion doc before moving on.

## Related

[[split-the-brand-voice-profile-per-platform]]
