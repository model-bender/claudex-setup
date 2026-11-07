---
id: run-true-ralph-loops-with-ralph-tui-or-a-bash-script
created: 2026-08-31
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/sean-kochel/how-to-run-a-ralph-loop-step-by-step_7TwIrPQnFfg_20260702.txt
---

# Run True Context-Reset Ralph Loops With ralph-tui or a Bash Script

## TL;DR

For Ralph loops that genuinely spawn a fresh context window per iteration, use a bash script or ralph-tui (bun install -g ralph-tui), which adds a guided create-PRD to task-list flow and a per-run iteration cap you can raise or lower to pull the plug when a loop stalls.

## Why it matters

The defining property of a Ralph loop is a clean context window per pass that reads only the task file's state; without it, iterations accumulate context and degrade the way one long session does. A managing tool with a per-run iteration cap also gives you a lever to stop a stalled loop rather than letting it keep burning quota.

## How to apply

Install with bun install -g ralph-tui and drive loops through its guided create-PRD and task-list flow, or write a bash script that relaunches a fresh session each pass. Whichever tool you pick, verify it actually starts a fresh window per iteration before trusting it for long autonomous runs.

## Related

[[official-ralph-plugin-does-not-reset-context]]
