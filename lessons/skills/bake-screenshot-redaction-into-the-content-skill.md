---
id: bake-screenshot-redaction-into-the-content-skill
created: 2026-11-22
status: active
supersedes: null
category: skills
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/gpt-6-astra-voice-mode-automates-literally-anything_9oi-b5Dvtso_20260910.txt
  - transcripts/nate-herk-ai-automation/build-sell-with-codex-5-hour-course_X-pbJWKmwi0_20260923.txt
---

# Put crop and redact rules for screenshots inside the content skill itself

## TL;DR

If a skill captures screenshots for publishing (for example a video to article skill), write the cropping and the blurring of API keys and personal emails into the skill so every run does it without being asked.

## Why it matters

The presenter's article skill screenshots the source video, crops shots to the relevant region and blurs sensitive items automatically. He says the blur behaviour is now worked into the skill, so he can publish the article after only a read through. The video in that demo had nothing sensitive in it, so the blur is not shown there; in his Codex course, runs of the same skill on other models put "sensitive details redacted" blocks over details in the screenshots.

## How to apply

In the skill's instructions add a step: for each screenshot, crop to the part the paragraph is about, and blur any API key, token or personal email before placing it. This lesson's inference: check a run on a video that does contain a secret before trusting it.

Checked: No mechanism named (the skill is the presenter's own; its contents are not shown).

## Related

[[build-a-record-mode-mod-that-masks-sensitive-values-on-screen]]
