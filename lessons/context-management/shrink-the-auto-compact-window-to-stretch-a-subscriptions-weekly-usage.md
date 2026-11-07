---
id: shrink-the-auto-compact-window-to-stretch-a-subscriptions-weekly-usage
created: 2026-10-19
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1x5vtb1/forcing_context_window_to_250k_has_dramatically/
  - https://www.reddit.com/r/ClaudeAI/comments/1x5vtb1/forcing_context_window_to_250k_has_dramatically/pgr132e/
  - https://www.reddit.com/r/ClaudeAI/comments/1x61pdw/3_months_on_max_20x_585_paid_17305_at_api_prices/
  - https://www.reddit.com/r/ClaudeCode/comments/1x7ifnd/i_went_from_exhausting_claude_codes_weekly_limits/
  - https://www.reddit.com/r/ClaudeCode/comments/1x6qgsc/small_habits_that_cut_my_token_usage_a_lot/pgxpmgv/
---

# Shrink the Auto-Compact Window to Stretch a Subscription's Weekly Usage

## TL;DR

Most of a long session's cost is cache reads of its own history, re-sent on every turn, so lowering the auto-compact window from 1M to about 250K (`/autocompact 250k`) keeps each turn small. One Max 20x user reports it turned a weekly limit that ran out in about 2 days into one that lasts the week.

## Why it matters

The cost shape is measured, not guessed: one user's three months of transcripts priced at API rates were dominated by cache reads ("33.4B tokens read from cache"), and 20 sessions out of 691 accounted for $16,047 of the $17,305 total. A session that runs for days pays for its entire history on every step, which dwarfs savings from lowering effort. This is the cost argument for a fixed window; the quality argument is in the lesson on setting a fixed token window.

## How to apply

Run `/autocompact 250k` (one reply in the thread suggests exactly this; the poster does not say how they set it, and another user cut to 400K as one of four changes, so neither isolates the window's effect). The window is saved per model since 2.1.288, so set it once on each model you use. Prefer handing off to a fresh session over letting one session run for days. Checked against Claude Code 2.1.303: `/autocompact` takes a token count, and the changelog says "Changed `/autocompact` to save the auto-compact window per model" (2.1.288). The usage effect is user-reported, not measured here.

> "Now that I have forced the context window to 250k down from 1M my usage lasts the whole week again.", u/Standard-Reply-04 on r/ClaudeAI

> "Almost all of the cost is cache reads: 33.4B tokens read from cache over the period. Every turn re-sends the whole conversation, so a session that runs for days pays for its entire history on every turn.", u/dspv on r/ClaudeAI

## Related

[[set-a-fixed-token-auto-compact-window]], [[set-autocompact-once-for-each-model-you-use]], [[dedupe-on-message-id-when-summing-tokens-from-claude-code-transcripts]]
