---
id: three-windows-permission-bypasses-fixed-in-2-1-232-and-2-1-233
created: 2026-08-16
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# On Windows, Upgrade Past 2.1.233 - Three Separate Permission Bypasses Were Fixed in Two Releases

## TL;DR

2.1.232 and 2.1.233 closed three distinct Windows permission bypasses: a PowerShell one that redirected later commands' file access, a Git Bash symlink one that let writes through unapproved, and an NT device-prefix one that bypassed UNC path validation and leaked NTLM credentials.

## Why it matters

Any one of these means the permission system was reporting a boundary it was not enforcing - the shape of bug review does not catch, because the config looks correct and nothing errors. Three in two releases says the Windows path-validation surface was systematically weaker than the Unix one, so a Windows install more than a couple of releases behind should be treated as having unenforced permission rules rather than merely being out of date.

The NTLM one is the sharpest: a crafted path does not just escape the sandbox, it can induce an outbound authentication attempt that hands over hashed credentials.

## How to apply

Upgrade Windows installs to 2.1.233 or later. If you mirror a Claude Code config across WSL and Windows, remember the two are separate installs on separate update tracks - check the Windows one explicitly with `claude --version` rather than assuming the WSL upgrade covered it.

> "Fixed Windows paths spelled with the NT `\??\` device prefix bypassing UNC path validation, closing an NTLM credential-leak vector", Claude Code CHANGELOG 2.1.233

> "Fixed a PowerShell permission bypass where variable-writing parameters could silently overwrite `$PSDefaultParameterValues` and redirect later commands' file access", Claude Code CHANGELOG 2.1.232

## Related

[[bash-input-redirection-is-not-permission-checked]], [[contain-agents-at-environment-layer-not-permission-prompts]], [[wsl-and-windows-claude-code-are-separate-installs]]
