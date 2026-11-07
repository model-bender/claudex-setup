---
id: navigate-agent-teammates-with-shift-up-down-and-teammode-tmux
created: 2026-08-31
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/learn-claude-code-agent-teams-in-12-minutes_20260307.txt
  - transcripts/simon-scrapes/how-to-use-claude-code-agent-teams-in-13-mins-opus-4-6_20260307.txt
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
  - transcripts/simon-scrapes/every-claude-code-workflow-explained-u0026-when-to-use-each_20260424.txt
---

# Navigate Agent-Team Teammates With Shift+Up/Down, or Watch Them All via teamMode Plus tmux

## TL;DR

Inside an agent-team session, Shift+Up/Down cycles between teammates, and setting the teamMode option while running under tmux gives a split-pane view of every teammate at once.

## Why it matters

A team puts several agents to work simultaneously but the leader's transcript shows you only one of them, so without the navigation keys or the split-pane view you cannot see what individual teammates are doing. Flipping to a specific teammate or watching all panes side by side is what makes monitoring and course-correcting a running team practical.

## How to apply

Use Shift+Up and Shift+Down to move between teammates in the session. For a persistent all-at-once view, set the teamMode setting (noted as `teamMode: teamX` in the source) and run the session under tmux to get a split pane per teammate.

## Related

[[agent-teams-for-cross-domain-collaboration]]
