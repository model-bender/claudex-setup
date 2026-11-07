---
id: plausible-verdict-routes-to-slack-not-autofix
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Route 'Plausible' Code-Review Verdicts to a Slack Message Instead of Auto-Fixing Them

## TL;DR

When /code-review returns a 'plausible failure' verdict (as opposed to medium/high severity), don't auto-fix it: have the agent message you on Slack explaining the finding and why it matters.

## Why it matters

In the transcript's example, /code-review flags a 'plausible failure case of the pricing changes if it's greater than 200,000 tokens', a verdict that's neither clearly wrong nor clearly right. The presenter adds a rule so this class of low-confidence finding gets surfaced to a human via Slack after the PR opens, rather than being silently fixed or silently dropped.

## How to apply

In your task-lifecycle instructions, add: 'For any plausible (not medium/high severity) code-review verdict, send a Slack message once the PR is open explaining the additional finding and why it matters, instead of auto-fixing it.'

## Related

[[route-self-improvement-loop-changes-into-three-approval-buckets]]
