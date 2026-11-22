---
id: review-md-require-file-and-line-evidence
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# Make the reviewer cite a file and line as evidence instead of guessing from a name

## TL;DR

Add an instruction that a behaviour claim needs a file:line citation, not an inference from how something is named.

## Why it matters

The article lists it among what good REVIEW.md files ask for. Per the docs, the instruction cuts false positives that would otherwise cost the author a round trip.

## How to apply

In `REVIEW.md` (or any reviewer subagent prompt): 'behavior claims need a file:line citation in the source, not an inference from naming'.

Checked: Code-review-customize.md (live docs at code.claude.com fetched 2026-11-22) gives the same instruction as its example for cutting wrong findings. REVIEW.md is read only by the managed Code Review service; the reviewer-subagent use is this lesson's extension.

## Related

[[tag-reverse-engineering-findings-as-seen-inferred-or-unknown]]
