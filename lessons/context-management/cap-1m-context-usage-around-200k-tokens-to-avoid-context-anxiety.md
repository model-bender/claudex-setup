---
id: cap-1m-context-usage-around-200k-tokens-to-avoid-context-anxiety
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
  - transcripts/simon-scrapes/the-only-claude-code-updates-you-need-to-know-apr-2026_20260424.txt
---

# Even With a 1M-Token Model, Stay Under ~200K Tokens to Avoid Context Anxiety

## TL;DR

Citing Cognition AI's research on Devin, models near their context ceiling start taking shortcuts or leaving work incomplete ('context anxiety'). The fix is to use a 1M-context model but deliberately not go past ~200,000 tokens, or note the cap in CLAUDE.md if you lack 1M context.

Opus 4.6 shipped a 1 million token context window, removing the hard blocker on huge codebases or documents, but the explicit caveat is not to actually load a million tokens in, performance is measurably worse the fuller the window gets.

## Why it matters

Claude 4.5+ models are aware of their own context window, and that awareness itself degrades behavior as the window fills, independent of actual capability.

A bigger context window changes what's technically possible, not what's advisable; treating it as a target to fill rather than a ceiling to avoid approaching leads to worse reasoning even though nothing errors out.

## How to apply

If you have a 1M-context model, treat 200,000 tokens as your working ceiling rather than the full window. Combine this with a long plan file: periodically ask Claude Code to tick off completed items from the plan, compact the conversation, and continue by re-tagging the plan file, instead of letting the session run to the edge of context.

Use the 1M window as headroom for genuinely large single-context jobs (big codebase review, long document analysis), but keep working context as lean as possible rather than routinely loading it near capacity; if output quality degrades on a long session, that's a sign to prune context rather than push the window further.

## Related

[[tick-off-the-plan-file-then-compact-and-re-tag-it]]
