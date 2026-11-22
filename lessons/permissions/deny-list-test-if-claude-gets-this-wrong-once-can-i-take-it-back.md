---
id: deny-list-test-if-claude-gets-this-wrong-once-can-i-take-it-back
created: 2026-11-22
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/anthropic-just-released-the-new-rules-of-claude-code_8Pg6G5h05hk_20261120.txt
---

# Pick Deny-Rule Entries With One Test: If Claude Gets This Wrong Once, Can I Take It Back?

## TL;DR

Let the model handle anything you can undo (bad code, a rewritten draft). Put anything you cannot undo (wiping unsaved work, reading API keys, sending email, deleting files) in a hard deny rule in settings rather than a prompt line.

## Why it matters

Lydia Hallie's talk, as the video relays it, gives this single question as the test for what belongs on the deny list. The video's presenter adds that the same test applies to his knowledge work: a rewritten draft is fine, a sent email or deleted files are not. The video also notes that a deny rule only sees the command, not what the command does, so a compromised script run by your tests could still read keys; the presenter points to /sandbox, which limits which files a command can open and which sites it can reach, for that gap.

## How to apply

1. List what Claude does in your project that you could not reverse: reading .env or SSH keys, deleting files, sending email or messages.
2. Add those as permissions.deny entries in settings (for example a Read deny on your .env file) so the block is enforced by the harness and is not just a prompt instruction.
3. Leave reversible actions (editing code, rewriting a draft) to the model.
4. For secrets that scripts could still reach, also turn on /sandbox so file and network access is limited at the OS level.

Checked: /sandbox: 69 hits in the claude 2.1.330 binary (command grep -c -a). permissions.deny in settings is a documented key and an existing lesson (permissions/another lesson) covers that deny entries are a hard stop; the reversibility test itself is the speaker's heuristic, not a mechanism.

