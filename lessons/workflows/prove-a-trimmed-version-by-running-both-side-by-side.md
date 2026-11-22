---
id: prove-a-trimmed-version-by-running-both-side-by-side
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-built-another-andrej-karpathy-using-claude_bvGptCLDhyo_20261009.txt
---

# Prove a trimmed script is equivalent by running old and new side by side

## TL;DR

When the agent simplifies or cuts code, have it run the original and the trimmed version on the same input and show both results.

## Why it matters

In the demo the reviewer cut what was not needed, then showed the trimmed version catches the same items as the original, so the cut is backed by evidence.

## How to apply

Add to the review instructions: after any cut, run both versions on the same data and show the outputs together.

Checked: No mechanism named.

