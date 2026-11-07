---
id: run-checkup-doctor-to-audit-setup-health-and-context-bloat
created: 2026-07-17
status: active
supersedes: null
category: commands
sources:
  - transcripts/sean-kochel/5-claude-cheat-codes-only-the-top-1-use_7tX7YMLDJjM_20260716.txt
---

# Run /checkup (aka /doctor) to Audit Setup Health and Kill Context Bloat

## TL;DR

/checkup (also aliased /doctor) audits your MCP servers, agents, skills, plugins, and CLAUDE.md files against a battery of checks and quantifies how much context budget each extension eats, surfacing the globally-installed skills/plugins silently degrading routing before you start work.

## Why it matters

Globally-installed skills, plugins, and MCP servers load their name+description into every session; once skills/commands blow past their slice of the budget (~1% is the target), routing degrades, skills stop firing and the wrong tools get picked, and you burn plan quota fighting errors that shouldn't exist. /checkup catches this proactively instead of after performance craters.

## How to apply

Run /checkup (or /doctor) in a project. It reports general setup health (broken or dangling install/config files), unused extensions you can disable, CLAUDE.md quality (over-long lines, contradictions), and a context check quantifying each skill/plugin's budget cost. Findings are clickable to apply the fix (disable an unused extension, set auto mode as default). Pair it with /context (per-session usage breakdown) and a context-percentage statusline for live monitoring.

## Related

[[context-auditing-slash-context]]
