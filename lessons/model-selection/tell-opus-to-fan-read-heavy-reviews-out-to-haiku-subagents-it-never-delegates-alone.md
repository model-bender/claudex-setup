---
id: tell-opus-to-fan-read-heavy-reviews-out-to-haiku-subagents-it-never-delegates-alone
created: 2026-11-22
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xxyc5a/does_delegating_to_cheaper_models_actually_save/
---

# For a Large Read-Heavy Review, Tell Opus to Fan the Reading Out to Haiku Subagents: Left Alone It Never Delegates

## TL;DR

In about 300 benchmark runs Opus never delegated on its own, while Opus directing Haiku subagents found more real errors on big docs checks for roughly half the cost.

## Why it matters

On an 85-page docs check Opus plus Haiku found 58 and 63 of 92 errors against 36 and 38 for Opus alone ($1.93 vs $4.11 per run); on a ~10k-line codebase and on short coding tasks delegation saved little or cost more, because each subagent rebuilds its own context.

## How to apply

For a review over a large codebase or long docs, say in the prompt to split the reading across Haiku subagents and to verify their findings itself; on small repos and short, well-tested coding tasks, let Opus work alone.

Checked: Installed 2.1.330 binary: the Agent tool's model parameter takes sonnet, opus, haiku or fable. The cost and error figures are the author's own small benchmark (mostly two runs per setup, Opus wrote the tests and judged), not verified.

> "Left alone, Opus never delegated in my runs, even on big jobs.", u/BeginningSir7334 on r/ClaudeCode

## Related

[[explore-subagents-run-on-your-main-model-route-cheap-search-to-your-own-haiku-agent]]
