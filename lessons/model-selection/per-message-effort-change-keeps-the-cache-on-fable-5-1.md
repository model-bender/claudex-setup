---
id: per-message-effort-change-keeps-the-cache-on-fable-5-1
created: 2026-09-12
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-anthropic-actually-prompts-fable-5-1_FBVNS1l5Vb8_20260910.txt
---

# On Fable 5.1, Change Effort Per Message and Keep the Prompt Cache

## TL;DR

Fable 5.1 supports a per-message effort change that preserves the prompt cache. On other models, running later turns at a different effort means setting a new top-level value on the request, which invalidates it.

## Why it matters

The standing rule is to never touch the model or effort dial mid-session, because both live in the cached prefix and changing either reprocesses the whole history uncached, which is why the usual workaround is to delegate the odd step to a subagent. Fable 5.1 relaxes that for effort specifically, so one genuinely hard turn inside an otherwise cheap conversation no longer costs a full re-cache. The model half of the rule still stands.

## How to apply

On Fable 5.1, raise effort for the single turn that needs it and drop it back afterwards, rather than pinning the session high or spinning up a subagent. On other models keep effort changes at session boundaries or delegate the step.

## Related

[[spawn-a-subagent-instead-of-switching-model-mid-session]], [[prompt-cache-what-breaks-it]], [[max-effort-is-a-trap-quality-plateaus-at-high]]
