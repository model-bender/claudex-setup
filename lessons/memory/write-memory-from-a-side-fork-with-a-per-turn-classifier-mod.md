---
id: write-memory-from-a-side-fork-with-a-per-turn-classifier-mod
created: 2026-10-19
status: active
supersedes: null
category: memory
tool: claude-code
sources:
  - transcripts/ray-amjad/most-claude-code-mods-are-toys-these-are-for-agentic-engineers_Od9706XIXcc_20261013.txt
---

# Move Memory Updates Out of the Main Session With a Per-Turn Classifier Mod

## TL;DR

Build a mod where a Haiku classifier checks each prompt for 'the user wants this remembered', and on a match a forked conversation writes the memory files while the main agent keeps on the task.

## Why it matters

Ray Amjad's demo: telling Claude to remember a latency target made Haiku classify the message, a pane showed 'memory updating', and the fork changed a MEMORY file and added a new one. The main session no longer has to do the task and the bookkeeping together.

## How to apply

1. Ask Claude (with the plugin-authoring skill) for a mod with a per-turn classifier plus a fork that writes memory files if it matches. 2. /reload-plugins. 3. Say something like 'remember that I want the ClickHouse P99 latency under 50 ms' and open the pane to see which files changed. The same idea is a custom alternative to the built-in memory, not a replacement for checking what it wrote. Checked: claude 2.1.303 binary lists model.classify and model.fork plugin calls; the demo outcome is the speaker's.

## Related

[[gate-a-fork-behind-a-small-model-classifier-after-every-turn]], [[disable-auto-memory-when-you-run-your-own]]
