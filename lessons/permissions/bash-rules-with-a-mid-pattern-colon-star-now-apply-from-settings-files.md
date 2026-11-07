---
id: bash-rules-with-a-mid-pattern-colon-star-now-apply-from-settings-files
created: 2026-10-02
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21282
---

# Re-check Bash rules with a mid-pattern `:*`, settings files now honor them

## TL;DR

A Bash permission rule with `:*` in the middle of its pattern used to be skipped when it came from a settings file, while `--allowedTools` honored it. Since 2.1.282 it applies from every source, with a startup warning on how it matches.

## Why it matters

A deny or allow rule you wrote with `:*` in the middle may never have fired. After the upgrade it can start blocking or allowing commands you did not expect.

## How to apply

Search your settings files for Bash rules where `:*` is not at the end of the pattern, read the new startup warning, and confirm each rule now matches what you meant, since a rule that was dormant is now live.

Verified: Read the entry in the local 2.1.282 block. Library grep: permissions/bash-input-redirection-is-not-permission-checked and tee-no-longer-bypasses-edit-deny-rules are about other rule gaps.

> "Fixed Bash permission rules with a mid-pattern `:*` being skipped in settings files while `--allowedTools` honored them; they now work from every source, with a startup warning on how they match", Claude Code CHANGELOG 2.1.282
