---
id: open-every-session-on-an-existing-project-with-first-run-the
created: 2026-08-22
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/
---

# Open every session on an existing project with "First run the tests"

## TL;DR

Begin any session against an existing codebase with the four-word prompt "First run the tests" so the agent discovers the suite, learns the invocation, and stays in a testing mindset for the rest of the session.

## Why it matters

The prompt does three jobs at once for four words: it proves a suite exists, it forces the agent to work out the run command itself (so it can re-run it after every later change), and the test count acts as a free proxy for project size and complexity. It also biases the agent toward extending the suite rather than shipping untested edits.

## How to apply

Literally prompt `First run the tests` as the first message of a session. Where the runner is unambiguous, name it instead, Willison uses `Run "uv run pytest"` for his Python projects because pyproject.toml is set up for it.

## Staleness

Verified still current, no flag, default, or model behaviour is involved; it is a plain opening prompt, and Claude Code still discovers and runs test suites from a bare instruction. One interaction to note in the lesson: this does NOT conflict with another lesson, whose scope limit is explicitly the red-green-refactor *design* cycle. Orienting the agent to an existing regression suite is the thing that lesson keeps.

> "It tells the agent that there is a test suite and forces it to figure out how to run the tests. This makes it almost certain that the agent will run the tests in the future to ensure it didn't break anything.", Simon Willison
