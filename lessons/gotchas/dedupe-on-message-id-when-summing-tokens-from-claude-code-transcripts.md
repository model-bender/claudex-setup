---
id: dedupe-on-message-id-when-summing-tokens-from-claude-code-transcripts
created: 2026-10-19
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1x61pdw/3_months_on_max_20x_585_paid_17305_at_api_prices/pgrzf6i/
---

# Dedupe on message.id When Summing Tokens From Claude Code Transcripts

## TL;DR

Claude Code writes one JSONL line per content block of an assistant response (thinking, text, each tool call), and every one of those lines repeats the same `usage` object, so summing `usage` over the lines of `~/.claude/projects/<project>/*.jsonl` overcounts tokens 2 to 3x.

## Why it matters

Homemade usage dashboards, "what would this cost at API prices" scripts and per-session cost reports built on the transcripts inflate spend by the number of blocks per response, and any routing or budget decision based on them is wrong by the same factor. Nothing errors: the totals just look plausible and high.

## How to apply

Group assistant lines by `message.id` and count each message's `usage` once. Checked on this machine with Claude Code 2.1.303 transcripts: three sessions had 368, 941 and 623 assistant lines but only 150, 379 and 284 distinct message ids, and the `usage` object was identical on every line of a message. Naive sums of all token types came out 2.46x, 2.44x and 2.15x the deduped totals (mostly cache reads); output tokens alone came out 2.96x, 3.78x and 3.28x. The commenter also dedupes across files because resumed sessions copy history into a new file; that half was not reproduced here (no message id appeared in more than one transcript in a 16-file sample), so check your own resumed sessions before relying on it.

> "Each assistant response shows up in the logs several times (once per content block), so I had to dedupe on message id or I was overcounting 2 to 3x.", u/ScRdX_TCU on r/ClaudeAI

## Related

[[audit-cross-tool-token-spend-with-ccusage]], [[shrink-the-auto-compact-window-to-stretch-a-subscriptions-weekly-usage]]
