---
id: demand-objective-evidence-not-a-plausible-implementation
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-had-fable-5-1-and-5-build-me-the-same-app_5FukkI4fbiU_20260910.txt
  - transcripts/nate-herk-ai-automation/gpt-6-astra-made-this-entire-video_dT5-x3u5nCg_20260910.txt
  - transcripts/nate-herk-ai-automation/i-made-codex-and-claude-code-build-the-same-app-one-clearly-won_WCrnS09vpfo_20260820.txt
---

# Tell a Long Autonomous Run to Keep Going Until It Has Objective Evidence, Not a Plausible Implementation

## TL;DR

In the goal prompt, write the definition of done and forbid stopping at something that merely looks built: keep orchestrating until there is objective evidence the complete product works. It biases the run, it does not guarantee it, so pair it with a verification pass.

## Why it matters

Nate Herk includes the same clause in three separate multi-hour runs. In the app build it is 'do not stop at a plausible implementation, but continue orchestrating until you have objective evidence that the complete product works and is presentation ready'; in the video production it is 'do not give me a draft or a POC, give me a finished working version that I can post on my YouTube channel'; in the head-to-head harness test it is 'do not stop at a prototype or first successful build, continue researching, building, testing, breaking, fixing, and retesting until the app is genuinely complete'.

The default stopping condition for a long autonomous run is 'the tasks I listed are done', which is satisfied by code that exists and was never exercised, and on a run measured in hours you do not find that out cheaply.

It is a bias, not a guarantee. In the head-to-head run one agent still shipped a 'demo workspace' with unwired backend pieces with the clause present, which is why the clause has to be paired with something that actually checks.

## How to apply

Put two things in the prompt alongside the goal: a bulleted definition of done naming the observable outcomes, and the explicit anti-stop clause ('do not stop at a prototype, a plausible implementation, or the first successful build; keep testing, breaking, fixing and retesting until it is genuinely complete').

Say what the evidence must be (the app runs, the flow completes end to end, the file renders) so the agent has something to verify against rather than its own confidence. Add a verification instruction so it checks its own output before reporting, and do not treat the clause alone as the check.

## Related

[[evidence-clause-in-long-running-prompts]], [[validation-loop-in-claude-md-is-critical]], [[goal-verifiable-finish-lines-with-safety-caps]], [[autonomous-ui-loop-acceptance-must-exercise-rendered-ui]], [[give-autonomous-agents-a-safe-exit-on-impossible-tasks]]
