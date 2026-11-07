---
id: never-run-agent-written-scripts-from-inside-an-untrusted-archive
created: 2026-08-29
status: active
supersedes: null
category: gotchas
source_type: post
tool: claude-code
sources:
  - https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/
---

# Never Let the Agent Run Its Own Script From Inside an Unpacked Untrusted Archive

## TL;DR

The working exploit against Opus 5 was not a malicious binary (Claude correctly refused that): it was Claude cd-ing into the extracted archive and running its own hand-written decoder there, which imported a `struct.py` the archive supplied.

## Why it matters

This inverts the usual instinct. Refusing the untrusted binary and writing your own replacement is the safety decision that becomes the exploit, and no permission rule flags `python3 -c` on a script the agent authored itself. As the post puts it, "Claude does not trust the supplied binary decoder, but it trusts the one it wrote itself."

## How to apply

Add a rule (or a hook on Bash) that agent-written scripts run from a clean directory, never with an untrusted extraction directory as cwd, and that Python is invoked with `-I`: "The capital -I enables Python isolated mode and prevents the child from loading the poisoned struct.py recursively." The root mechanism to remember: "Python places the extracted archive directory on its module search path."

> "Python places the extracted archive directory on its module search path.", Johann Rehberger (Embrace The Red)

## Related

[[auto-mode-is-not-injection-containment-isolate-the-session]], [[open-untrusted-material-in-a-claude-restricted-session]]
