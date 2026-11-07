---
id: prompt-cache-is-one-hour-on-subscription
created: 2026-07-17
status: active
supersedes: null
category: context-management
sources:
  - transcripts/nate-herk-ai-automation/claude-code-for-non-coders-6-hour-course_jdbOVepEtUE_20260712.txt
---

# On a Subscription, Claude Code's Prompt Cache Lasts ~1 Hour: the 5-Minute Figure Is the API/Subagent Default

## TL;DR

The widely-repeated "5-minute prompt-cache window" is the API's ephemeral default (also what subagents get); a Claude Code session on a subscription keeps its cache warm for ~1 hour, so an idle gap under an hour still resumes at the ~10% cached-input rate instead of re-billing the whole context.

## Why it matters

The 5-minute number made people think a short break nuked their cache and spiked usage, so they'd rush follow-ups or needlessly abandon sessions. On a subscription that's wrong: the real TTL is roughly an hour, which changes when a session is genuinely stale (hand it off) versus cheaply resumable, and on a 150k+ token session, paying full rate to reprocess is brutal, so the distinction matters. The 5-minute default still applies on API billing and to subagents (raisable to an hour at a higher cache-write cost).

## How to apply

On a subscription, resume within ~1 hour to keep cache hits; only past an hour is it worth a handoff (summarize open decisions/files → `/clear` → paste the summary into a fresh session) rather than reviving an expired cache. On API billing, or when spawning subagents, treat 5 minutes as the window, or extend the ephemeral TTL to 1h if the higher cache-write cost is worth it. Independently of the timer, avoid mid-session model switches and CLAUDE.md edits, which bust the cache regardless.

## Related

[[prompt-cache-what-breaks-it]], [[context-rot-prevention-compact-proactively]]
