---
id: use-deep-research-for-cross-checked-multi-angle-research
created: 2026-11-22
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-changed-completely-every-new-concept-explained_YAuWBqZ_gjs_20261018.txt
  - transcripts/simon-scrapes/5-claude-tips-everyone-recommends-but-shouldn-t_v9YVQoeSp-I_20261022.txt
---

# Use /deep-research when a question needs many sources cross-checked

## TL;DR

`/deep-research <question>` runs a built-in workflow that searches from several angles, cross-checks sources, discards claims that do not hold up and returns one report.

## Why it matters

Research that needs dozens of workers does not fit one or two subagents; the workflow checks findings against each other before you see anything. The source adds to use it only when you really need it. Claude does not launch `/deep-research` on its own; you run it.

## How to apply

Type `/deep-research <your question>`; it needs the WebSearch tool. The source also recommends setting the dynamic workflow size to `small` (fewer than 5 agents) in `/config`, or with `/config workflowSizeGuideline=small`. The docs describe that guideline as advice for workflows Claude writes and do not say it bounds the bundled `/deep-research`, so watch the run's token use in `/workflows`.

Checked: Live docs at code.claude.com/docs (fetched with curl 2026-11-22) workflows.md and commands.md: `/deep-research <question>` is a built-in workflow that fans out web searches, cross-checks, votes on each claim and returns a cited report; requires WebSearch. workflows.md also gives the size guideline table (`small` is fewer than 5 agents) and the `workflowSizeGuideline` key. Claude Code CHANGELOG: 'Changed `/deep-research` to start only when invoked manually; Claude no longer launches it on its own'. `deep-research` string present (14 matches) in the Claude Code 2.1.330 binary. The transcript's broader claim that workflows never start on their own is wrong with ultracode on, where Claude plans one for each substantive task. The transcript's 'six predefined patterns' claim was not verified.

## Related

[[invoke-verify-and-code-review-manually-they-no-longer-auto-run]]
