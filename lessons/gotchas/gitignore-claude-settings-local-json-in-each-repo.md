---
id: gitignore-claude-settings-local-json-in-each-repo
created: 2026-11-15
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://news.ycombinator.com/item?id=50408126
  - https://www.reddit.com/r/ClaudeAI/comments/1xtx4ik/heads_up_claude_codes_dont_ask_again_has_been/
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Add .claude/settings.local.json to Each Repo's .gitignore: Claude Code Only Ignores It on Your Own Machine

## TL;DR

Claude Code keeps settings.local.json out of git by writing a pattern into your global git excludes, not the project's .gitignore, so on a fresh clone or another machine `git add .` commits it, along with any secret saved in its allow rules.

## Why it matters

A scan cited in both sources found 1,122 public GitHub repositories with committed settings.local.json files holding passwords and keys. Boris Cherny of the Claude Code team says the file is meant to stay local and that every team should run secret scanning whatever agent it uses. Since 2.1.323, "don't ask again" keeps a rule that looks like it holds a secret, or that would be saved to a tracked settings.local.json, for the session only.

## How to apply

Add `.claude/settings.local.json` to each repo's .gitignore and check with `git ls-files | grep -E '\.claude/settings(\.local)?\.json'`. If the file is already tracked, rotate any secret in it first, then `git rm --cached` it. Turn on secret scanning on the host.

Checked: the installed Claude Code 2.1.325 binary writes the ignore pattern to the file `git config --global core.excludesfile` names (5 hits for `core.excludesfile`), falling back to `~/.config/git/ignore`; on this machine that file's first line is `**/.claude/settings.local.json`.

> ".claude/settings.local.json is meant to stay local. This is not a file you should check into source control. We automatically gitignore it when Claude creates the file, so in this case the files were manually created and checked in", Boris Cherny (Claude Code team) on Hacker News

> "The reason it leaks is a bit subtle. Claude Code keeps the file out of git by adding it to your personal global git excludes, and those only exist on your own machine.", u/Predictor_2718 on r/ClaudeAI

## Related

[[approve-secret-bearing-commands-once-and-write-a-prefix-rule]], [[turn-on-secret-scanning-on-the-git-host-for-agent-config-leaks]]
