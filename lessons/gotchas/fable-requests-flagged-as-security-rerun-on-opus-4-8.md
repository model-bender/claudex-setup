---
id: fable-requests-flagged-as-security-rerun-on-opus-4-8
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-and-gpt-get-nerfed-after-launch-they-admitted-it_BqFimJpU1g8_20261120.txt
---

# Check which model answered: flagged security requests on Fable re-run on Opus 4.8

## TL;DR

Requests on Fable that a safety filter flags as security related are answered by Opus 4.8 instead. Output you take for Fable's may not be, so check before judging the model on security-flavoured work.

## Why it matters

The speaker cites a benchmark where the debugging score fell from 86 to 26 because nine of twelve tasks never reached Fable, and their own test where 14 of 63 questions were routed to Opus 4.8.

## How to apply

Watch for the switch notice in the transcript. To be asked each time, run /config, select 'Switch models when a message is flagged', and choose 'Ask each time', or set switchModelsOnFlag to false. After a fallback the session stays on the fallback model until you run /model.

Checked: Code.claude.com/docs/en/model-config.md 'Automatic model fallback' fetched 2026-11-22: for Fable models and Opus 5.5 'cybersecurity-flagged requests re-run on Opus 4.8'; a notice is shown in the main conversation; switchModelsOnFlag and the /config option confirmed; category-based fallback needs v2.1.219 or later. The 86 to 26 and 14 of 63 figures are the speaker's and were not verified.

## Related

[[reasoning-extraction-phrasing-can-silently-reroute-model]], [[check-the-per-model-usage-breakdown-after-a-long-autonomous-run]]
