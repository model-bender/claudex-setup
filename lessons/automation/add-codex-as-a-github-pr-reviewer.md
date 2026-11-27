---
id: add-codex-as-a-github-pr-reviewer
created: 2026-11-22
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/john-kim/how-i-review-ai-code-meta-senior-staff-engineer_b2QkhmQ0sT0_20260923.txt
---

# Add Codex as a reviewer on GitHub pull requests

## TL;DR

Codex has a GitHub integration that reviews pull requests automatically when they open, or on demand when you call it on a PR.

## Why it matters

It gives every PR a review pass that runs outside the session that wrote the code. The speaker notes it costs money.

## How to apply

Connect the repository to Codex and turn on Automatic review in the Codex code review settings, or request one on a PR by commenting `@codex review`. The transcript only says it runs on PR open or when you add Codex on the PR; the setting name and the comment text come from the docs check. The reviewer appears on GitHub as the chatgpt-codex-connector bot.

Checked: Codex docs page "Review GitHub pull requests with Codex" (fetched with curl 2026-11-22 at learn.chatgpt.com/docs/third-party/github, where developers.openai.com/codex/cloud/code-review now redirects; codex-cli 0.171.0 installed): the repository must be connected to Codex; `@codex review` in a PR comment requests a review; Automatic review is turned on per repository under Review code in Codex settings (or under Personal preferences), with a Review trigger choosing when it runs; reviews are posted by the chatgpt-codex-connector bot. The speaker's hedge that a separately trained review model is used was not confirmed and is left out.

## Related

[[route-work-between-claude-code-and-codex-by-task-type]]
