---
id: drive-mobile-only-apps-through-iphone-mirroring
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/mark-kashef/gpt-6-astra-s-computer-use-is-ridiculously-good_tU-fO6cADvQ_20260910.txt
---

# Reach Mobile-Only Apps by Pointing Computer Use at the iPhone Mirroring Window

## TL;DR

Open macOS iPhone Mirroring and tell Codex to drive it. That gives computer use a path into apps with no desktop client and no API, on the real device and the real account.

## Why it matters

Mark Kashef found the mirroring window is just another app to a computer-use agent: 'use the iPhone mirroring app I opened to configure Instagram on my actual phone', and it opened the app, confirmed it was on the right account, and worked through media quality and other settings, returning a checklist in about five minutes. He flags his own surprise that it could take control of the phone at all. This is the escape hatch for the large category of software that exists only as a mobile app, where the usual ladder of plugin, API and browser automation has no rung to stand on.

## How to apply

Open iPhone Mirroring on the Mac and leave it focused, then name it in the prompt: 'use the iPhone mirroring app I opened to <task> on my actual phone.' Tell it which account or profile it should be on and have it verify that before acting. Combine with an explicit list of forbidden actions, since this is a live device. Useful beyond settings: exercising a TestFlight build's user journey the same way you would a desktop app.

## Related

[[enumerate-forbidden-actions-when-computer-use-drives-a-live-account]]
