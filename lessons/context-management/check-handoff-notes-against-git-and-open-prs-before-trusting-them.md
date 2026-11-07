---
id: check-handoff-notes-against-git-and-open-prs-before-trusting-them
created: 2026-10-19
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1x2os3k/ive_used_claude_code_every_day_for_a_year_this_is/
  - https://www.reddit.com/r/ClaudeCode/comments/1x2os3k/ive_used_claude_code_every_day_for_a_year_this_is/pf7j2wm/
---

# Make Your Session-Start Command Check Handoff Notes Against git and Open PRs Before Trusting Them

## TL;DR

Handoff notes drift from what really happened, so a start-of-session command should compare them with the git log, the open PR list and any running jobs, and report where they are wrong before the agent acts on them.

## Why it matters

A fresh session treats the handoff note as ground truth. If the note says a branch is merged or a job finished when it is not, the agent builds on a false premise and the mistake compounds; one commenter names summary drift as the failure they kept hitting. Git and PR checks catch drift about state, not about decisions ("we decided X"), so that commenter also keeps the verbatim transcript beside the note.

## How to apply

In your session-start command or skill, have Claude read `git log`, the open PRs (`gh pr list`) and the status of background jobs, compare each against the note's claims, and print the mismatches first, before any planning. Pair it with a handoff command that writes the note before you stop.

> "Before trusting the notes, \`/session-start\` checks them against git, open PRs and running jobs, and tells you where they're wrong.", u/Bill-Negative on r/ClaudeCode

> "the failure I kept hitting was the summary quietly drifting from what actually happened.", u/Kindly_Leader4556 on r/ClaudeCode

## Related

[[summarize-recent-commits-to-rebuild-context]], [[tell-fresh-session-not-to-act-until-instructed-after-handoff]], [[build-a-session-handoff-skill-for-manual-context-clearing]]
