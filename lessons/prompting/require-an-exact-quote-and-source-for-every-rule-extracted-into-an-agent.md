---
id: require-an-exact-quote-and-source-for-every-rule-extracted-into-an-agent
created: 2026-10-11
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-built-another-andrej-karpathy-using-claude_bvGptCLDhyo_20261009.txt
---

# Require an exact quote and source for every rule you distil from a person's material into an agent

## TL;DR

When Nate built a teaching agent from Karpathy's writing, each rule had to link to an exact quote and where it came from, and the agent must say when it is inferring.

## Why it matters

It stops Claude making rules up and lets you click through to the source page or timestamp. A rule with one source stays on a bench until a second source arrives.

## How to apply

Prompt the rule-extraction step: each rule needs a verbatim quote plus a source reference, and if there is no source say explicitly that it is inferred. Output the rules as a subagent file and a slash-command skill (his were /karpathy-teach and /karpathy-ingest).

## Related

[[markdown-wiki-knowledge-base-over-vector-rag]], [[split-a-claude-owned-wiki-from-a-read-only-raw-source-folder]]
