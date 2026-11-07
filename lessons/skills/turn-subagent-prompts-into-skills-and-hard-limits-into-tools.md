---
id: turn-subagent-prompts-into-skills-and-hard-limits-into-tools
created: 2026-11-06
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-s-new-subagent-rules-will-change-how-you-build_ybx0mmd22pQ_20261026.txt
---

# When Folding a Subagent Back Into the Main Agent, Make Its Prompt a Skill and Its Approval Gates Tools

## TL;DR

A refunds or shipping subagent becomes a refunds or shipping skill (split into small referenced files), its API calls become tools, and any hard limit such as approval moves into the tool layer.

## Why it matters

Ray relays Anthropic's guidance for replacing per-team subagents with one agent loop using progressive disclosure. Anthropic says hard limits such as approval gates belong in tools rather than prompts. Ray's way of doing that is a self-hosted MCP gateway (executor.sh) whose policies mark each action as needing approval, auto-approved or blocked; he blocks email sending, for example.

## How to apply

1. For each subagent, move its prompt into a skill; keep SKILL.md short and push detail into referenced files.
2. Expose its API calls as tools on the main agent.
3. Put approval gates in the tool layer, for instance a gateway with per-action policies, not in prompt text.

Checked: claude 2.1.318 binary: ENABLE_TOOL_SEARCH 16 hits (the deferred-tool mechanism Ray mentions). The gateway product (executor.sh) is not checked; no mechanism claimed beyond what Ray showed.

## Related

[[skill-md-under-200-lines-progressive-disclosure]], [[scope-tool-access-not-just-the-prompt-to-restrict-agent-actions]]
