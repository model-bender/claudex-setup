---
id: monitor-watches-expire-at-30-minutes-and-can-drop-events
created: 2026-09-24
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Monitor Watches Now Auto-Expire at ~30 Minutes and Can Drop Events in the Re-Arm Gap

## TL;DR

The Monitor tool's `persistent: true` option (no-timeout background watching) was replaced with a hard ~30-minute deadline that requires Claude to notice the expiry and re-arm; GitHub issue #94393 shows the re-arm has a gap where events from an external process can be lost entirely, not just delayed.

## Why it matters

The old lesson in this library says "For persistent watches: specify persistent: true", that no longer holds. Worse, per reporters (issue #94393, corroborated by multiple users through 2026-09-16), the schema still validates timeout_ms up to 3600000 (1 hour) and rejects higher, but the tool's own confirmation text and actual behavior cap the real lifetime at ~30 minutes regardless of what you request, and a user with log-tailing monitors reports "As of 2.1.268 that premise breaks... When a watch expires and re-arms, anything the external process appends during the teardown/re-arm window is never delivered. There's no way for the monitor to 'catch up.'"

## How to apply

Don't build a Monitor watch that assumes it runs unattended for hours; expect a ~30-minute (10-minute in -p) forced expiry with a one-time notice, and know that a fast-moving external log/event source can produce writes during the re-arm window that the watch will never see. For anything that must not miss events, poll or re-establish state on each re-arm rather than assuming continuity.

> "Changed Monitor watches to always have a deadline (at most 30 minutes; 10 in single-prompt `-p` runs) and notify Claude to re-arm, replacing the no-timeout `persistent` option", Claude Code CHANGELOG 2.1.271
