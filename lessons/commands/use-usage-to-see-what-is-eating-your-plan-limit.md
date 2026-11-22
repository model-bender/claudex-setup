---
id: use-usage-to-see-what-is-eating-your-plan-limit
created: 2026-11-22
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-pros-don-t-pay-for-max-they-do-these-5-things-instead_ZRKAw472Nmk_20261108.txt
---

# Run /usage to see which skills, subagents, plugins and MCP servers are using your limit

## TL;DR

Before concluding that limits were cut, run /usage. On Pro or Max it attributes recent usage to skills, subagents, plugins and MCP servers.

## Why it matters

It replaces guessing which habit costs the most with a measured breakdown.

## How to apply

Run /usage and read the attribution shares. Press w to see the last 7 days (the video's tip) or d for the last 24 hours (from the docs check).

Checked: Live docs at code.claude.com fetched with curl on 2026-11-22, costs page, 'Plan usage breakdown': on Pro, Max, Ultra, Team or Enterprise, /usage attributes recent usage to skills, subagents, plugins and individual MCP servers. The figures come from local session history on this machine only. /usage present in Claude Code 2.1.330 installed binary.

## Related

[[ask-for-a-subagent-only-when-output-is-huge-and-name-what-it-returns]], [[run-checkup-doctor-to-audit-setup-health-and-context-bloat]]
