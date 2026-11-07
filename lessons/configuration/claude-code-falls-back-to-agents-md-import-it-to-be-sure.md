---
id: claude-code-falls-back-to-agents-md-import-it-to-be-sure
created: 2026-09-24
status: active
supersedes: null
category: configuration
tool: [claude-code, codex]
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  - https://simonwillison.net/2026/Sep/18/thariq-shihipar/
  - https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/
  - https://github.com/anthropics/claude-code/issues/95690
---

# Claude Code Reads AGENTS.md When a Directory Has No CLAUDE.md, but Import It Explicitly If You Disable Telemetry

## TL;DR

Since 2.1.277 Claude Code falls back to AGENTS.md in a directory with no CLAUDE.md, so a Codex-first repo no longer needs a symlink; but the fallback sat behind a remote flag that defaulted off until 2.1.281, so with telemetry or nonessential traffic disabled it was silently skipped. A one-line CLAUDE.md containing `@AGENTS.md` loads it unconditionally.

## Why it matters

The changelog line reads as unconditional, and for most sessions it now is. The failure mode was silent: with `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` set, on the first session after an upgrade, or on Bedrock, Vertex or a gateway, the flag could not be fetched and its fallback was off, so the file was skipped with no warning (reproduced on 2.1.278 and 2.1.280 in issue 95690). The scout's byte comparison of the installed 2.1.281 bundle shows the fallback default flipped to on, but the flag lookup is still in the path.

## How to apply

For a repo whose instructions live in AGENTS.md, either rely on the fallback on 2.1.281 or later, or make it certain with `echo '@AGENTS.md' > CLAUDE.md` (the @-import does not depend on the flag). The choice can be changed under "Project instructions" in `/config`. Setting the telemetry env vars to `0` does not help: any non-empty value counts as set. Checked: `AGENTS.md` appears in the installed 2.1.281 binary; the fallback's default flipped between 2.1.280 and 2.1.281 per the scout's diff.

> "Added AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads AGENTS.md instead; change it under "Project instructions" in `/config` (not yet on Bedrock, Vertex or Foundry)", Claude Code CHANGELOG 2.1.277

> "With telemetry or nonessential traffic turned off, a local AGENTS.md is skipped without a warning.", Przemek Szypowicz (blog.szypowi.cz)

## Related

[[unset-telemetry-opt-out-vars-because-0-still-counts-as-set]]
