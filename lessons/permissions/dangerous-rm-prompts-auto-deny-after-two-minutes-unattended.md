---
id: dangerous-rm-prompts-auto-deny-after-two-minutes-unattended
created: 2026-09-24
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Unattended Auto and Bypass Sessions Now Auto-Deny a Dangerous rm After Two Minutes

## TL;DR

Since 2.1.281 the dangerous-rm prompt in auto mode and `--dangerously-skip-permissions` waits two minutes, then denies the command with a rewrite hint so an unattended run keeps going instead of hanging on the prompt.

## Why it matters

Before this, a flagged `rm` in an unattended run either blocked forever on a prompt nobody would answer or, in the command-substitution case, ran unprompted. Now the run survives, but the removal silently does not happen, so a cleanup step can be skipped while the job reports success.

## How to apply

In unattended runs, check the transcript or output for the denied-rm rewrite hint rather than assuming a cleanup ran, and write removals with a guarded target (the prompt suggests a `${VAR:?}` guard) so they are not flagged. Set `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1` only if you want the old wait-forever behaviour. Checked: the variable has 4 occurrences in the installed 2.1.281 binary.

> "Changed the dangerous `rm` prompt in `--dangerously-skip-permissions` and auto mode to wait 2 minutes for an answer, then deny the command with a rewrite hint so unattended sessions keep going (`CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1` turns this off)", Claude Code CHANGELOG 2.1.281

## Related

[[rm-of-command-substitution-output-now-always-prompts]]
