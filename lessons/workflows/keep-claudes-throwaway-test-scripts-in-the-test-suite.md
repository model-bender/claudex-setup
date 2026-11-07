---
id: keep-claudes-throwaway-test-scripts-in-the-test-suite
created: 2026-10-19
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1x5or3q/what_is_an_ai_lifehack_that_people_dont_seem_to/pgob4jx/
---

# Tell Claude to Keep Its Throwaway Test Scripts in the Unit Test Suite

## TL;DR

The scratch script Claude writes to check a new function is a regression test you have already paid for, so tell Claude to add it to the project's test suite instead of deleting it.

## Why it matters

Once that check is thrown away, the next change to the function runs unchecked, or Claude spends tokens writing the same check again from scratch.

## How to apply

Add a standing instruction to CLAUDE.md (or the task prompt): when you write a script to verify new code, turn it into a test in the project's suite and run it with the rest, rather than deleting it.

> "Everytime AI builds a function for you. It  creates a test script then throws it away. Just tell it to put it into the unit test suite", u/SteelCookie on r/ClaudeAI

## Related

[[replace-screenshot-responsive-checks-with-a-playwright-cdp-audit-script]]
