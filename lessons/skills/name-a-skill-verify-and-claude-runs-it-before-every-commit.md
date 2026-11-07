---
id: name-a-skill-verify-and-claude-runs-it-before-every-commit
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21286
---

# Name a skill `verify` and Claude runs it right before every code commit

## TL;DR

A project or user skill called exactly `verify` makes Claude run it right before committing code, with no CLAUDE.md rule needed. It is an instruction to Claude, not an enforced block.

## Why it matters

It replaces a CLAUDE.md line asking for tests before `git commit`, and it skips docs-only and tests-only commits on its own. It does not replace a PreToolUse hook: the changelog says Claude "is now told to run it", so keep a hook where a commit must never land without a passing run.

Corrected 2026-10-03: an earlier version called the skill a pre-commit gate that replaces a PreToolUse hook. The source describes guidance to the model, not a blocking mechanism.

## How to apply

Create `.claude/skills/verify/SKILL.md` that runs your tests, lint and build; keep the name exactly `verify`.

Verified: Changelog 2.1.286 entry read from the saved raw CHANGELOG. The 2.1.287 binary carries the related pre-ship guidance as templated text with the same exemptions ('Skip for docs-only or test-only changes'). Not exercised live.

> "Improved commit guidance: when your project or user skills include one named `verify`, Claude is now told to run it right before committing, except for docs-only and tests-only commits", Claude Code CHANGELOG 2.1.286
