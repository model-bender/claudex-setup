---
id: bias-model-routing-audit-by-token-limit-frequency
created: 2026-09-01
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/austin-marchese/17-tricks-to-build-10x-faster-with-claude_ZzHB2mPHb2g_20260724.txt
---

# Bias a Model-Routing Audit Toward Cheaper or Stronger Models by How Often You Hit Token Limits

## TL;DR

When running an audit prompt that recommends per-skill models and context settings, tell it to bias its picks toward cheaper models if you run out of tokens often, or toward stronger models if you rarely do.

## Why it matters

The presenter's audit prompt for assigning minimum-viable models to skills includes this explicit dial: 'depending on how often you run out of tokens, you could say bias towards using cheaper or better models. Cheaper if you run out of tokens all the time, better if you rarely run out.' This tunes a one-size-fits-all model-routing audit to your actual usage pattern.

## How to apply

When asking Claude to audit your skills and recommend a model + context-fork setting for each, add a line like 'bias your recommendations toward cheaper models since I frequently hit token limits' (or the opposite if you rarely do).

## Related

[[minimum-viable-model-year-ago-test]]
