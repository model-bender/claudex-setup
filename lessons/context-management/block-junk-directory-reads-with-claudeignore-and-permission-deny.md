---
id: block-junk-directory-reads-with-claudeignore-and-permission-deny
created: 2026-07-17
status: active
supersedes: null
category: context-management
sources:
  - transcripts/simon-scrapes/stop-using-fable-5-in-claude-code-it-s-holding-you-back_d9XCX0PcOq0_20260712.txt
---

# Keep Junk Directories Out of Context With .claudeignore Plus an Enforced Permissions Deny

## TL;DR

Stop heavy generated dirs (node_modules, dist, build, coverage, lock files, vendor) from eating context by layering a root `.claudeignore` (advisory) with a `permissions.deny` on `Read` of those paths in settings.json (enforced), a measured setup reported ~85% context reduction.

## Why it matters

Those directories carry enormous character counts that waste tokens the instant Claude reads them. `.claudeignore` alone is only advisory, Claude may still decide to read an ignored path, so it's not a guarantee. A `permissions.deny` on Read is enforced: Claude cannot open the path even if it wants to, making the savings reliable rather than best-effort.

## How to apply

Create `.claudeignore` in the repo root listing node_modules, dist, build, coverage, lock files, vendor, etc. Then in settings.json (project or global) add `permissions.deny` entries like `Read(node_modules/**)`, `Read(dist/**)`, `Read(**/*.lock)`. Commit both so the whole team inherits the same context savings. Keep the deny list to genuinely generated/irrelevant paths so you don't block files Claude legitimately needs.

## Related

[[context-auditing-slash-context]], [[convert-docs-to-markdown-before-feeding-claude]], [[match-tool-parameters-in-permission-rules]]
