---
id: permission-deny-rules-hold-under-dangerously-skip-permissions
created: 2026-09-01
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/john-kim/how-i-use-claude-code-meta-staff-engineer-tips_20260307.txt
---

# Configured Permission Denies Still Apply Under --dangerously-skip-permissions

## TL;DR

Even with permission prompts fully skipped, entries you put in `/permissions` (e.g., blocking `rm -rf` or deletion mutations) still get enforced.

## Why it matters

John Kim explains that skip-permissions 'will completely just ignore it except for like anything you put into your slash permissions,' meaning you can keep a hard backstop even in yolo mode.

## How to apply

Before running with `--dangerously-skip-permissions`, add explicit deny rules via `/permissions` for destructive operations you never want auto-approved, such as `rm -rf` or database drops.

