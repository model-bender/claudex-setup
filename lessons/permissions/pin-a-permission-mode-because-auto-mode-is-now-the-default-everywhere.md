---
id: pin-a-permission-mode-because-auto-mode-is-now-the-default-everywhere
created: 2026-10-02
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21284
---

# Pin a Permission Mode, Because Auto Mode Is Now the Default on Every Plan and Provider

## TL;DR

With no permission mode configured, interactive terminal and VS Code sessions now start in auto mode on every plan and provider, and so do `claude -p` and Python Agent SDK sessions on third-party providers or with telemetry off. If you want per-command review, set `permissions.defaultMode` explicitly.

## Why it matters

The older lesson scoped the auto-mode default to Pro, Max and Team accounts. Between 2.1.283 and 2.1.285 the default spread to third-party providers and telemetry-off sessions (2.1.283), every plan and provider including VS Code (2.1.284), and headless `claude -p` and Python SDK runs on third-party providers (2.1.285). A setup that relied on the absence of a setting to get prompts now runs under the classifier without being told.

## How to apply

Set `permissions.defaultMode` in settings, or pass `--permission-mode <mode>` in scripts, which still overrides the default. `Shift+Tab` cycles modes during a session; `/permissions` edits allow and deny rules mid-task (applied from the next tool call) but does not change the mode. Check which mode you are in before an unattended run.

Corrected 2026-10-02: an earlier version said `/permissions` changes the running session's mode. The 2.1.288 binary describes it as "Manage allow and deny tool permission rules", and the permission-modes docs say "During a session: press `Shift+Tab` to cycle permission modes".

Verified: `claude --help` on 2.1.287 lists `--permission-mode <mode>`; read the 2.1.283, 2.1.284 and 2.1.285 entries in the local changelog. Library grep: only the Pro/Max/Team flip is recorded.

> "Changed interactive terminal and VS Code sessions to start in auto mode when no permission mode is configured, on every plan and provider; `permissions.defaultMode` still overrides it", Claude Code CHANGELOG 2.1.284

## Related

[[auto-mode-is-not-injection-containment-isolate-the-session]]
