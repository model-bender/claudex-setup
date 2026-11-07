---
id: tell-fresh-session-not-to-act-until-instructed-after-handoff
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
---

# After Pasting a Handoff Summary Into a Fresh Session, Tell It Not to Act Yet

## TL;DR

When you copy a handoff summary into a newly cleared session, explicitly say 'don't do anything yet until I tell you' so the agent doesn't rush into stale next-steps.

## Why it matters

The creator did this deliberately after clearing context and pasting a handoff message into both a fresh Claude session and a fresh Codex session: 'I just wanted to read that and get familiarized with what's going on... don't do anything yet until I tell you what to do.' Without that line, a fresh session tends to treat the pasted summary's implied next steps as a go-ahead and starts acting on assumptions that may already be outdated.

## How to apply

After pasting a handoff/summary block into a new or cleared session, append an explicit instruction like 'read this for context only, take no action until I give you the next task.'

## Related

[[persist-plan-findings-and-failures-in-a-three-file-memory-pattern]]
