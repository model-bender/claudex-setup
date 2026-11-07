---
id: give-the-agent-the-emulator-so-it-self-tests
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/edmund-yong/i-coded-another-profitable-app-from-scratch-everything-i-did-no-bs-step-by-step_kPVsX6lov_I_20260910.txt
---

# Give the Coding Agent the Running Emulator So It Tests Its Own Build

## TL;DR

Grant the agent access to the simulator or emulator your app runs in, so it can exercise the screen it just changed rather than handing you an untested build.

## Why it matters

Without it every change costs a manual round trip through you, which is the bottleneck on a solo build. The creator granted Codex full system access for exactly this on a React Native and Expo app, so it could interact with the running iOS emulator and self-test its own code during local development.

## How to apply

Start the emulator before the session, confirm the agent can drive it, and make 'exercise the changed screen in the emulator' part of the done condition for each task. Scope the access deliberately, since this is a broad grant.

## Related

[[run-codex-browser-qa-concurrently-while-claude-keeps-building]]
