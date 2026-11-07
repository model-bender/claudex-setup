---
id: track-per-layer-decay-cadence-in-a-rot-md-file
created: 2026-09-24
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-to-actually-choose-the-right-ai-agent_6LNlCpQPYFc_20260920.txt
---

# Track Each Setup Layer's Decay Rate in a rot.md File to Set Its Own Audit Cadence

## TL;DR

Different layers of a personal Claude Code or agent setup go stale at very different speeds. Write an assumed refresh cadence per layer, identity and core context every 1-3 months, skills monthly, rules weekly, hooks around every 6 months, into a dedicated rot.md file, and audit each layer on its own schedule instead of one blanket review.

## Why it matters

Treating every part of a setup as equally due for review either under-audits the fast-decaying layers (skills and rules shift as soon as you hit a new edge case) or wastes effort re-reviewing the stable ones (identity, hooks). Writing the assumed decay rate down per layer turns 'I should probably review this sometime' into an actual schedule, and makes it visible when a layer is overdue.

## How to apply

Create a rot.md at the root of your setup. List each layer, identity/substrate, skills, rules, hooks, agents, with the cadence you expect it to need refreshing on, and the date you last reviewed it. Revisit each layer on its own listed cadence rather than doing one pass over everything at once.

## Related

[[split-aios-context-into-expertise-and-situational]], [[prune-skill-learnings-file-on-a-fixed-cadence]]
