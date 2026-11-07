---
id: let-idle-compaction-shrink-a-200k-conversation-or-turn-it-off
created: 2026-10-19
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21299
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21302
---

# Expect Idle Compaction on a 200K+ Session Left for About 54 Minutes, and Turn It Off Where You Need the Full History

## TL;DR

Since 2.1.299 a terminal conversation over 200K tokens that sits idle for about 54 minutes is compacted before its one-hour prompt cache expires, so plan for a compaction notice when you come back, or switch it off for that session.

## Why it matters

Without it, the first message after a long break reprocesses the whole conversation uncached. With it, a long run you return to has lost detail to a summary, which matters for work that waits on you (a decision sheet, a review) and counts toward the compactions you tolerate in one session.

## How to apply

Leave it on for ordinary sessions. To keep full history, use the `Idle compaction` row in `/config` (2.1.302), set `"idleCompaction": false` in settings.json, or raise the floor with `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS`. Checked: `idleCompaction` 9 hits and `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` 6 hits in the 2.1.303 binary.

> "Added idle compaction in the terminal: a 200K+ token conversation left idle for about 54 minutes is compacted before its one-hour prompt cache expires, so your next message doesn't reprocess it all", Claude Code CHANGELOG 2.1.299

## Related

[[prompt-cache-is-one-hour-on-subscription]]
