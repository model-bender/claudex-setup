---
id: ask-for-headless-browser-use-to-keep-working-in-the-foreground
created: 2026-08-22
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/codex-s-browser-agent-automates-literally-anything_CB5bG4mvnS0_20260820.txt
---

# Ask for Headless Browser Use When You Want to Keep Working, Headed When You Need to Watch

## TL;DR

Codex's browser agent runs either headed (visible in the app pane, you watch the mouse move) or headless (in the background), and you pick per task simply by asking for it in the prompt.

## Why it matters

The two modes trade supervision for throughput. Headed is what you want while you are still calibrating a flow: the creator could watch Codex's own cursor click Continue, trip the required-field validation, fill the form and move on, which is how he caught what it was actually doing rather than what it reported. Headless is what you want for volume: it runs in the background so you can keep working in the foreground without the browser stealing focus, and a job can grind for hours without disturbing you. Because the choice is per task rather than a global setting, a long QA sweep or a scheduled skill can run out of sight while an unproven flow stays visible.

## How to apply

State the mode in the prompt: ask it to run headless when you want the work to happen in the background over a long stretch, and leave it headed (the default in the desktop app's browser pane) when you want to watch the flow. Use headed for the first runs of any new browser skill, then switch to headless once the flow is proven. Note that headless also removes the ability to spot a wrong click in real time, so pair it with an explicit report of what it did.
