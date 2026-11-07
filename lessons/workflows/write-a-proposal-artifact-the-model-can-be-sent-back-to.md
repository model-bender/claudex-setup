---
id: write-a-proposal-artifact-the-model-can-be-sent-back-to
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/sean-kochel/why-your-agentic-workflows-don-t-work_ILKrUq_8aC4_20260820.txt
---

# Write the Why as a Proposal Artifact, Then Send the Model Back to It When It Drifts

## TL;DR

Before the design and the spec, write a proposal document capturing why you are building this, because it becomes the reference the model consults for decisions you never specified and the thing you point at when the build goes sideways.

## Why it matters

In the creator's four-part planning artifact set (proposal, design, spec, tasks), the proposal is the one he calls most important and the one people skip. Its function is not documentation, it is runtime guidance: at any point where the model faces a decision that was not specified in detail in the task list, it can read back the motivation and infer what you would have wanted. It is also your recovery mechanism when an autonomous build wanders, the move being to say "go read the proposal and tell me where you think this went south, because this is not the intention behind what we were building", which turns a vague complaint into a diagnosis against a written standard. The design document answers what (system design, data models, new versus extended endpoints) and the spec supplies acceptance criteria in when-this-happens-then-that form, which is what lets you judge whether a 15-hour unattended build actually delivered.

## How to apply

Sequence the planning artifacts as proposal (why), design (what, including architecture and API contracts), spec (acceptance criteria per behaviour), then tasks. Write the proposal yourself or edit it until you agree with it completely, since everything downstream inherits it. Keep it in the repo alongside the plan so the model can read it mid-build, and reference it by name when correcting drift rather than restating your intent from memory. Treat the whole set as a loop you repeat per feature, not a one-time document.

## Related

[[write-acceptance-criteria-as-when-then-pairs-to-judge-an-unattended-build]]
