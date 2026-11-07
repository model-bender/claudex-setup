---
id: pair-a-review-routine-with-a-next-day-apply-routine
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/austin-marchese/this-fixes-claude-s-biggest-problem-karpathy-s-method_4hIvG849w4Y_20260910.txt
---

# Pair a Review Routine With an Apply Routine the Next Day, or Approved Changes Sit Until the Next Cycle

## TL;DR

When a scheduled self-improvement run produces a change list you have to sign off, schedule a second run a day later in apply mode. Otherwise an approved fix waits a full cycle before anything acts on it.

## Why it matters

Austin Marchese hit this with a weekly Friday run: 'if we just have this run on Friday, it will wait until the next Friday to apply the changes, and that means I'm waiting a week with stale data that I know is an issue that is just sitting there not getting fixed.' The human approval step is what makes the loop safe, but it also means the analysis run and the application run are two different events, and a single cadence silently couples the fix latency to the review cadence. His fix is a second routine on Saturday running the same skill in apply-fixes mode against the file the Friday run wrote.

## How to apply

Give the skill a mode argument, for example '/dream full-analysis' and '/dream apply-fixes'. Schedule the analysis run on your review cadence and the apply run shortly after, and have apply mode read the previous run's output file, act only on the items you marked approved, and report what it changed. Have the analysis run also check the previous cycle's output first so nothing is proposed twice.

## Related

[[route-self-improvement-loop-changes-into-three-approval-buckets]], [[give-a-reusable-sub-skill-a-mode-argument]], [[auto-dream-memory-consolidation]]
