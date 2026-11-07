---
id: keep-client-deliverables-in-a-client-facing-repo-referenced-by-path
created: 2026-08-31
status: active
supersedes: null
category: memory
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/5-hacks-to-instantly-level-up-your-ai-os_Ek1NBfnnTH0_20260724.txt
---

# Segment Client Records Per Client and Keep Deliverables in a Separate Client-Facing Repo Referenced by Path

## TL;DR

Keep the internal record of each engagement (dates, scope, call notes, pricing) in one folder per client inside your own knowledge base, but store the deliverables in a separate client-facing repo and reference its path, so pushing your own repo never drags client deliverables along.

## Why it matters

Mixing deliverables into your personal knowledge base means every push of your own repo risks shipping client work with it. Per-client folders keep the internal record segmented and findable, and the recorded path still lets the agent navigate to the deliverables when a task genuinely needs them.

## How to apply

Create one folder per client inside your own knowledge base holding engagement dates, scope, call notes, and pricing. Put the actual deliverables in a dedicated client-facing repository, and record that repo's path in the client's folder so the agent can reference it on demand instead of duplicating the content.

## Related

[[split-a-growing-knowledge-store-into-per-feed-wikis]]
