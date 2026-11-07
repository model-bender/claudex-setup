---
id: say-in-an-appropriate-subdirectory-instead-of-naming-the-path
created: 2026-08-22
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/guides/agentic-engineering-patterns/gif-optimization/
---

# Say "in an appropriate subdirectory" instead of naming the path yourself

## TL;DR

When you know a repo has a convention for where a kind of file lives but cannot remember what it is, deliberately underspecify the location and let the agent read the convention out of the tree.

## Why it matters

This inverts the usual "be specific" instinct in the one case where vagueness beats precision: the agent can see the whole file tree and you cannot hold it in your head. Guessing a concrete path risks inventing a second convention alongside the existing one, which is exactly the drift that later confuses agents. Willison notes the same repo has no CLAUDE.md or AGENTS.md at all and agents still infer the layout by scanning the tree.

## How to apply

In the prompt, write the placement as a constraint rather than a path, "in an appropriate subdirectory", "wherever this project keeps X", for supporting files, build scripts, fixtures, and vendored patches.

## Staleness

Verified still current, pure prompt phrasing, no version-dependent behaviour, and it depends only on the agent being able to list the repo, which every current harness does.

> "Saying \"in an appropriate subdirectory\" was enough for Claude to figure out where to put it - it found and used the existing lib/ directory.", Simon Willison
