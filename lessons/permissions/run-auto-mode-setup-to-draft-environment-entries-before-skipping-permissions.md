---
id: run-auto-mode-setup-to-draft-environment-entries-before-skipping-permissions
created: 2026-10-19
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1x7ix85/the_permission_system_is_exhausting/ph4ledl/
---

# Run /auto-mode-setup to Draft autoMode.environment Before Reaching for --dangerously-skip-permissions

## TL;DR

Auto mode's classifier trusts only the working directory and the repo's configured remotes, so work on your own servers, buckets or org repos keeps getting blocked until it is described in `autoMode.environment`; `/auto-mode-setup` drafts those entries from your project and recent sessions for you to review.

## Why it matters

When auto mode blocks routine server work, the common reaction (and the top replies in the source thread) is to switch to `--dangerously-skip-permissions`, which throws away the classifier entirely. The blocks are usually not the classifier being strict but the classifier having no trust context for your infrastructure, which is a configuration gap with a built-in fix.

## How to apply

Run `/auto-mode-setup` in the project. It reads the project's CLAUDE.md, README, config files and git remotes, your `autoMode` and `permissions.allow` settings, and the hosts and command names from Claude's recent commands there (never your messages), then shows a draft you accept or discard as a whole; on accept it writes `~/.claude/settings.json`. Then run `claude auto-mode config` to see the effective result. Checked against the Configure auto mode docs and the 2.1.303 binary: the command needs a Pro, Max or Team plan and v2.1.228 or later (v2.1.233 on native Windows), does not run in a cloud session or with feature-flag fetching off, and the settings key is `autoMode.environment` (singular).

> "**`/auto-mode-setup`** drafts those environment entries for you from your project's CLAUDE.md, README, config and git remotes, plus the hosts and command names Claude ran in your recent sessions there. You review the draft before it's saved to `~/.claude/settings.json`. (Pro/Max/Team, v2.1.228+.)", u/kuroudo_ai on r/ClaudeCode

## Related

[[auto-mode-not-run-row-means-the-classifier-failed-not-a-denial]]
