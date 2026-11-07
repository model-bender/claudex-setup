---
id: put-long-reference-documents-before-the-question
created: 2026-09-24
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/give-me-20-minutes-i-will-make-you-a-claude-pro_-URQjhtvxZo_20260920.txt
---

# Place long reference documents above your question, not after it

## TL;DR

For long-context prompts (roughly 20k tokens or more: a transcript, a spec, a spreadsheet pasted into a session), put the document near the top and your question and instructions at the bottom. Anthropic's docs report that queries at the end can improve response quality by up to 30 percent.

## Why it matters

Instructions-first reads more naturally, so most people write prompts that way. The docs say the reverse order measurably helps, especially with complex, multi-document inputs, which is exactly what a pasted spec plus logs plus a question looks like.

## How to apply

When a prompt carries a large pasted document, paste it first (wrapped in its own tags if there are several), then write the question and instructions last. Checked against Anthropic's long-context tips page, now at platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips (the docs.claude.com URL redirects), fetched 2026-09-24: "Put longform data at the top ... This improves performance across all models" and "Queries at the end can improve response quality by up to 30 percent in tests, especially with complex, multidocument inputs."
