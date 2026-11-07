---
id: rewind-leaves-bash-written-edits-on-disk-in-auto-mode
created: 2026-08-29
status: active
supersedes: null
category: gotchas
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/issues/87575
---

# In Auto Mode, /rewind Silently Leaves Bash-Written Edits on Disk

## TL;DR

Auto mode steers edits into `sed -i`, heredocs, and python one-liners, and the checkpoint system never sees those writes, so `/rewind` reports a successful restore while the files keep every change.

## Why it matters

The failure is invisible: you believe a rejected change is undone, keep working, and the model builds on top of it. A mixed session hides it completely, since a single tracked `Edit` call makes the restore menu look healthy while the `sed`-edited files keep their changes. As one reporter put it, "One `Edit` call anywhere makes the menu look healthy and the failure silent."

## How to apply

After any `/rewind` in an auto-mode session, run `git status` and `git diff` before continuing, and treat the diff (not the rewind confirmation) as the truth. Alternatively disable the Bash-first directive with `CLAUDE_CODE_THRIFTY_SONIC=0`, which works in a `settings.json` `env` block, not just the shell.

> "Those writes aren't tracked by the checkpoint system, so /rewind reports success but leaves every change on disk.", anthropics/claude-code issue #87575

## Related

[[auto-mode-tells-claude-to-edit-with-sed-and-heredocs-instead]], [[rewind-can-recover-a-cleared-conversation]], [[set-claude-code-thrifty-sonic-0-to-disable-bash-first-editing]]
