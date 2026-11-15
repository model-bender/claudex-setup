@AGENTS.md

## Claude Code only

Everything above comes from `AGENTS.md`, the one file holding the rules Claude Code and Codex share for this repo. **To change a shared rule, edit `AGENTS.md`, never this file** (see its "Instruction files" section). Its closing "Codex only" section does not apply to you. Everything below applies to Claude Code alone.

- When authoring or debugging a hook, skill, command or agent, consult the `claude-code-guide` subagent rather than writing frontmatter or event wiring from memory. It reads the live docs. A plausible-but-wrong hook fails silently rather than erroring, so this is the class of mistake review does not catch.
