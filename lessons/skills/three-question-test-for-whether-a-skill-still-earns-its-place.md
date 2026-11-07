---
id: three-question-test-for-whether-a-skill-still-earns-its-place
created: 2026-10-25
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/mark-kashef/anthropic-just-donated-claude-skills-here-s-what-to-delete_2IPR6F3cQ_I_20261024.txt
---

# Keep a Skill Only If It Runs Exact Code, Knows What the Model Cannot, or Covers an API With No Connector

## TL;DR

Ask three questions of every skill: does it run the same code each time, does it hold knowledge the model lacks and cannot look up, and is it still not replaced by a connector or MCP server.

## Why it matters

Mark Kashef argues most skills written a year ago were crutches for weaker models. His own example: a Calendly API skill became obsolete the day Calendly released an MCP server. He also reports having had more than 121 skills bloating context with names and descriptions, and six overlapping design skills that made results inconsistent between sessions depending on which loaded. Skills that pass are code-running ones (his video-editing skill, over 22,000 lines), personal knowledge (how you write emails, client report formats), and short cheat sheets for an API with many endpoints.

## How to apply

For each skill ask: 1. Does it run exact code every time? 2. Does it know something the model does not and cannot find online (your preferences, client formats)? 3. Is there now a product, connector or MCP server that makes it obsolete? A skill failing all three is a deletion candidate; one that is personal may shrink to a single line in AGENTS.md or overlap with your memory file, so check for that. Then consider merging overlapping survivors. This test judges whether a skill should exist; the related explainability test judges overlap. Checked: n/a (judgment framework from the creator; his claims about skills being donated to the Linux Foundation and Opus 5 behaviour were not verified and are not used in the lesson)

## Related

[[explainability-test-to-prune-overlapping-skills]], [[simplify-a-skill-after-a-model-upgrade-instead-of-adding-detail]]
