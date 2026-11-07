---
id: re-run-a-bulk-fix-prompt-until-the-score-stops-moving
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/jono-catliff/claude-code-seo-audit-fix-your-whole-website-in-1-prompt-steal-this_M2KJ5-sFbbg_20260910.txt
  - transcripts/jono-catliff/claude-code-seo-agent-automate-everything-500k-earned__0wKlt1vHLY_20260910.txt
---

# Expect to Re-Run a Bulk-Fix Prompt Several Times, One Pass Never Closes Hundreds of Items

## TL;DR

A prompt or skill that has to land hundreds of fixes never finishes in one pass, because fixing one item regresses another. Re-issue the identical prompt (or rerun the same skill on the same target) until the measured score stops improving, and put an explicit stop condition in the prompt itself.

## Why it matters

Both creators hit the same wall from different directions. Jono Catliff's bulk-fix prompt landed roughly 400 of 500 items on the first pass and climbed to 450, then 480, on re-runs, because fixing one item frequently regresses another and the conflicts resolve across passes rather than within one. The scoring-skill case is the same shape: people read the first score as the skill's ceiling and either accept a mediocre result or start hand-patching, when the same skill run again on the same target keeps improving it. Treating the first output as the deliverable is how a fix-everything run silently ships a partially-fixed target.

## How to apply

Put an explicit stop condition in the prompt itself, along the lines of "do not stop until you have re-checked your own progress against <the external score> and it is near perfect", so the agent does not declare done at the first plausible stopping point. Then re-issue the identical prompt, or rerun the same skill on the same target, until the measured number stops moving, and read the remaining findings by hand. Pair it with an external scoreboard so "near perfect" is a number rather than a judgement, and prefer skills that apply their own fixes rather than handing back a report, so each pass actually changes the artifact. Expect wall-clock proportional to the size of the target.

## Related

[[give-bulk-fix-work-an-external-audit-score-as-its-target]], [[verify-touched-symbols-after-agent-says-done]]
