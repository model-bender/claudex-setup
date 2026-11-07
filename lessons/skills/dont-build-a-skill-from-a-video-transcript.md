---
id: dont-build-a-skill-from-a-video-transcript
created: 2026-08-31
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/sean-kochel/why-your-agentic-workflows-don-t-work_ILKrUq_8aC4_20260820.txt
---

# Don't Ask a Model to Rebuild Someone's System From a Video Transcript

## TL;DR

Pasting a YouTuber's transcript into a model and asking it to build you their skill or workflow reliably blows up: a transcript carries no artifacts, no acceptance criteria, and no integration checks. Rebuild the idea through your own spec process instead.

## Why it matters

A transcript describes a system without containing it, so the model reconstructs the missing pieces by guessing, and nothing validates the result against how your project actually works. The source calls this a terrible idea that will blow up in your face, even when the underlying technique is genuinely useful.

## How to apply

When a technique from a video looks worth adopting, extract the idea, then run it through your normal build process (spec, plan, tasks, your own quality gates) so it acquires artifacts and acceptance criteria native to your project. Never hand the raw transcript to a model as the build prompt.

## Related

[[gate-every-feature-on-a-constitution-file]]
