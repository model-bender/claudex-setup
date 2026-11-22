---
id: start-code-mode-in-auto-mode-when-its-code-may-run-long
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/ray-amjad/code-mode-is-claude-code-s-biggest-harness-change-yet_DRNbxPk9Ab8_20261120.txt
---

# Start a Code Mode session in auto mode if its code may run for a long time

## TL;DR

Long-running Code Mode code can detach into the background and be checked with the Poll tool, but per the docs only when the session was started in auto or bypassPermissions mode. Otherwise Claude waits and the code is stopped after ten minutes.

## Why it matters

The transcript says a script that runs too long simply detaches and Claude polls it. The live docs add the condition: backgrounding (up to two hours) needs a session started in auto or bypassPermissions mode; in other modes the code stops after ten minutes.

## How to apply

For long loops or builds in Code Mode, start with `claude --permission-mode auto` (with Code Mode on). If Claude still waits, the docs say to check that you have not left auto mode with Shift+Tab and did not pass tool names to `--tools`; if the session was started in another mode, exit and run `claude --continue --permission-mode auto`. Stop background code from `/tasks` by selecting the task and pressing `x`.

Checked: Live docs https://code.claude.com/docs/en/code-mode.md fetched 2026-11-22 with curl, plus installed binary claude 2.1.330: 'Long-running code' section gives the ten minute and two hour limits and the auto or bypassPermissions condition. The transcript's unconditional wording is corrected here.

## Related

[[try-claude-code-code-mode-for-tasks-with-many-tool-calls]]
