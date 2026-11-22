---
id: try-claude-code-code-mode-for-tasks-with-many-tool-calls
created: 2026-11-22
status: active
supersedes: null
category: settings
tool: claude-code
sources:
  - transcripts/ray-amjad/code-mode-is-claude-code-s-biggest-harness-change-yet_DRNbxPk9Ab8_20261120.txt
---

# Try Claude Code's experimental Code Mode for tasks that chain many tool calls

## TL;DR

Code Mode makes Claude write JavaScript that calls its tools (Bash, Read, Edit, MCP) in one step, so intermediate results stay out of the context window. Turn it on with CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1 and read the generated code with Ctrl+O.

## Why it matters

Without it every tool result is re-read on each later call. The video's presenter reports that in his own experiment on real open source issues Code Mode used about half the input tokens and about 71% of the total cost (his measurement, not an Anthropic figure). Claude can also keep a variable from one script and reuse it in a later one, and loop, filter and dedupe across many files before anything returns to the conversation.

## How to apply

1) Check claude --version is 2.1.323 or later. 2) Set CLAUDE_CODE_EXPERIMENTAL_CODE_MODE to 1 in your shell, or in the env block of ~/.claude/settings.json (it is ignored in project settings). 3) Start claude and confirm the prompt asking to turn on Code Mode; Claude Code restarts. 4) Give it a task with many related calls, such as a change repeated across many files or a search whose results need filtering. 5) Press Ctrl+O and expand a Code row to read the JavaScript. Caveats from the docs: it is experimental, needs a terminal session on a subscription or Console account (not Bedrock, Vertex, Foundry or a gateway), and you cannot use Remote Control, Claude in Chrome or computer use in a Code Mode session. The video says the setup command warned about a mod that hooks tool calls; the changelog says Code Mode was later changed to start even when a mod hooks tool calls.

Checked: Checked 2026-11-22 on Claude Code 2.1.330: command grep -c -a CLAUDE_CODE_EXPERIMENTAL_CODE_MODE on the binary found 6 matching lines; docs page code.claude.com/docs/en/code-mode (curl) gives the env var, v2.1.323 minimum, Ctrl+O to read the code, the project-settings exclusion and the limits; the changelog lists Code Mode as added in 2.1.323 and, in 2.1.327, changed to start even when an installed mod hooks tool calls. The transcript's REPL and poll tool names were not checked and are left out. The 50% input tokens and 71% cost figures are the presenter's own test, not verified.

