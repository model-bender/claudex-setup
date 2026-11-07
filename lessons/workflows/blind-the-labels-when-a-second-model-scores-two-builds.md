---
id: blind-the-labels-when-a-second-model-scores-two-builds
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/i-had-fable-5-1-and-5-build-me-the-same-app_5FukkI4fbiU_20260910.txt
  - transcripts/nate-herk-ai-automation/i-made-codex-and-claude-code-build-the-same-app-one-clearly-won_WCrnS09vpfo_20260820.txt
---

# Strip the Labels Before Asking a Second Model to Compare Two Builds

## TL;DR

When a second agent evaluates two versions of the same thing, hand it unlabelled targets (two ports, two directories, session logs relabelled Agent A and Agent B) and never say which model, harness or approach produced which. Ask for per-dimension scores plus a strengths list, not an overall winner.

## Why it matters

A labelled comparison invites the evaluator to reason from reputation rather than from the artefact in front of it, and the label is the one input that has nothing to do with the work. The same blinding protects you from your own bias while you click through the two versions.

Nate Herk ran two builds of the same spec and had Codex test both, identified only as port 4382 and port 5321: 'I had Codex open these two up and I didn't tell which was which.' It came back with a weighted score per dimension and a concrete per-version strengths list, including one behavioural difference he had not spotted, that rejecting an approval falsely reported mitigation in one build.

The same shape works on session logs rather than running apps. After running an identical task in both harnesses, one creator consolidated each session end to end, stripped anything identifying the tool, and handed the pair to Codex as Agent A and Agent B. The output was a per-category scorecard rather than a verdict: product judgment and scope to Claude Code (clear must versus defer decisions, against Codex's 135 capabilities with less restraint), architecture and execution to Codex (immutable revisions, offline recovery, migration safety, concurrency handling), testing and reliability to Codex by a wide margin (cross-browser, property tests, fault injection), efficiency to Claude Code at 9.0 versus 5.5. That the judge was one of the competitors and still named its rival the overall winner is what makes the result credible rather than self-serving: judgments against the judge's own interest are the ones worth trusting.

## How to apply

Serve the two versions on neutral identifiers: ports or directory names with no model or branch in them, or logs relabelled Agent A and Agent B. Strip branding baked into the built artifact too, not just the filename.

Prompt for exercise, not opinion: 'I gave two agents the same spec, here is what they built, test the heck out of them and tell me what is better about each one.' Ask for per-dimension scores plus a strengths list rather than a single winner, because the category verdicts are the reusable output (see [[route-work-between-claude-code-and-codex-by-task-type]]).

Reveal the mapping only after the report exists, and weigh the result against cost and wall-clock before calling anything a win. Re-run the exercise on model releases: one creator notes the shape of his previous results reversed, having previously found Codex the faster and leaner of the two.

## Related

[[separate-evaluator-agent-exercises-the-running-app]], [[subagent-per-competing-approach-then-main-session-decides]], [[route-work-between-claude-code-and-codex-by-task-type]]
