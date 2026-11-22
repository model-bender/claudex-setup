---
id: ask-codex-to-write-hard-blocks-into-config
created: 2026-11-22
status: active
supersedes: null
category: permissions
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/master-96-of-codex-in-under-35-minutes_DFlELTiSPk8_20261009.txt
---

# Have Codex write never-do-this blocks into its config files

## TL;DR

For actions that must never happen, do not rely on the permission mode alone. Ask Codex to add a block for them in the config under .codex.

## Why it matters

The permission modes are coarse. The speaker says granular 'never do this' rules can be worked into the config files.

## How to apply

Ask Codex which commands to block and have it write the rule. From the docs, the mechanism for commands is a rules file: a .rules file under a rules/ folder next to a config layer (for example ~/.codex/rules/default.rules) holding a prefix_rule with `decision = "forbidden"`, which blocks a matching command without prompting. The docs frame rules as controlling which commands Codex can run outside the sandbox. Project-local rules under `<repo>/.codex/rules/` load only when that project's .codex layer is trusted, and Codex reads rules at startup, so restart it. Test a rule with `codex execpolicy check --rules <file> -- <command>`. Rules are marked experimental.

Checked: Rules mechanism checked against the live Codex docs (learn.chatgpt.com/codex/agent-configuration/rules, fetched 2026-11-22) and codex-cli 0.171.0, where `codex execpolicy check` on a test rule returned `"decision": "forbidden"` for `git push --force origin main`. The transcript names no file; the rules-file detail is from the docs.

## Related

[[permission-deny-rules-hold-under-dangerously-skip-permissions]], [[codex-directory-trust-switches-on-project-local-hooks]]
