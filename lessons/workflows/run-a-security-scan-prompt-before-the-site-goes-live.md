---
id: run-a-security-scan-prompt-before-the-site-goes-live
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-fable-5-2-built-my-website-here-s-how-to-actually-put-it-online_usOWZyFSxsA_20261120.txt
---

# Before a Claude-built site goes live, ask Claude on the server for a full security scan: exposed keys and server lockdown

## TL;DR

Ask Claude on the server to scan for anything personal such as API keys sitting in the open, and to check that the server itself is locked down. Do it before launch.

## Why it matters

The creator forgot and ran it the morning after launch. The scan found no leaked keys, but it found the server was not locked down and 20 security updates were pending. The creator then typed "fix it all", and the fixes included adding fail2ban to block repeated wrong-password attempts.

## How to apply

Prompt: run a full security scan to make sure that there's nothing personal, like API keys sitting in the open, and then make sure that the server's locked down. Review the findings, then tell it what to fix.

Checked: No Claude Code mechanism named (fail2ban is a third-party Linux tool, transcribed as 'fail to ban').

## Related

[[anchor-a-prelaunch-security-audit-to-a-named-standard]]
