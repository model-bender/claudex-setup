---
id: switch-off-built-in-skills-you-never-trigger
created: 2026-11-06
status: active
supersedes: null
category: skills
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xhn8az/i_switched_off_every_builtin_claude_code_skill_i/
---

# Switch Off the Built-In Skills You Never Trigger: They Load Into Every Session Regardless

## TL;DR

Built-in skills cost context in every session whether or not they fire, so audit the list and turn off the ones you never trigger (the author names the API reference skill firing on the word "Claude", Deep Research spawning helper agents, and the Artifact skills for a panel he had already blocked).

## Why it matters

The cost is paid per session and is invisible unless you look, and a skill that fires on a common word also changes behaviour you did not ask to change.

## How to apply

Review the installed skills, turn off the built-ins you never trigger (a skillOverrides entry set to off per skill, or disableBundledSkills for all of them), and check the per-skill token breakdown in /context to see what the removal bought.

Checked: claude 2.1.318 binary: skillOverrides 22 hits; its text says a bundled skill can be "set to off in the skillOverrides setting, or turned off with every other bundled skill by the disableBundledSkills setting or CLAUDE_CODE_DISABLE_BUNDLED_SKILLS".

> "Every skill and add-on gets loaded into the session whether you use it or not, so I went through the lot and killed what was just eating tokens for me.", u/shadowdog000 on r/ClaudeCode

