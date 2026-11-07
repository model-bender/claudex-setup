---
id: fork-vs-btw-for-multistep-tool-calling-asides
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-subagent-upgrade-yet_20260424.txt
---

# Use a Fork Instead of /btw When a Side Question Needs Tool Calls

## TL;DR

/btw (or /bytheway) only supports a single-turn answer with no tool calls, while a forked subagent can run multiple steps and call tools like MCP servers; pick a fork whenever the aside needs research or tool use.

## Why it matters

Asking a tool-requiring question through /btw won't work the way you expect since it can't call out to anything; a fork gets the full main-conversation context plus the ability to actually go look something up.

## How to apply

For a quick side question answerable from context alone, use /btw. For a side question that needs to hit an MCP server, browse, or otherwise call tools, ask for a forked subagent instead.

