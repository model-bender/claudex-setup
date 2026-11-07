---
id: wire-the-org-wiki-in-and-tell-claude-to-flag-contradictions
created: 2026-07-25
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Connect the Product Wiki and Add a Rule to Consult It: and Stop When It Contradicts You

## TL;DR

Reading the codebase only tells the agent what already exists, not what's coming. Add the wiki as a connector and put a CLAUDE.md rule in that tells exploring subagents to read it, plus an explicit instruction to ask for clarification when the wiki and your request disagree.

## Why it matters

Autonomy is bounded by how much context the agent can pull for itself, and decisions and upcoming features live in Notion, not in code. An agent without wiki access makes locally-correct choices that conflict with work already planned. The contradiction clause is the load-bearing half: without it the agent silently picks one source, and a wrong silent pick is worse than a question, you only find out at review. Note also that adding a connector merely makes the wiki *reachable*; the agent won't consult it until a rule reminds it the wiki exists.

## How to apply

Add the wiki's connector at the account or organization level on claude.ai (Notion, or whatever you use). Then add a CLAUDE.md rule of roughly this shape: when exploring in a subagent, read the product wiki via the MCP, a lot of information about upcoming features lives there; if you find a contradiction between what the user told you and the wiki, ask for clarification before continuing. Scope it to the exploration subagent so wiki content doesn't sit in the main context.

## Related

[[team-agentic-os-shared-context-folders]]
