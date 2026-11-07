---
id: scope-skills-per-project-not-globally-to-cut-startup-context
created: 2026-07-10
status: active
supersedes: null
category: configuration
sources:
  - transcripts/sean-kochel/15-claude-code-tricks-that-feel-like-cheating_qGAuqbbj1Ls_20260703.txt
  - transcripts/sean-kochel/7-claude-code-tools-to-stop-wasting-tokens_bhB57Meachc_20260703.txt
---

# Install Skills Per-Project, Not Globally: Every Skill's Description Taxes Session Startup

## TL;DR

Each installed skill/plugin loads its name and description into context at session start (so Claude can decide whether to invoke it), so a large global library silently taxes every session, install experimental or rarely-used skills into the specific projects that need them and audit the startup cost.

## Why it matters

One creator's global catalog of 82 skills loaded ~9k tokens of skill descriptions (and 30-40k total) into every session before the first prompt, pure overhead on unrelated work and a real driver of both cost and context rot; his runaway token usage traced back to bloated startup context.

## How to apply

Run a startup-context audit (a token-optimizer plugin fans out review agents over your CLAUDE.md, memory, skills, MCPs, custom commands, and settings/hooks and shows where the tokens go, or just use /context) to find the offenders, then move skills you're only testing or occasionally need out of the global catalog into per-project installs; this is the skills analog of choosing MCP servers selectively, and pairs with disable-model-invocation for manual-only skills.
