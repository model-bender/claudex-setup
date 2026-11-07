---
id: autocontinue-at-usage-limit-resumes-the-task-after-reset
created: 2026-10-19
status: active
supersedes: null
category: settings
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-changed-completely-every-new-concept-explained_YAuWBqZ_gjs_20261018.txt
---

# Let Claude Code Wait Out a Usage Limit and Resume the Task With autoContinueAtUsageLimit

## TL;DR

When a claude.ai usage limit stops a session, Claude Code can wait for the reset and continue the task by itself instead of leaving a half-finished job. If it was cancelled, /rate-limit-options re-arms it.

## Why it matters

Simon Scrapes says a limit hit mid-task used to leave you with a half-finished job to restart, and that now the task waits and picks up where it stopped. He says it is on by default in Claude Code and covers the 5-hour window, not the weekly one, so one task cannot spend next week's tokens. It will start spending your next window without asking.

## How to apply

1. Leave the setting on for unattended runs, or set `autoContinueAtUsageLimit` in settings (when off, the limit dialog offers the wait as a choice instead). 2. If the wait was cancelled, run /rate-limit-options to wait again. 3. The auto continue is cancelled if the session moves to the background, relaunches, exits, hands off to Desktop or is sent to the cloud, so keep the process alive. Checked: claude 2.1.303 binary: settings key autoContinueAtUsageLimit with description 'When a claude.ai usage limit stops your session, wait for the limit to reset and continue the task automatically. When off, the limit dialog offers the wait as a choice instead.'; strings 'Automatic continue cancelled' and '/rate-limit-options to re-arm'. The default-on and 5-hour-only claims are the speaker's and were not verified.

## Related

[[bound-auto-resume-with-resume-interrupted-turn-max-age-ms]]
