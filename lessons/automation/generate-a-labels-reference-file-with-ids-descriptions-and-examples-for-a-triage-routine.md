---
id: generate-a-labels-reference-file-with-ids-descriptions-and-examples-for-a-triage-routine
created: 2026-10-02
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/jono-catliff/full-claude-code-masterclass-beginner-to-expert-in-2-hours-2026_R3mx8XHX8ns_20261002.txt
---

# Have Claude generate a labels reference file with IDs, descriptions and example emails for a triage routine

## TL;DR

Ask Claude to pull your real Gmail labels into a markdown file with name, label ID, description and example emails, and point the routine at it.

## Why it matters

Jono Catliff says that handing Claude a list of labels with no guidance would not sort well. The name is for you, the ID (like label_864622) is what Gmail and Claude use, and the description and examples tell Claude what belongs in each. A cloud routine cannot see local files, so they push the project to GitHub and attaches that repo to the routine.

## How to apply

Create the labels in Gmail. In a new conversation ask Claude to write references/gmail-labels.md with one entry per label (title, ID, description, examples). Push the project to GitHub, attach the repo to the routine, and reference the file in the routine prompt.

Verified: No mechanism claims. The repo requirement for cloud routines matches the existing dedicated-lean-repo-per-cloud-routine lesson. The label ID format is the creator's example.

## Related

[[dedicated-lean-repo-per-cloud-routine]]
