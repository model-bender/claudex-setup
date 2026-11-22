---
id: press-f-in-usage-to-have-claude-apply-the-recommendations
created: 2026-11-22
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-pros-don-t-pay-for-max-they-do-these-5-things-instead_ZRKAw472Nmk_20261108.txt
---

# Press f in /usage to have Claude Code apply the recommendations it can

## TL;DR

When /usage shows recommendations, press f and Claude Code acts on the ones it can.

## Why it matters

It turns the audit into the fix without you writing the prompt.

## How to apply

/usage, look for a footer hint such as 'f to fix 2 of 3', press f. Rows ending in 'run <command>' are not applied; run those yourself.

Checked: Live docs at code.claude.com fetched with curl on 2026-11-22, costs page, 'Apply recommendations with the fix shortcut': requires Claude Code v2.1.305 or later; it runs /effort rows directly and gives Claude one prompt for the other rows, asking it to show each change first; no f hint while Remote Control is connected. Installed version is 2.1.330.

## Related

[[run-checkup-doctor-to-audit-setup-health-and-context-bloat]]
