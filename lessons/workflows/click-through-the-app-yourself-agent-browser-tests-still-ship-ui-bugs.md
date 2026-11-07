---
id: click-through-the-app-yourself-agent-browser-tests-still-ship-ui-bugs
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/i-made-codex-and-claude-code-build-the-same-app-one-clearly-won_WCrnS09vpfo_20260820.txt
---

# Budget a Manual Click-Through, Agent-Written Browser Tests Still Ship Obvious UI Bugs

## TL;DR

Both harnesses ran their own browser test suites (102 and 391 browser tests) and both still shipped navigation dead ends, dead controls and silent save failures that a few minutes of clicking found immediately.

## Why it matters

This is the case where the agent did do UI testing and it was still not enough. Claude Code's build ran 296 unit tests, 199 test cases and 102 browser tests; Codex's ran roughly 2,300 unit tests, 341 test cases and 391 browser tests. The creator's own five-minute walkthrough still found: an image upload whose preview reported "image preview unavailable", a theme colour picker that did not respond to clicks, a settings pane with no reachable log out, question numbering stuck at 1 with inconsistent "1 of 3" counters, a selected field not highlighting until you clicked away and back, a form title silently not saving until republished, and design and webhook screens with no way to navigate back. His conclusion is that you cannot underestimate how much testing is needed and that agents do not think to test what you did not drive them to test.

## How to apply

Treat the agent's test count as evidence of effort, not of correctness. After any autonomous build, walk the primary flows yourself: create, edit, navigate back out of every sub-screen, save, reload, and check whether what you typed survived. Feed the found bugs back as a fix list, then have the agent add the missed cases as regression tests so the same class does not reappear. Pay special attention to navigation and persistence, which is where both runs failed, and to states the agent has no reason to visit unless told (mobile viewport, returning to edit a previously saved value).
