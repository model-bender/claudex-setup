---
id: connect-claude-and-codex-by-installing-both-clis-no-plugin
created: 2026-10-11
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/6-ways-opus-5-5-gpt-6-astra-upgrade-your-workflow_ucer2chlfM8_20261007.txt
---

# Connect Claude and Codex by Installing Both CLIs and Telling Each to Call the Other

## TL;DR

Mark says that with both CLIs installed, each desktop app can call the other's headless CLI: in Claude a prompt names 'the Codex CLI', in Codex it names the Claude CLI, no plugin or skill.

## Why it matters

He sees `codex exec` in Claude's output when it forwards the request. The other options he lists are the official Codex plugin and a PR reviewed by the other model.

## How to apply

Install both CLIs and prompt, for example, 'don't use any plugins or skills, use the Codex CLI and send this to <model> on medium reasoning.'

Checked: codex exec --help lists 'exec  Run Codex non-interactively'; `claude --print` appears 51 times in 2.1.296 binary

## Related

[[pick-the-codex-integration-layer-by-job-exec-sdk-app-server]]
