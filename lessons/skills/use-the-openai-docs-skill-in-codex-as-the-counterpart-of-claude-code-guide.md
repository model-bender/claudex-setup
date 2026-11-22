---
id: use-the-openai-docs-skill-in-codex-as-the-counterpart-of-claude-code-guide
created: 2026-11-22
status: active
supersedes: null
category: skills
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/your-claude-codex-setup-is-a-mess-here-s-the-fix_eXoBC1TY8m4_20261018.txt
---

# In Codex, use the openai-docs skill when tailoring your workspace, as you would claude-code-guide in Claude Code

## TL;DR

When reorganising a workspace, tell the agent your business, what you do and your goal, and have it consult the tool's own documentation reader (the `claude-code-guide` subagent in Claude Code, the `openai-docs` skill in Codex) so the plan follows current practice for that tool.

## Why it matters

The agents' built-in knowledge of their own harness goes stale. The docs readers fetch current guidance, so the workspace plan fits how each tool works now.

## How to apply

Claude Code: ask it to use the `claude-code-guide` agent while planning the workspace. Codex: ask it to use the `openai-docs` skill. Give both the same description of the business and goal.

Checked: `claude-code-guide` is a built-in subagent: live docs code.claude.com/docs/en/sub-agents.md table row 'claude-code-guide | Haiku | When you ask questions about Claude Code features', 3 hits in the 2.1.330 binary. Codex: system skill directory ~/.codex/skills/.system/openai-docs present with codex-cli 0.171.0 (the transcript's 'OpenAI Doc skill').

