---
id: codex-adds-cross-browser-and-fault-injection-tests-by-default
created: 2026-09-01
status: active
supersedes: null
category: model-selection
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/i-made-codex-and-claude-code-build-the-same-app-one-clearly-won_WCrnS09vpfo_20260820.txt
---

# Route Cross-Browser, Property, and Fault-Injection Test Coverage to Codex: Claude Code's Default Suite Skips It

## TL;DR

In a head-to-head build, Codex added cross-browser testing, property tests, and fault injections unprompted, while Claude Code's default test suite covered security and data-correctness but not mobile/cross-browser or fault injection.

## Why it matters

If a project genuinely needs cross-browser or fault-injection coverage, don't assume Claude Code will reach for it on its own the way Codex does; either ask for it explicitly or route that slice of testing to Codex.

## How to apply

For test-writing work where cross-browser, mobile, property-based, or fault-injection coverage matters, either explicitly instruct Claude Code to add it, or hand that testing phase to Codex.

## Related

[[route-work-between-claude-code-and-codex-by-task-type]]
