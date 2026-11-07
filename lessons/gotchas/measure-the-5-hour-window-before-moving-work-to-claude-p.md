---
id: measure-the-5-hour-window-before-moving-work-to-claude-p
created: 2026-11-06
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/97074
---

# Measure the 5-Hour Window Before Moving Work to claude -p: Users Report It Drains 1.3x to 2.9x Faster

## TL;DR

Several users running controlled A/B tests report that the same work through `claude -p` (entrypoint sdk-cli) or the Agent SDK (sdk-ts) drains the 5-hour usage window much faster than the interactive TUI or the VS Code extension.

## Why it matters

The issue thread has independent reproductions on Max and Pro plans and a Team plan, using Opus 5, Opus 5.5 and Sonnet 5.5, with ratios from about 1.3x to 2.9x depending on the interactive baseline. One reproducer reports the weekly meter is unaffected and only the 5-hour window moves. No Anthropic explanation or fix is recorded in the thread; this is a reported, repeatedly reproduced behaviour, not confirmed intent.

## How to apply

Before moving a workload from interactive to scheduled `claude -p` or SDK runs, measure the 5-hour utilization before and after one run and budget for a multiple of the interactive cost. If automation keeps tripping the 5-hour limit, spread runs out or run the heavy ones interactively until the issue is resolved.

> "The same tokens on the same model should use the same share of the 5-hour window, whether they come from `claude -p` or from the interactive TUI.", anthropics/claude-code issue 97074 (multiple independent reproductions)

## Related

[[start-a-new-conversation-instead-of-resuming-a-cold-one-on-pro-or-max]]
