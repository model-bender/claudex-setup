---
id: monitor-tool-now-works-with-telemetry-disabled-from-2-1-310
created: 2026-10-25
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21310
---

# With Telemetry or Nonessential Traffic Off, the Monitor Tool Only Exists From 2.1.310

## TL;DR

Before 2.1.310 the Monitor tool (and plugin monitors) was missing on Bedrock, Vertex and Foundry and in sessions with telemetry or nonessential traffic disabled; 2.1.310 adds it there and also blocks long foreground sleeps there.

## Why it matters

A skill or rule that tells Claude to wait on a condition with Monitor silently fell back to something else in a privacy-hardened setup, and a foreground `sleep` that used to work there is now refused.

## How to apply

If you set `DISABLE_TELEMETRY` or disable nonessential traffic, update to 2.1.310 before relying on Monitor-based waits, and replace foreground sleeps with a Monitor wait. Checked: in a 2.1.310 session with `DISABLE_TELEMETRY=1` set, Monitor appears among the available tools.

> "Added the Monitor tool and plugin monitors on Bedrock, Vertex, and Foundry, and when telemetry or nonessential traffic is disabled; long foreground sleeps are now blocked there too", Claude Code CHANGELOG 2.1.310

## Related

[[monitor-watches-expire-at-30-minutes-and-can-drop-events]]
