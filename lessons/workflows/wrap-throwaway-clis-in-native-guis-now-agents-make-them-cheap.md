---
id: wrap-throwaway-clis-in-native-guis-now-agents-make-them-cheap
created: 2026-08-29
status: active
supersedes: null
category: workflows
source_type: post
tool: claude-code
sources:
  - https://simonwillison.net/2026/Aug/21/stop-making-tuis/
---

# Turn Your Throwaway CLIs Into Native GUI Apps: Agents Made Real UIs Nearly Free

## TL;DR

Coding agents have collapsed the cost of a usable native GUI, so stop defaulting personal tools to CLIs and TUIs: point the agent at an existing CLI and have it wrap a real UI around it.

## Why it matters

The settle-for-a-terminal-UI habit predates agents making GUI scaffolding nearly free; both Thomas Ptacek (author) and Simon Willison (endorsing) argue the trade-off has flipped, and Willison's own vibe-coded macOS menu-bar monitors have survived months of daily use as evidence.

## How to apply

Take one personal CLI script you actually use and prompt Claude Code to build a native app around it (a macOS menu-bar app is the canonical starter), rather than adding another TUI layer.

> "If you haven't tried your hand at turning one of your 500 throwaway CLIs into a native app, you're doing yourself a disservice. Go build a native UI. It'll probably change the way you think.", Thomas Ptacek (endorsed by Simon Willison)
