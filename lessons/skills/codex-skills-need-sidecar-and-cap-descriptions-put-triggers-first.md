---
id: codex-skills-need-sidecar-and-cap-descriptions-put-triggers-first
created: 2026-07-10
status: active
supersedes: null
category: skills
tool: codex
sources:
  - transcripts/mark-kashef/how-to-instantly-run-any-skill-in-claude-codex_tjjX43FoAUg_20260704.txt
---

# Adapt a Claude Code Skill Before Using It in Codex: In SKILL.md, Not a Sidecar, and Front-Load Trigger Keywords

## TL;DR

A Claude Code skill needs adapting before it works well in Codex: strip the Claude-only frontmatter, add a short description, and state the `$name` invocation explicitly in the body. Codex also truncates skill descriptions when you have many, so lead with trigger keywords. Keep a converter skill so porting isn't hand-work.

## Why it matters

Claude Code loads every skill description up to a character limit at session start, but Codex truncates them when you have many skills, so triggers placed at the end of a Codex description may never be read, and the skill silently won't fire.

The structural differences are real too: Claude Code's `allowed-tools` and `argument-hint` mean nothing to Codex, and Codex resolves invocation by `$name` rather than `/name` in the CLI. Hand-porting on every provider switch is wasted effort.

> **CORRECTED 2026-07-17, the sidecar YAML is wrong; the adaptation is real.** This lesson previously said a Codex skill "needs a companion sidecar/config YAML (icon, default prompt, tool dependencies, invocation policy) that Claude Code skills lack." **Verified against a live install and refuted:** `@opengsd/gsd-core` ships **71 skills into `~/.agents/skills`, every one of them a lone `SKILL.md` with no sidecar file of any kind.** If a sidecar were required, that entire shipped skill set would be inert.
>
> What the same evidence *confirms* is the underlying claim that a Claude Code skill shouldn't just be copied over: **all 71 differ from their `~/.claude/skills` twins** (0 identical). The adaptation is real, it just lives **inside `SKILL.md`**:
> - Claude-only frontmatter (`allowed-tools`, `argument-hint`) is **dropped**
> - a `metadata.short-description` is **added** (note how directly this addresses the description-truncation problem above)
> - an adapter block is **injected** into the body, spelling out the invocation contract: *"This skill is invoked by mentioning `$gsd-add-tests`. Treat all user text after `$gsd-add-tests` as `{{GSD_ARGS}}`."*
>
> **Still open:** a raw unadapted Claude skill folder has been shown invoking successfully in the Codex *app*, which suggests unadapted skills may *work* while adapted ones work *reliably*. The observation here is what a real distributed tool chooses to ship, not a controlled test of whether a bare copy fires.

## How to apply

Port by adapting the `SKILL.md` itself, there is no second file to write:

1. Put the trigger keywords **first** in the description, and keep it short.
2. Drop `allowed-tools` and `argument-hint`; add a `metadata.short-description`.
3. State the invocation contract in the body: how the skill is called (`$name` in the CLI, `/name` in the app) and how arguments arrive.

Maintain one adapter skill (a neutral shared structure plus per-provider cartridges) that converts between the two formats, so you can move skills across Claude Code and Codex turn-key and stay model-agnostic.

## Related

[[codex-has-no-custom-slash-commands-port-them-as-skills]], [[port-a-project-between-claude-code-and-codex-by-layer]]
