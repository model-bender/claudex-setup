---
id: let-a-self-improvement-loop-apply-changes-unattended-only-with-an-exact-pass-or-fail-check
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/how-to-build-self-improving-ai-agents-with-claude-stanford-s-method_UUg5oij7ptw_20261122.txt
---

# Let a self-improvement loop apply its own changes only when the check is an exact pass or fail; otherwise have it propose and you approve

## TL;DR

Austin Marchese describes three autonomy levels: you suggest the fix, AI suggests and you approve, AI improves itself unattended. Run the unattended level only where the verifier has an exact, measurable pass or fail criterion; otherwise stay at the level where you approve each change.

## Why it matters

He says people assume self-improving means automatic, and that you likely want level two: the agents run against your past outputs, propose a change and leave you the decision. Letting AI loop through fixes on its own can lead to no longer understanding how your agent works, because it modifies itself without you seeing it. The transcript ties the level to verifiability: with an 'extremely verifiable pass or fail test case' full automation can work, which is why it is mostly seen in technical work. Where the criterion is a matter of taste, a full loop struggles in practice and your sign-off has to be the final check.

## How to apply

Ask before automating: can the verifier decide each case without judgment? If yes (tests, exact matches), an automatic loop with an iteration cap is reasonable (he stops at 10). If no, have the loop stop after producing a proposed change plus evidence, and apply it only on your approval.

Checked: No mechanism named.

## Related

[[route-self-improvement-loop-changes-into-three-approval-buckets]], [[run-new-loops-in-training-mode-first]], [[coach-agent-writes-a-candidate-file-beside-the-live-agent-one-change-per-draft]]
