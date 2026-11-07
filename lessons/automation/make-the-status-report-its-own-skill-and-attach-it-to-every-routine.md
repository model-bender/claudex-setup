---
id: make-the-status-report-its-own-skill-and-attach-it-to-every-routine
created: 2026-08-22
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/austin-marchese/boris-cherny-s-4-step-playbook-to-10x-your-ai-productivity_clDlAmHsiKw_20260820.txt
---

# Make Reporting Its Own Skill and Attach It to Every Routine

## TL;DR

Instead of writing reporting instructions into each scheduled routine, build one small skill (for example send-slack-update) and add it to the end of every routine so all autonomous work lands in a single channel you actually check.

## Why it matters

Scheduling work is only half of delegation: the creator's framing is that a routine is like telling a coworker "every Monday at 8:00 a.m. I want this report sent to me", and a team member who does the work but never reports is useless. Duplicating the reporting instructions inside every routine means the format drifts per routine and updating the destination means editing all of them. Factoring the report into a single skill gives one place to change the channel, the format, and the level of detail, and it composes with whatever the routine already does (his example chains a topic-research-report skill with the update skill on a Monday schedule). It also forces a single destination, which is the point: the update has to land somewhere you already look, whether that is a Slack #automation-updates channel, WhatsApp, or Telegram.

## How to apply

Build one skill whose only job is posting a run summary to your chosen channel, then reference it as the final step of each routine rather than restating the instructions. Pick one destination you check daily and send everything there rather than per-routine channels. Keep the skill's output spec strict so every routine reports in the same shape, which makes an anomalous run obvious at a glance. If several routines report at once, have the skill include which routine produced the update.
