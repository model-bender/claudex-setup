---
id: connect-a-profiling-mcp-to-hunt-ui-jank
created: 2026-09-01
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/john-kim/how-i-use-claude-code-meta-staff-engineer-tips_20260307.txt
---

# Connect a Profiling MCP (e.g., Perfetto) So Claude Reads Traces to Find Jank

## TL;DR

For performance issues, hook up a profiling MCP like Perfetto, have Claude run a trace, then let it inspect the timings itself to spot jank.

## Why it matters

John Kim describes this as a validation loop specifically for performance work, parallel to the debug-log-plus-emulator loop for race conditions: have Claude both produce and read its own performance evidence rather than you interpreting traces manually.

## How to apply

Wire a Perfetto (or similar) MCP into the session, ask Claude to run the app and capture a trace, then ask it to read the trace and identify jank from the timing data.

## Related

[[pre-aggregate-profiling-data-for-agents]]
