---
id: review-md-goes-at-repo-root-and-local-code-review-ignores-it
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# Put REVIEW.md at the repository root, and know local /code-review does not read it

## TL;DR

REVIEW.md belongs at the repo root (not under `.claude/rules`), is read from the base or default branch, and only the managed Code Review service reads it.

## Why it matters

The creator guesses it sits beside CLAUDE.md or under `.claude/rules`. The docs say root, optionally plus subdirectory files on a protected branch, read never from the PR's own changes. The local `/code-review` command reads your CLAUDE.md files and not REVIEW.md, so rules you want in both places go in CLAUDE.md. The managed service is for Team and Enterprise plans on GitHub, so on other plans REVIEW.md has no reader.

## How to apply

Commit `REVIEW.md` at the root, merge it first, and protect the default branch. Keep shared rules in CLAUDE.md and PR-only rules in REVIEW.md.

Checked: Code-review-customize.md, code-review-local.md and code-review.md (live docs at code.claude.com fetched 2026-11-22); corrects the transcript's `.claude/rules` guess.

## Related

[[fix-a-recurring-review-finding-at-its-source-not-per-pr]]
