---
id: start-research-prompts-with-short-broad-searches-then-narrow
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/everyone-ignore-these-claude-concepts-but-they-change-everything_6VjeXzvpoJo_20261120.txt
---

# Tell Claude to start with short, broad searches and narrow down, and size the effort to the question

## TL;DR

For research or any find-me-options task, ask for broad short searches first, then a focused pass; do not open with one very specific question.

## Why it matters

Anthropic's multi-agent research write-up says agents often default to overly long, specific queries that return few results, and that they counteracted this by prompting agents to start with short, broad queries, evaluate what is available, then narrow. The video extends it to picking tools, content ideas or suppliers: list every option first, then compare the best three.

## How to apply

Prompt wording: use short, broad search terms first, see what is out there, then narrow; if a search comes up empty, go broader. Ask for the full list of options before the shortlist. Match the effort to the question: the write-up's rule of thumb is one agent with 3 to 10 tool calls for simple fact-finding, and more subagents and calls for comparisons and complex research.

Checked: Checked 2026-11-22: Anthropic engineering post 'How we built our multi-agent research system' contains 'prompting agents to start with short, broad queries, evaluate what's available, then progressively narrow focus' and, under 'Scale effort to query complexity', 'Simple fact-finding requires just 1 agent with 3-10 tool calls'. The video's 80% figure was not verified and is left out.
