---
id: skill-scripts-run-without-loading-their-source-into-context
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everything-you-know-about-skills-is-outdated_e7TY56-yIvM_20261002.txt
---

# Put exact steps in skill scripts because only their output costs context

## TL;DR

Claude runs a skill's script through bash and does not read the script into context, so only the output uses tokens.

## Why it matters

Simon Scrapes notes that scripts in a skill get run rather than read into memory, so Claude spends no context on the script body. That makes a script both the consistent option for fragile steps and a cheap one.

## How to apply

Keep a scripts/ folder next to SKILL.md. In the skill steps, tell Claude to run the script and use its output, rather than pasting the same logic into the instructions.

Verified: Anthropic skill best practices page, fetched 2026-10-02: 'Utility scripts can be executed through bash without loading their full contents into context. Only the script's output consumes tokens.'

## Related

[[skills-add-scripts-to-avoid-repeated-api-scaffolding]]
