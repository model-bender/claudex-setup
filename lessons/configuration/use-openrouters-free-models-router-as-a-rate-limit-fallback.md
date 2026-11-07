---
id: use-openrouters-free-models-router-as-a-rate-limit-fallback
created: 2026-08-29
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/this-stealth-model-makes-claude-code-free-here-s-how__kK_4cOYF4o_20260824.txt
---

# Point Claude Code at OpenRouter's free-models router to keep doing light knowledge work after you hit your limits

## TL;DR

Individual free OpenRouter models appear and vanish, so don't pin one by name: OpenRouter's dedicated free-models-router model routes each request to whichever free model is currently available. Wired into Claude Code's env block, it's a serviceable fallback for light knowledge work when your daily/weekly credits are gone. Expect it to be much slower, and never send sensitive data to anonymous providers.

## Why it matters

A free model swapped into the Claude Code harness still reads your CLAUDE.md and context files, invokes your skills, and uses web fetch/search. The creator's test runs completed real deliverables (a branded landing page with verification passes, a YouTube analytics report) at a total cost of ~$0.13 for 61M tokens. But the specific free models rotate ("OpenRouter seems to switch out these models that are free sometimes"), so a pinned slug breaks; the free-models router "just selects free models at random, whichever ones are available", making the setup durable. The honest caveats are real: builds that take regular Claude ~30 minutes took 6 hours, and stealth models are anonymous providers of unknown origin, so sensitive data doesn't belong there.

## How to apply

Create an OpenRouter account and API key, put the key in ANTHROPIC_AUTH_TOKEN in the env block of .claude/settings.json, and set the free-models-router slug (or a specific free model's slug) in every model slot; open a new terminal session and confirm the model name in the header. Reserve this configuration for the out-of-credits scenario and for light knowledge work (searching your wiki, processing transcripts, drafting reports), not deep technical builds, orchestration of dynamic workflows, or anything with confidential data. Keep your normal Anthropic-auth `claude` untouched for real work.

## Related

[[route-claude-code-to-cheaper-or-local-models]], [[one-launch-alias-per-open-weight-model-via-openrouter]], [[swap-every-model-env-slot-when-rerouting-claude-code]]
