---
id: benchmark-skill-mines-chat-history-and-a-personal-rubric
created: 2026-08-10
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/mark-kashef/stop-guessing-which-model-to-use-build-this-instead_3ICM9ZdflZA_20260809.txt
---

# Package a /benchmark Skill That Mines Your Chat History and Scores Against a Rubric You Wrote

## TL;DR

Have Claude scan your own chat history to extract the tasks you actually run, write your own scoring rubric so the model is not grading its own homework, then package both as a `/benchmark` skill you invoke per model release: `/benchmark compare Opus 5 low vs Opus 5 high on my cold-email task`.

## Why it matters

Another lesson establishes that you should test on your own work rather than trust public benchmarks; this is the harder half of that, and two details make it work. First, the task set comes from your chat history rather than your memory of what you do, you will not recall your real recurring workload accurately. Second, the rubric is authored by you (quality as *you* define it, instruction fidelity, token efficiency, speed, turn count), because a model scoring itself against dimensions it also chose is not evidence. Together they turn "is this new model or effort tier worth switching to" into a 30-40 minute automated answer instead of a guess from someone else's demo.

## How to apply

Have Claude scan your local chat-history export (Claude Code sessions, ChatGPT exports) for recurring tasks and initiatives. Separately write your rubric dimensions and define what each means for your use case, including subjective ones. Package the flow as a skill invoked as `/benchmark <compare A vs B on task, N trials>`; have it confirm the test matrix, spin up a live tracking artifact showing per-trial progress, run the trials, then report scored against your rubric with a plain verdict and the raw outputs plus turn/token counts behind each score. Re-run against your own task set on each model or effort-tier release. Expect verdicts like "dead even, not worth switching outside of cost", a null result is a real result and saves you the migration.

