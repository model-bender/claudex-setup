---
id: generate-character-sheets-and-storyboards-before-ai-video
created: 2026-08-29
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/turn-claude-into-a-one-person-marketing-team-in-38-mins_yCACmFTiCto_20260824.txt
---

# Generate character sheets and storyboards before AI video, and QA-reject takes before delivery

## TL;DR

For UGC-style or narrative AI video, have Claude first generate reusable character images, then storyboard frames for each scene, and only then generate video from those boards, with a final QA pass that screenshots outputs and rejects off-brand takes before reporting done.

## Why it matters

Direct text-to-video is uncontrolled: characters drift between clips and the story wanders. In the transcript's UGC ad run, Claude (driving Higgsfield) organized the output into creators/, boards/, video/, and QA/ folders: four persistent character images that can be reused as a standing brand avatar across future campaigns, board images that made "the video generation... way more in control because it's planned out with images first", and a QA pass that screenshot-checked each clip and rejected one with a bad back panel before declaring the batch finished. That structure is worth prescribing rather than hoping the model improvises it.

## How to apply

In the generation prompt or skill, require the pipeline explicitly: (1) generate character/creator images consistent with brand guidelines and save them for reuse; (2) generate storyboard frames per scene from those characters; (3) generate video conditioned on the boards; (4) run a QA pass that screenshots frames, checks logos/packaging/text against brand assets, and rejects failures into a QA folder with the reason. Reuse the character images in later batches for a consistent on-page persona instead of regenerating people every time.

## Related

[[higgsfield-mcp-for-cinematic-motion]], [[visual-self-validation-screenshot-grading]], [[bring-your-own-hero-video-to-claude-design-with-matched-first-and-last-frames]]
