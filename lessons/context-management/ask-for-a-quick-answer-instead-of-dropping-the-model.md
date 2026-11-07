---
id: ask-for-a-quick-answer-instead-of-dropping-the-model
created: 2026-09-12
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Append 'Give Me a Quick Answer' Instead of Downgrading the Model for One Question

## TL;DR

For a throwaway question deep in an expensive session, add 'give me a quick answer' to the prompt. The model skips the deep reasoning for that one turn and the prompt cache is never touched.

## Why it matters

The instinct is to drop from Opus 5 to a smaller model or lower the effort dial for the cheap question, but both rebuild the whole cached prefix, so you pay to re-cache everything when you switch back. The in-prompt instruction gets the same speed with no prefix change: the demo answered a date question in about a second while still on Opus 5.

## How to apply

Keep the model and effort dial where they are and put the instruction in the message: '<question>. Give me a quick answer.' Use a subagent instead when you need a genuinely different model for real work rather than a one-line answer.

## Related

[[spawn-a-subagent-instead-of-switching-model-mid-session]], [[prompt-cache-what-breaks-it]]
