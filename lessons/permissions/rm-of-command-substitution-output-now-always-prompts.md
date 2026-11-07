---
id: rm-of-command-substitution-output-now-always-prompts
created: 2026-09-24
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# rm -rf "$(pwd)"-Style Command-Substitution Targets Now Always Prompt, Even With an Allow Rule

## TL;DR

Before 2.1.281, an `rm -rf` whose target was purely command-substitution output (like `rm -rf "$(pwd)"`) could run completely unprompted under auto mode or --dangerously-skip-permissions, even bypassing an existing Bash allow rule that should not have covered it; it now always stops for approval unless you explicitly opt out.

## Why it matters

This was a real gap in the dangerous-rm safety net specifically for the command-substitution form, in the two modes (auto, --dangerously-skip-permissions) where nobody is watching every command; a rule written to allow something narrower could have inadvertently covered this pattern too.

## How to apply

If you run headless/unattended sessions in auto or --dangerously-skip-permissions mode and legitimately need this pattern to proceed without a prompt (e.g. a scripted cleanup step), set CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT=1 deliberately; otherwise expect a new prompt to appear where one didn't before on upgrade. Checked: `CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT` confirmed present in the installed 2.1.281 binary (command grep -c -a: 4 hits).

> "Fixed a recursive `rm` whose target is only command-substitution output, such as `rm -rf "$(pwd)"`, running unprompted in auto and `--dangerously-skip-permissions` mode; it now asks even with a Bash allow rule, unless run with `CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT=1`", Claude Code CHANGELOG 2.1.281
