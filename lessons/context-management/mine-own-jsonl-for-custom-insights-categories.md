---
id: mine-own-jsonl-for-custom-insights-categories
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/mark-kashef/you-re-ignoring-the-two-best-features-in-claude-code_xssGpNx3its_20260704.txt
---

# Mine Your Own Session JSONL Instead of Only Reading /insights' Format

## TL;DR

Your Claude Code sessions are stored as JSONL files, so you can build fully custom usage categories and analytics directly from that data instead of being limited to /insights' built-in report format.

## Why it matters

/insights structures its report a particular way, but because the underlying session data is just JSONL, you can slice and categorize it however you actually want.

## How to apply

Point a script or a Claude session at your session JSONL files and have it extract and categorize whatever metrics matter to you, rather than relying solely on the /insights webpage's fixed sections.

## Related

[[mine-jsonl-transcripts-for-model-behavior-playbook]]
