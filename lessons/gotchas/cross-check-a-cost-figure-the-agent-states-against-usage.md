---
id: cross-check-a-cost-figure-the-agent-states-against-usage
created: 2026-09-12
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-made-codex-and-claude-code-build-the-same-app-one-clearly-won_WCrnS09vpfo_20260820.txt
---

# Do Not Quote a Cost Figure the Agent States in Prose: Read It Off /usage

## TL;DR

In one multi-hour run the agent's own summary put the spend near 447 dollars while the session's /usage stats across the session and its subagents came to closer to 800. A narrated cost number is a guess, not a reading.

## Why it matters

Cost is the number people quote straight out of a final summary without checking, and it is the number the agent is least able to observe, because spend inside subagents does not land in the orchestrator's own accounting. Believing the prose figure understates what a workflow actually costs, which is how an expensive habit survives a cost review.

## How to apply

After any long or fan-out run, take the figure from /usage rather than from the final message, and include the subagent rows. If you are reporting cost to anyone else, or deciding whether a workflow is affordable, quote the usage panel and say that is where it came from.

## Related

[[check-the-per-model-usage-breakdown-after-a-long-autonomous-run]]
