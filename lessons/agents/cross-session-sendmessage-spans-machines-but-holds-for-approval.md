---
id: cross-session-sendmessage-spans-machines-but-holds-for-approval
created: 2026-08-07
status: active
supersedes: null
category: agents
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Don't Assume Cross-Session SendMessage Auto-Delivers to a Bypassed-Permissions Session

## TL;DR

`SendMessage` and `ListAgents` now work across separate Claude Code sessions on any of your machines (macOS and Linux), but a message aimed at a session running with bypassed permissions is held for your approval rather than delivered.

## Why it matters

The default is asymmetric, and the asymmetry lands exactly where it hurts: messages to ordinary sessions auto-deliver, but the bypassed-permissions session (the one most likely to be running unattended) queues its inbound messages behind a dialog. A pipeline that assumes instant delivery stalls silently, waiting on an approval nobody is watching for.

## How to apply

Discover remote sessions with `ListAgents`. If a target session runs with bypassed permissions and the pipeline needs instant delivery, tune the `crossSessionInbound` and `dialogExpiry` settings rather than assuming the default. Also note that failed deliveries are now reported as errors instead of a false "Message sent", so trust the error but not the silence.

> "Added `crossSessionInbound` and `dialogExpiry` settings: cross-session messages sent to a session running with bypassed permissions are held for your approval, and messages to other sessions auto-deliver", Claude Code CHANGELOG 2.1.224

## Related

[[supervisor-agent-unblocks-worker-agents-and-escalates-by-exception]]
