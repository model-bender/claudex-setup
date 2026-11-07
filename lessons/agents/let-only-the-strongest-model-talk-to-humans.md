---
id: let-only-the-strongest-model-talk-to-humans
created: 2026-08-29
status: active
supersedes: null
category: agents
source_type: post
tool: [claude-code, codex]
sources:
  - https://yegge.ai/essays/fences-not-sandboxes/
---

# Let Only Your Strongest-Judgment Model Talk to Humans, Enforced at the Slack/Email Boundary

## TL;DR

In a mixed-model agent fleet, route all human-facing communication through the single strongest-judgment model and enforce the restriction at the channel boundary itself; cheaper models stay headless.

## Why it matters

Yegge runs ~50-60 agents (headless Sonnet/Opus fleets under Fable orchestration) with about 10 outside humans, and found that what fails in human contact is judgment, not coding ability ("butting into conversations, talking over people, mansplaining everything to death"). A boundary-enforced fence makes the topology rule unbreakable rather than advisory.

## How to apply

Give only the top-tier model the credentials to post to Slack, email, or other human channels, checked at the integration layer (bot token scoping, gateway policy), not in prompts; implementation and monitoring agents report inward to the orchestrator instead.

> "A Wheelhouse example of a fence is Fable being the only model allowed to talk to humans externally. The fence is enforced at the Slack and email boundaries.", Steve Yegge

## Related

[[escalate-agent-rules-one-enforcement-tier-per-violation]], [[dont-pipe-agent-status-posts-into-team-slack]]
