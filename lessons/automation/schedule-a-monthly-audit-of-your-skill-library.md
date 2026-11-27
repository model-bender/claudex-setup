---
id: schedule-a-monthly-audit-of-your-skill-library
created: 2026-11-22
status: active
supersedes: null
category: automation
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/how-to-actually-choose-the-right-ai-agent_6LNlCpQPYFc_20260920.txt
---

# Schedule a monthly automated audit of your whole skill library

## TL;DR

Run a recurring job that has an agent re-read the current tool documentation, refine every skill against it, and report which installed skills you are not using.

## Why it matters

Skill libraries bloat: the guest's example is people who downloaded some 300 skills, load them every time and use five. Each tool also treats skills a little differently. He has AI read the current documentation and runs this audit monthly on a cron job, so the library is refreshed and trimmed on a schedule.

## How to apply

Write the audit as a prompt or skill: fetch the current skills docs, check each skill against them, list unused skills, merge ones that belong in a compound skill, and make each one model agnostic so it works across your tools. Schedule it monthly; the transcript only says 'cron job'. From the docs check: a skill library on your own machine needs a local scheduler (system cron running the CLI headless, or a local scheduled task in Claude Code Desktop, which takes a custom cron expression). A cloud scheduled task created with `/schedule` runs on a fresh clone of a GitHub repository with no access to local files, so it only fits if your skills live in a repo.

Checked: code.claude.com docs fetched with curl 2026-11-22 (Claude Code 2.1.330): commands.md lists `/schedule` for cloud scheduled tasks, formerly routines; routines.md says each run clones the selected repositories; desktop-scheduled-tasks.md says local tasks run on your machine with access to local files, only while the app is open and the computer awake, and cloud tasks have no access to local files. The transcript names no specific scheduler beyond 'cron job'.

## Related

[[curate-a-bulk-skill-pack-before-installing-not-after]], [[track-per-layer-decay-cadence-in-a-rot-md-file]]
