---
id: run-autocompact-200k-behind-a-gateway-that-stops-at-200k
created: 2026-10-02
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21285
---

# Run `/autocompact 200k` if your gateway only serves 200K, custom base URLs now assume 1M

## TL;DR

Behind a proxy or gateway, Claude Code now assumes a 1M window for 1M-capable models, so a 200K-limited gateway fails mid-session unless you cap it.

## Why it matters

Auto-compact fires late, near 1M, so a gateway that rejects over 200K errors out before compaction ever triggers.

## How to apply

Run `/autocompact 200k`, or set `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` (2.1.287 names it for Bedrock, Vertex, Foundry and the apps gateway).

Verified: `command grep -c -a '/autocompact' 2.1.287` returned 5. Library has set-a-fixed-token-auto-compact-window (the mechanism) but not this proxy default change.

> "Changed sessions behind a custom `ANTHROPIC_BASE_URL` to use the 1M context window of models that have one (Opus 4.7+, Sonnet 5+, Fable); run `/autocompact 200k` if your gateway stops at 200K", Claude Code CHANGELOG 2.1.285

Corrected 2026-10-02: since 2.1.288 the window is saved per model, so run `/autocompact 200k` once for each model you use behind that gateway.

> "Changed `/autocompact` to save the auto-compact window per model, so each model keeps its own setting when you switch", Claude Code CHANGELOG 2.1.288
