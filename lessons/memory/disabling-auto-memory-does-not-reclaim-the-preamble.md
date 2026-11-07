---
id: disabling-auto-memory-does-not-reclaim-the-preamble
created: 2026-07-25
status: active
supersedes: null
category: memory
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/issues/63903
---

# `autoMemoryEnabled: false` Does Not Reclaim the Memory Preamble: Verify With `/context`

## TL;DR

Turning off auto-memory stops the writes but still loads the hardcoded memory preamble into every session's system prompt, even with an empty memory directory.

## Why it matters

The usual advice is to disable built-in auto-memory if you run your own memory system, on the reasoning that you stop paying for redundant work. The context cost does not actually go away, and for a custom routing system the preamble actively suggests routes you don't want taken. So you get the instruction pollution without the feature.

## How to apply

After setting `autoMemoryEnabled: false`, run `/context` on a fresh session and read the "Memory files" bucket before assuming the budget was freed. **REVISIT: the reported figures (~11.3k tokens on Sonnet, ~16.2k on Opus) were measured on 2.1.149 and the "still reproducible" confirmations come from a single commenter keeping the issue off the staleness bot**, treat the numbers as indicative and measure locally rather than quoting them.

> "Setting `autoMemoryEnabled: false` in `~/.claude/settings.json` correctly disables auto-memory writes and stops Claude from attempting them, but the hardcoded memory preamble (instructional text + \"currently empty\" branch + formatting templates) still loads into the system prompt at session start.", anthropics/claude-code issue #63903

## Related

[[be-a-context-minimalist-provision-a-lean-harness]], [[context-auditing-slash-context]]
