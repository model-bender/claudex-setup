---
id: rerun-a-skill-on-every-past-approved-output-when-you-change-it
created: 2026-11-15
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/ask-claude-these-5-questions-it-ll-make-you-build-10x-faster_fFktpPMQzjI_20261112.txt
---

# Keep each approved skill output and rerun the edited skill on all of them to catch regressions

## TL;DR

For skills judged by a human, store every output the reviewer approved and, after each skill edit, rerun the skill on all earlier cases so nothing regresses.

## Why it matters

The author calls this a slow eval for non-technical work: it needs human judgment, so it cannot self-improve in a loop, but it still builds a test suite over time. A skill fixed for the latest feedback can quietly break an earlier edge case.

## How to apply

Generate the output with the skill, get the reviewer's feedback, adjust the skill until it is approved, then store the approved version. Next time, after changing the skill for new feedback, rerun it on all past approved inputs and compare. The example was a /generate-report skill built for an engineering firm.

## Related

[[grow-a-skill-with-one-sentence-fixes-for-failures-you-actually-watched]]
