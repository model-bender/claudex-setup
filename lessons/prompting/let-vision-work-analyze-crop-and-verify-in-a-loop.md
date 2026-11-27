---
id: let-vision-work-analyze-crop-and-verify-in-a-loop
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-anthropic-actually-prompts-fable-5-1_FBVNS1l5Vb8_20260910.txt
---

# For visual deliverables, let the model crop and re-inspect what it sees rather than judge in one look

## TL;DR

On dense visual input the model does its best work when it can analyze, crop and visually verify step by step. Give it that loop when it checks sites, slide decks or charts.

## Why it matters

The presenter quotes Anthropic's Fable 5.1 prompting guide on vision and applies it to the websites and slide decks people build, where the verification step is visual.

## How to apply

Run the visual check as an agent that can take a screenshot, crop regions and look again, instead of passing one full-page image. The live doc adds: give it a container with image libraries such as PIL and OpenCV, or at least an image-cropping tool.

Checked: Live docs fetched 2026-11-22: platform.claude.com prompting-claude-fable-5-1 'Give vision work tools to crop and zoom': 'On complex visual inputs such as dense charts, Claude Fable 5.1 does its best work when it can iteratively analyze, crop, and visually verify what it sees.' The general prompting best-practices page and the Opus 5.5 and Sonnet 5.5 guides give the same advice (a crop tool, or a container with PIL and OpenCV, for dense charts and drawings). The container and crop-tool detail in How to apply is from the docs, not the transcript.

## Related

[[right-size-screenshots-so-claude-can-locate-the-code]]
