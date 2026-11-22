---
id: give-claude-explicit-permission-to-say-it-does-not-know
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/everyone-ignore-these-claude-concepts-but-they-change-everything_6VjeXzvpoJo_20261120.txt
---

# Give Claude explicit permission to say it does not have enough information

## TL;DR

Add a line to the prompt that lets Claude admit uncertainty, such as saying it lacks enough information to assess a point. Anthropic's docs say this can drastically reduce false information.

## Why it matters

By default Claude tends to answer every question even when it lacks the facts; an allowed way out lowers made-up answers.

## How to apply

In prompts about a document or data, add: if you're unsure about any aspect or if the material lacks necessary information, say I don't have enough information to confidently assess this. This lesson's suggestion: put the line in skills or commands that analyse supplied material.

Checked: Checked 2026-11-22: Anthropic docs page 'Reduce hallucinations' (platform.claude.com, fetched by curl) says 'Explicitly give Claude permission to admit uncertainty. This technique can drastically reduce false information' and gives the example wording. No Claude Code mechanism.
