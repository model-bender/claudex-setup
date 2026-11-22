---
id: have-the-agent-back-up-a-device-and-build-trace-logging-before-wiping-and-reflashing
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/mark-kashef/claude-fable-5-2-can-do-so-much-more-than-build-apps_5cZontQjBH4_20261122.txt
---

# Before Letting an Agent Wipe a Device, Make It Take a Full Backup and Set Up Trace Logging for Troubleshooting

## TL;DR

When pointing an agent at hardware or firmware, include in the first prompt: research the exact model, break down every component, make a full backup of the software and firmware, and build tracing so errors can be traced later.

## Why it matters

Kashef's eight-part prompt for rebuilding a robot's firmware included the backup before wiping, and a troubleshooting part where the agent tracks and traces errors, which later let Opus iterate from the traces.

## How to apply

In the opening prompt: 1. search the exact make and model, docs and owner forums; 2. list every component; 3. back up software and firmware before any change; 4. include a troubleshooting section that records traces (for example screenshots every second while testing).

Checked: No mechanism claim. The Firecrawl use in the transcript was not checked.
