---
id: claude-ai-synced-skills-lose-bash-and-file-expansion
created: 2026-08-16
status: active
supersedes: null
category: skills
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Don't Author a claude.ai Skill That Relies on `!` Bash or `@` File Expansion

## TL;DR

A skill written in the claude.ai UI and synced down to your machine loses its `!` command execution and `@` file expansion locally as of 2.1.228, so the pre-computed context those lines were supplying is silently absent.

## Why it matters

This is the classic silent no-op shape: the skill loads, runs, and looks right - only the two directives that made it useful are inert, and only on the local side, so it may still behave correctly when you test it on claude.ai. A skill whose whole job was "run `git log` and reason about the output" becomes a skill that reasons about nothing.

The same hardening also means a synced skill can no longer shadow a same-named local command or MCP prompt. If you believed a claude.ai skill was taking precedence, it may in fact be losing to your project skill.

## How to apply

Author any skill whose body uses `!`-inline-bash or `@file` directly on disk in `.claude/skills/<name>/SKILL.md`. Treat claude.ai-synced skills as prose-only, and move pre-computation into a script the skill invokes rather than into inline directives.

> "Hardened skills synced from claude.ai: they no longer shadow local commands or MCP prompts, their descriptions are sanitized and labeled, and on your machine their bodies don't run `!` commands or expand `@` files", Claude Code CHANGELOG 2.1.228

## Related

[[claude-plugin-validate-checks-a-bare-skills-directory]], [[skills-encode-lived-experience-not-obvious-behavior]]
