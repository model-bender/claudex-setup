---
id: fan-out-research-subagents-by-data-source
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
---

# Assign Each Research Subagent Its Own Data Source When Mining for Pain Points

## TL;DR

When researching a product idea from scratch, give each parallel subagent a distinct data source (owned community, YouTube comments, Reddit, X) rather than one subagent covering everything, then consolidate at the end.

## Why it matters

The creator's ideation prompt explicitly split research this way: 'I want you to use our primary data which could be things like YouTube comments, people talking in our school community... but then also I want you to go on more of the publicly accessible data like secondaries forums of Reddit, LinkedIn X, Instagram... spin up different sub agents, and I want you to do research, scrape different methods, and then at the end, come back, consolidate everything.' The result was five parallel research agents each pulling from a different source (YouTube API, community, X, Firecrawl, Perplexity) before one consolidation pass.

## How to apply

When briefing an orchestrator for open-ended research, enumerate the data sources explicitly and tell it to spin up one subagent per source (rather than one subagent per hypothesis), then have the orchestrator do a single consolidation pass across all of them.

