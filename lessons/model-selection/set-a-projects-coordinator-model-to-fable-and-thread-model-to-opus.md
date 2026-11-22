---
id: set-a-projects-coordinator-model-to-fable-and-thread-model-to-opus
created: 2026-11-22
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/anthropic-just-released-the-new-rules-of-claude-code_8Pg6G5h05hk_20261120.txt
---

# In a project, set the coordinator model to Fable and the thread model to Opus

## TL;DR

The coordinating session does not write code, so give it the model that is best at deciding what to do and judging what comes back (Fable 5.2) and run the worker threads on Opus 5.5.

## Why it matters

The rule is to match the model to the role: judgement for the coordinator, execution for the threads. The coordinator half comes from the Anthropic talk the video covers; running the threads on Opus 5.5 is Nate Herk's own suggestion.

## How to apply

In Project settings > General set Coordinator model to Fable 5.2 and Thread model to Opus 5.5.

Checked: Live docs fetched with curl on 2026-11-22 (claude-projects.md): 'Coordinator model' and 'Thread model' (each with an effort setting) are in Project settings > General; a new project runs Opus everywhere, high effort for threads and low effort for the conversation. The transcript says 'Fable 5 2' and 'Opus 5.5'.

## Related

[[claude-code-projects-main-chat-has-no-connectors-and-threads-default-to-opus-high]], [[let-claude-code-projects-split-thoughts-into-threads]], [[delegate-all-execution-off-fable-to-preserve-its-separate-weekly-cap]]
