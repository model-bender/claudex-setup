---
id: tell-the-codex-browser-agent-to-try-to-break-your-ui
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/codex-s-browser-agent-automates-literally-anything_CB5bG4mvnS0_20260820.txt
---

# Tell Codex's Browser Agent to Try to Break the App, and Set a Scenario Floor With /goal

## TL;DR

Adversarial phrasing ("try your best to break it") turns Codex's browser use into a QA pass that finds data-integrity and responsiveness bugs, and /goal lets you demand a minimum number of distinct edge-case scenarios instead of accepting whatever it tried.

## Why it matters

A neutral "test this" walks the happy path; the adversarial framing produced concrete, non-obvious findings on a simple form: invalid contact data got through validation, changing the country code to UK silently reset to US when returning to edit, and it switched itself to mobile view and found responsiveness failures the creator had not tested at all. It narrated its own strategy ("I'm now testing keyboard submission and restart behavior, which often exposes bypasses the click path misses"), which is exactly the class of case a human tester skips. In the creator's larger SaaS build the same technique ran 85 focused automation checks with real click, type and submit workflows and surfaced a batch of fixable bugs. The argument is throughput, not perfection: you are choosing between untested and tested-a-hundred-times, and real users behave more unpredictably than your own five or six edge cases.

## How to apply

Open the app (localhost is fine) in the Codex in-app browser, then prompt along the lines of "you have the UI open, I want to make sure there are no bugs and that this thing can't break, use your browser use and just test the heck out of this, try different things, try your best to break it, and let me know what bugs you find". Read the pass/fail list it returns and hand the failures straight back as a fix task. When the default effort is too shallow, escalate with /goal and a quantity floor, for example "don't stop until you've tried 100 different unique scenarios of UI edge cases, then come back to me". Ask explicitly for mobile as well as desktop if it does not switch viewports on its own.
