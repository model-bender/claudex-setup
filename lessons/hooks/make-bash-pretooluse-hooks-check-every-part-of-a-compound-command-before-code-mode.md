---
id: make-bash-pretooluse-hooks-check-every-part-of-a-compound-command-before-code-mode
created: 2026-11-22
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xy0xr9/psa_claude_code_has_an_experimental_code_mode_now/19sqwgcet8sow/
---

# Before Turning On Code Mode, Make Bash PreToolUse Hooks Check Every Part of a Compound Command

## TL;DR

In Code Mode a Bash call made from Claude's JavaScript can reach your PreToolUse hook with a prefix, so a hook that only matches the start of the command (such as `git push`) lets it through.

## Why it matters

The Code Mode docs give the example that a `git push` in a folder named `app` reaches the hook as `cd 'app' && git push`, and in auto mode the classifier reviews the script as a whole without seeing values computed at run time, so your rules and hooks are what still judge each individual call.

## How to apply

Make the hook split the command on `&&`, `||`, `;` and pipes and test each part, the way Bash permission rules already do; to inspect the script itself, add a PreToolUse hook that matches `REPL` and reads `tool_input.code`.

Checked: Live docs code.claude.com/docs/en/code-mode (curl, 2026-11-22), section Permission checks: each tool call in the code goes through deny/ask rules and PreToolUse hooks under the tool's usual name; the `cd 'app' && git push` example; the advice to make a shell-command hook check each part of a command; the `REPL` matcher with `tool_input.code`; auto mode's classifier reviews each piece of code, not each tool call, and does not see run-time values. Installed 2.1.330 binary: 6 lines match CLAUDE_CODE_EXPERIMENTAL_CODE_MODE and 4 match "REPL". The comment itself only names the caveat; the specifics come from the docs.

> "Caveats around governance (what is visible to the auto classifier, and have to take care with how it interacts with hooks)", u/SansSariph on r/ClaudeCode

## Related

[[try-claude-code-code-mode-for-tasks-with-many-tool-calls]], [[in-code-mode-check-the-script-itself-with-a-pretooluse-hook-on-repl]]
