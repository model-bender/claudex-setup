---
id: at-mention-files-instead-of-asking-claude-to-find-them
created: 2026-08-22
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/sean-kochel/anthropic_LWx5jp7eoBE_20260820.txt
---

# @-Mention a File Instead of Telling Claude to Go Find It

## TL;DR

An @-mention attaches the file's contents directly to the request, while naming the file in prose makes the model search directories and read outputs first, so the same work costs extra tool calls and extra context.

## Why it matters

This is the one item in the list the creator did not already know worked this way. Saying "go find the file named smoke-tests.md" starts a search across directories, and every search output plus every read is tokens that land in your context and your bill. The @-mention path attaches the actual file to the request that gets sent, so there are no search operations, no read calls, and no intermediate output to parse. The cost is invisible because both paths succeed, you just pay more for the lazy one, and the habit compounds across a long session. He frames it as one of two noise-reduction levers alongside keeping noisy command output out of the main window.

## How to apply

Where you know the path, use the @ picker to attach the file rather than describing it, and do this by default for the files you reference repeatedly. Reserve prose descriptions for cases where you genuinely do not know where something lives and want the model to search. Combine with the noise-reduction habit: for commands whose output is bulky and mostly irrelevant (git status in a repo full of untracked files), delegate the call to a cheap subagent that returns only the distilled answer instead of dumping the raw output into your main context.
