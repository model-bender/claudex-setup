---
id: run-maintenance-routines-on-opus-by-default
created: 2026-08-16
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://x.com/bcherny/status/2088140601967730978
  - https://x.com/bcherny/status/2088021350871175304
---

# Run Unattended Maintenance Routines on Opus by Default - Sonnet Costs You Guardrails

## TL;DR

For unattended repo-maintenance routines, Opus is the default, Fable is reserved for the few genuinely hard routines, and dropping to Sonnet is a real option that you pay for in PR auditing, prompt iteration, and extra checks.

## Why it matters

This converts "use the cheapest model that works" into a concrete exchange rate for autonomous work. The cheaper model does not simply fail - it shifts cost onto your review time and your guardrail-writing. That cost is invisible in a token bill and very visible in your afternoon.

It also caps the escalation instinct in the other direction: Fable is needed "only for a few of the hard routines", not as the standing choice for anything unattended.

## How to apply

Start scheduled routines on Opus. Move one to Sonnet only once you have added explicit checks to the prompt and are willing to audit its PRs more closely. Escalate to Fable only for routines that actually fail on Opus.

> "Sonnet 5 could definitely do many of these. If using Sonnet I'd spend a bit more time auditing PRs and iterating on routines' prompts then adding in checks and guardrails .", Boris Cherny

> "We use Opus for most of these. Only need Fable for a few of the hard routines.", Boris Cherny

## Related

[[run-a-portfolio-of-daily-maintenance-routines]], [[model-selection-opus-sonnet-haiku-use-cases]], [[route-long-projects-to-fable-and-single-prs-to-opus-5-medium]], [[bookend-each-work-item-with-the-strongest-model]]
