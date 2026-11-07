---
id: disable-1m-context-now-clamps-every-native-1m-model
created: 2026-08-07
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Expect CLAUDE_CODE_DISABLE_1M_CONTEXT to Bite on Any Native-1M Model Now, Not Just a Fixed List

## TL;DR

`CLAUDE_CODE_DISABLE_1M_CONTEXT` used to apply only to a hardcoded model list; as of 2.1.223 it holds every Claude model with a native 1M window to 200K via auto-compaction, and a startup warning appears when auto-compaction is not actually holding the session to 200K.

## Why it matters

The change cuts both ways. If you set the variable for cost control on a 1M model that was not on the old list, it silently did nothing and you were running with the full window. Now it applies, so a session you expected to hold a large context will start compacting instead. The new startup warning is the useful half: the failure case is surfaced rather than turning into a silent context blowout.

## How to apply

On a native-1M model such as Opus 5 (1M context), stop treating this variable as a no-op just because the model is not an older one. Check whether it is set before diagnosing unexpected compaction, and watch for the startup warning if you depend on the 200K cap actually holding.

> "Changed `CLAUDE_CODE_DISABLE_1M_CONTEXT` to hold every Claude model with a native 1M window to 200K via auto-compaction, not just a fixed list; a startup warning now appears when auto-compaction isn't holding the session to 200K", Claude Code CHANGELOG 2.1.223

## Related

[[avoid-the-1m-context-model-without-usage-credits]]
