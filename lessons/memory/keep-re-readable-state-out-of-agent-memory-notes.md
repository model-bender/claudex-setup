---
id: keep-re-readable-state-out-of-agent-memory-notes
created: 2026-11-15
status: active
supersedes: null
category: memory
tool: claude-code
source_type: canonical
sources:
  - https://www.anthropic.com/research/components-of-agent-memory
---

# Keep state the agent can re-read each turn out of its memory notes

## TL;DR

Sonnet 3.7 saved everything, including money and map position. It wrote 413 memory files across 225 folders, earned one badge, and its notes kept going out of date. Fable 5 wrote nine files, kept only what it had worked out (strategy, plans, tested rules) and earned four badges.

## Why it matters

Memory of live state goes stale and costs time to search. Notes about what the agent derived itself, which vanish unless written down, are the only ones that pay off.

## How to apply

In memory instructions, say to store derived rules, plans and verified traps, and not facts available from the repo, git log or a command. Keep a small top-level index or dashboard file for current goal and plan.

> "can be read off the screen every turn, so storing it is redundant.", Anthropic, The components of agent memory

## Related

[[prune-auto-memory-regularly-or-it-rots]], [[memory-md-loads-only-200-lines-or-25kb-whichever-comes-first]]
