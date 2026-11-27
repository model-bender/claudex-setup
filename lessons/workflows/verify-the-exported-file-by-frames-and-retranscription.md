---
id: verify-the-exported-file-by-frames-and-retranscription
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/gpt-6-astra-made-this-entire-video_dT5-x3u5nCg_20260910.txt
---

# Verify a rendered video from the exported file: sample frames and re-transcribe the audio

## TL;DR

Have the agent check the exported video file, not the project: look at frames from the render, transcribe the finished audio, and compare that transcript with the script. Then fix what does not match and render again.

## Why it matters

This is how the agent described its own process in the video it produced. The stated reason is that a clipped title or a sound covering a word only shows up in the export, and it can then go back to the project and fix it.

## How to apply

Put it in the prompt or skill: after rendering, extract frames from the output file and inspect them, transcribe the output audio, diff the transcript against the script, fix the project for any mismatch, re-render. Keep the sources so the output can be compared with them.

Checked: No mechanism named. The quote is the agent-written narration of the produced video, read out in the transcript. The presenter does not describe these steps himself: his prompt only asked it to work in some verification so it was not handing him the first version.

## Related

[[review-agent-made-animations-by-eye-because-it-misses-clipping-edge-cases]]
