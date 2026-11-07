---
id: mock-the-ui-with-fake-data-before-planning-the-backend
created: 2026-10-11
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/edmund-yong/my-new-claude-code-setup-for-coding-2027-tutorial-newest-model_mVnosH9KemU_20261009.txt
---

# Mock the new feature's UI with realistic fake data before planning the backend

## TL;DR

Edmund copies the layouts of successful apps, has Claude build the interface on mock data, and only then uses plan mode for the architecture.

## Why it matters

He says this catches design flaws and lets him test the full user experience before committing to tooling, which is hard to change later. He then asks Claude in plan mode to ask as many clarifying questions as it needs, and he says a good plan implements with minimal changes.

## How to apply

1. Find two or three apps with the same feature and pick the cleanest layout. 2. Prompt Claude to build the first interface with a realistic mock data set. 3. Review the feel. 4. Switch to plan mode, tell Claude to ask clarifying questions before finalising, then implement.

## Related

[[spec-developer-workflow-with-clarifying-questions]]
