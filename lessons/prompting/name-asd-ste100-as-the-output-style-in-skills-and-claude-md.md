---
id: name-asd-ste100-as-the-output-style-in-skills-and-claude-md
created: 2026-11-06
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xlbuq6/forget_the_usual_claude_tips_what_are_the_strange/19rzsa7565rgh/
---

# Tell Skills and CLAUDE.md to Write in ASD-STE100 to Stop Verbose, Cryptic Output

## TL;DR

Naming ASD-STE100 (Simplified Technical English, the aerospace maintenance-manual writing standard) as the output format in skills and CLAUDE.md gives the model a concrete style target instead of "be concise".

## Why it matters

"Be concise" is a no-op the model cannot check itself against, while a named published standard carries approved vocabulary, short sentences and one instruction per sentence, which is exactly the shape wanted for agent-facing prose.

## How to apply

Put one line in the rule file or skill telling it to write output in ASD-STE100, and check whether the result reads shorter and less hedged than before.

> "For every skill / Claude md I instruct to follow ASD-STE100 format to prevent Claude from being too verbose and cryptic.", u/Remy_Builds on r/ClaudeCode
