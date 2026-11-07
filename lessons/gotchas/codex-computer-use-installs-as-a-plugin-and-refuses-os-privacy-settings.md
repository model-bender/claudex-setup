---
id: codex-computer-use-installs-as-a-plugin-and-refuses-os-privacy-settings
created: 2026-08-22
status: active
supersedes: null
category: gotchas
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/codex-s-browser-agent-automates-literally-anything_CB5bG4mvnS0_20260820.txt
---

# Codex Computer Use Is a Separate Plugin Install, and It Refuses OS Privacy Permissions

## TL;DR

Browser use is built in but computer use is not: install it from the plugins page first, expect a blue tint around your screen while it drives, and expect it to decline privacy-scoped OS settings and admin prompts.

## Why it matters

The two capabilities get conflated, but they are separate: browser use covers anything inside a browser, computer use covers your actual desktop (system settings, native apps), and computer use only appears after you search "computer use" on the plugins page and install it, which takes seconds but is easy to miss. Two behaviours are worth knowing before you rely on it. First, it self-limits: it announced "I'll stop if Windows asks for an admin password or presents a security sensitive permission that it can't safely interpret", and when asked to toggle a Bluetooth-devices option it initially refused because it read Bluetooth access as a privacy permission, though it then completed the in-app version of the setting. Second, it is visually unmistakable, the screen edges take on a blue hue for the duration, so you always know it has control.

## How to apply

Go to plugins, search computer use, install. Prompt it with what you want done on the desktop, for example opening a native app and changing an in-app setting. Do not build workflows that depend on it flipping OS-level privacy toggles or getting past admin prompts, keep those manual. Because sessions are remotely reachable, this also makes phone-driven desktop control possible: with Codex remote access you can trigger a computer-use task on a machine you are not sitting in front of.
