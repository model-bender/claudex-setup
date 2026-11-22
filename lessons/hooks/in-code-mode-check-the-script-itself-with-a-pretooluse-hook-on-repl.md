---
id: in-code-mode-check-the-script-itself-with-a-pretooluse-hook-on-repl
created: 2026-11-22
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xy0xr9/psa_claude_code_has_an_experimental_code_mode_now/19sqwgcet8sow/
---

# In Code Mode, Check the Script Itself With a PreToolUse Hook That Matches REPL and Reads tool_input.code

## TL;DR

In Code Mode your existing hooks judge each tool call Claude's JavaScript makes; to check the script itself, add a PreToolUse hook whose matcher is `REPL` and read the code from `tool_input.code`.

## Why it matters

In Code Mode Claude writes JavaScript that calls its tools, and each tool call in that code goes through deny and ask rules and PreToolUse hooks under the tool's usual name. In auto mode the classifier reviews the script as a whole without seeing values computed at run time, so your rules and hooks are what still judge each individual call. A hook on `REPL` adds a check on the script before it runs.

## How to apply

Add a PreToolUse hook with the matcher `REPL` that reads `tool_input.code`, next to Bash hooks that split a command on `&&`, `||`, `;` and pipes and test each part. Checked: the Code Mode docs (code.claude.com/docs/en/code-mode, curl 2026-11-22) give the `REPL` matcher with `tool_input.code`.

## Related

[[make-bash-pretooluse-hooks-check-every-part-of-a-compound-command-before-code-mode]]
