---
id: spike-the-whole-automation-chain-before-polishing-any-step
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/austin-marchese/6-easy-steps-to-automate-99-of-your-life-with-claude_ktY1b2-OKRA_20260910.txt
---

# Spike the Whole Automation Chain End to End Before Polishing Any One Step

## TL;DR

Before building an automation properly, hand-run the ugliest version that touches every step of the chain, to prove no step is impossible. Asking Claude whether it is possible is not the spike.

## Why it matters

Austin Marchese borrows the engineering spike for this: 'before you build anything that's perfectly polished, you build the fastest, ugliest version that connects all of the pieces end to end.' His own example is the failure mode: a daily brief that reads email and Slack then emails him a summary would have been impossible before Anthropic shipped outbound email, so a week of polishing the read side would have been wasted. He is explicit that the model's own feasibility verdict is not evidence: 'Claude saying it's possible is just the first part, you actually have to go and build it, don't just take Claude's word for it.' The cost of skipping the spike is not a bad automation, it is discovering the blocker after you have invested in the steps before it.

## How to apply

List the steps as trigger, each data source, the transform, and the delivery. Then run the whole chain once by hand in a single conversation, connecting whatever connectors it needs, and confirm every step actually produced its output. Only then package it. Spike anything whose permissions you do not control (work accounts, outbound send, connector scopes) before anything else.

## Related

[[prove-a-process-as-a-manual-skill-before-automating-it]], [[skill-frequency-test-inner-loop]]
