---
id: read-the-agent-written-pr-description-before-you-make-anyone
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/
---

# Read the agent-written PR description before you make anyone else read it

## TL;DR

The first review pass on agent output, code *and* the generated PR description, is the author's job, not the reviewer's; ship evidence you did it.

## Why it matters

The description is the part reviewers trust most and verify least, and agents write it fluently enough to sound validated when it is not. Willison's framing is the useful one: opening an unreviewed PR delegates your work to colleagues who could have prompted an agent themselves.

## How to apply

Before opening, read the generated description end to end, keep the change small enough to review efficiently (splitting into separate commits is cheap when the agent does the git work), and attach proof you exercised it, manual testing notes, rationale for specific implementation choices, or screenshots and video of the feature working.

## Staleness

Verified still current, a social/process norm with no tooling dependency; if anything it binds harder now that background sessions open draft PRs on their own. OVERLAP TO REVIEW BEFORE WRITING: [[make-every-autonomous-pr-carry-its-own-proof]] already covers "attach the evidence" for *autonomous routine* PRs. The genuinely new claim here is narrower, the human author owns the first review pass, and the agent-written *prose* is part of what must be reviewed. If that is not enough delta, fold it into the existing lesson instead of adding a file.

> "Agents write convincing looking pull request descriptions. You need to review these too! It's rude to expect someone else to read text that you haven't read and validated yourself.", Simon Willison
