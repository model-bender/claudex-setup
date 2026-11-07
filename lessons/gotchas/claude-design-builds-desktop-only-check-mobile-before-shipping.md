---
id: claude-design-builds-desktop-only-check-mobile-before-shipping
created: 2026-07-17
status: active
supersedes: null
category: gotchas
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-design-builds-beautiful-3d-websites-instantly-full-tutorial_TcFeSjwTo7g_20260624.txt
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
---

# Claude Design Builds Desktop-Only: Ask for Mobile Explicitly Before Shipping

## TL;DR

Neither Claude Design nor Claude Code optimizes a generated site for mobile unless you ask. Check the browser devtools device view before deploying, because the desktop-tuned layout usually breaks on a phone.

## Why it matters

A finished, on-brand site rendered beautifully on desktop and "obviously is not good" in mobile view, and a landing page that only works on a laptop is one most of its traffic can't use.

The remedy is one request away, and restructuring for small screens doesn't have to disturb the desktop version.

## How to apply

Before deploying, open the site on localhost, press F12, and switch to the device/mobile view.

Then tell Claude Code specifically what should change on small screens, move the hero video below the text, keep the headline on one line, and state explicitly that the desktop layout must stay as it is.

## Related

[[claude-design-export-404s-on-vercel-because-html-is-not-at-repo-root]], [[prompt-interaction-states-they-are-omitted-by-default]]
