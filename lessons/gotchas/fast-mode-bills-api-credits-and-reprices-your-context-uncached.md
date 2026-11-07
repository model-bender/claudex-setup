---
id: fast-mode-bills-api-credits-and-reprices-your-context-uncached
created: 2026-08-29
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/19-claude-code-mistakes_icM0ewXGvAw_20260824.txt
---

# Fast mode bills API credits, sticks across sessions, and re-pays your whole context uncached

## TL;DR

Fast mode (~2.5x speed, runs on Opus) has two cost traps: it bills your API usage credits rather than your subscription plan and stays on by default across sessions until you type "fast off"; and the first time you enable it mid-conversation, your entire accumulated cached context is repriced at the full fast-mode uncached input rate.

## Why it matters

Both traps are invisible until the bill arrives. Because fast mode persists across sessions, one experiment can leave every subsequent conversation burning API credits while you believe you're on your plan; Claude even auto-disables it if usage credits aren't enabled, which is the tell that it's credit-billed. The mid-conversation trap is worse: prompt caching had been making each message cheap, and flipping fast mode invalidates that cache, so a 100k-token conversation instantly costs the full uncached fast-mode input price for all of it.

## How to apply

Treat fast mode as something you enable at the start of a fresh, short conversation, not toggle mid-task. Watch for the fast-mode symbol in the UI to know it's active, and explicitly type "fast off" when done, since it survives session switches. If a conversation already carries heavy context, finish it at normal speed rather than converting the whole cache to uncached fast-mode input.

## Related

[[avoid-the-1m-context-model-without-usage-credits]], [[prompt-cache-what-breaks-it]], [[check-the-per-model-usage-breakdown-after-a-long-autonomous-run]]
