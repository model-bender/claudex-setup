---
id: replace-hard-limits-with-follow-the-surrounding-style
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/anthropic-engineers-just-10x-d-everyone-s-claude-code_oz2CwrPV2Rg_20261009.txt
---

# Swap fixed caps in your instructions for 'follow the style of the surrounding code'

## TL;DR

Where an instruction sets a hard limit (the transcript's example is how many comments Claude may write), replace it with a rule that tells Claude to match the conventions of the code around it.

## Why it matters

As reported in the transcript, Claude Code's own system prompt used to put a hard limit on how much Claude could write in comments even though some projects needed more explanation, and Anthropic replaced it with an instruction to follow the surrounding code's style. A fixed cap is wrong for some projects; a relative rule adapts.

## How to apply

Search your CLAUDE.md and skills for numeric or absolute caps on output and rewrite them as 'follow the style of the surrounding code' or the equivalent for the artefact in question. The replacement line, as write-ups of the article quote it: "Write code that reads like the surrounding code: match its comment density, naming, and idiom."

Checked: No mechanism named. The transcript attributes the example to an Anthropic engineer's article; a web search identified it as Thariq Shihipar's "The new rules of context engineering for Claude 5 models" (X, 2026-07-24). The original was not fetched, but two write-ups fetched with curl on 2026-11-22 (mager.co and claudefa.st) quote the same old rule ("default to writing no comments", "one short line max") and the same replacement line.

## Related

[[soften-absolute-rules-until-they-are-true-every-time]]
