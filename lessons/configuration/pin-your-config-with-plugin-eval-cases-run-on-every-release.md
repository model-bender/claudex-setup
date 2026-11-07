---
id: pin-your-config-with-plugin-eval-cases-run-on-every-release
created: 2026-08-29
status: active
supersedes: null
category: configuration
source_type: canonical
tool: claude-code
sources:
  - https://news.ycombinator.com/item?id=49468946
---

# Pin Your CLAUDE.md, Skills, and Hooks With claude plugin eval Cases Run on Every Release

## TL;DR

Write eval cases in Anthropic's `claude plugin eval` format that run the real agent against your setup, and re-run them on every Claude Code release and every PR that touches the config, instead of noticing behaviour drift by feel.

## Why it matters

Config artifacts have no build and no test, so a release that changes the system prompt or the model behind an alias silently changes behaviour. Running each case with and without the setup loaded is what proves a rule is doing work: the author measured a guard hook stopping `git reset --hard` at 1.00 with the hook versus 0.33 without, and a conventions skill at 1.00 versus 0.50.

## How to apply

Generate cases from the existing setup in `claude plugin eval` format, run them in a throwaway copy of the repo, and wire a GitHub Action to the Claude Code release feed. Two of the author's caveats worth encoding: "Scores lie without reasons" (keep each grader's reasoning, since a pass can come from the model refusing on its own before the hook fires) and "Eval workspaces are not sandboxes" (one hook-less run tore down a real Docker stack from a temp directory).

> "Claude Code shipped 25 versions in the last 30 days, the model behind an alias changes with no changelog, and a teammate can edit a skill in a PR nobody tests. The only signal I had was \"it feels different\".", Hacker News comment (config-drift eval author)

