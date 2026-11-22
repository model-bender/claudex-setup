---
id: run-a-cloud-bug-review-with-code-review-ultra-and-mind-the-three-free-runs
created: 2026-11-22
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/tristen-o-brien/opus-5-5-made-claude-code-unstoppable-7-levels-in-13-minutes_Zu-hJAHKJug_20261002.txt
---

# Use the cloud ultrareview for a deep bug check, knowing only three runs are free

## TL;DR

The ultrareview command runs a deep bug review of your branch's changes in Anthropic's cloud. It needs a git repository and a claude.ai login, and you get three free runs before it costs money.

## Why it matters

It is a deeper check than a local pass (it found two small bugs in the speaker's project, which Claude then fixed), but it is metered, so spend the free runs deliberately.

## How to apply

In a git repository run /code-review ultra (the transcript calls it /ultrareview, which the docs list as an alias when the feature is available to your account). With no argument it reviews the diff between your current branch and the default branch, uncommitted changes included; pass a PR number to review a GitHub pull request instead. Confirm the dialog, which shows the scope, remaining free runs and the estimated cost, then let Claude fix the findings. A paid run needs usage credits turned on.

Checked: Code.claude.com/docs/en/ultrareview.md (fetched 2026-11-22). Corrections to the transcript: the documented command is /code-review ultra with /ultrareview as an alias; it reviews a branch or PR diff, not the whole project (it falls back to every file only with no merge base or on a first commit); it launches a fleet of reviewer agents, not one agent; it needs a claude.ai login; the 3 free runs are a one-time allotment per account on Pro, Max and Ultra and do not refresh; after that a run is billed as usage credits (typically $5 to $25); a run counts once the cloud session starts. In the Claude Code 2.1.330 binary, 'ultrareview' has 119 matching lines and '/code-review ultra' 14.

## Related

[[ultrareview-multi-agent-verification-pattern]]
