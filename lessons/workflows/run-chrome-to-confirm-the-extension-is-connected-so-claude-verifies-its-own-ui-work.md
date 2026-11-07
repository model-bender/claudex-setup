---
id: run-chrome-to-confirm-the-extension-is-connected-so-claude-verifies-its-own-ui-work
created: 2026-10-11
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/edmund-yong/my-new-claude-code-setup-for-coding-2027-tutorial-newest-model_mVnosH9KemU_20261009.txt
---

# Run /chrome to confirm the browser extension is connected before long UI sessions

## TL;DR

Edmund runs /chrome to check the connection and permissions and follows the prompts until everything is green, so Claude can read the browser and test results before finishing.

## Why it matters

He says a connected extension makes sessions smoother because Claude can retrieve information from the browser, verify its own work and test the results. He uses auto mode for the build and plan mode first, with Fable 5.1 at max effort for that session.

## How to apply

In Claude Code run /chrome, follow the instructions to configure the extension until each item shows enabled, then start the build.

Checked: command grep -c -a -- '/chrome' on claude 2.1.296 = 35. Edmund says 'Chrome include' in the transcript (a speech-to-text artifact); I took it to mean /chrome and did not verify any subcommand.
