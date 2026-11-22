---
id: try-to-break-the-app-with-a-fixed-edge-case-list
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/john-kim/building-apps-with-ai-is-hard-until-you-learn-this_8fvUXkotDPc_20261108.txt
---

# Try to break the app with a fixed list of edge cases

## TL;DR

QA by trying to break the app: no network, empty (null) states, text too big, leaving the app and coming back mid-task, killing it mid-save, an incompatible shared file, tapping buttons very fast several times, swiping quickly.

## Why it matters

These are the cases the speaker says expose real bugs; the list is concrete enough to reuse on every build.

## How to apply

Run the list by hand on each build. It can also be given to the agent as explicit test scenarios (handing it to the agent is this lesson's inference; the transcript does it by hand).

Checked: No mechanism named.

## Related

[[tell-the-codex-browser-agent-to-try-to-break-your-ui]], [[click-through-the-app-yourself-agent-browser-tests-still-ship-ui-bugs]]
