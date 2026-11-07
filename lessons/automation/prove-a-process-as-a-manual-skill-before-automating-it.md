---
id: prove-a-process-as-a-manual-skill-before-automating-it
created: 2026-07-12
status: active
supersedes: null
category: automation
sources:
  - transcripts/austin-marchese/you-re-the-problem-not-claude-6-fixes-to-10x-output_rs2fFITXd6g_20260710.txt
---

# Never Automate a Process You Haven't First Proven as a Hand-Run Skill

## TL;DR

Before reaching for AI on any inefficiency, run the delete-first order (question the requirement, delete it if you can, then simplify), and only after a surviving process has been done repeatedly as a Claude skill you actively use should you promote it to an automation, gating the 'should I build this automation?' decision behind a dedicated sign-off skill.

## Why it matters

Automating a process you haven't systematized manually bakes in steps that should have been deleted and failure modes you never observed, the classic error is optimizing something that shouldn't exist; a skill you've hand-run is proven and improvable, whereas an automation built on an unproven process just wastes the build effort.

## How to apply

For a recurring task: question whether the step is needed, delete if possible, simplify what's left, handle it with Claude as an assistant, then package the repeat into a skill you refine each run. Only promote a proven skill to a scheduled loop/automation, and keep an 'automation-verification' skill that must sign off before you build one so it isn't an impulse. Complements the frequency gate [[skill-frequency-test-inner-loop]] and [[run-new-loops-in-training-mode-first]].
