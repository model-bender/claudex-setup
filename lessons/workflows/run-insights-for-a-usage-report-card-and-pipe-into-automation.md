---
id: run-insights-for-a-usage-report-card-and-pipe-into-automation
created: 2026-07-10
status: active
supersedes: null
category: workflows
sources:
  - transcripts/mark-kashef/you-re-ignoring-the-two-best-features-in-claude-code_xssGpNx3its_20260704.txt
---

# Run /insights for a 30-Day Usage Report Card, Then Pipe Its Recommendations Into Rules and Automation

## TL;DR

/insights reads your last 30 days of session JSONL and generates an HTML report card - what you work on, where you fail (wrong-diagnosis loops, over-broad actions), quick wins, hook suggestions, and an 'on the horizon' section with ready-to-paste meta-prompts - which you then feed straight back into .claude/rules and a scheduled skill to compound self-improvement.

## Why it matters

It turns your own transcript history into targeted, actionable feedback only Claude Code could know (top tools, failure patterns, features you are not using), and because it emits ready-to-run prompts and rule snippets you can close the loop automatically instead of just reading a dashboard. Distinct from /stats (cost) and /team onboarding (for teammates) - this grades and improves your own usage.

## How to apply

Update to a version that has it, run /insights, and scrub client data before opening the HTML. Then act on it: 'take the suggested rules from the /insights report and save them as new rules in my .claude folder', or build a skill that runs /insights, extracts the friction points, stores them (e.g. Obsidian via its CLI) and emails a summary via the Google Workspace CLI, and schedule it monthly with /loop or /schedule. Pair with /powerup (a built-in 10-lesson interactive ASCII tutorial) to get beginners to ~80% first.

## Related

[[powerup-built-in-interactive-tutorial-for-beginners]]
