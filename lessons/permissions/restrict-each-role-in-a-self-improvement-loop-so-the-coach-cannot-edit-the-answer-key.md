---
id: restrict-each-role-in-a-self-improvement-loop-so-the-coach-cannot-edit-the-answer-key
created: 2026-11-22
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/austin-marchese/how-to-build-self-improving-ai-agents-with-claude-stanford-s-method_UUg5oij7ptw_20261122.txt
---

# Restrict Each Role in a Self-Improvement Loop So the Verifier Is Read-Only and the Coach Cannot Edit the Answer Key or the Live Agent

## TL;DR

Use separate subagents for generator, verifier and coach. Make the verifier read-only through its tools list, and block the coach from the answer key and the live agent file with path-level rules, because per-agent tool lists work on whole tools, not on files.

## Why it matters

The transcript gives two reasons the coach must not touch the answer key or the verifier: if it could, the easiest way to pass the test is to change the test, and an agent that can see the test and also write the fix learns to pass the test rather than do the job. Splitting the roles into separate agents is what lets you restrict, programmatically, which tools and files each one can reach.

## How to apply

1. Give the verifier read-only tools: list only Read, Grep and Glob in its tools field, or put Write and Edit in disallowedTools. 2. The coach needs Write or Edit to draft its candidate, and tools and disallowedTools act on whole tools: a disallowedTools entry with a specifier such as Edit(answer-key.md) removes Edit from the coach entirely. So block the answer key and the live generator file with a path rule instead: an Edit deny rule for those paths in permissions.deny (it applies to the main conversation and to subagents, so you edit those files by hand), or a PreToolUse hook in the coach's frontmatter that refuses edits to those paths. 3. Keep the answer key as a file only you edit.

Checked: Checked 2026-11-22 against code.claude.com/docs/en/sub-agents (curl): tools and disallowedTools are frontmatter fields, and 'An entry with a specifier, such as Bash(git push *), still removes the whole tool'; the same page documents hooks in subagent frontmatter and PreToolUse hooks for conditional rules. The permissions docs give Edit(path) deny rules. disallowedTools has 115 matching lines in the claude 2.1.330 binary. The path-level setup itself was not run.

## Related

[[pair-worker-subagents-with-observer-watchdog-agents]]
