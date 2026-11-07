---
id: chain-skills-with-condensed-handoff-summaries
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/simon-scrapes/the-easiest-way-to-get-ahead-with-claude-code_20260424.txt
---

# Chain Skills So Each One Hands the Next a Condensed Summary, Not Its Raw Work

## TL;DR

When one skill's output feeds another (e.g. research to content to repurposing), have the upstream skill do its heavy lifting in its own context and return only a clean, condensed summary, so the downstream skill's context stays unpolluted by raw intermediate data.

## Why it matters

Pasting a research skill's full raw output into a content skill's prompt hands it thousands of unneeded tokens, defeating context hygiene even though each skill individually is lean.

## How to apply

Design the handoff explicitly: have the upstream skill's final step produce a short structured summary (topics, angles, key facts) as its actual output, and have the downstream skill's SKILL.md instruct it to consume that summary rather than the raw research.

## Related

[[prune-exploration-output-before-it-feeds-the-plan]]
