---
id: port-a-project-between-claude-code-and-codex-by-layer
created: 2026-07-17
status: active
supersedes: null
category: configuration
tool:
  - claude-code
  - codex
sources:
  - transcripts/nate-herk-ai-automation/how-to-use-your-claude-code-projects-in-codex-in-5-mins_kB9iMD0EjT8_20260627.txt
  - transcripts/nate-herk-ai-automation/100-hours-testing-claude-code-vs-chatgpt-codex-honest-results_RLjaUES9P8A_20260627.txt
  - transcripts/nate-herk-ai-automation/master-97-of-codex-in-1-hour-full-course_3TdD8Qv5Tk8_20260626.txt
  - transcripts/john-kim/complete-beginner-s-guide-to-openai-s-codex-app_20260424.txt
---

# Port a Project Across Claude Code and Codex in Three Layers: Only One of Them Actually Changes

## TL;DR

Split your project into shared knowledge (docs, references, scripts, every agent reads these unchanged), skills and agents (same content, different location), and tool-specific config (genuinely different files). Then hand the conversion to the agent itself: `CLAUDE.md` becomes `AGENTS.md`, and `.claude/` splits into `.codex/` (config.toml, agents as TOML) and `.agents/` (skills).

## Why it matters

The bulk of a mature setup is just markdown in folders and is already portable, only the thin config layer is tool-specific. So migration is a 30-second job rather than a rebuild, and knowing which layer a file lives in tells you whether to convert it, move it, or leave it alone.

Skill files (markdown + YAML frontmatter) are byte-identical across both and only need relocating. Subagent definitions are the real conversion: Claude Code uses markdown, Codex uses TOML.

**The recurring cost is drift, not the port.** Once both files exist, a change to `CLAUDE.md` that isn't mirrored into `AGENTS.md` silently splits the two tools' behaviour.

## How to apply

Prompt the agent to do it:

> I built this project with Claude Code and I need Codex to use it too, read both products' docs, create AGENTS.md from CLAUDE.md, create the .codex config, put skills in .agents/, put agents in .codex/, and make sure everything important converts.

Both global (`~/.claude` vs `~/.codex` and `~/.agents`) and project-level scopes exist on each side, so port the level you actually use.

Afterwards, whenever you make a substantive `CLAUDE.md`, skill, or subagent change, say "mirror that into AGENTS.md" in the same breath.

If you run both tools against one repo at once, keep them off the same file, two agents editing one file overwrite each other.

This is the concrete mechanics of [[portable-setup-via-open-standards]].

## Related

[[import-claude-code-into-codex-and-turn-on-sync]], [[codex-has-no-custom-slash-commands-port-them-as-skills]], [[codex-subagents-dont-auto-invoke]]
