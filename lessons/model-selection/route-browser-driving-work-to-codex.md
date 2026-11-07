---
id: route-browser-driving-work-to-codex
created: 2026-09-12
status: active
supersedes: null
category: model-selection
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/i-tested-gpt-6-astra-vs-fable-5-1-on-15-real-use-cases_WfJPBVXPt8k_20260910.txt
---

# Route Tasks That Drive a Real Web UI to Codex, Claude Loses Them on the Mechanics

## TL;DR

For work whose success depends on operating someone else's web interface (uploading files into a CMS, building something inside a web design tool), hand it to Codex. Claude's failures here are mechanical rather than aesthetic and they invalidate the whole deliverable.

## Why it matters

Nate Herk gave both tools the same browser jobs and Claude failed the mechanics twice: drafting courses into a community platform it could not upload the videos at all despite being handed the files and links, and asked to reproduce a reference image in a web design tool it returned output he called laughable next to Codex's. He states this is not a one-off, he has run the CMS task multiple times and in general finds the GPT models significantly better with browser use. Note this is orthogonal to design taste, where Claude still holds up.

## How to apply

Split the pipeline by surface: Claude for the code, the copy and the design artifacts, Codex for the step that has to click through a real interface. Set Codex's browser up first (allowed domains, log in once so it acts as you) so the handoff is one prompt rather than a setup session. Re-test after model releases rather than treating this as permanent.

## Related

[[route-work-between-claude-code-and-codex-by-task-type]], [[track-model-capability-failures-and-retest-on-release]]
