---
id: dont-pipe-agent-status-posts-into-team-slack
created: 2026-08-29
status: active
supersedes: null
category: automation
source_type: post
tool: [claude-code, codex]
sources:
  - https://registerspill.thorstenball.com/p/joy-and-curiosity-96
---

# Don't Pipe Routine Agent Status Posts Into Team Slack: Everyone Goes Notification-Blind in Days

## TL;DR

Agent-emitted broadcast notifications ("shipped X", "error Y") into shared channels stop being read within days; the Amp team disabled theirs once someone admitted the blindness.

## Why it matters

This is firsthand counter-evidence to the popular pattern of wiring agent status output into team Slack, from a team that builds an agent. Volume from agents outpaces human attention far faster than human-authored posts do, so the channel silently stops functioning as an alerting mechanism while still looking wired-up.

## How to apply

Keep agent reporting pull-based (dashboards, PR descriptions, logs, on-demand status skills) and reserve push notifications for events that demand a human action. If a broadcast channel exists, watch for glaze-over within days and kill it rather than letting it decay into noise.

> "We've had Amp post messages into our Slack when something went wrong or when something was shipped and it took just a couple of days for everyone to glaze over them.", Thorsten Ball

## Related

[[let-only-the-strongest-model-talk-to-humans]], [[make-the-status-report-its-own-skill-and-attach-it-to-every-routine]]
