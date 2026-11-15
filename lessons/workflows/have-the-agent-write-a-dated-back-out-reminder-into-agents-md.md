---
id: have-the-agent-write-a-dated-back-out-reminder-into-agents-md
created: 2026-10-25
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
source_type: post
sources:
  - https://ghuntley.com/patch/
  - https://ghuntley.com/answer/
---

# When an Agent Applies a Temporary Workaround, Have It Write a Dated Back-Out Reminder Into AGENTS.md

## TL;DR

After an agent applies a stopgap, have it add a dated, self-contained section to AGENTS.md (or CLAUDE.md) saying what to check on or after a date, how to remove the workaround, how to verify, and to delete the section afterwards. The next session that loads the file does the back-out, so no ticket is needed.

## Why it matters

Temporary mitigations tend to become permanent. Huntley's own reasoning: "I won't carry this tech debt for long because an agent will automatically back it out in a couple of days."

## How to apply

His example section is headed "Temporary reminder: eMudhra root blacklist (from 2026-10-22)" and names the condition to test, when to check again if it is not met, the files to delete, a verification step, and an instruction to delete the section. In a later post Huntley reports the follow-through: after applying temporary monkey patches during a security incident, he asked the agent to add "in seven days' time, get rid of my patches" to AGENTS.md, and the next agent to open that machine backed out the pins and checked that upstream was fixed. It still needs a session that loads the file after the date.

> "You can prompt an agent to update the AGENTS.MD to automatically back out these patches, let's say in five days from now, just by using the AGENTS.MD as a reminder", Geoffrey Huntley

> "Instead of creating a Jira ticket, I added a reminder to my AGENTS.md.", Geoffrey Huntley

## Related

[[tag-workarounds-with-revisit-expiration-condition]]
