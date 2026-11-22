---
id: commit-deny-rules-to-project-settings-so-cloud-sessions-get-them
created: 2026-11-22
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/anthropic-just-released-the-new-rules-of-claude-code_8Pg6G5h05hk_20261120.txt
---

# Commit your deny rules to the repository's .claude/settings.json so single-repository cloud sessions pick them up

## TL;DR

Deny rules kept only in your personal settings do not reach a cloud session. Commit them to the repository's `.claude/settings.json` and every single-repository cloud session picks them up. Cloud threads in a Claude Code project and multi-repository sessions do not read them.

## Why it matters

A cloud session starts from a fresh clone of the repo, so the repo (or your organisation's server-managed settings) is where a rule must live to apply there. The video says to commit the rules 'into your project' so 'every session in the future will pick them up'; the docs narrow that to sessions with one repository.

## How to apply

Put the `permissions.deny` rules in the repository's `.claude/settings.json` and commit it. If `.claude/` is gitignored in your repo, nothing in it reaches a cloud session or a scheduled cloud routine, so the rule has to go in the routine's prompt or in a tracked settings file instead (this last sentence is this lesson's inference from the docs).

Checked: Live docs fetched with curl on 2026-11-22. settings.md, 'Settings in cloud sessions': shared project settings are 'read in a session with one repository outside a project's threads'; user and project local settings (`~/.claude/settings.json` and `.claude/settings.local.json`) are 'not read'; in a cloud thread in a project 'none of a repository's `.claude/settings.json` permission rules, hooks, or `env` apply'; a session with several repositories reads only `enabledPlugins` and `extraKnownMarketplaces`; server-managed settings do reach cloud sessions. claude-code-on-the-web.md adds that repository permission rules are ignored when managed settings set `allowManagedPermissionRulesOnly` (17 hits in the 2.1.330 binary). The transcript does not name the file and gives none of these limits.

## Related

[[push-commits-before-starting-a-cloud-session-the-session-starts-from-pushed-state]], [[deny-list-test-if-claude-gets-this-wrong-once-can-i-take-it-back]]
