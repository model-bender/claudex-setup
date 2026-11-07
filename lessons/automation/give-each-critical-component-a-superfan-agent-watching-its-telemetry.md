---
id: give-each-critical-component-a-superfan-agent-watching-its-telemetry
created: 2026-10-19
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://www.anthropic.com/engineering/redesigning-source-control
---

# Give Each Critical Component Its Own Agent That Watches Only That Component's Telemetry and Logs

## TL;DR

Alongside normal alerts, Anthropic runs one Claude per component, each in its own channel with access to that component's telemetry and logs, briefed to look for anything strange.

## Why it matters

Anthropic says these single-focus agents catch subtle and novel issues that make fixed alerts look one-dimensional by comparison.

## How to apply

Pick a component, give one agent read access to its logs and metrics and a brief to watch only that component, and keep the existing alerts in place. Anthropic uses an internal Slack-based tool for this; the pattern, not the product, is the transferable part. Checked: no mechanism named.

> "We call these Claudes “superfans.” We have a scion-daemon superfan, a scion-cache superfan, an Antique merge queue superfan, and so on. They have access to our telemetry and logs, and act like an experienced engineer who has nothing better to do than to refresh charts and look for anything strange.", Anthropic engineering blog

