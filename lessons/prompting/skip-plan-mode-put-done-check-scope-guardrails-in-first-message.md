---
id: skip-plan-mode-put-done-check-scope-guardrails-in-first-message
created: 2026-10-25
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/5-claude-tips-everyone-recommends-but-shouldn-t_v9YVQoeSp-I_20261022.txt
---

# Skip Plan Mode on Opus 5.5 and Put Four Lines in the First Message: Done, Check, Out of Scope, Guardrails

## TL;DR

Plan mode mostly surfaced the assumptions Claude guessed from a thin brief. Instead, state what plan mode would have exposed up front: what done looks like, how it will be checked, what is out of scope, and what Claude must not touch.

## Why it matters

Simon's reading of the plan-mode debate: older models needed the 'don't code yet' reminder, but Opus 5.5 explores files and sequences work itself. The plan's real value was a list of assumptions you could correct before building, so you were still making the same decisions, just later. Making them before pressing enter gets the same protection without the extra round trip.

## How to apply

Write the request plus four lines. 1) Done: e.g. 'match last month's layout, with an ad spend section after the leads section'. 2) Check: e.g. 'totals must match the October sheet'. 3) Out of scope: e.g. 'don't change the summary page'. 4) Guardrails: e.g. 'stay out of the client shared folder, only work on this sheet'. If you cannot answer one of the four, ask Claude to interview you first. If you still want to see its assumptions, ask for a one-line plan before it starts. Plan mode itself (Shift+Tab twice, or /plan) remains available when you want it. Checked: Searched the installed claude 2.1.310 binary: the string /plan is present (20 hits), so the command still exists. The transcript's claims about what the Claude Code team said in September are the creator's account and were not verified. The four-line structure is the creator's recommendation, not a product feature.

## Related

[[write-a-definition-of-done-with-a-length-cap-for-narrow-tasks]], [[ask-claude-to-interview-you-with-askuserquestion-before-a-large-build]]
