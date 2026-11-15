---
id: set-auto-allow-bash-if-sandboxed-to-keep-sandboxed-bash-prompt-free
created: 2026-11-15
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Set sandbox.autoAllowBashIfSandboxed: true explicitly, because sandboxed Bash now follows the normal permission flow

## TL;DR

Turning the sandbox on no longer implies "no prompts"; the auto-allow is now opt-in via one key.

## Why it matters

Anyone who enabled the sandbox to cut permission prompts will see them return after updating to 2.1.325. A second entry says the same for managed settings: set the key in your highest-ranking managed source.

## How to apply

If the sandbox boundary is your prompt substitute, add `sandbox.autoAllowBashIfSandboxed: true` to settings. If you want the old prompts, do nothing. The docs say it holds even against a bare `Bash` ask rule.

Checked: `autoAllowBashIfSandboxed` has 15 hits in the installed Claude Code 2.1.325 binary.

> "Changed sandboxed Bash commands to follow the normal permission flow by default; set `sandbox.autoAllowBashIfSandboxed: true` to keep running them without prompts", Claude Code CHANGELOG 2.1.325

## Related

[[sandbox-mode-for-safe-exploration]]
