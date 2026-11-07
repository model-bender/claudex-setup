---
id: delegate-all-execution-off-fable-to-preserve-its-separate-weekly-cap
created: 2026-08-22
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
---

# Keep Fable Purely Orchestrating and an All-Day Build Costs ~7% of Its Weekly Cap

## TL;DR

Fable's usage limit is separate and small; if you forbid it from writing or running anything and make it delegate every implementation task to Opus/Sonnet subagents, a full day of agent work consumes single-digit percentages of that cap.

## Why it matters

Nate Herk built an entire SaaS app (Next.js + Supabase + Stripe, ~55 commits, 8 hours) with Fable 5 as project manager and checked the meter three times: 3% of the weekly Fable limit after the first phase, ~4% mid-build, 7% at the end. His framing is explicit: 'because Fable isn't doing this, because it's Opus or Sonnet doing all this, our limit is going to last a lot longer' - versus 'hey Fable, go build me an app', which 'uses all of those tokens and becomes very expensive very quick.' This is the quota argument for the pure-delegator pattern, distinct from the context argument in [[pure-delegator-orchestrator-preserves-context-across-a-long-session]]: even if context weren't a constraint, the economics alone justify keeping the expensive model off the keyboard.

## How to apply

Open the session on Fable and state the constraint in the first prompt: 'You are the project manager. You are not the executor. Delegate work to sub agents using Opus or Sonnet, whichever fits the complexity - you decide whether to use subagents, agent teams, dynamic workflows, or worktrees.' Give it the plan document as the source of truth and require each delegated worker to write progress back to the plan (or its own status folder) so the orchestrator can track state without re-reading code. Let the orchestrator choose the parallelisation mechanism rather than prescribing it. Once the plan exists and the delegation is running, you can drop back to Opus for the follow-up conversation - Nate switches back explicitly, noting 'we really don't need Fable to be doing this.'

## Related

[[pure-delegator-orchestrator-preserves-context-across-a-long-session]], [[make-delegated-workers-write-progress-back-to-the-plan]]
