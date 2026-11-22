---
id: count-thinking-as-context-earlier-thinking-blocks-stay-in-on-opus-4-5-and-fable
created: 2026-11-22
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xzsy2b/besides_using_agents_what_burns_tokens/19suupy4zie6b/
---

# Count Thinking as Context: On Opus 4.5+ and Fable, Earlier Thinking Blocks Stay In and Are Re-Read Every Turn

## TL;DR

Thinking is not a one-off output cost: on keep-all models every earlier turn's thinking blocks stay in the conversation and count as input on each later turn.

## Why it matters

The commenter measured one 3-hour, never-compacted session growing from 44k to 420k context, with about 39% of the growth (about 147k tokens) being thinking, so a high effort level is paid once as output and again as input for the rest of the session.

## How to apply

Run routine turns at a lower effort, write decisions to a file and /compact at natural breaks, and start unrelated tasks in a fresh session instead of stacking them in one long one.

Checked: Live API docs platform.claude.com/docs/en/build-with-claude/thinking (curl, 2026-11-22), section Thinking block preservation by model: Opus 4.5 and later Opus models, Sonnet 4.6 and later, Haiku 5.5 and Fable 5, 5.1 and 5.2 keep all prior turns' thinking, and the docs name the tradeoff as context usage because retained blocks count as input like any other history. The 39% share is the commenter's own measurement of one session, not verified.

> "On Opus 4.5 and later, earlier thinking blocks stay in context (it's in the extended thinking docs).", u/digora-dev on r/ClaudeCode
