---
id: replace-persona-preambles-with-pointers-done-criteria-and-a-self-check
created: 2026-08-29
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/19-claude-code-mistakes_icM0ewXGvAw_20260824.txt
---

# Replace persona preambles with where-to-look, done criteria, and a self-check

## TL;DR

Role/persona openers ("you're a senior copywriter with 20 years experience... take a deep breath") measurably do nothing: a test of 162 personas across ~2,500 prompts found no improvement over asking directly. Spend the same words on three things Anthropic's own guidance rewards: where the extra context lives, what done looks like, and a "before you finish, verify your answer against X" self-check.

## Why it matters

The persona habit survives from 2024-era prompting and burns the highest-attention opening lines of every prompt on words the model doesn't use. The Claude Code team effectively confirmed this from the inside by cutting their own system prompt by around 80% and saying that stuffing prompts with examples is no longer best practice. The three replacement elements map to Anthropic's prompting guidance directly, and the self-check line gives the model a verification criterion instead of leaving you as the verification loop.

## How to apply

Delete persona and pep-talk lines from prompt templates. Reinvest the word budget: (1) tell it where to look for additional context ("the client notes are in the onboarding folder"); (2) state the definition of done ("a one-page proposal covering their three pain points with the price listed at the bottom"); (3) add a self-check using the documented phrasing "Before you finish, verify your answer against..." followed by your check ("...every number against our notes, and flag anything you can't back up"). Roughly the same length as the persona preamble, but every word gets used.

## Related

[[delete-examples-and-negative-constraints-from-claude-md]], [[done-when-prompt-scaffold-for-codex]], [[validation-loop-in-claude-md-is-critical]]
