---
id: opus-5-5-max-effort-can-exhaust-the-output-cap-and-return-nothing
created: 2026-10-02
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/
---

# Treat Opus 5.5 max effort as able to exhaust the output cap and return nothing

## TL;DR

On Opus 5.5 at max effort, reasoning can consume the whole 128k output cap on a simple task and return no answer, so max can fail outright, not just cost more.

## Why it matters

This is a concrete failure mode of max beyond overthinking: a paid run that ends with no output. Simon's two failed runs cost $2.56 each and took nearly 20 minutes. Caveat: the test was an API run on an SVG prompt, not a Claude Code session.

## How to apply

Keep /effort at high or xhigh by default on Opus 5.5 and Sonnet 5.5, and use max only for a task you can afford to lose, as the docs warn it "is prone to overthinking".

Verified: https://code.claude.com/docs/en/model-config.md (fetched 2026-10-02) lists max for Opus 5.5 and Sonnet 5.5 and says max "may show diminishing returns and is prone to overthinking". Installed Claude Code 2.1.287 contains CLAUDE_CODE_EFFORT_LEVEL (11 matches via command grep -c -a). The 128k hit is Simon's observation only, not checked in Claude Code.

> "Opus 5.5 has a 128,000 maximum output token limit (as do the other Claude models), and it hit that while it was still reasoning about the SVG!", Simon Willison

## Related

[[max-effort-is-a-trap-quality-plateaus-at-high]]
