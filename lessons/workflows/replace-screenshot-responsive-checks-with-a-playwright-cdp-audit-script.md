---
id: replace-screenshot-responsive-checks-with-a-playwright-cdp-audit-script
created: 2026-10-19
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1x5or3q/what_is_an_ai_lifehack_that_people_dont_seem_to/pgoj4h6/
  - https://www.reddit.com/r/ClaudeAI/comments/1x5or3q/what_is_an_ai_lifehack_that_people_dont_seem_to/pgo6agt/
---

# Replace Screenshot-Based Responsive Checks With a Playwright/CDP Audit Script, Then Wrap It in a Skill

## TL;DR

Instead of having Claude resize a browser and read screenshots on every check, have it write a Playwright and Chrome DevTools Protocol script once that reports overflowing boxes, hidden text, broken or upscaled images and too-small tap areas without a model judging each page, then make a skill that points at the script.

## Why it matters

The screenshot loop spends thinking, tool calls and image review on every run, and it can miss screen sizes or the lower parts of a long page. A script runs without a model and gives the same result every time, so Claude only spends tokens calling it and reading its error list, and the skill means no future session has to be told it exists or search the machine for it.

## How to apply

Ask Claude for the audit script (layout and asset checks that do not need vision), keep it somewhere every project can reach, and write a skill that references it so Claude Code, Codex or any other harness runs it by default. Keep screenshot review for what the script cannot judge.

> "So instead the first level is you ask it to write a script using playwright and Chrome's CDP  to first audit things that don't require it to actually see the page: boxes overflowing, text or contents hidden, broken or upscaled images, tap areas that are too small, and so on...The script returns the list of errors without needing an AI at all.", u/WheresMyEtherElon on r/ClaudeAI

> "Have AI create a program to do the task instead of the AI doing it themselves. Next time you do it it’ll cost no tokens", u/5xaaaaa on r/ClaudeAI

## Related

[[have-claude-verify-a-responsive-site-with-the-playwright-plugin]], [[skills-add-scripts-to-avoid-repeated-api-scaffolding]], [[keep-claudes-throwaway-test-scripts-in-the-test-suite]]
