---
id: allow-skill-by-name-before-loop-or-scheduled-runs-use-it
created: 2026-11-15
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Add Skill(name) to permissions.allow before a /loop or scheduled task runs a skill that declares allowed-tools or hooks

## TL;DR

A skill whose frontmatter has allowed-tools or hooks now stops a scheduled task or /loop at a prompt unless you pre-allow it.

## Why it matters

Existing unattended jobs that call such a skill start stalling after the update, with no obvious cause. A neighbouring 2.1.325 entry says the same about "Always allow" rules in Desktop, IDE and SDK hosts.

## How to apply

For each scheduled or looped job, list the skills it calls, check their frontmatter for `allowed-tools` or `hooks`, and add `Skill(<name>)` to `permissions.allow`.

Checked: the `Skill(` rule form appears in the installed Claude Code 2.1.325 binary (9 hits); it is a permission pattern, not a flag.

> "Changed scheduled tasks and `/loop` to ask before running a skill that declares `allowed-tools` or hooks; add `Skill(name)` to `permissions.allow` to run it unattended", Claude Code CHANGELOG 2.1.325

## Related

[[loop-command-for-recurring-in-session-tasks]]
