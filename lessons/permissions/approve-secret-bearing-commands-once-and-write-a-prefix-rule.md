---
id: approve-secret-bearing-commands-once-and-write-a-prefix-rule
created: 2026-11-15
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xr0s2i/psa_yes_and_dont_ask_again_saves_the_exact/19sbz4u7jv4u9/
---

# Never pick "don't ask again" on a command with an inline secret: approve once, then write a prefix rule and keep the secret in an env var

## TL;DR

The allow rule saved by "Yes, and don't ask again" can contain the command text exactly as approved, so a token typed into it is stored in plain text. Approve with plain "Yes" and add a rule like `Bash(psql:*)` yourself, with the credential in an env var or a .pgpass file.

## Why it matters

Rotating a leaked secret is expensive, and the leaked value stays in git history after the line is deleted. The fix is to keep it out of the approval in the first place.

## How to apply

When a permission prompt shows a credential, choose plain "Yes" and add a prefix rule by hand. Make commands read secrets from variables (`$DB_URL`, `PGPASSWORD`) so any rule that does get saved holds only the variable name.

Checked: the `Bash(<cmd>:*)` prefix form is in the Claude Code 2.1.325 binary. The word-for-word save was not reproduced here (every saved Bash rule on this machine is a prefix wildcard), and since 2.1.323 "don't ask again" keeps a rule that looks like it holds a secret for the session only, so this mainly guards older versions and secrets that check misses.

> "When the prompt shows a command with a secret inline, choose plain "yes" and then add a rule like `Bash(psql:*)` yourself, with the password in `PGPASSWORD` or a `.pgpass` file. The approval you save then has nothing sensitive in it.", u/CCodeSI on r/ClaudeCode

## Related

[[gitignore-claude-settings-local-json-in-each-repo]]
