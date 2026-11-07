---
id: use-agent-swarms-only-for-independent-search-tasks
created: 2026-11-06
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/openai-and-anthropic-agree-on-what-comes-after-loops_yrRpnx_iugY_20261106.txt
---

# Use a Coordinated Agent Swarm for Independent Search Work Like Bug and Vulnerability Hunting, Not for Building

## TL;DR

Ray cites an Anthropic result where a coordinated swarm found 266 vulnerabilities for 27 million tokens versus 21 for 6.5 million with simple parallel fan-out. Anthropic's swarms failed at building working apps, and a YC Minecraft run with an open-ended goal also failed.

## Why it matters

Bug hunting is independent work, so more agents help. Building an application is tangled work, where agents get on each other's toes. His own factory with roles and personas started fast then stalled on rules and messaging, like the Minecraft agent experiment he cites.

## How to apply

1. Fan out only truly independent tasks: comparing 5 libraries, one agent per codebase area for bug hunts, bug bashing.
2. Do not run builder, QA, security and ops personas as a standing team of personas on current models.
3. Keep implementation in one agent.

Inference, not from the source: Neither Ray nor Anthropic measured swarms against single agents on everyday Claude Code build tasks; the build-side advice rests on Ray's persona-factory trial.

