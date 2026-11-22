---
id: measure-reviewer-noise-by-how-people-respond-to-comments
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# Measure reviewer noise by sorting its comments by how the author responded

## TL;DR

Classify every reviewer comment by outcome: fixed, said it was wrong, said the behaviour was intentional, or decided it does not matter.

## Why it matters

The article's point: it is easy to catch more bugs if you do not mind flagging a lot of non-bugs, so recall has to be read next to what people did with the comments.

## How to apply

Periodically tally resolved review threads into the four buckets. Tuning the reviewer instructions when the non-fixed share grows is this lesson's inference; the article only says it measures noise this way.

Checked: No mechanism named.

