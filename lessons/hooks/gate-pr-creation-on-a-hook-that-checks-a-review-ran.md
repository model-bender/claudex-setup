---
id: gate-pr-creation-on-a-hook-that-checks-a-review-ran
created: 2026-11-22
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# Use a hook that checks Claude ran a review before a PR is submitted

## TL;DR

A lifecycle hook can check, at PR submission time, whether a review has been run in the session.

## Why it matters

It makes the self-review step a property of the setup instead of something the agent has to remember. The creator warns against a hook so aggressive that it blocks PR submission during long autonomous runs.

## How to apply

A PreToolUse hook with matcher `Bash` and `"if": "Bash(gh pr create *)"` that looks for evidence a review ran (for example in the session transcript at the input's `transcript_path`) and exits 2 to block when it finds none. The transcript names no event, matcher or evidence check; that wiring is this lesson's inference.

Checked: hooks.md (live docs at code.claude.com fetched 2026-11-22): PreToolUse, the `if` field with permission-rule syntax, `transcript_path` in the common input, and exit 2 blocking the tool call are documented; the docs call the `if` filter best-effort. 'PreToolUse' has 183 string hits in Claude Code 2.1.330. Not tested against a real payload.

## Related

[[add-a-stop-hook-that-blocks-finishing-when-code-was-written-but-not-run]], [[gate-agent-prs-on-a-test-that-fails-without-the-patch]]
