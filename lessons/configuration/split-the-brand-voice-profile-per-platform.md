---
id: split-the-brand-voice-profile-per-platform
created: 2026-08-22
status: active
supersedes: null
category: configuration
tool: claude-code
about: claude-cowork
sources:
  - transcripts/simon-scrapes/the-only-claude-cowork-setup-busy-entrepreneurs-actually-need_BMEaJTl3Vo0_20260820.txt
---

# Split the Brand Voice Profile Into a Core Voice File Plus Per-Platform Companion Guides

## TL;DR

You do not have one voice, you have a different one per platform, so keep core voice DNA and rules in one file and generate separate LinkedIn, email and community guides by having Claude scrape what you have actually written on each.

## Why it matters

A single flat voice profile averages your platforms together and produces writing that fits none of them, since tone and structure genuinely differ between a LinkedIn post, a client email and a community reply. The 80/20 build is to let Claude do the extraction rather than writing the guide by hand: connect to Gmail via MCP and scrape your sent mail, scrape your LinkedIn posts, your community replies, your client messages, and have it read hundreds of real examples per platform and pull out the patterns. The creator's structure is one brand-context voice profile file holding core voice DNA and the rules that apply everywhere, with companion docs per platform hanging off it. His caveat is worth keeping: Claude has become decent at not sounding generic out of the box, but it will never sound like you without real examples of your own work.

## How to apply

Three routes in increasing order of effort and quality. First, have Claude interview you with 10 to 20 questions about how you talk and what you would never say, which is the fastest path from zero. Second, scrape your real output per platform through the relevant connectors and generate one guide per platform. Third, keep it alive: whenever you correct a stylistic choice, update the rule set so the same correction is not needed again. Store the core file plus companions in the shared context folder and have CLAUDE.md route to them conditionally, for example load the voice profile whenever writing content.
