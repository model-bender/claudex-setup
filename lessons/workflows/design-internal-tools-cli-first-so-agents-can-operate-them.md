---
id: design-internal-tools-cli-first-so-agents-can-operate-them
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/john-kim/ai-coding-is-hard-until-you-start-setting-goals_P0I8jl7WUf0_20261015.txt
---

# Design internal tools with a CLI as the main interface so agents can operate them

## TL;DR

When you build an internal tool, specify a CLI alongside the web and mobile front ends and treat it as the way agents will use the tool.

## Why it matters

The creator's opening prompt for a new website to run the YouTube workflow asks for the website, a native mobile app, and 'my ideal way to interact with this website and etc. is via a CLI agentically', the same pattern as the creator's other internal tools. The creator's second-brain tool is a CLI too, and the agents can use it 'because it's a straight up CLI tool'.

## How to apply

Put the CLI in the first plan. Giving every main action in the UI a matching command the agent can call is this lesson's inference; the video says only that the CLI is the intended way to work with the tool agentically.

Checked: No mechanism named.

## Related

[[cli-tools-over-mcp-for-tokens]]
