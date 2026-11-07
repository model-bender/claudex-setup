---
id: blind-test-a-claude-md-change-with-naive-subagents
created: 2026-09-13
status: active
supersedes: null
category: agents
source_type: post
tool: claude-code
sources:
  - https://registerspill.thorstenball.com/p/joy-and-curiosity-99
---

# Prove a New CLAUDE.md Rule Is Discoverable by Spawning Subagents Who Were Not Told About It

## TL;DR

After adding a rule or a tool pointer to CLAUDE.md, spawn fresh subagents, give them an ordinary task that should surface it, and check whether they used it unprompted.

## Why it matters

Re-reading your own prose cannot tell you whether an instruction is findable, and a plausible-but-undiscovered rule fails silently: the file looks right and nothing uses it. This turns discoverability into an empirical check with a pass or fail.

## How to apply

Edit the instruction file, then spawn subagents with no mention of the change and a task that would naturally require it. If they do not reach for it, rewrite the instruction, not the agent, and spawn fresh ones again. Use fresh subagents rather than forks, since a fork inherits the context that would give the answer away.

> "Go and spawn three other agents in three separate orbs and ask them to test this. Obviously, do not tell them that we changed the AGENTS.md file or that we added this tool to test database performance; just ask them to do something", Thorsten Ball
