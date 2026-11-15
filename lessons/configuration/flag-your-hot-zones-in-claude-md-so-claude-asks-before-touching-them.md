---
id: flag-your-hot-zones-in-claude-md-so-claude-asks-before-touching-them
created: 2026-11-15
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/austin-marchese/ask-claude-these-5-questions-it-ll-make-you-build-10x-faster_fFktpPMQzjI_20261112.txt
---

# List your hot zones in CLAUDE.md and require Claude to flag them and wait for approval

## TL;DR

Name the few parts of your work that must be right (a payment flow, a plugin that ships to users) and add a CLAUDE.md rule that Claude flags any change touching them and waits for your approval.

## Why it matters

The author's advice is to let AI carry everything else and monitor the outcome, but to spend extra care on hot zones. (Inference) Without a standing rule, Claude treats a payment flow like any other file.

## How to apply

Use a prompt (the video shows one on screen) to have Claude help you identify your hot zones. Add to CLAUDE.md: anytime I am working on a hot zone, flag it and make sure I approve. For a hot zone, also build a minimum viable eval: the input you change, a program Claude writes that runs a suite of tests, and a report of how the input did.
