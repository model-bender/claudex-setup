---
id: rebuild-heavy-use-skills-from-scratch-not-edit
created: 2026-07-10
status: active
supersedes: null
category: skills
sources:
  - transcripts/ray-amjad/cheap-fable-5-ends-this-week-here-s-where-it-actually-matters_B1sYKOWVHR0_20260705.txt
---

# Rebuild Heavy-Use Skills From Scratch (Don't Edit) With a Stronger Model

## TL;DR

Because models generate new code far better than they edit existing code, rebuild your most-used skills from scratch with a stronger model - in a clean folder from the original seed prompt so it can't copy the current skill - then diff old vs new and keep the better one.

## Why it matters

Skills accumulate cruft and often haven't been touched since an older model; editing preserves the old-model structure, whereas a from-scratch rebuild by a stronger model produces a cleaner skill you keep using even after you fall back to the cheaper model - good maintenance for skills last updated on, say, Opus 4.6.

## How to apply

Find your top skills via /usage (or have a cheap model grep your transcript history for the top ~20 by usage); recover the original prompt + seed data that created each from session history; rebuild in a fresh folder with no access to the current skill (prevents copying); compare. Optionally tune the rebuilt skill for the cheaper runtime model by having the strong model trial-run it in a weaker (e.g. Opus 4.8) sub-agent, judge the outputs, and readjust.
