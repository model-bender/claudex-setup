---
id: quiet-mode-env-vars-for-client-and-confidential-work
created: 2026-07-12
status: active
supersedes: null
category: settings
sources:
  - transcripts/simon-scrapes/12-hidden-tricks-that-unlock-claude-code_M2p7OvKLAWw_20260710.txt
---

# Add a Privacy 'Quiet Mode' Env Bundle to settings.json for Client/Confidential Work

## TL;DR

For client or confidential projects, disable Claude Code's outbound analytics/telemetry, Sentry error reporting, the periodic feedback survey, and non-essential model calls via the settings.json env block, and untick 'Help improve AI models' in claude.ai privacy settings.

## Why it matters

By default Claude Code sends analytics and error logs to external services and makes non-essential LLM calls (tips, banter, flavor), which is a liability under client confidentiality, and the interrupting 'How is Claude doing?' survey breaks your flow mid-task.

## How to apply

In the env block of ~/.claude/settings.json (all projects) or the project file set DISABLE_TELEMETRY and DISABLE_ERROR_REPORTING plus the feedback-survey disable to their off values, or set CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 to flip the whole outbound bundle at once, then in claude.ai Settings > Privacy turn off 'Help improve AI models.' Complements another lesson.

Corrected 2026-09-24: `DISABLE_NON_ESSENTIAL_MODEL_CALLS` has 0 occurrences in the 2.1.278, 2.1.280 and 2.1.281 binaries, so it no longer does anything. `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is not a drop-in replacement: it also blocks plugin downloads and remote flag fetches. Corrected again 2026-10-25: the How to apply line still told readers to set it; it is now out of that list (still 0 occurrences in the 2.1.310 binary).

## Related

[[flip-all-outbound-traffic-off-with-claude-code-disable-nonessential-traffic]]
