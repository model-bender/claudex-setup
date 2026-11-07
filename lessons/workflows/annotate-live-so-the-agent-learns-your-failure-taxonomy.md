---
id: annotate-live-so-the-agent-learns-your-failure-taxonomy
created: 2026-07-25
status: active
supersedes: null
category: workflows
source_type: post
tool: claude-code
sources:
  - https://parlance-labs.com/blog/posts/auto-evals/index.html
---

# Don't Run Error Analysis One-Shot: Annotate Live and Let the Agent Learn Your Failure Taxonomy

## TL;DR

Every automated eval system tested treated error analysis as traces-in / report-out, and none interviewed the user first. The fix is to have the agent build a small review UI over your traces, then learn the taxonomy from your live annotations round by round.

## Why it matters

The failures no system caught were the ones invisible in the transcript, "fully automated approaches always failed to catch interactions that 'looked correct' but fell short of providing a great user experience": SMS Markdown artifacts, unhandled sales objections, missed human handoffs. You can't pre-write that context into a prompt, because criteria drift means you don't know your own criteria until you've read the traces.

## How to apply

Ask the agent to build a throwaway review interface over your trace dump, annotate what bothers you while it watches, and have it return suspected new instances for you to accept or dismiss. Each round pulls more product context into the eval suite. This is the interactive loop on top of one-shot error analysis, do the clustering pass first, then keep annotating.

> "The agent watches her annotations in real time (she uses Claude's monitor tool for this), learns a taxonomy of failures from them, and brings back new suspected instances for her to accept or dismiss.", Antaripa Saha and Hamel Husain

## Related

[[error-analysis-before-llm-judge-no-blanket-score]], [[run-traces-through-your-coding-agent-before-buying-an-eval-platform]]
