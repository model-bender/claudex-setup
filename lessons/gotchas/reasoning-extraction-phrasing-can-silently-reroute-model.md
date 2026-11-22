---
id: reasoning-extraction-phrasing-can-silently-reroute-model
created: 2026-07-02
status: active
supersedes: null
category: gotchas
sources:
  - transcripts/nate-herk-ai-automation/how-anthropic-engineers-actually-prompt-fable-5_vcU85OrwuV0_20260702.txt
---

# "Explain Your Reasoning" Phrasing Can Reroute You to a Weaker Model

## TL;DR

A standing "explain / show your reasoning" line, especially in a system prompt, can trip a safety check and reroute your request to a different, less-capable fallback model.

## Why it matters

The model runs a safety check and can hand requests that look like reasoning-extraction (or hacking, or dangerous-bio) to a fallback model. Nate says that outside the raw API response the swap is silent. In Claude Code it is not: the main conversation shows a notice in the transcript, and the session stays on the fallback model until you run /model. Corrected in place on 2026-11-22: the lesson said the swap is always silent, which the Claude Code docs contradict (the id keeps its old name so existing links still resolve).

## How to apply

Keep "explain your reasoning" / "reveal your chain of thought" out of system prompts, and don't phrase tasks in ways that read as malicious. If output quality suddenly drops, look for a fallback notice in the transcript, run /model to return to the original model, and reword the prompt. To be asked before each switch, set `switchModelsOnFlag` to `false`, or choose Ask each time under Switch models when a message is flagged in /config.

Checked: Live docs https://code.claude.com/docs/en/model-config.md (Automatic model fallback) fetched 2026-11-22 with curl, Claude Code 2.1.330 installed (`switchModelsOnFlag` present in the binary): 'In your main conversation, it shows a notice in the transcript.' and 'After a fallback, the session continues on the fallback model.' The section names cybersecurity and biology as the usual triggers and has no mention of reasoning, so that trigger is the transcript's claim. Surfaces other than Claude Code were not checked. (Note the tension with [[request-post-tool-summaries-to-learn-from-claude]], ask for a plain-English summary of *what it did*, not for its internal reasoning.)

## Related

[[request-post-tool-summaries-to-learn-from-claude]], [[avoid-the-1m-context-model-without-usage-credits]]
