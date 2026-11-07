---
id: swap-a-noun-for-a-verb-and-ask-claude-which-professions-already-solve-your-problem
created: 2026-10-19
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/ray-amjad/your-prompts-are-too-small-for-claude-code_RbfQayMNtJc_20261018.txt
---

# Turn the Task Noun Into a Verb, Then Ask Claude Which Jobs Already Solve That Problem

## TL;DR

Describe what the artifact must do, not what it is, and ask Claude to interview you and name professions that face a problem of that shape.

## Why it matters

Ray Amjad relays Felix's 'range': a deck becomes 'getting busy people to believe a story about cause and effect and decide under uncertainty in 30 minutes' (journalists, editors, analysts). His error-message example: the noun is 'error page', the verb is 'help a confused person get unstuck alone', which support agents do for a living. Claude is not doing this by default today, so you prompt for it.

## How to apply

Prompt: 'Here is my problem. Interview me, then tell me which jobs already deal with a problem shaped like this and what they actually do.' In his example he then had the agent pull six months of support tickets, match each to its error, rank by count, and rewrite the top four errors (the 'entity too big' message became one stating the 6 GB upload against a 5 GB limit and the options). Checked: prompt technique, nothing to verify against the binary; the examples are from the transcript.

