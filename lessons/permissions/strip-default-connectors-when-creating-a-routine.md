---
id: strip-default-connectors-when-creating-a-routine
created: 2026-08-29
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/simon-scrapes/19-claude-code-mistakes_icM0ewXGvAw_20260824.txt
---

# Strip the default connectors when you create a routine

## TL;DR

A new routine gets every one of your connectors attached by default, so each scheduled run can reach all of your tools and pays context for their definitions; remove every connector the routine doesn't need at creation time, and retro-edit existing routines to redact access.

## Why it matters

Full tool access on an unattended scheduled run is the worst place for it: nobody is watching when the routine acts, and a routine that only summarizes a feed has no business holding your email or database connectors. It also costs money, because the attached connectors' definitions and metadata load into the routine's context on every run. The default is silently maximal, so unless you actively prune, every routine you've ever created is over-privileged right now.

## How to apply

In the desktop app (or your Claude account), go to code, then routines. When setting up a new routine, all connectors are added by default; walk the list and remove every one the routine doesn't need before saving. Then audit existing routines the same way, opening each and removing connector access it never uses.

## Related

[[wire-cloud-scheduled-tasks-through-connectors-not-local-files-or-keys]], [[scope-tool-access-not-just-the-prompt-to-restrict-agent-actions]]
