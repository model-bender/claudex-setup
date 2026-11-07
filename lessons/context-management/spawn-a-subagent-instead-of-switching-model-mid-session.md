---
id: spawn-a-subagent-instead-of-switching-model-mid-session
created: 2026-08-22
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/sean-kochel/anthropic_LWx5jp7eoBE_20260820.txt
---

# Need a Different Model or Effort Level Mid-Session? Spawn a Subagent Instead of Switching

## TL;DR

Changing the model or the effort level in a running session invalidates the cache and forces a full reread on the next message, so delegate the differently-modelled step to a subagent and leave the main session's prefix intact.

## Why it matters

Both the model picker and the effort dial are part of the cached prefix, so touching either mid-conversation throws away the cache; at 100,000 tokens into a session that means the next message reprocesses the entire history, which costs real money on API billing and burns through subscription limits. The usual advice is to make model switches between sessions, which is correct but inconvenient when you are mid-task and only need a different level for one step. A subagent sidesteps the trade entirely: it runs in its own context at whatever model and effort you specify and returns only its result, so the parent session never changes its own prefix. It also composes with the reason you wanted the switch in the first place, since a cheaper model on a noisy step keeps the noise out of the main window too.

## How to apply

When you catch yourself reaching for the model picker mid-session, phrase it as a delegation instead, for example "kick off a Haiku subagent to check the current git status of our branch" or hand a heavier reasoning step to a subagent pinned at the higher level. Keep effort and model changes for session boundaries. Reserve this for steps whose output is a compact answer, since a subagent is a poor fit for large multi-file edits that need the full conversation's nuance.
