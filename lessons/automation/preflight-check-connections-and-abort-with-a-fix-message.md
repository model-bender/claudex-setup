---
id: preflight-check-connections-and-abort-with-a-fix-message
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/austin-marchese/6-easy-steps-to-automate-99-of-your-life-with-claude_ktY1b2-OKRA_20260910.txt
---

# Make Every Automation Check Its Connections First and Abort With the Fix

## TL;DR

Open each automation skill with a pre-flight check that every connector, key and path it needs is live. If one is missing, stop immediately and report exactly what to reconnect, instead of running the job without it.

## Why it matters

Austin Marchese demonstrates both halves: with Slack disconnected, the unguarded version 'goes ahead and tries running without that connection even though it'll never actually work', burning the full run; the guarded version 'breaks essentially right away'. He calls this a self-breaking system and pairs it with self-correcting loops for a reason, an automation that fails late has already spent the tokens and, worse, may deliver a partial result that looks complete. The abort message matters as much as the abort: it turns a failed run into a one-line fix rather than an investigation.

## How to apply

Add a first step to the skill that asserts each dependency is reachable (connector authorised, file present, credential valid). On any failure, halt and emit a message naming the missing dependency and the exact action to restore it, then send that message through the same channel the run reports to. Apply it to every skill a routine invokes, not just the newest one.

## Related

[[explicit-numeric-receipts-for-automations]], [[guard-unattended-agent-runs-with-a-stall-watchdog-and-bounded-retry]], [[stop-and-diagnose-slow-unattended-automation]]
