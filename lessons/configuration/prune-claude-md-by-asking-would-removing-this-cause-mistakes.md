---
id: prune-claude-md-by-asking-would-removing-this-cause-mistakes
created: 2026-10-25
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/simon-scrapes/5-claude-tips-everyone-recommends-but-shouldn-t_v9YVQoeSp-I_20261022.txt
---

# Prune CLAUDE.md Line by Line: Delete What Claude Already Does Unprompted, Keep What It Cannot See in Your Files

## TL;DR

Simon Scrapes calls both 'add a line for every mistake' and 'delete the whole file every 6 months' half right. Test each line with 'would removing this cause Claude to make mistakes?', delete the ones it already follows, and keep decisions and preferences that are not visible in the repo.

## Why it matters

Simon quotes Repo Rails: deleting treats a quality problem as a quantity problem. Deleting everything throws away rules that were doing real work (a team decision already made, a client who hates certain phrases) without telling you which ones. Every line costs context whether or not it helps.

## How to apply

1) Run the prompt audit first to flag instructions written for older models and references to files that no longer exist. 2) Go through what is left line by line and ask: would removing this make Claude get something wrong? 3) Delete the lines Claude already does without being told. 4) Keep the lines that carry information it cannot infer from your files. Checked: The prompt-audit subcommand exists in the installed 2.1.310 binary (14 hits for prompt-audit) and is covered by an existing lesson. The per-line test is attributed in the transcript to Anthropic's guidance; that attribution, the 200-line figure and the 80% system-prompt cut were not verified and are left out of the lesson body.

## Related

[[keep-the-context-half-of-a-skill-delete-the-procedure-half]], [[run-doctor-prompt-audit-on-your-own-config-after-a-model-upgrade]]
