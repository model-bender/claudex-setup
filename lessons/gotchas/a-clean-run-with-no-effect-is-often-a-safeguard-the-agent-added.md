---
id: a-clean-run-with-no-effect-is-often-a-safeguard-the-agent-added
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/how-to-build-gpt-6-astra-automations-that-don-t-eat-your-usage-limit_FqnNL8fnUWo_20260920.txt
  - transcripts/nate-herk-ai-automation/build-sell-with-codex-5-hour-course_X-pbJWKmwi0_20260923.txt
---

# When an agent-built automation runs cleanly but does nothing, ask the agent to read the run before you change anything

## TL;DR

Agents add safeguards you did not ask for. In the video Codex shipped the automation with an enabled flag set to false and with duplicate-send prevention, so two hosted test runs finished without sending anything. Hand the run back to the agent and ask what happened before treating it as a bug.

## Why it matters

The first run reported status disabled because the enable variable was false. The second reported delivered but sent nothing because it found the earlier test message from the same day and skipped the duplicate. Neither was a failure, and the dedupe guard was worth keeping.

## How to apply

Tell the agent which run you triggered and what you expected, and ask it to check the run. For a deliberate re-test, ask it to override the guard once and leave the guard in place.

Checked: No mechanism named (behaviour of the generated code, as observed in the video).

## Related

[[stop-and-diagnose-slow-unattended-automation]]
