---
id: cd-then-git-compounds-always-ask-route-git-through-absolute-paths
created: 2026-10-25
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xbxoza/my_claude_code_setup_it_runs_like_a_small/19rg98q7uu8cg/
---

# Claude Code Asks Before Every cd-Then-git Compound by Design, So Have Git Run Without the cd

## TL;DR

A Bash command that changes directory and then runs git gets its own approval prompt, which an earlier "allow" does not clear, because git run in another directory can pick up that repo's hooks or config; the poster avoids it by sending git through one fixed entry point.

## Why it matters

Outside auto mode this prompt recurs on every such command and looks like a broken allow rule. It is a deliberate check, so the fix is to change the command shape, not the rules.

## How to apply

Tell Claude in CLAUDE.md to run git without a preceding `cd` (absolute paths, or one wrapper script that a single allow rule covers), or deny the `cd ... && git` shape with a PreToolUse hook whose message names the allowed form. A wrapper skips exactly the check the prompt exists for, so limit it to repos you trust. Whether `git -C <path>` avoids the prompt was not tested. Checked against the installed 2.1.310 binary: the reason "This command changes directory before running a version-control command, which can pick up untrusted hooks or repository configuration from the target directory. Approve only if you trust it." sits beside the miss kind `cd-git-compound`.

> "So next time it tries to "cd <someother-repo> && git something", it asks for approval AGAIN.", u/aaraujo666 on r/ClaudeCode
