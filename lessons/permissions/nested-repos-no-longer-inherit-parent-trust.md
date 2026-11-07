---
id: nested-repos-no-longer-inherit-parent-trust
created: 2026-08-16
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Audit Repos You Cloned Inside a Trusted Directory - They Used to Inherit Trust Silently

## TL;DR

Before 2.1.232, a git repo cloned inside an already-trusted directory inherited that trust, so its `CLAUDE.md`, `.claude/settings.json`, and hooks loaded without you ever confirming it. Each repository now requires its own trust confirmation.

## Why it matters

Cloning a reference repo into a working tree, vendoring a dependency, or dropping a scratch clone under a trusted project is completely routine - and each one was a path for an untrusted repo's instructions and hook definitions to activate with no prompt. A hook is arbitrary code that runs on tool events, so this was a silent code-execution surface, not just an instruction-injection one.

After upgrading, the extra trust prompts you see for nested repos are the fix, not a regression.

## How to apply

Upgrade to 2.1.232 or later. Then audit anything cloned inside a trusted directory before that point:

```
find . -mindepth 2 -name .git -maxdepth 4
```

For each hit, check for a `CLAUDE.md`, `.claude/settings.json`, or hook definitions you never approved.

> "Fixed nested git repositories inheriting trust from a parent directory; each repository now requires its own trust confirmation", Claude Code CHANGELOG 2.1.232

## Related

[[contain-agents-at-environment-layer-not-permission-prompts]], [[codex-directory-trust-switches-on-project-local-hooks]]
