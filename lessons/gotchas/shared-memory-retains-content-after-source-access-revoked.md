---
id: shared-memory-retains-content-after-source-access-revoked
created: 2026-08-07
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/this-setup-gives-your-team-the-same-claude-memory-steal-it_PzaC81yCJg0_20260807.txt
---

# A Memory Add-On Keeps Its Own Copy, So Revoking Source Access Later Removes Nothing

## TL;DR

A memory add-on that auto-captures whatever context a session pulled in, including content fetched from a permissioned source like Notion, keeps that as its own permanent copy. Revoking someone's Notion access afterward does not remove what they can still recall through memory. On a team plan the workspace admin can typically see every user's personal memories too.

## Why it matters

Teams that treat "restrict access in Notion" as the access-control boundary are wrong once a memory layer sits in front of Claude. Once memory has ingested a document, memory is a second, un-revocable copy of it. Capture happens automatically at end of session with no personal-versus-shared split by default, which makes this a security blind spot rather than a setup detail.

## How to apply

- Before enabling auto-capturing shared memory, treat any document a teammate might read as effectively permanent once accessed. Do not rely on later permission changes elsewhere to restrict it retroactively.
- Keep genuinely sensitive or client-confidential work in folders and sources you never open in a memory-enabled session.
- Tell teammates the workspace admin can see all personal memories, not just the shared team container, before anyone treats their own memory as private.

## Related

[[supermemory-container-tag-for-shared-team-memory]], [[harden-always-on-agents-least-privilege-and-capable-models]]
