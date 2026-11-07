---
id: fix-a-recurring-review-finding-at-its-source-not-per-pr
created: 2026-10-19
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: canonical
sources:
  - https://claude.dev/blog/solving-code-review-at-anthropic/
---

# When the Automated Reviewer Keeps Flagging the Same Thing, Fix It in the Skill, a Lint Rule or the Instruction File

## TL;DR

Turn a review comment that keeps recurring into a lint rule, a skill edit or an instruction-file line, rather than fixing it again in each PR.

## Why it matters

A per-PR fix costs a review round every time, and review noise costs more when the author is an agent. The post also says every review loads CLAUDE.md, so in a large codebase it should stay short and point to other docs.

## How to apply

When the same finding appears a third time, add a lint rule or edit the review skill or CLAUDE.md, and check the next reviews stop raising it. Checked: no mechanism named; REVIEW.md is a hosted Code Review feature read from the base branch, per the Code Review docs page.

> "When the automated reviewer keeps flagging the same thing, we fix it at the source: in the skill, with a lint rule, or with updates to instructional files", Claude Code team blog (Addy Osmani, Morgan Westlee Lunt, Qing Wang)

