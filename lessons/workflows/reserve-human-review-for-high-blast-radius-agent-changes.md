---
id: reserve-human-review-for-high-blast-radius-agent-changes
created: 2026-09-13
status: active
supersedes: null
category: workflows
source_type: post
tool: claude-code
sources:
  - https://martinfowler.com/rachels-ramblings/code-review.html
---

# Name the Trigger Conditions for Human Review Instead of Reviewing Every Agent Diff

## TL;DR

Write down which agent-authored changes require a human (architectural change, security boundary, large blast radius, unfamiliar critical code, stated low confidence) and automate or auto-merge the rest.

## Why it matters

Reviewing every diff does not scale with the rate agents produce them, so an unwritten policy degrades into skimming everything equally badly. An explicit trigger list spends your attention where a mistake is expensive and lets deterministic checks cover the rest.

## How to apply

Record the trigger list in the repo's review policy, auto-merge on green outside it, and push formatting, lint and known-pattern security checks into pre-merge automation rather than manual review.

> "There are absolutely changes where I want another experienced human looking. An example would be a fundamental architectural change. ... Other examples could be something crossing a sensitive security boundary, a change with a huge blast radius, an unfamiliar part of a critical system or simply something where the team says, 'I'm not confident about this.'", Rachel Laycock, Thoughtworks
