---
id: keep-sibling-agent-prompt-prefixes-identical-to-share-the-cache
created: 2026-08-31
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Keep Parallel Sibling Agents' Prompt Prefixes Identical So They Share One Prompt Cache

## TL;DR

In a fan-out, the first agent writes the prompt cache and same-prefix siblings read it; divergent per-agent preambles mean every agent pays full input cost on the most expensive part of the fan-out.

## Why it matters

N simultaneous agents with an identical prompt prefix cost one cache write plus N-1 cheap cache reads, while N slightly different prefixes cost N full-price cache misses. The prefix is therefore a direct token-cost multiplier on parallel work, and it is easy to defeat by accident with per-agent customization that adds little value. This holds regardless of any stagger or launch timing knobs.

## How to apply

When designing a fan-out, put everything shared (system prompt, instructions, reference material) in an identical prefix across the sibling agents and push the per-agent differences to the end of the prompt. Avoid customizing each agent's preamble, since divergent preambles leave no shared prefix worth caching.

## Related

[[never-zero-the-workflow-prefix-stagger]]
