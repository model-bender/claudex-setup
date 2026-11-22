---
id: exit-2-not-1-in-stop-and-task-completed-gate-hooks
created: 2026-11-22
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/anthropic-just-released-the-new-rules-of-claude-code_8Pg6G5h05hk_20261120.txt
---

# Make Completion-Gate Hooks Exit 2, Not 1, or Claude Still Marks the Task Done

## TL;DR

A hook that runs your tests or checks before Claude may finish must exit with code 2 on failure. Exit 1 is only a non-blocking error, so the work is still treated as finished.

## Why it matters

The speaker says most test tools exit with 1 on failure and the task then 'just gets marked as completed anyway'. Only exit code 2 sends Claude back to fix the problem. The Claude Code hooks docs agree: exit 2 blocks on Stop (prevents Claude from stopping) and TaskCompleted (prevents the task being marked complete), while any other non-zero code is reported as a non-blocking error and the action proceeds.

## How to apply

1. Write the check as a command hook on Stop or TaskCompleted (for example the test suite, or a format check after edits on a PostToolUse hook).
2. Make the script exit 2 when the check fails, and print the failure reason to stderr so Claude sees what to fix. A bare `npm test` or `pytest` returns 1 on failure, so wrap it: run it, and `exit 2` if it failed.
3. Exit 0 when the check passes.
4. This lesson's suggestion, not the video's: test the gate once by breaking a test on purpose and confirming Claude is sent back instead of finishing.

Checked: Hooks docs (code.claude.com/docs/en/hooks, fetched 2026-11-22, claude 2.1.330 installed): exit code 2 table lists Stop 'Prevents Claude from stopping', TaskCompleted 'Prevents the task from being marked as completed'; 'Other exit codes' section says a hook that does not exit 0 or 2 is a non-blocking error and does not stop the action. The onFailure "block" option, which makes other failures block on most events, has no effect on Stop, SubagentStop and TaskCompleted hooks, so exit 2 is the way to gate those events. For a blocking exit the docs say 'Your stderr is the reason'; the stderr detail is not in the transcript.

## Related

[[add-a-stop-hook-that-blocks-finishing-when-code-was-written-but-not-run]]
