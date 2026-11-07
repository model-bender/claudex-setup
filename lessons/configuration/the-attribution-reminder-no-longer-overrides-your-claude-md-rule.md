---
id: the-attribution-reminder-no-longer-overrides-your-claude-md-rule
created: 2026-09-13
status: active
supersedes: null
category: configuration
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Re-Verify Your No-Attribution Rule Actually Holds, It Was Being Overridden Before 2.1.269

## TL;DR

A CLAUDE.md or memory rule banning commit and PR attribution could be silently overridden by Claude Code's own attribution reminder until 2.1.269; only managed settings can still force attribution now.

## Why it matters

If you wrote a never-add-Co-Authored-By rule and assumed it was honoured, it may not have been, and the failure was invisible because the line simply appeared anyway. Knowing the cause matters: attribution surviving after 2.1.269 means a managed-settings policy, not an ignored instruction file.

## How to apply

Upgrade to 2.1.269 or later and check the next commit is clean. If attribution still appears, look for an organization managed-settings policy rather than rewriting your own rule. A commit-msg hook that strips the line remains the belt-and-braces guard.

> "Fixed the attribution reminder overriding a CLAUDE.md or memory rule against commit and pull request attribution; lines set by managed settings still apply", Claude Code CHANGELOG 2.1.269

## Related

[[omit-session-url-from-commits-with-attribution-setting]]
