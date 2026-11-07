---
id: manual-only-skill-refusal-now-asks-you-to-run-it
created: 2026-08-07
status: active
supersedes: null
category: skills
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# On Pre-2.1.222 Versions, Check That a Gated Skill Isn't Being Reimplemented From Memory

## TL;DR

When Claude was blocked from auto-invoking a skill marked `disable-model-invocation`, it used to just replicate the skill's workflow itself. As of 2.1.222 the refusal tells it to ask you to run the skill instead.

## Why it matters

`disable-model-invocation` exists so a skill runs only when a human explicitly triggers it, which is the right gate for destructive or expensive workflows. Claude quietly reimplementing those steps from memory defeated the entire point of the gate while looking like compliance, since the skill genuinely was not invoked.

## How to apply

If you gate a skill this way and are on 2.1.222 or later, the handback now happens reliably. On an older version, do not assume the gate holds: watch whether Claude starts performing the skill's steps inline after refusing, and treat that as the gate failing rather than as helpfulness.

> "Improved the refusal when Claude tries to invoke a skill with `disable-model-invocation`: Claude is now told to ask you to run the skill instead of replicating its workflow", Claude Code CHANGELOG 2.1.222

