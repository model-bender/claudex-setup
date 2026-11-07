---
id: triage-adversarial-review-findings-against-trust-boundaries-before-fixing
created: 2026-10-19
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://www.anthropic.com/engineering/redesigning-source-control
  - https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/
---

# Triage Adversarial-Review Findings Against Your Trust Boundaries Before the Agent Fixes Them All

## TL;DR

An adversarial reviewer will push the fixer to add defenses against hypothetical threats, so a person has to decide which findings to reject before the agent applies them.

## Why it matters

Reviewers find flaws by construction and the fixing agent tends to apply every finding, so complexity piles up. Anthropic's source-control team had engineers steer Claude away from over-engineering in response to hypothetical concerns.

## How to apply

After a reviewer round, sort findings against the system's trust boundaries and state them in the fix prompt (for example, which internal service is trusted and needs no extra validation). Checked: no mechanism named.

> "Anthropic also makes extensive use of adversarial review, and, while this is incredibly effective in many ways, it can also be myopic, so skilled engineers needed to steer Claude away from over-engineering parts of the system in response to hypothetical concerns.", Anthropic engineering blog

## Related

[[measure-agent-over-engineering-with-net-new-loc-and-complexity]], [[scope-team-tasks-small-add-adversarial-reviewer]]
