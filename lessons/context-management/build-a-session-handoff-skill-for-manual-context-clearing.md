---
id: build-a-session-handoff-skill-for-manual-context-clearing
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
  - transcripts/nate-herk-ai-automation/claude-just-destroyed-every-video-editing-tool_ZNbgOhxhzXg_20260624.txt
---

# Build a 'Session Handoff' Skill That Outputs a Paste-Back Summary Before You Clear Context

## TL;DR

Before you /clear a session, have Claude write a handoff summary (what was built, the decisions taken, where the files live, what is next), copy it, clear, then paste it back as the first message of the fresh session. Package the ask as a reusable 'session-handoff' skill so you get the same structure every time.

## Why it matters

Clearing without a handoff loses the plan and the file locations. Continuing without clearing keeps paying for everything already in the window. The summary is what lets you do both.

Two creators land on the identical move from different work. One ran it mid-build at roughly half the context window: "I'm going to use a skill called session handoff, which is basically just going to give us a summary of what's been done, files that are important so that I can clear the session and paste it back in." The other hit 263k of a 1M token budget in a video-render back-and-forth and asked for "a summary of everything you've built and where the different files are so I can clear the session."

Packaging it as a skill rather than retyping the ask is the part worth copying: it fixes the structure, so you get the same four sections every time instead of whatever the model feels like summarising that day. It is also the manual alternative to a built-in handoff or recap command, for when you want control over exactly what carries forward.

## How to apply

Write a skill (for example `session-handoff`) that instructs the model to produce a structured summary: what was accomplished, decisions locked in, key file paths, and open next steps. Invoke it before /clear, copy its output, then paste it as the first message of the new session.

Ad hoc, the prompt is "give me a summary of everything you've built and where the different files are so I can clear the session."

Two things to pair with it: ask for the handoff written as a prompt for the next session rather than as a summary for a human, and tell the fresh session to read it for context and take no action until you say so.

## Related

[[write-the-handoff-as-a-prompt-for-the-next-session]], [[tell-fresh-session-not-to-act-until-instructed-after-handoff]], [[handoff-or-clear-context-at-half-window]], [[persist-plan-findings-and-failures-in-a-three-file-memory-pattern]]
