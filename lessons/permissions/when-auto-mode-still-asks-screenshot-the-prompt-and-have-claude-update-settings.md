---
id: when-auto-mode-still-asks-screenshot-the-prompt-and-have-claude-update-settings
created: 2026-11-15
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/austin-marchese/how-to-prompt-claude-like-the-top-1-karpathy-s-method__cSM8Xe0sd8_20261112.txt
---

# In auto mode, screenshot an approval you would always accept and ask Claude to stop asking

## TL;DR

Turn on auto mode, and whenever Claude still asks for an approval you would always grant, show it the prompt and ask why it asked and to not ask again so it updates your settings.

## Why it matters

Manually approving everything is the bottleneck on long runs. The transcript's fix is to let Claude edit its own permission settings for each repeated approval.

## How to apply

Switch to auto mode. When an approval you always accept appears, screenshot it and ask Claude why it asked and to update your settings so it does not ask again. Review the resulting permission rule (inference: the transcript does not say which settings file changes). (Inference) Keep any rule for a destructive action out of the allowlist.

Checked: auto is one of the permission modes in the installed Claude Code 2.1.325 binary; which settings file Claude edits was not stated in the transcript.

## Related

[[auto-mode-not-run-row-means-the-classifier-failed-not-a-denial]]
