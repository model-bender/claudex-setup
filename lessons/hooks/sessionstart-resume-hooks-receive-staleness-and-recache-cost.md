---
id: sessionstart-resume-hooks-receive-staleness-and-recache-cost
created: 2026-08-31
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Branch SessionStart Resume Hooks on Session Staleness and Estimated Re-Cache Cost

## TL;DR

Since 2.1.251, SessionStart hooks firing on resume receive the session's staleness and the estimated re-cache cost, so a resume hook can decide whether reinjecting context is worth it instead of always paying for it.

## Why it matters

A resume hook that always reinjects context pays the injection cost on every resume, even when the session is fresh and the cache is still warm. With staleness and estimated re-cache cost handed to the hook as inputs, that decision can finally be made per resume rather than hardcoded.

## How to apply

In a SessionStart hook matched on resume, read the session staleness and estimated re-cache cost values the hook now receives and branch on them: skip reinjection for a fresh session, reinject for a stale one. Available since Claude Code 2.1.251, per the changelog: SessionStart resume hooks now receive session staleness and the estimated re-cache cost.

## Related

[[gate-model-switches-with-a-premodelswitch-hook]]
