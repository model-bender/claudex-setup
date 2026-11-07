---
id: shared-scratchpad-file-for-subagent-observability-and-synthesis
created: 2026-07-10
status: active
supersedes: null
category: agents
sources:
  - transcripts/mark-kashef/how-i-built-an-ai-council-with-claude-code-subagents_LpM1dlB12-A_20260703.txt
---

# Give Parallel Subagents a Shared Scratchpad File to Observe Them and Synthesize Without Sycophancy

## TL;DR

Have each parallel subagent append its reasoning, key insights, and confidence to one shared markdown file, so you can watch otherwise-opaque subagents mid-run and then have the main session read the file and weigh their independent conclusions instead of rubber-stamping its own.

## Why it matters

Subagents run in isolated contexts and only return a final summary, so you're normally blind to their progress until they finish; a shared append-only file is a lightweight, non-intimidating observability window, and feeding three independent virgin-context conclusions back to the main model lets it neutrally synthesize perspectives rather than defaulting to 'you're absolutely right.'

## How to apply

Instruct each subagent (e.g. optimist / devil's-advocate / neutral council) to document its thinking and confidence to shared_reasoning.md as it works, and persist that instruction in CLAUDE.md so it holds as you add more agents; then have the main session read the file and give one synthesized recommendation. You can also have them stress-test each other's entries in a second parallel pass.
