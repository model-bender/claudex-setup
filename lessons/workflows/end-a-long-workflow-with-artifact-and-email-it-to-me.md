---
id: end-a-long-workflow-with-artifact-and-email-it-to-me
created: 2026-08-16
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://x.com/_catwu/status/2073806626965049686
---

# End a Long Workflow With "Make an Artifact and Email It to Me" So You Can Walk Away

## TL;DR

Specify the delivery mechanism up front - dynamic workflow, then artifact, then email - so a long autonomous run finishes into your inbox in reviewable form instead of into a terminal you have to come back to.

## Why it matters

The corpus covers dynamic workflows and the Artifact tool separately, but not chaining them into an async hand-off. Naming the output format *and* the delivery channel in the same prompt is precisely what makes closing the laptop safe: without it, a two-hour run ends in scrollback you have to be present to receive.

It also forces the output shape to be decided before the work starts, which is when you actually know what you want per row.

## How to apply

Append "make an artifact and email it to me" to a long-running workflow prompt, naming the fields you want per row so the result arrives as a reviewable page rather than a wall of text. The worked example:

> "one of my new favorites is for sourcing candidates:
> - tell cc about the role and backgrounds i'm looking for
> - ask cc to kick off a dynamic workflow to find 100 candidates, and include linkedin, twitter, blog, podcasts, and one-line pitch for each
> - ask cc to make an artifact and email it to me. then, i lock my laptop and head out for the day
> - i review the list on the go once cc is done!", Cat Wu

## Related

[[html-as-default-artifact-not-markdown]], [[explicit-numeric-receipts-for-automations]]
