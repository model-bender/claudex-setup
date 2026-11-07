---
id: code-review-rules-section-in-agents-md
created: 2026-07-25
status: active
supersedes: null
category: configuration
source_type: post
tool: codex
sources:
  - https://developers.openai.com/blog/custom-code-review-rules-for-codex
---

# Put a `## Code Review Rules` Section in AGENTS.md to Encode the Invariants Reviewers Keep Re-Explaining

## TL;DR

A `## Code Review Rules` section in AGENTS.md, scoped to the directory it governs, stating the invariant plus the safe path, turns tribal review knowledge into findings Codex cites back to the author.

## Why it matters

OpenAI's eval suite puts numbers on it: "rule-guided variants recovered 98% of the required custom findings, compared with 58.3% in the baseline control." The rules catch the class of problem a diff cannot show, a rename that compiles cleanly but breaks an existing wire contract, which is exactly what a new contributor, or an agent working in an unfamiliar service, will miss.

## How to apply

Add `## Code Review Rules` to the AGENTS.md nearest the code it governs (repo-wide at root, service-specific in the subdirectory). Each rule states a consequential, non-obvious invariant *and* the safe alternative, the post's example covers `raw response item events (rawResponseItem/*), even while experimental` with "Keep the existing name or add a backward-compatible event." Describe outcomes rather than function names, leave formatting and lint to CI, and delete rules that repeatedly produce noise, since broad instructions compete for attention.

> "Codex Code Review can now use custom repository rules in AGENTS.md to catch those issues and point authors to the guidance behind a finding. If you already use AGENTS.md to guide coding tasks, the same file can help guide reviews, too.", Hari Srikanth, OpenAI

## Related

[[agents-override-md-and-the-project-doc-byte-cap]]
