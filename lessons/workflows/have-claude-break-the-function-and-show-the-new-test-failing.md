---
id: have-claude-break-the-function-and-show-the-new-test-failing
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xxlgbz/how_do_you_stop_claude_code_from_mocking_the/19sq1e1v290gx/
---

# Before Accepting a New Test, Have Claude Break the Function Under Test and Show the Test Failing

## TL;DR

A test that mocks the very thing it is meant to verify cannot go red, so asking Claude to break the function on purpose and run the test exposes it at once.

## Why it matters

Claude tends to mock the database call or helper and then assert the mock returned what it was told to, so the suite is green while the real query is broken, and the thread's OP reports a second auditing agent signing off on such tests because they look clean.

## How to apply

After Claude writes or changes a test, ask it to temporarily break the function under test, run the test, show you the failure, then revert the break.

Checked: no mechanism claim; a second commenter in the same thread (u/Full-SpoonFood) independently describes the same check.

> "i sometimes ask it to intentionally break the function and show me the test failing", u/Financial_Leader9701 on r/ClaudeCode

