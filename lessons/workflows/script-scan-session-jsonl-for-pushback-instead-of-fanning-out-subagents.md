---
id: script-scan-session-jsonl-for-pushback-instead-of-fanning-out-subagents
created: 2026-10-19
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/your-claude-codex-setup-is-a-mess-here-s-the-fix_eXoBC1TY8m4_20261018.txt
---

# Audit Your Past Sessions With a Keyword Script Over the JSONL Files, Not Subagents Reading Every Conversation

## TL;DR

To learn where you pushed back on or got frustrated with the agent, have it write a script that scans the session JSONL files for pushback keywords and for which tools were or were not called. Do not fan out subagents to read hundreds of conversations end to end.

## Why it matters

Mark Kashef used to ask Claude or Codex to spin up subagents to read past conversations and analyze tools and difficulties, but with hundreds or thousands of conversations the cost adds up fast. The script version produced his setup report in about 30 minutes, and the run used only about a third of the context window even though it covered both Claude and Codex environments. It also surfaced forgotten leftovers, such as eight dead sound hooks from his early Claude Code days.

## How to apply

1. Prompt: write a quick script over my Claude Code and Codex session JSONL files that finds messages where I push back or sound frustrated, and counts which tools are called or never called.
2. Have it report what you rarely or never use, which rules are outdated, and what is set up in one tool but not the other.
3. Read only the script's summary, then ask for deeper reads of the few flagged sessions.
Checked: on this machine (Claude Code 2.1.303, codex-cli 0.163.0) session transcripts exist as JSONL under ~/.claude/projects/<project>/ and a ~/.codex/sessions directory exists. The keyword approach and its savings are the speaker's claim and were not tested.

## Related

[[mine-own-jsonl-for-custom-insights-categories]], [[write-each-setup-audit-to-a-dated-report-so-the-score-trends]]
