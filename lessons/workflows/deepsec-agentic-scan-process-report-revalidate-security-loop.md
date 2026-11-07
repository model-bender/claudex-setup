---
id: deepsec-agentic-scan-process-report-revalidate-security-loop
created: 2026-07-10
status: active
supersedes: null
category: workflows
sources:
  - transcripts/sean-kochel/vercel-just-fixed-vibe-coding-s-biggest-problem_hTpHmLFXBrc_20260703.txt
  - transcripts/sean-kochel/the-5-tool-fix-for-claude-code-s-worst-habits_hqcZZuvBUSY_20260703.txt
  - transcripts/sean-kochel/turning-a-vibe-coded-demo-into-a-real-product-11-things_wur4BdeE8jk_20260703.txt
---

# Run DeepSec as an Agentic Scan -> Process -> Report -> Fix -> Revalidate Security Loop

## TL;DR

Vercel's DeepSec is an agent-powered vulnerability scanner whose npx pipeline (init -> scan regex-triages candidate files in <1s -> process runs a batched LLM deep-dive -> report groups findings by severity -> revalidate reads git history to confirm each fix) catches subtle AI-app holes a Semgrep pass or casual review misses.

## Why it matters

AI-generated apps routinely ship non-obvious vulnerabilities - prompt injection via unsanitized user text spliced into a system prompt, a DB silently wiped on abnormal server exit, an unrate-limited signup key - that deterministic scanners and human skim-reads don't surface; DeepSec's cheap regex triage plus expensive LLM analysis only on candidate files, and a git-history-aware revalidate step (~$1) after a full run (~$19-30), makes a repeatable affordable audit loop rather than a one-shot scan.

## How to apply

`npx deepsec init`, paste its setup command into Claude Code/Codex (or pass a Vercel API key to run on their infra and name the agent to avoid Codex/Claude errors), then `pnpm deepsec scan <project>` (fast candidate-file triage), `deepsec process` (batched LLM analysis -> findings), `deepsec report` (severity-grouped report.md/json), pipe the findings into a fix pass (e.g. an OpenSpec fast-forward), then `deepsec revalidate` which diffs git history to mark each issue fixed or still-open; run ~weekly. It's static analysis, so it won't catch interaction/business-logic flaws that need runtime testing.
