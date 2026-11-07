---
id: name-a-known-pattern-like-tracer-bullet-to-steer-agent-architecture
created: 2026-09-24
status: active
supersedes: null
category: prompting
tool: [claude-code, codex]
source_type: post
sources:
  - https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock
---

# Borrow software-engineering vocabulary as "leading words" to steer agent architecture

## TL;DR

Naming a known software-engineering pattern in your prompt (e.g. "tracer bullet" from The Pragmatic Programmer, meaning build a thin end-to-end path first) gets a coding agent to apply that pattern's discipline instead of building layer by layer and leaving bugs at the seams.

## Why it matters

Matt Pocock's stated failure mode is specific: agents build software layer by layer and that causes bugs between the layers; naming the pattern instead of describing the desired behavior from scratch reliably fixed it for him and he now mines classic engineering books for more such terms.

## How to apply

When asking an agent to scaffold a new feature, name the pattern instead of just the goal, e.g. "build this as a tracer bullet: one thin path end to end through every layer, then flesh it out" rather than open-ended "build feature X".

> "When he instructed the agent to use "tracer bullets" to build an app (aka implement a "golden path"), the agent started to produce better code! Since then, Matt has started reading classic software engineering books to discover other "leading words" that guide agents efficiently.", Gergely Orosz (interviewing Matt Pocock)
