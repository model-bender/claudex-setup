---
id: accept-the-resume-from-summary-offer-on-stale-sessions
created: 2026-09-12
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Accept the Resume-From-Summary Offer on Big Stale Sessions

## TL;DR

Resume a session older than an hour that burned over 100k tokens and Claude Code stops before your first message to offer resuming from a summary instead. Take the offer.

## Why it matters

Resuming a session that size rereads the entire conversation history uncached, which the video calls the most expensive single request you can make, and you were going to have to refresh that context window anyway.

## How to apply

When the prompt appears on /resume, choose 'resume from summary' rather than the full session. Reserve a full resume for sessions still inside the cache window where the exact wording of earlier turns matters.

## Related

[[sessionstart-resume-hooks-receive-staleness-and-recache-cost]], [[prompt-cache-is-one-hour-on-subscription]], [[compact-inside-the-cache-window-not-after-it-expires]]
