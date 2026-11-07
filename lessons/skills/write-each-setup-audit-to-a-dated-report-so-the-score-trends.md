---
id: write-each-setup-audit-to-a-dated-report-so-the-score-trends
created: 2026-09-12
status: active
supersedes: null
category: skills
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/i-turned-gpt-6-astra-into-the-ultimate-ai-second-brain_yysILVsfLFM_20260910.txt
---

# Have Your Setup-Audit Skill Write a Dated Scored Report, So You Can See the Trend

## TL;DR

A recurring audit of your own agent setup should write each run to its own dated file in an audits/ folder with a score, not just print to the terminal. The value is the trend line across runs, not any single verdict.

## Why it matters

Nate Herk's audit skill scores a fresh workspace 30 out of 100 across four dimensions and files the report: 'every single time you run this, it will store your scores every time so that you can see how you're actually improving your system month over month.' A one-off audit tells you what is weak today, which you mostly already knew; the stored series tells you whether the improvements you made since the last audit actually moved anything, which is the only way to know if the work was worth it. He then feeds the newest report into a separate level-up pass that proposes the next moves, which only works because the report is a file.

## How to apply

Make the audit skill end by writing audits/<date>-audit.md containing the per-dimension score, the total, and the specific gaps. Keep the dimensions fixed between runs or the scores stop comparing. Run it on a fixed cadence rather than when you feel like it, and have the follow-up improvement skill read the most recent report rather than re-auditing from scratch.

## Related

[[skill-log-file-for-continuity-between-runs]], [[run-insights-for-a-usage-report-card-and-pipe-into-automation]], [[pass-fail-verdict-step-in-custom-skills]]
