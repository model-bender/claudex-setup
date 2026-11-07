---
id: skill-model-and-effort-pins-are-ignored-when-claude-invokes-the-skill
created: 2026-10-11
status: active
supersedes: null
category: skills
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/98898
---

# Do Not Count on a Skill's model: or effort: Pin When Claude Invokes It: Only a Typed /skill-name Applies It

## TL;DR

An open issue (reproduced on 2.1.296) reports that `model:` and `effort:` in skill frontmatter apply when you type `/skill-name` but are ignored when Claude calls the same skill through the Skill tool.

## Why it matters

A cost or quality pin you rely on (for example a cheap model for a mechanical skill) silently does nothing when the skill is auto-invoked, so that turn runs at the session's model and effort.

## How to apply

Where the pin must always apply, add `disable-model-invocation: true` so the skill only runs when typed, or move the work into a subagent definition whose own model and effort apply. Confirm by checking the model recorded for that turn in the transcript. Checked: `disable-model-invocation` has 16 hits in the 2.1.296 binary.

> "A skill's `model:` and `effort:` frontmatter is applied when the user types `/skill-name`, but silently ignored when Claude invokes the same skill via the Skill tool. The turn keeps the session model and session effort.", anthropics/claude-code issue #98898

## Related

[[a-skill-model-pin-is-an-uncached-model-switch-for-that-turn]]
