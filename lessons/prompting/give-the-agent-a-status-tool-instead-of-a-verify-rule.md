---
id: give-the-agent-a-status-tool-instead-of-a-verify-rule
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-s-new-subagent-rules-will-change-how-you-build_ybx0mmd22pQ_20261026.txt
---

# Give the agent a tool that reads the result instead of writing a 'verify it went through' rule

## TL;DR

With recent models you can drop rules like 'verify the refund actually went through'. Give the agent a tool that returns the status and it checks its own work.

## Why it matters

The video says recent models check their work as they go when they have the right tool, so the instruction is redundant and the tool is what makes verification possible. The Anthropic article the video discusses says the same in general terms: recent models 'check their work as they go, which makes some harness elements redundant'.

## How to apply

For each 'verify X' rule in a prompt or skill, ask whether the agent has a way to read X's state. If not, add the tool. Then try removing the rule.

Checked: No mechanism named. The article (claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop, read 2026-11-22) contains the general claim quoted above; the refund-status example does not appear in the article text and is the speaker's illustration, as is the transfer to coding agents.

## Related

[[delete-double-check-and-verify-again-instructions-from-prompts]]
