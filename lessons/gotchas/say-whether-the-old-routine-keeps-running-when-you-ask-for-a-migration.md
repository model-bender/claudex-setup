---
id: say-whether-the-old-routine-keeps-running-when-you-ask-for-a-migration
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/how-to-build-gpt-6-astra-automations-that-don-t-eat-your-usage-limit_FqnNL8fnUWo_20260920.txt
  - transcripts/nate-herk-ai-automation/build-sell-with-codex-5-hour-course_X-pbJWKmwi0_20260923.txt
---

# When you ask Codex to migrate a routine, say whether the old one should keep running

## TL;DR

Asked to move a scheduled routine to a new host, Codex paused the original desktop routine by its own decision. If you want both running (a demo, a parallel trial), say so in the migration prompt, and read the final report for side effects.

## Why it matters

The speaker did not want the old routine paused and only found out from the completion summary.

## How to apply

Add a line to the prompt such as 'leave the existing routine enabled' or 'pause the old one only after I confirm the new one works'.

Checked: No mechanism named (observed behaviour in the video).

