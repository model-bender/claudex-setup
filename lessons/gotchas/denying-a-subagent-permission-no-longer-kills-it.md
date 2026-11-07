---
id: denying-a-subagent-permission-no-longer-kills-it
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# Denying a Subagent's Permission Request No Longer Stops It, It Tries a Different Approach

## TL;DR

When a subagent asks for a tool permission and you press no, it used to stop completely; now it continues working and tries an alternative approach instead of dead-ending.

## Why it matters

Under the old behavior, one accidental or intentional denial could silently end a whole subagent task with no recovery, forcing you to notice it stopped and restart it.

## How to apply

Expect that pressing 'no' on a subagent's permission prompt is no longer a hard stop; the subagent will attempt another way to accomplish the step, so check its next actions rather than assuming it halted.
