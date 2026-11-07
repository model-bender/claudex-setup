---
id: tell-claude-to-re-ground-its-final-message-after-unattended-runs
created: 2026-08-07
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://x.com/alexalbert__/status/2065493229760565758
---

# Tell Claude to Write Its Final Message as a Re-Grounding, Not a Continuation

## TL;DR

On long or unattended runs, the terse shorthand Claude builds up between tool calls leaks into the final summary, which is the one message the user actually reads cold. Add an explicit instruction to write that message for a reader who saw none of the working thread.

## Why it matters

This is a more precise fix than "summarize clearly". The problem is a specific mismatch: brevity and invented shorthand are genuinely good *between* tool calls, and actively bad in the one message a user reads after an overnight run. Anthropic's own prompting guidance for Fable targets exactly that seam, and Alex Albert called the snippet the best fix he had found for output he otherwise could not keep up with.

## How to apply

Put a version of this in CLAUDE.md, a system prompt, or a skill used for long-running and background work: terse shorthand is fine between tool calls, but the final summary is for a reader who did not see any of it. Lead with the outcome in one sentence, then the one or two things you need from them, each explained as if new. Drop working shorthand, arrow chains, hyphen-stacked compounds, and any labels invented mid-run. Give each file, commit, or flag its own plain-language clause. When forced to choose between short and clear, choose clear.

> "Fable feels superhuman at working over long agentic conversations, sometimes to the point where I can't keep up with what it's telling me. This prompt snippet has been the best fix I've found for getting it to write clearly and drop any jargon:", Alex Albert

## Related

[[branch-a-confusing-reply-to-author-a-custom-output-style]], [[restate-bash-output-in-text-it-is-not-reliably-shown]]
