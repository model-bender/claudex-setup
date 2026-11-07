---
id: diagnose-and-update-the-smallest-durable-place-after-a-skill-correction
created: 2026-09-24
status: active
supersedes: null
category: skills
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/anthropic-engineer-explains-what-to-build-instead-of-ai-agents_HIRDzMtuWFk_20260920.txt
  - transcripts/nate-herk-ai-automation/build-sell-with-codex-5-hour-course_X-pbJWKmwi0_20260923.txt
  - transcripts/nate-herk-ai-automation/how-to-build-codex-skills-better-than-99-of-people_9KOtMsZ9I28_20260920.txt
---

# After Correcting a Skill, Diagnose the Cause and Update the Smallest Durable Place, Not Just the Output

## TL;DR

When you correct a skill's result, don't just say fix it. Have the agent classify whether the miss was the process, missing context, a weak rule, or unreliable code, update the skill's instructions (or a reference file, or a rule) at the smallest place that fixes it, then rerun the same task to verify.

## Why it matters

A correction that only fixes the one output is thrown away the moment you close the chat, so the same mistake gets paid for again on the next run. Treating every run's feedback (both what worked and what didn't) as an update to the skill itself is what actually compounds: one creator describes never treating a skill as finished, giving feedback and telling it to update almost every time he runs it, while still keeping some oversight rather than dropping it to zero once trust builds.

## How to apply

After a bad or partial result, prompt: 'Review what went wrong during this run. Decide whether the cause was the process, missing context, a weak rule, or unreliable code. Update the skill in the smallest durable place. Then rerun the same task and verify the fix.' Make this a standing habit for skills you run often, giving explicit positive and negative feedback each time rather than only correcting failures.

## Related

[[prune-skill-learnings-file-on-a-fixed-cadence]], [[skill-log-file-for-continuity-between-runs]], [[update-brand-voice-file-on-every-manual-correction]], [[point-the-routine-at-a-skill-not-a-pasted-prompt]]
