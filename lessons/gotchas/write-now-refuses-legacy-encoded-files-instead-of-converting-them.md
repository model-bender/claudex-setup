---
id: write-now-refuses-legacy-encoded-files-instead-of-converting-them
created: 2026-10-19
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21299
---

# Expect Write to Refuse Windows-1252, Shift-JIS, GBK and UTF-16BE Files Instead of Silently Converting Them to UTF-8

## TL;DR

Since 2.1.299 Write refuses legacy-encoded files it used to re-encode to UTF-8 without telling you, and Read handles UTF-16LE with a byte-order mark correctly.

## Why it matters

The silent conversion corrupted text and changed bytes with no notice. The failure is now explicit, so a workflow that touches such files needs a plan rather than a retry.

## How to apply

Keep files that must not be re-encoded away from Write, or convert them deliberately first. Using `iconv` or a byte-level shell edit is this lesson's inference, not the changelog's. Checked: no mechanism named.

> "Fixed Read garbling UTF-16LE files with a byte-order mark, and Write dropping byte-order marks or silently converting Windows-1252, Shift-JIS, GBK or UTF-16BE files to UTF-8 (now refused)", Claude Code CHANGELOG 2.1.299

## Related

[[strip-the-utf-8-bom-from-agent-skill-and-command-files-a-bom]]
