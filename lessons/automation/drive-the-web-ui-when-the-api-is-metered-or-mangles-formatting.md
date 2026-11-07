---
id: drive-the-web-ui-when-the-api-is-metered-or-mangles-formatting
created: 2026-08-22
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/codex-s-browser-agent-automates-literally-anything_CB5bG4mvnS0_20260820.txt
---

# Prefer the API, Except When It Is Metered or Mangles Formatting, Then Drive the Web UI

## TL;DR

API-first is still the rule, but there are two named exceptions where browser use wins: the API charges per call while browser use rides your existing subscription, and the API handles rich formatting or media attachments badly.

## Why it matters

The creator's own hierarchy is API, then a deterministic macro script, then vision-driven browser use, and he estimates the API covers about 95% of automation needs. But he deliberately posts X articles through the browser rather than the X API for two reasons: the API is "a little bit weird with the formatting" and "weird with sometimes adding things like media or thumbnails", and it bills per usage whereas browser use is included in the Codex subscription he already pays for. In his run the browser path did what the API path could not: it opened Drafts, clicked through the composer, pasted the article body, uploaded a thumbnail, and dragged a screenshot down into the right position in the article. The same reasoning covers metered APIs generally, where the marginal cost per run makes a frequently scheduled automation expensive.

## How to apply

Before defaulting to the API, check two things: does it charge per call on top of what you already pay, and does it faithfully handle the formatting and media the task needs? If either answer is bad, build the flow as a browser-use skill instead and save it for reuse. If the interaction is fixed and needs no vision or reasoning (the same pixels in the same order every time), ask Claude or Codex to write a deterministic macro script instead, which is cheaper and safer than a vision loop. Keep vision-driven browser use for the cases that genuinely need to look at the page and decide what to click next.
