---
id: wrap-agent-pr-descriptions-in-details-under-a-human-opener
created: 2026-11-15
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
source_type: post
sources:
  - https://simonwillison.net/2026/Nov/9/details-summary/
---

# Wrap the agent-written PR description in details/summary under a short human-written opener

## TL;DR

Open the PR description with a short paragraph you curated, plus a screenshot if useful. Put the full agent-written text inside <details><summary>, with the model name and effort level as the summary line.

## Why it matters

His stated reason: "I want human editorial judgement." Agent PR descriptions are accurate but read as slop, so reviewers skip them, and the collapsed block keeps the detail without the wall of text. GitHub Markdown renders these tags in PR and issue comments.

## How to apply

Have the agent emit its long description inside a <details><summary>Claude Opus 5.5 Medium</summary> ... </details> block, then write or approve the opener above it yourself.

> "I use the model name and often the effort level as that summary, to make it abundantly clear what is going on", Simon Willison

## Related

[[read-the-agent-written-pr-description-before-you-make-anyone]]
