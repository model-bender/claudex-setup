---
id: make-a-long-one-shot-build-previewable-from-the-first-commit
created: 2026-08-22
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/2026/Aug/5/raccoon-heist/
---

# Make a long one-shot build previewable from the first commit

## TL;DR

When you set an agent loose on a long unattended build, instruct it to land a runnable index.html on the branch first and to "commit and push as often as possible", so a GitHub Pages preview shows progress mid-run instead of only at the end.

## Why it matters

An hours-long autonomous run is otherwise a black box until it finishes; committing a loadable entry point early converts every intermediate push into a live artifact you can click, so you catch a wrong direction while it is still cheap to redirect. Simon: "Telling it to 'push as often as possible' means commits start landing in that branch straight away."

## How to apply

In the initial prompt include the literal instruction "Commit and push as often as possible so I can preview your work - start with an index.html that presents a title screen, then build from there", with GitHub Pages already serving the branch so each push republishes.

> "Tell Claude what to work on, and encourage it to commit an `index.html` page as quickly as possible.", Simon Willison
