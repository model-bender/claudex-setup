---
id: record-a-narrated-screen-demo-to-author-a-cowork-skill-for-ui-only-software
created: 2026-07-25
status: active
supersedes: null
category: skills
tool: claude-code
about: claude-cowork
sources:
  - transcripts/simon-scrapes/anthropic-just-solved-claude-cowork-s-biggest-limitation-goodbye-mcp_9QSumbWubZ4_20260724.txt
---

# Teach Claude UI-Only Software With Cowork's Recorder Skill: Narrate While You Record, Then Answer Its Questions

## TL;DR

Claude Cowork's Recorder Skill captures your screen, clicks, typing, and voice in one pass and turns them into a `SKILL.md`, so software with no API and no MCP (legacy enterprise portals, admin panels, ManyChat) becomes automatable. The narration track is the point: you speak the branching rules and preconditions that clicks alone can't show.

## Why it matters

The demo recorded 61 steps from 240 seconds of work, steps the creator says he "didn't have to explain" because he talked through them while clicking. Crucially, the follow-up question round caught two real defects in his own process: it asked whether the skill should also flip the Notion row's status to "live" (a step he'd forgotten), and pointed out that he downloaded a video and thumbnail from Drive but never used them in any ManyChat step (a leftover from a different process). A silent recorder would have baked both mistakes in. This is the one automation path for tools that will never get an MCP, and the concrete instance of the record-and-replay tier.

## How to apply

In the Claude desktop app (updated), open the Co-Work folder and start Recorder Skill, it is Mac-only at the time of recording, and it records all screens, clicks, keystrokes, and mic. While you work, say the things the screen doesn't show: which row to pick ("take the latest video"), the precondition ("only if the DM automation column is on not-started, if it's live, skip"), and the terminal state ("switch it back to live at the end"). Hit Done, answer the clarifying questions honestly, treat them as a review of your own process, and tell it to drop steps that don't serve the goal, then save the generated `SKILL.md`. Before you invoke it, enable Claude in Chrome under Settings, or the skill has no way to open the browser window it recorded you working in. Execution is screenshot-by-screenshot, noticeably slow, and burns a lot of tokens. Once it works, attach it to a scheduled task ("each day, check if there's a new video and run this if so") rather than relying on auto-invocation.

## Related

[[feed-raw-video-to-claude-code-or-codex-and-say-watch-dont-just-transcribe]], [[retest-a-recorded-skill-on-changed-inputs-not-the-demo-case]]
