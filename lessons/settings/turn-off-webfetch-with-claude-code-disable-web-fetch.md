---
id: turn-off-webfetch-with-claude-code-disable-web-fetch
created: 2026-10-02
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21285
---

# Turn off WebFetch entirely with `CLAUDE_CODE_DISABLE_WEB_FETCH`

## TL;DR

One env var removes WebFetch without writing a deny rule.

## Why it matters

For confidential work or locked-down automation, a variable is simpler than a permissions entry and cannot be allow-listed around.

## How to apply

Set `CLAUDE_CODE_DISABLE_WEB_FETCH=1` in the settings `env` block or the launching shell.

Verified: `command grep -c -a 'CLAUDE_CODE_DISABLE_WEB_FETCH' 2.1.287` returned 10. Library grep found nothing.

> "Added `CLAUDE_CODE_DISABLE_WEB_FETCH` environment variable to turn off the WebFetch tool", Claude Code CHANGELOG 2.1.285
