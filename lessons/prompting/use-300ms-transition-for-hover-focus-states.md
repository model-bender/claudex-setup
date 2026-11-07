---
id: use-300ms-transition-for-hover-focus-states
created: 2026-09-01
status: active
supersedes: null
category: prompting
tool: [claude-code, claude-design]
sources:
  - transcripts/jono-catliff/claude-code-web-design-10-years-covered-in-66-minutes_2Gda_ZvV1V4_20260701.txt
---

# Specify a ~300ms Transition Duration for Hover and Focus State Changes

## TL;DR

Ask for roughly 300 milliseconds of transition time on hover/focus effects (color inversion, scale, underline reveal) instead of leaving them instant, since instant state changes read as unpolished.

## Why it matters

The gap between a button that snaps to its hover color and one that eases into it over ~300ms is one of the clearest visible 'AI slop vs. professional' signals, and it's a single number Claude applies consistently once given.

## How to apply

In an interaction-states prompt, name the duration explicitly, e.g. 'add a 300ms transition to all hover and focus state changes (color, scale, underline).'

## Related

[[prompt-interaction-states-they-are-omitted-by-default]]
