---
id: watch-a-vision-driven-browser-skill-for-ten-runs-before-scheduling-it
created: 2026-08-22
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/codex-s-browser-agent-automates-literally-anything_CB5bG4mvnS0_20260820.txt
---

# Supervise a Vision-Driven Browser Skill for About Ten Runs Before Putting It on a Schedule

## TL;DR

A browser skill captured from one successful natural-language run is not proven; watch it repeat roughly ten times and tighten its steps into strict instructions before you attach it to a scheduled routine.

## Why it matters

The seductive part is how cheap capture is: the creator described a Relay statement download in plain English, it opened the site, used the saved session, navigated to accounts and statements, downloaded two CSVs into the right project folder, and saved the whole flow as a skill on the first try with no feedback. His own caveat is that this is exactly the wrong basis for unattended scheduling on a bank account, because the agent is using vision plus reasoning to decide what to click, so the same skill can behave differently as the page shifts or a login screen appears. His stated rule is to run the skill while watching closely at least ten times, and to make the skill's script very strict rather than leaving it as loose narration. This is specifically about vision-driven nondeterminism, which is a different failure mode from an API skill that either works or errors.

## How to apply

After capturing the flow, run it manually about ten times while watching the browser pane, and after each run edit the skill so ambiguous steps become explicit (which element, which order, what to do when the login screen appears). Only then attach it to a scheduled routine, for example a monthly statement pull triggered against the most recent month. Keep the first scheduled runs reviewed rather than fire-and-forget, and re-verify after any redesign of the target site.
