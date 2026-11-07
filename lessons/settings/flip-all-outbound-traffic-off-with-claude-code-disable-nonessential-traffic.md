---
id: flip-all-outbound-traffic-off-with-claude-code-disable-nonessential-traffic
created: 2026-09-12
status: active
supersedes: null
category: settings
tool: claude-code
sources:
  - transcripts/simon-scrapes/12-hidden-tricks-that-unlock-claude-code_M2p7OvKLAWw_20260710.txt
---

# Set CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 Instead of Listing Every Opt-Out Key

## TL;DR

Rather than setting DISABLE_TELEMETRY, DISABLE_ERROR_REPORTING and the rest one by one, CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 turns the whole non-essential outbound bundle off with one env key.

## Why it matters

Enumerating the flags means your confidentiality posture is only as complete as the last time you checked the list: a telemetry or reporting channel added in a later release is not covered by the keys you already wrote, and nothing warns you. One umbrella key stays correct across upgrades.

## How to apply

In the env block of ~/.claude/settings.json (or the project settings file for a single client repo) set CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC to 1 rather than enumerating individual disable keys, then confirm on a fresh session that nothing non-essential still dials out.

## Related

[[quiet-mode-env-vars-for-client-and-confidential-work]], [[disable-nonessential-traffic-also-turns-off-projects-and-claude-design]]
