---
id: soften-absolute-rules-until-they-are-true-every-time
created: 2026-07-25
status: active
supersedes: null
category: prompting
source_type: post
tool: claude-code
sources:
  - https://simonwillison.net/2026/Jul/21/cat-and-thariq/
---

# Soften Absolute Rules in CLAUDE.md Until They're True 100% of the Time

## TL;DR

The Claude Code team rewrote its own system prompt away from "if you make a front-end change, always verify" to a conditional instruction, because an absolute rule that is wrong some of the time still gets applied every time.

## Why it matters

Standard advice is to make CLAUDE.md rules emphatic, ALWAYS, IMPORTANT, NEVER. The team that writes Claude Code's actual system prompt says the opposite: you hand the model this prompt on 100% of turns, so a rule that's only right 80% of the time misfires on the other 20% and fights your explicit "just make a quick fix" instruction. Cat Wu's test is whether a well-intentioned human could misread it.

## How to apply

For each absolute rule in your CLAUDE.md, ask whether a well-intentioned human could apply it somewhere you wouldn't want it; if so, rewrite it as a conditional with the trigger attached. The team's own worked example went from "if you make a front-end change, always verify" to "most of the time when you're doing front-end work you can't fully understand the experience by hitting the backend endpoints, so when you make larger changes to the user experience, please run the app locally."

> "In general, whenever you give a prompt to the model, you should think about the ways in which it could be misinterpreted by a well-intentioned human, in order to better understand how the model might interpret it — and soften the prompt so that it's actually 100% accurate, because you're giving this prompt to the model 100% of the time.", Cat Wu (via Simon Willison)

## Related

[[delete-examples-and-negative-constraints-from-claude-md]]
