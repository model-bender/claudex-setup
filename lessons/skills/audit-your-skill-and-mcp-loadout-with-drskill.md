---
id: audit-your-skill-and-mcp-loadout-with-drskill
created: 2026-08-07
status: active
supersedes: null
category: skills
tool: claude-code
source_type: post
sources:
  - https://www.dbreunig.com/2026/07/24/manage-your-agent-s-loadout-with-dr-skill.html
---

# Audit Your Skill and MCP Loadout With drskill Before It Silently Degrades Routing

## TL;DR

Skills and MCP servers accumulate invisibly. `drskill` inventories what a given harness actually loads, scans for 34 issue categories, LLM-judges overlap between skills, and audits traces for what you never use.

## Why it matters

Breunig found an enterprise agent auto-loading 600+ skills inherited from colleagues, and his own agent loading a duplicate note-taking skill out of a stock bundle of about 100. Nobody chose that loadout; it accreted. Every description competes for routing attention, so the cost shows up as worse tool selection rather than an error you can trace.

## How to apply

Install with `uv tool install drskill` (or `pip install drskill`). Run `drskill list --harness claude-code` to see exactly what Claude Code loads, `drskill scan` for the 34 issue categories, `--deep` to have an LLM judge distinctness and overlap between skills, and `drskill audit` against session traces to find skills that load but never fire.

> "looks for 34 different issue categories, across MCPs and Skills", Drew Breunig

## Related

[[run-checkup-doctor-to-audit-setup-health-and-context-bloat]], [[curate-a-bulk-skill-pack-before-installing-not-after]], [[skills-complementary-not-overlapping]]
