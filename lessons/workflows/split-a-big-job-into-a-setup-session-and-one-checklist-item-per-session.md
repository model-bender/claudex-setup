---
id: split-a-big-job-into-a-setup-session-and-one-checklist-item-per-session
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/simon-scrapes/everyone-ignore-these-claude-concepts-but-they-change-everything_6VjeXzvpoJo_20261120.txt
---

# Split a big job into a setup session that only writes the checklist, then one item per session

## TL;DR

Make the first session do no work: it writes a checklist of everything to do plus a progress file. Every later session does one checklist item, verifies it and updates the progress file.

## Why it matters

The video says one long chat either tries everything at once and loses track, or does a little and declares itself finished early. With a checklist and progress file, a session that starts with no memory can read the notes and carry on.

## How to apply

Session 1 prompt: create the checklist and progress file only, do not start the work. Each later session: read the progress file, do exactly one unchecked item, check it, update the progress file. Combine with the JSON checklist lesson so items cannot be quietly edited.

Checked: Checked 2026-11-22: Anthropic's 'Effective harnesses for long-running agents' post describes an initializer session that creates init.sh, claude-progress.txt and an initial commit, then coding sessions that make incremental progress one feature at a time. No Claude Code mechanism claim.

## Related

[[make-delegated-workers-write-progress-back-to-the-plan]]
