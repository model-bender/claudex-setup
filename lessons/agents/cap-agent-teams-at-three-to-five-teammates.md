---
id: cap-agent-teams-at-three-to-five-teammates
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
---

# Start Agent Teams at 3-5 Teammates: Token Cost Scales Roughly Linearly Per Teammate

## TL;DR

Running more than 3-4 teammates at once starts to feel like overkill because token spend scales close to linearly with headcount, even though nothing technically stops you from spawning more.

## Why it matters

It's easy to over-provision an agent team the same way you'd over-hire a project team, but each extra teammate is a full parallel Claude Code instance burning tokens the whole time it's active.

## How to apply

Default new agent teams to 3-5 teammates; only add more once you've confirmed a specific need justifies the extra token spend.

## Related

[[cap-parallel-subagent-concurrency-with-max-concurrent-subagents]]
