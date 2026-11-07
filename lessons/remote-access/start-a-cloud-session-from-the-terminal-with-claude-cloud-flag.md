---
id: start-a-cloud-session-from-the-terminal-with-claude-cloud-flag
created: 2026-10-19
status: active
supersedes: null
category: remote-access
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-changed-completely-every-new-concept-explained_YAuWBqZ_gjs_20261018.txt
---

# Start a Cloud Session From the Terminal With claude --cloud, Then Pull It Back With --teleport

## TL;DR

A task can run on a cloud machine instead of yours: start it with `claude --cloud`, close the laptop, and bring the conversation back later with `claude --teleport`.

## Why it matters

Simon Scrapes says each cloud task gets its own machine, several can run at once, they keep going when the laptop is closed, and it runs on the normal plan with no extra machine charge (his claim, not checked). The transcript renders the flag as 'claude-cloud'; the real flag is --cloud.

## How to apply

1. `claude --cloud "describe the task"` creates a cloud session; `claude --cloud <session_id or claude.ai/code URL>` attaches to an existing one. 2. Other entry points he lists: claude.ai/code, or picking cloud instead of local in the desktop app. 3. `claude --teleport` (or /teleport) pulls the session and its history back to the laptop. Checked: `claude --help` on 2.1.303 lists '--cloud [description|session_id|url] Create a cloud session with the given description, or attach to an existing one by session ID or claude.ai/code URL' and '--teleport [session]'.

## Related

[[teleport-sessions-between-cloud-web-and-terminal]], [[environment-switching-local-cloud-ssh]]
