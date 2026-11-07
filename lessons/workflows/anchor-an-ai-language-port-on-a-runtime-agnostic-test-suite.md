---
id: anchor-an-ai-language-port-on-a-runtime-agnostic-test-suite
created: 2026-08-29
status: active
supersedes: null
category: workflows
source_type: post
tool: [claude-code, codex]
sources:
  - https://newsletter.pragmaticengineer.com/p/inside-anthropic
---

# Anchor an AI Language Port on a Runtime-Agnostic Test Suite Before Starting

## TL;DR

Frame an AI-driven rewrite as a mechanical port with minimal behavioral change, verified by the existing test suite unchanged; this only works if the suite does not depend on the implementation language.

## Why it matters

The unchanged suite is the high-confidence signal that the port works. Bun's suite is written in TypeScript and tests the runtime black-box, which is what made a 64-agent Zig-to-Rust port verifiable; if your tests are written in the language being replaced, the agents have no ground truth until you build a language-independent harness.

## How to apply

Before fanning agents out on a port, confirm the test suite runs against the new implementation without translation (black-box or CLI-level tests); write the port plan and style guide, then use all-tests-pass as the merge criterion.

> "The least risky approach to getting something shippable would be a mechanical port from Zig to Rust, with the minimal number of behavioral changes, using the exact same test suite we already use for testing Bun.", Jarred Sumner (quoted by Gergely Orosz)

## Related

[[suggest-only-workers-one-committing-orchestrator-at-high-fan-out]]
