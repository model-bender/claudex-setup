---
id: auto-mode-is-not-injection-containment-isolate-the-session
created: 2026-08-29
status: active
supersedes: null
category: permissions
source_type: post
tool: claude-code
sources:
  - https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/
  - https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/
---

# Don't Count Auto Mode as Prompt-Injection Containment: It Can Even Block the Cleanup

## TL;DR

A targeted injection chain (a zip whose extracted files poison the agent's own decoder script) succeeded roughly 60-80% of the time against Opus 5 in auto mode, and in some runs the classifier let the malicious process start and then denied the command Claude issued to kill it, so treat auto mode as prompt reduction, not containment.

## Why it matters

The published evaluation this contradicts showed ~0% attack success for Opus 5 plus probes plus auto mode, so the classifier reads as much stronger than it is. Johann Rehberger's stated conclusion is that "Auto Mode IS NOT a substitute for running your agent in an isolated environment and monitoring what it is up to", and Simon Willison's endorsement adds that "The safety mechanism itself can become part of the failure." A defence layer that can block remediation while permitting the compromise is not a defence layer to build on.

## How to apply

Run anything that ingests attacker-controlled content in a VM, container, or OS sandbox with restricted egress and no credentials in reach (or in a `claude --restricted` session), and monitor it. Keep the model-plus-probes-plus-auto-mode stack as depth, never as the boundary.

> "The classifier allowed the creation of the malware process, but then it blocked the command intended to stop it!", Johann Rehberger (Embrace The Red)

## Related

[[open-untrusted-material-in-a-claude-restricted-session]], [[never-run-agent-written-scripts-from-inside-an-untrusted-archive]], [[default-to-claude-tag-a-feedback-channel-is-an-injection-vector]]
