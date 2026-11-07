---
id: make-video-proof-mandatory-for-ui-changing-prs
created: 2026-08-16
status: active
supersedes: null
category: workflows
tool:
  - claude-code
  - codex
source_type: post
sources:
  - https://x.com/steipete/status/2088486859244741020
  - https://github.com/openclaw/openclaw/blob/main/AGENTS.md
---

# Make Video Proof Mandatory for UI-Changing PRs, Because Screenshot Self-Review Is Not QA

## TL;DR

Add a rule to AGENTS.md/CLAUDE.md making before/after screenshots or a short video mandatory PR evidence for any UI-visible change, captured from a real running surface rather than a test harness.

## Why it matters

Left to itself, the agent will claim a UI change works based on reading the code or glancing at its own screenshot, and that demonstrably misses obvious visual defects. Making the proof a *gate* rather than a suggestion is what stops "looks right to me" from being the last word.

The escape hatch matters as much as the rule: requiring the agent to state the exact blocker in the PR when proof is infeasible prevents it from quietly skipping the requirement, which is what a rule with no named exception invites.

## How to apply

Write it as a hard gate with a named escape hatch. The working version:

> "UI-visible change (Control UI, native app, or user-visible chat/session behavior): before/after screenshots or a short video are mandatory PR evidence, captured from a real running surface and sanitized."

...requiring the agent to "state the exact blocker in the PR" when proof is infeasible. For gateway or flow changes, specify Playwright `recordVideo` against the running dashboard, with "waits on asserted UI states, not sleeps."

> "Added a short instruction to our shared AGENTS MD file to upload videos to each PR that changes UI state.", Peter Steinberger

## Related

[[upload-pr-images-and-video-via-the-github-uploads-api]], [[make-every-autonomous-pr-carry-its-own-proof]], [[visual-self-validation-screenshot-grading]], [[separate-evaluator-agent-exercises-the-running-app]]
