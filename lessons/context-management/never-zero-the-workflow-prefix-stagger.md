---
id: never-zero-the-workflow-prefix-stagger
created: 2026-08-16
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Don't Set `CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS=0` - the Stagger Is What Buys the Cache

## TL;DR

Workflow fan-outs deliberately delay same-prefix sibling agents so the first one writes the prompt cache and the rest read it; zeroing the stagger to "launch faster" makes every sibling pay full input cost.

## Why it matters

The intuitive optimization is backwards. N simultaneous agents with an identical prompt prefix means N cache misses, so the knob that looks like a latency win is a direct token-cost multiplier on the most expensive part of a fan-out. This also explains the visible pause at the start of a parallel wave - that pause is the cache being populated, not the tool being slow.

Anyone who saw the stagger, assumed it was overhead, and set it to `0` made their fan-outs cost more while feeling faster.

## How to apply

Leave `CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS` unset. Only ever raise it, never set `0`. Keep sibling agents' system-prompt prefixes identical so there is a shared prefix worth caching in the first place - divergent per-agent preambles defeat the mechanism regardless of the stagger.

> "Improved workflow fan-outs to stagger same-prefix sibling agents so subsequent agents read the cached prompt prefix instead of re-paying it (`CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS=0` disables)", Claude Code CHANGELOG 2.1.229

## Related

[[prompt-cache-what-breaks-it]], [[keep-sibling-agent-prompt-prefixes-identical-to-share-the-cache]]
