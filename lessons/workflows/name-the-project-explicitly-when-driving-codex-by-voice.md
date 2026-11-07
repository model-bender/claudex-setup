---
id: name-the-project-explicitly-when-driving-codex-by-voice
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/john-kim/unboxing-openai-s-sold-out-codex-micro_iz7aonhDKvE_20260820.txt
---

# Voice Control in Codex Has No Screen Context - Name the Project, and Pin Your Threads

## TL;DR

ChatGPT voice chat now drives Codex threads (start a task, spawn a second task in parallel, pin a thread), but it has no idea what you're looking at, so refer to work by project name; and switch the thread list from recent to pinned so thread slots stop reordering under you.

## Why it matters

Driving Codex hands-free works - John Kim starts a game running and, in the same breath, has it begin a watch version of a separate app as a new parallel task. But the failure mode is consistent: asked to work on 'my Anime Pomodoro', Codex replied 'I'm still pinning down which project is your Anime Pomodoro one' and had to be told it was the Xcode project. His summary is that the voice layer 'doesn't really have that context to what I'm looking at, it just kind of has its own context.' Separately, the thread controls felt like they were 'swapping on me' because the list defaults to most-recent chats, so the position of a given project keeps moving; switching to pinned chats made the slots stable and matched how he actually works. He also hit a case where voice would not start the agent in an existing thread and only worked after opening a new one - observed once, so treat it as a thing to try rather than a rule.

## How to apply

When speaking to Codex, name the project or repo explicitly in the instruction ('in the Xcode project for the Pomodoro app, start the simulator') rather than relying on deictic references to whatever is on screen. Pin the threads you work on daily and set the thread list to pinned rather than recent, so a given project keeps a stable position. Say 'pin this' to have Codex pin a thread it just created. If a voice command fails to launch the agent inside an existing thread, retry from a new thread before assuming the feature is broken.
