---
id: open-untrusted-material-in-a-claude-restricted-session
created: 2026-08-29
status: active
supersedes: null
category: permissions
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Read Untrusted Material With claude --restricted, Which Strips Every Command-Running Tool

## TL;DR

When a session's job is to read attacker-influenced content (a scraped page, a downloaded archive, a third-party repo), launch it with `claude --restricted` so there is no shell to hijack, instead of relying on permission prompts or the auto-mode classifier.

## Why it matters

`--restricted` is a capability removal, not a policy check: it drops the command-running tools and `WebFetch`, keeps file tools inside the working directory, and refuses `bypassPermissions`. Crucially it also ignores user, project, and local settings files, so a malicious repo's own `.claude/settings.json` or hooks cannot re-widen the session.

## How to apply

Run `claude --restricted` (or set `CLAUDE_CODE_RESTRICTED=1`) for triage and reading sessions over untrusted input; re-add a specific tool only by naming it in `--tools`. Available since 2.1.248.

> "Added `--restricted` (or `CLAUDE_CODE_RESTRICTED=1`): removes the built-in tools that run commands or code and `WebFetch` (unless named in `--tools`), keeps file tools inside the working directory, refuses `bypassPermissions`, and ignores user, project and local settings files", Claude Code CHANGELOG 2.1.248

## Related

[[auto-mode-is-not-injection-containment-isolate-the-session]], [[never-run-agent-written-scripts-from-inside-an-untrusted-archive]]
