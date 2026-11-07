---
id: cap-haiku-5-5-autocompact-at-100k-on-api-billing
created: 2026-10-11
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://x.com/lydiahallie/status/2107898889508700209
  - https://x.com/bcherny/status/2107909939025052107
---

# On API Billing, Cap Haiku 5.5's Auto-Compact Window at 100K to Stay in the Cheaper Pricing Tier

## TL;DR

On API billing, setting Haiku 5.5's auto-compact window to 100K keeps it in the cheaper token pricing tier, and because the window is saved per model it only affects Haiku (subagents included).

## Why it matters

Boris Cherny adds that at 100K context Haiku 5.5 is 10x cheaper than Haiku 4.5. The per-model save means the cap does not shrink your Opus or Sonnet sessions.

## How to apply

Run `/model haiku`, then `/autocompact 100k`. This matters on API billing; on a subscription plan the pricing tier does not apply (inference).

> "If you're on API billing, you can set Haiku 5.5's autocompact window to 100K so you stay in the cheaper token pricing tier! It's saved per model so this only applies to Haiku (incl. subagents) > /model haiku > /autocompact 100k", Lydia Hallie

> "Haiku 5.5 is a good Haiku. With 100k token context, it's also 10x cheaper than Haiku 4.5", Boris Cherny

## Related

[[set-autocompact-once-for-each-model-you-use]], [[set-a-fixed-token-auto-compact-window]]
