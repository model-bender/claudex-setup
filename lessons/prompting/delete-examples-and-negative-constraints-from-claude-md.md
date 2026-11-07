---
id: delete-examples-and-negative-constraints-from-claude-md
created: 2026-07-25
status: active
supersedes: null
category: prompting
source_type: post
tool: claude-code
sources:
  - https://simonwillison.net/2026/Jul/21/cat-and-thariq/
---

# Delete Examples and "Do Not Do X" Lists From Your CLAUDE.md: Frontier Models Are Hurt by Both

## TL;DR

Anthropic cut the Claude Code system prompt substantially for Fable-class models by removing worked examples and negative "don't do X" constraints, do the same to your own CLAUDE.md and agent prompts.

## Why it matters

Two named mechanisms, not vibes. Examples cap the model below its own creativity: Thariq Shihipar reports that "the initial, maybe Opus 4-ish models wanted a lot of examples, and removing examples was extremely helpful, because it was just more creative than the examples we gave it." And hard negatives are such a strong pull that they override a user's own later, contradicting instruction, so a prohibition you wrote months ago quietly wins an argument against what you're asking for right now.

## How to apply

Sweep `CLAUDE.md`, `.claude/agents/*.md`, and any `--append-system-prompt` / `--system-prompt-file` content: delete illustrative examples, and rewrite each "never / don't do X" line as positive context describing the situation rather than the prohibition. Keep examples only where the output format is genuinely non-obvious and cannot be described.

> "The other thing we did is try to give it more context and fewer 'do not do this' instructions, because that's a very strong impulse for Claude, and especially if it conflicts with user instructions later on, that can be extremely confusing to Claude.", Thariq Shihipar (via Simon Willison)

## Related

[[soften-absolute-rules-until-they-are-true-every-time]]
