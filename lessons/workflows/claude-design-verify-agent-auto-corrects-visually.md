---
id: claude-design-verify-agent-auto-corrects-visually
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
---

# Claude Design Runs an Automatic Visual Verify Pass After Every Generation

## TL;DR

After generating a deck, page, or app screen, Claude Design's agent screenshots and reviews its own output (shown as a "verify agent" status) and silently fixes specific broken elements it spots, without being asked.

## Why it matters

In the transcript this shows up as "the verify agent check completed... let me fix slide six because there was this wrong and let me fix slide 10 because this was wrong." Not knowing this is normal completion behavior, you might interrupt a run mid-self-correction or manually flag an issue the tool is already about to fix on its own.

## How to apply

Let a generation run through its verify pass before jumping in with manual corrections. Treat "verify" / "verifying" activity in the log as the tool's own screenshot-review-fix loop, not a stall.

## Related

[[route-ui-work-to-vision-capable-models-only]], [[visual-self-validation-screenshot-grading]]
