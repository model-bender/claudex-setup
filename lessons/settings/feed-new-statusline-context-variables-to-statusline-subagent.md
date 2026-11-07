---
id: feed-new-statusline-context-variables-to-statusline-subagent
created: 2026-09-01
status: active
supersedes: null
category: settings
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
---

# Feed the New Context-Remaining Statusline Variables to the /statusline Subagent

## TL;DR

Anthropic added two new template variables that give the statusline a more accurate read on remaining context; paste them into a prompt to the /statusline subagent and ask it to wire your statusline's context/battery indicator to use them directly instead of computing the estimate itself.

## Why it matters

The transcript walks through this: 'they added these two variables that allow the status line to have a better display of the remaining context. So you could copy this over and then go to Claude, do /statusline to spawn up the status line sub-agent, paste that in here, and then say can you update the status line battery to include this instead... It now updates the command so it doesn't have to do the calculation anymore.'

## How to apply

Run `/statusline` to launch the statusline-building subagent, paste in the two new context-remaining variables, and ask it to update your existing statusline script to read from them instead of manually estimating remaining context.

