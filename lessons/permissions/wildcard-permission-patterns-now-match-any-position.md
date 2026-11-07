---
id: wildcard-permission-patterns-now-match-any-position
created: 2026-09-01
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# Wildcards in Permission Rules Now Match at Any Position, Not Just the End

## TL;DR

You can now put a wildcard anywhere in a Bash permission pattern, e.g. allow any install command or any git subcommand, instead of only being able to wildcard the trailing portion.

## Why it matters

Previously you had to enumerate every prefix variant you wanted to allow; a mid-pattern wildcard lets one rule cover a whole family of commands sharing a keyword anywhere in the string.

## How to apply

In your settings.json permissions, write a wildcard at any position in the pattern, e.g. an allow rule matching any command containing 'install' or any 'git *' subcommand, instead of only anchoring the wildcard at the end.

## Related

[[match-tool-parameters-in-permission-rules]]
