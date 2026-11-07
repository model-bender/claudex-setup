---
id: hardcode-the-destination-of-a-repeated-agent-action
created: 2026-09-24
status: active
supersedes: null
category: gotchas
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/build-sell-with-codex-5-hour-course_X-pbJWKmwi0_20260923.txt
  - transcripts/nate-herk-ai-automation/how-to-build-gpt-6-astra-automations-that-don-t-eat-your-usage-limit_FqnNL8fnUWo_20260920.txt
---

# Hard-Code a Repeated Automation's Destination Instead of Leaving It to the Agent's Judgment Each Run

## TL;DR

An unattended agentic routine given open judgment over the same low-stakes decision every run (which channel to message, say) can drift over time: one creator's simple DM routine started sending to the wrong channels after about a month of unattended runs. Hard-code the fixed target (channel ID, message ID) in the generated code instead of re-deciding it via the agent each time.

## Why it matters

A routine built as a full agent re-interprets its instructions every time it runs, so a decision that looks fixed (always DM this one channel) can quietly vary run to run and eventually land somewhere wrong, with no error thrown. A deterministic script with the destination hard-coded cannot do that; it either runs or fails visibly.

## How to apply

For any part of a recurring automation that should genuinely never change run to run (who gets notified, which record gets updated, which channel receives a message), put that value directly in the generated code as a constant rather than leaving the agent to resolve it fresh from a general instruction each time.

## Related

[[pick-the-codex-integration-layer-by-job-exec-sdk-app-server]]
