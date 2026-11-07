---
id: branch-a-confusing-reply-to-author-a-custom-output-style
created: 2026-08-07
status: active
supersedes: null
category: configuration
tool: claude-code
about: null
sources:
  - transcripts/ray-amjad/opus-5-is-exhausting-anthropic-reveals-the-fix_szjakRcw7V0_20260807.txt
---

# When a Reply Reads as Jargon-Dense Word Salad, Branch It Into Several Rewrites and Save the One That Lands

## TL;DR

If a model's default prose is too dense or verbose to read comfortably, use /branch on that exact message to fork off the main thread, ask it to regenerate the same content in 4-5 different tones (plain-English, Slack-DM casual, Simplified Technical English, etc.), pick the one you actually understand, then have it turned into a saved output style, without burning tokens or polluting your working conversation.

## Why it matters

Output quality that's technically correct but hard to parse still costs you time, Anthropic's own team has flagged this internally and recommends output styles as the fix, but picking a style by guessing from the built-in list is hit-or-miss. Branching lets you A/B several candidate voices against a real confusing reply you already have, rather than picking blind, and doing it on a branch keeps the experiment out of the conversation you're actually trying to get work done in.

## How to apply

When output reads like noise, fork off that message into a scratch conversation (as of this writing, `/branch`; **REVISIT: this command has been renamed more than once, confirm the current one with `/help`**, see [[fork-is-now-a-background-session-subtask-is-the-in-session-fork]]), then ask for several rewrites of the same content in different registers (plain English, ASD-STE100 Simplified Technical English, casual Slack-DM style, etc.). Once one reads right, tag `@claude-code-guide` and say "turn this into an output style," then set it with `/config` → output style. Output styles persist per-project (stored in `.claude/settings.local.json`), so different projects can carry different defaults, pick Explanatory when onboarding into an unfamiliar repo, and a custom style for everyday work once you've found one that fits.

## Related

[[btw-command-ask-questions-without-polluting-context]], [[fork-is-now-a-background-session-subtask-is-the-in-session-fork]]
