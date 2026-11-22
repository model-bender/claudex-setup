---
id: ask-for-a-thread-to-run-on-your-machine-when-it-needs-local-files
created: 2026-11-22
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/simon-scrapes/the-new-claude-is-quietly-incredible-17-best-features_KjuANoI8HDw_20261103.txt
---

# Ask Claude to run a thread on your own machine when the job needs local files

## TL;DR

Project threads usually run in the cloud. When a job needs files that exist only on your computer, ask Claude to run that thread on your machine instead.

## Why it matters

A cloud thread works only on the project's repositories and on copies of files uploaded to the project. Per the docs, a thread on your machine works in the live folder with that machine's tools, MCP servers, hooks and permission rules, while the project's other threads keep running in the cloud. If the job only needs to read a few local files, the docs suggest uploading them to the project instead.

## How to apply

In the project conversation, say the task should run on your computer (the docs also list **Work locally** in the **+** menu). Per the docs, first make the folder available through Remote Control: in the desktop app, Settings, Code (or Claude Code), turn on 'Use this computer from your phone and claude.ai' and add the folder, or run `claude remote-control` in the folder and leave it running. Then click **Allow once** on the card Claude answers with.

Checked: Live docs fetched with curl on 2026-11-22 (claude-projects.md, 'Run a thread on your own computer'): needs Claude Code v2.1.280 or later on that computer (installed: claude 2.1.330, where `claude remote-control --help` works); the thread runs only while that computer is awake with Remote Control on, starts with the project's instructions but not its memory files, and is unavailable when 'Require trusted devices' is on for the account.

## Related

[[push-commits-before-starting-a-cloud-session-the-session-starts-from-pushed-state]]
