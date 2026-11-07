---
id: advisor-fails-after-any-prior-tool-use-not-above-a-token-count
created: 2026-07-25
status: active
supersedes: null
category: gotchas
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/issues/67609
---

# Don't Route Judgment Calls Through `/advisor` Mid-Session: Any Prior Tool Call Breaks It on Fable 5

## TL;DR

The Fable 5 advisor fails with `advisor_tool_result_error: "unavailable"` not above a token threshold as the issue title suggests, but after **any** prior `tool_use` block in the session, so it works as a session's first tool call and never again.

## Why it matters

The escalation pattern the archive recommends, a cheap executor consulting a stronger advisor mid-session when it gets stuck, is precisely the case that fails, and it fails at the moment of need rather than up front. Two independent replications (on 2.1.209 and 2.1.204) found the same trigger, which rules out the token-count explanation people naturally reach for.

## How to apply

Replace the mid-session advisor call with a subagent, `Agent(model="fable")`, and pass the relevant content explicitly in the prompt, since a subagent does not share conversation history. **REVISIT: written against 2.1.209/2.1.204.** Anthropic's 2.1.210 note ("Fable temporarily shows as unavailable in the advisor picker while a server-side issue causing Fable advisor failures is fixed") is a picker-level mitigation rather than a fix, so re-test before trusting the advisor again.

> "**Controlled 2×2 on 2.1.209 — the trigger appears to be any prior `tool_use` block, not model or token count**", anthropics/claude-code issue #67609

## Related

[[advisor-tool-escalation-pattern]]
