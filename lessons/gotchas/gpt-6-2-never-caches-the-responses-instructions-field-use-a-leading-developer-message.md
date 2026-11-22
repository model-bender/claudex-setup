---
id: gpt-6-2-never-caches-the-responses-instructions-field-use-a-leading-developer-message
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: codex
source_type: post
sources:
  - https://x.com/bebuu_ai/status/2123291268814094409
  - https://github.com/openai/codex/issues/62312
  - https://x.com/steipete/status/2123487048250327497
---

# On GPT-6.2 Sol and Astra, put the system prompt in a leading developer message, not the Responses instructions field, or it never caches

## TL;DR

When building or configuring a custom harness on the Responses API with GPT-6.2 Sol or Astra, send the system prompt as a leading developer message inside input, because the top-level instructions field stays at 0 cached tokens.

## Why it matters

A 64K to 72K system prompt is billed at full price every step; the issue reports cache hit rate falling from 97.4% to 46.4% moving from 6.1 Sol to 6.2 Sol, and the cache diagnostics wrongly report a hit, so the problem hides unless you read cached_tokens.

## How to apply

Check usage.input_tokens_details.cached_tokens on step 2 and later; if it is 0 while you use instructions, move the same text into a leading developer message in input (the workaround the issue's table verifies). Steinberger says harnesses are mostly not updated yet.

Checked: Read the live openai/codex issue 62312 via gh (state OPEN, created 2026-11-18): body says instructions is never written to or read from the prompt cache on gpt-6.2-sol and gpt-6.2-astra, and the same text as a leading developer message caches from step 2. Post text and UTC date verified via api.fxtwitter.com. Not tested against the live API (paid).

> "OpenAI Codex issue #62312 found that on GPT-6.2 Astra and Sol, anything placed in the top-level instructions field of a Responses API request isn't actually cached.", @bebuu_ai on X, citing openai/codex issue 62312

## Related

[[prompt-cache-what-breaks-it]]
