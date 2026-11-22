---
id: keep-advisor-off-long-context-sessions-each-consult-sends-the-whole-transcript-uncached
created: 2026-11-22
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1xvnq0t/psa_using_fable_as_an_advisor_doesnt_touch_your/19slmoac306w4/
---

# Keep /advisor Off Long-Context Sessions: Each Consult Sends the Whole Transcript to the Advisor Uncached

## TL;DR

Every advisor consult is a separate inference on the advisor model that reads the executor's full transcript, and Claude Code does not turn on advisor-side caching, so each call on a large context is billed as fresh input at the advisor model's rate.

## Why it matters

The library frames the advisor as cheaper than running the stronger model throughout, which holds early in a session; at 300k to 500k context each consult re-reads all of it on Fable or Opus with no cache discount, and the executor decides on its own when to consult.

## How to apply

Use the advisor for short or early-session work and run `/advisor off` (or unset `advisorModel`) before a session grows large; for a late judgment call, spawn a subagent on a stronger model with only the relevant context instead.

Checked: Live API docs platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool (curl, 2026-11-22): the advisor receives the executor's full transcript as quoted context, is billed at the advisor model's rates, and its `caching` option defaults to null (off). Installed 2.1.330 binary builds the tool as {type: advisor_20260301, name, model, defer_loading} with no caching field (0 matches for an advisor caching object); the /advisor command's argument hint includes `off` and the `advisorModel` setting exists. The OP's headline claim that Fable advisor calls skip the Fable weekly limit is disputed in the thread and is not part of this lesson.

> "The advisor for each agent is given the full context of the agent calling it at input price, and it is not cached.", u/ashjohnr on r/ClaudeAI

## Related

[[advisor-tool-escalation-pattern]]
