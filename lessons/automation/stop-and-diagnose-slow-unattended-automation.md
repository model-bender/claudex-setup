---
id: stop-and-diagnose-slow-unattended-automation
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/master-97-of-codex-in-1-hour-full-course_3TdD8Qv5Tk8_20260626.txt
---

# Stop and Ask an Automation What's Wrong Once It Runs Well Past Its Normal Time

## TL;DR

If a recurring automation that usually takes ~20 minutes is still running after 40+, interrupt it and ask what's happening rather than let it keep trying.

A Codex automation that normally finishes in ~20 minutes but runs 20+ minutes over may be stuck because it can't overwrite a file (like an Excel workbook) that you have open on your machine.

## Why it matters

Letting a stuck automation keep running burns session tokens and time on a path that a human could resolve in seconds (e.g., closing a locked file or fixing a wrong model setting).

Codex can't write to a locked/open file, and it will keep retrying silently rather than immediately telling you the real blocker, burning time and tokens.

## How to apply

Track how long a routine normally takes; if a run passes roughly double that with no clear progress, stop it, ask 'why is this taking so long,' and act on the answer before restarting.

If a routine run is taking far longer than usual, stop it, ask it what's wrong, and check whether the deliverable file it's updating is open in another program; close it and re-run.

## Related

[[guard-unattended-agent-runs-with-a-stall-watchdog-and-bounded-retry]]
