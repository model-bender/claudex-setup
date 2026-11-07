---
id: openspec-living-spec-contract-breaks-surface-on-archive
created: 2026-07-10
status: active
supersedes: null
category: workflows
sources:
  - transcripts/sean-kochel/openspec-will-change-how-you-vibe-code-forever_nFq4POtqom4_20260703.txt
  - transcripts/sean-kochel/turning-a-vibe-coded-demo-into-a-real-product-11-things_wur4BdeE8jk_20260703.txt
  - transcripts/sean-kochel/vercel-just-fixed-vibe-coding-s-biggest-problem_hTpHmLFXBrc_20260703.txt
---

# Use OpenSpec So Every Change Reconciles Into a Living Spec That Flags Broken Requirements

## TL;DR

OpenSpec is a spec-driven framework where each change lives in changes/ and its archive/sync step merges finished work back into a master openspec/specs/ directory - and if the change violates a requirement in an existing feature's spec, archiving surfaces the conflict and forces you to reconcile it, killing the stale-documentation drift that plagues Spec Kit/BMAD.

## Why it matters

Spec-driven tools get you a clean first build but their specs rot as the app changes, and a stale architecture note silently steers the model into wrong decisions it never tells you about; OpenSpec keeps the spec as the enforced source of truth so docs can only change through structured changes and spec-breaking changes can't hide.

## How to apply

Install OpenSpec and run `openspec init`; drive it with explore (callable at ANY point to hash out ambiguities before committing - unlike Spec Kit which assumes you jump straight to the spec), propose (emits proposal + design + spec + task files), validate (you can add a Chrome-MCP visual-fidelity check as an extra pass), apply, then archive/sync to fold the change into master specs and catch breakages. Use new/continue for iterative stepwise planning (reintegrate info mid-plan) and fast-forward to auto-run remaining stages on-rails; chain in other libraries' skills (e.g. Obra's worktree + TDD skills) since it doesn't lock you into one process.
