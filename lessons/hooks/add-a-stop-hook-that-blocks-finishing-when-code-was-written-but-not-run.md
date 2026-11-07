---
id: add-a-stop-hook-that-blocks-finishing-when-code-was-written-but-not-run
created: 2026-10-11
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-built-another-andrej-karpathy-using-claude_bvGptCLDhyo_20261009.txt
---

# Add a Stop hook that blocks the answer if the agent wrote code and never ran it

## TL;DR

Nate Herk's Karpathy agent includes a hook that fires when the agent tries to finish its turn and sends it back with one message if code was written but not run.

## Why it matters

It bakes a verification loop in so the agent runs, tests and fixes before you see the final result. In his demo a script that worked in Claude's test crashed on an emoji under a normal Windows terminal, which running it that way revealed.

## How to apply

Ask Claude Code to write the hook for you with a prompt like 'if you wrote code and never ran it, block the answer with: you have to run this before you say it works'. Register it on the Stop event in settings (inference: Nate does not name the event, only that it runs when the agent tries to finish its turn).

Checked: Stop appears 36 times as a quoted string in the 2.1.296 binary; event name is inference from 'fires when the agent tries to finish its turn'
