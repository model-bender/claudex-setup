---
id: hyperframes-broken-preview-skip-to-full-render
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-just-destroyed-every-video-editing-tool_ZNbgOhxhzXg_20260624.txt
---

# If HyperFrames' Local Preview Shows '0 of 0 Seconds', Skip It and Ask for a Full Render Instead

## TL;DR

HyperFrames' HTML-based localhost preview sometimes fails to load a composition's duration and just shows 0 seconds of 0 seconds; rather than debugging the preview, tell Claude Code to render the full video and review that instead.

## Why it matters

Chasing a broken preview wastes time; a full render gives you something concrete to give feedback on and is a working fallback when the preview pipeline is flaky (this happened intermittently for the creator, unlike Remotion which he says never has this problem).

## How to apply

If a HyperFrames preview URL shows 0/0 seconds duration, say 'just render the full video and I'll give you feedback from there' instead of iterating on the preview. Weigh this against render cost on very long videos.
