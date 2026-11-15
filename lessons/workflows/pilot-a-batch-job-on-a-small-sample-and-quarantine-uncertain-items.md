---
id: pilot-a-batch-job-on-a-small-sample-and-quarantine-uncertain-items
created: 2026-11-15
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/i-tested-14-uncensored-ais-this-one-let-me-do-anything_uox59Sj4z4k_20261112.txt
---

# For a bulk file job, make the agent show a small sample, write copies elsewhere, and quarantine uncertain items

## TL;DR

Before an agent runs over thousands of files, have it process a small sample for your approval, write approved copies to a separate location, list each decision, and park uncertain ones for review.

## Why it matters

The author organised about 10,000 photos by person using reference photos. He ran that job on an uncensored DeepSeek model after Claude refused to identify faces, with these safeguards: copies elsewhere, a per-file list, a quarantined short list and a small sample first. He gives hallucination risk as the reason to build a clone in a separate folder.

## How to apply

Prompt the agent to: use reference examples for each category, write organised copies elsewhere instead of moving originals, list each file name with what it assigned, move uncertain cases to a short list for your approval, and show a small sample first, running the remainder only after the sample passes. For clones or rewrites, also ask it to build in a separate folder from the original and test itself against the original.

