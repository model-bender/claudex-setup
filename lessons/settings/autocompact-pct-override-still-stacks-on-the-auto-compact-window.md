---
id: autocompact-pct-override-still-stacks-on-the-auto-compact-window
created: 2026-11-15
status: active
supersedes: null
category: settings
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xo6dfy/thanks_to_two_lines_in_the_claude_setting_i_was/
---

# CLAUDE_AUTOCOMPACT_PCT_OVERRIDE stacks on autoCompactWindow: 300000 at 75 compacts near 210K, not 300K

## TL;DR

The percent override still works in 2.1.325, and it is applied to the window you set. Claude Code compacts at min(window x pct, window - 13,000), where the window is autoCompactWindow minus an output reserve of up to 20,000 tokens. So `"autoCompactWindow": 300000` with `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=75` compacts at about 210K.

## Why it matters

The post recommends "300K & 75%" on the belief that compaction needs 25% headroom. The code already keeps 13K tokens of room below the effective window, so the override only makes compaction fire about 90K earlier than the window the user picked. Users then misjudge their real working context. This also corrects [[set-a-fixed-token-auto-compact-window]], which says the percentage threshold is gone: the default percentage is gone, the override is not.

## How to apply

Use one setting. Set autoCompactWindow (or `/autocompact`) to the token count where you actually want compaction, and leave CLAUDE_AUTOCOMPACT_PCT_OVERRIDE unset. If you keep both, the real trigger is (window - 20,000) x pct.

Checked: on Claude Code 2.1.325, `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` has 9 hits and `autoCompactWindow` 73; the threshold formula was read from the binary, not run live.

> "75 is real trick many people forgets ... because the agent needs a space to be able to compress so if you kept it at 80 or 90 or 100 there where the issues rise . and lower than 75 it get excessive .", u/Machine2024 on r/ClaudeCode

## Related

[[set-a-fixed-token-auto-compact-window]], [[shrink-the-auto-compact-window-to-stretch-a-subscriptions-weekly-usage]]
