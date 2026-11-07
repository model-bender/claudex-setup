---
id: run-slow-waits-from-the-main-session-not-a-big-context-subagent
created: 2026-10-25
status: active
supersedes: null
category: agents
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xble3m/subagents_get_a_5minute_prompt_cache_what_i/
---

# Never Let a Big-Context Subagent Wait on a Slow Command: Run the Wait From the Main Session

## TL;DR

Subagent requests use a 5-minute prompt cache even on a subscription, so a subagent that waits on a long test run re-writes its whole context on its next turn; run slow commands from the main session and hand failures to a fresh agent.

## Why it matters

The poster measured avoidable cache rebuilds at about a quarter of four months of usage, mostly from waiting subagents, and saw them fall from 27% to 5% of usage in the week after the change (their own transcripts, one week).

## How to apply

Keep each subagent to one short task. Run test suites, end-to-end harnesses and polls from the main thread in the background, logging to a file and printing only the exit code and failing lines, then give the failures to a fresh agent. Message an existing subagent again only if it finished within the last 5 minutes. The alternative is paying for `subagentPromptCacheTtl: "1h"`. Checked against the installed 2.1.310 binary: the `subagentPromptCacheTtl` description says it covers everything outside the main conversation and defaults to 5 minutes unless `ENABLE_PROMPT_CACHING_1H=1`.

> "When a subagent with a big context waits on something slow (a test suite, an e2e harness, a poll loop), its next turn writes the whole context to the cache again.", u/27medkamal on r/ClaudeCode

## Related

[[prompt-cache-is-one-hour-on-subscription]], [[opt-into-the-1-hour-prompt-cache-with-promptcachettl-on-api-billing]]
