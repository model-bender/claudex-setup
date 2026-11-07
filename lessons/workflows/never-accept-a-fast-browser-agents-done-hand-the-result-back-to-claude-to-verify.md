---
id: never-accept-a-fast-browser-agents-done-hand-the-result-back-to-claude-to-verify
created: 2026-10-11
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/simon-scrapes/you-should-be-using-jev-s-browser-agent-here-s-why_zac3kEUwIlg_20261009.txt
---

# Do not accept a fast browser agent's 'done': hand the result back to Claude for an independent check

## TL;DR

In a Claude plus classifier-model browser loop, Claude must verify the goal when the classifier says done, because it can report a false done on an error page.

## Why it matters

Simon's demo (10 blog posts of competitor sites) said done in 77 seconds with 10 pages complete, but only one or two screenshots were real blog pages. He cites the browser-use team's own readme that done needs an independent verification check.

## How to apply

Design the loop so the fast model (Jev in his build) picks the action and element, scripts execute it, and Claude plans, writes any text to type and checks the finished output against the goal. Also stop and return to Claude if confidence is below the threshold (0.7 in his example) or the classifier says blocked. Keep goals short and one per page or form since the classifier sees only the last five actions.

Checked: third-party model and library (Jev, Jev ultrafast); no Claude Code mechanism named

## Related

[[ultrareview-multi-agent-verification-pattern]]
