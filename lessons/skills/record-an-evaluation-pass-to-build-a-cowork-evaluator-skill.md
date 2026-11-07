---
id: record-an-evaluation-pass-to-build-a-cowork-evaluator-skill
created: 2026-08-07
status: active
supersedes: null
category: skills
tool: claude-code
about: claude-cowork
sources:
  - transcripts/austin-marchese/stop-typing-in-claude-press-record-instead_FI4NdYXltA4_20260807.txt
---

# Record Yourself Grading Output, Not Just Doing the Task

## TL;DR

Cowork's Record feature captures screen plus voice, so record yourself reviewing a bad example next to a good one, not just performing the task. That transfers your judgment and yields a skill that checks its own output before you ever see it.

## Why it matters

The default recording pattern captures *process*, never *taste*: the skill learns the clicks but has no way to tell an acceptable result from a bad one. For an email-draft skill, the creator recorded himself narrating why a one-paragraph draft was bad and a bulleted one was good, turned that into an explicit checklist, and required the skill to cite which item passed or failed. The result appends a visible pass/fail rationale to its own draft. A vibes verdict ("looks solid") is useless training signal; a checklist plus cited evidence is checkable and hard to fake.

## How to apply

For any recorded skill with a quality bar:

1. Gather one clearly bad and one clearly good real example, and narrate exactly why each is bad or good while screen-recording.
2. Convert that narration into a numbered checklist Claude can check mechanically ("name spelled correctly", "no 'Dear' as an opener", "bullets for action items"), not a vague quality bar.
3. Require evidence, not a verdict: the skill must state which checklist items passed or failed and why, appended visibly to its output, before you look at it.

## Related

[[record-a-narrated-screen-demo-to-author-a-cowork-skill-for-ui-only-software]], [[retest-a-recorded-skill-on-changed-inputs-not-the-demo-case]], [[skill-self-improvement-loop-binary-assertions]]
