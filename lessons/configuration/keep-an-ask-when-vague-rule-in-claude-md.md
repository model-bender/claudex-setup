---
id: keep-an-ask-when-vague-rule-in-claude-md
created: 2026-11-15
status: active
supersedes: null
category: configuration
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xmhy1d/the_karpathy_claudemd_clearly_changed_claude/
---

# Put "ask when the request is vague" in CLAUDE.md: in a 24-run A/B it was the rule that changed behaviour, not correctness

## TL;DR

With and without the four-rule forrestchang/andrej-karpathy-skills CLAUDE.md (Claude Code 2.1.312, Opus 5.5, 4 tasks x 3 runs), the rules changed two things. Claude asked before coding on a vague task (2 of 3 runs, against 0 of 3), and it added regression tests. Hidden-test correctness, time and cost ($2.56 vs $2.69) barely moved.

## Why it matters

Opus 5.5 already makes surgical, simple changes, so most of a rule pack is redundant. The gain you can measure is the ask-first behaviour, which decides whether you or the model picks the interpretation of a vague request.

## How to apply

Keep a short "ask when the scope is unclear" line in CLAUDE.md rather than importing a whole rule pack. If you adopt that file anyway, append it: the poster warns the repo's `curl -o` install overwrites an existing CLAUDE.md.

> "With it, 2 of 3 stopped to ask first. All 6 noticed the date problem, so the file changed when you get to decide, not whether Claude spotted it.", u/vinishkapoor on r/ClaudeCode
