---
id: check-which-registry-your-editor-installs-the-claude-code-extension-from
created: 2026-11-06
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xj7d4p/the_official_claude_code_vs_code_extension_was/19rvj4zlskrz5/
---

# Check Which Registry Your IDE Pulls the Claude Code Extension From: a Trojanized Build Was Served From One Marketplace for Hours

## TL;DR

A modified Claude Code extension build (2.1.313) that planted an ssh backdoor was served from one marketplace for an 11-hour window on 2026-10-29, which makes the registry your editor installs from part of your threat model.

## Why it matters

The npm package, the Open VSX extension and the Microsoft VS Code extension were all clean, so the exposure came entirely from which storefront the editor resolved, something most people never check or pin.

## How to apply

Confirm which marketplace your editor is configured against and which extension version is installed; if you were on the affected version in that window, check for an unexpected entry in authorized_keys.

> "OpenSourceMalware, the researchers who analyzed it, corrected their own post to say the origin was Cursor, not Open-VSX, and listed what is NOT malicious: the npm package, the OpenVSX extension, and the Microsoft VS Code extension.", u/bitspace on r/ClaudeCode

## Related

[[treat-public-hints-of-a-security-bug-as-live-exploits]]
