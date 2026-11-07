---
id: keep-attribution-in-object-form-in-shared-settings
created: 2026-09-24
status: active
supersedes: null
category: configuration
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Keep `attribution` in Object Form in Any settings.json Shared Across CLI Versions

## TL;DR

2.1.281 added a single settings.json switch, `"attribution": false`, that suppresses all commit/PR attribution at once (not just the session URL sub-setting the library already covers); but writing it as a bare boolean breaks the whole settings file on older CLI versions, so any settings.json shared across machines/versions should use the object form instead.

## Why it matters

This is a stronger, more mechanical kill switch than relying on a CLAUDE.md prose rule, which this same CHANGELOG line's neighbor (2.1.269) already had to fix once because the harness's own attribution reminder was overriding CLAUDE.md instructions. It's specifically relevant to any settings.json synced across machines on different Claude Code versions (e.g. via a dotfiles repo): an older CLI encountering the bare `"attribution": false` boolean will skip loading that entire settings file rather than just ignoring the one key.

## How to apply

In a settings.json that must stay readable by older Claude Code versions, write attribution as the object form (its sub-keys are commit, pr, sessionUrl, commitTrailers) rather than the new boolean shorthand, so an out-of-date install doesn't silently drop every other setting in the file too. Checked: The `attribution` settings key and its sub-fields `["commit","pr","sessionUrl","commitTrailers"]` confirmed present in the installed 2.1.281 binary's settings schema/validation code (command grep -a -o).

> "Added `"attribution": false` in `settings.json` to hide all commit and PR attribution; older CLI versions skip a settings file that holds it, so keep the object form in files shared across versions", Claude Code CHANGELOG 2.1.281

## Related

[[omit-session-url-from-commits-with-attribution-setting]], [[the-attribution-reminder-no-longer-overrides-your-claude-md-rule]]
