---
id: agent-team-state-lives-under-claude-teams-directory
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/learn-claude-code-agent-teams-in-12-minutes_20260307.txt
---

# Debug an Agent Team by Reading ~/.claude/teams/<team-name>/ Directly on Disk

## TL;DR

Claude Code's agent-teams feature writes its full state to disk under a per-team folder: a config file, a tasks folder, and an inboxes folder holding every message passed between teammates.

## Why it matters

The creator opened this directory directly to show what's inside: "we can see we have a config file. We can see that we have the list of team members... the prompt that was actually given to the team member... a folder with the same team name and tasks that contains all the tasks... finally, there's an inboxes which contains all the agent inboxes and the messages that they're receiving" - all inspectable outside the terminal UI.

## How to apply

Look under `~/.claude/teams/<team-name>/` for the team config (members, per-member prompt, model, color), a same-named tasks folder with the task list, and an inboxes folder with each teammate's received messages, to debug what a team run actually did.

## Related

[[navigate-agent-teammates-with-shift-up-down-and-teammode-tmux]], [[spawn-teammates-via-the-agent-name-param-no-teamcreate]]
