---
id: agent-team-split-pane-reliably-works-only-in-tmux
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
---

# Agent-Team Split-Pane View Reliably Works Only in tmux, Not iTerm2

## TL;DR

Despite iTerm2 being documented as a supported terminal for the agent-team split-pane display mode, only tmux was actually confirmed working.

## Why it matters

Following the docs and setting up iTerm2 for split panes can leave you stuck on the single in-process view with no visible error explaining why.

## How to apply

Set up tmux, not iTerm2, if you want the split-pane agent-team view; use the in-process/all-in-one-terminal mode otherwise.

## Related

[[navigate-agent-teammates-with-shift-up-down-and-teammode-tmux]]
