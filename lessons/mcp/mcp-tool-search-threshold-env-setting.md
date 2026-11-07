---
id: mcp-tool-search-threshold-env-setting
created: 2026-09-01
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
---

# Tune the MCP Tool-Search Auto-Enable Threshold in settings.json

## TL;DR

Claude Code auto-enables MCP tool search once your MCP tool descriptions would otherwise consume more than 10% of the context window by default; you can override this via an env setting with values true, false, auto, or auto:N for a custom percentage.

## Why it matters

The transcript gives the exact default and override mechanism: 'by default, if Claude Code sees that your MCP tool descriptions would take up more than 10% of a context window, then it will automatically enable MCP tool search... you can do this pretty easily in your settings.json by adding this as an env and defining the number.' Someone who wants tool search on more aggressively (or always off) needs this exact knob.

## How to apply

In .claude/settings.json's env block, set the MCP tool-search threshold variable to `true` (always on), `false` (always off), or `auto:N` where N is a percentage (e.g. `auto:5` to trigger at 5% instead of the 10% default) instead of leaving it at the implicit `auto` default.

## Related

[[stop-pruning-mcp-servers-tool-search-loads-schemas-on-demand]]
