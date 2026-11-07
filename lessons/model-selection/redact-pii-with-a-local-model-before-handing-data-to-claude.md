---
id: redact-pii-with-a-local-model-before-handing-data-to-claude
created: 2026-09-12
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/austin-marchese/you-re-overpaying-for-claude-code-use-this-open-source-strategy-instead_WyFrrdof5oU_20260910.txt
---

# Put a Local Model in Front of Claude to Strip PII From Regulated Data

## TL;DR

When the data itself cannot leave the machine but the work needs a frontier model, run a local model first to clean and de-identify, then send the cleaned material to Claude. The constraint is the raw records, not the task.

## Why it matters

Austin Marchese's concrete case is an accounting firm that wants to use Claude but will not put client PII into a hosted model: 'by having local models, you can use AI to clean things up before it hits Claude.' This is the one genuinely useful reason to stand up a local model in his walkthrough, and it is different in kind from the cost-driven reasons: it is not a downgrade, the local model is doing the job it is adequate for (pattern-level redaction over text you control) so that the frontier model can do the job only it can do. Routing the whole task to the local model instead trades capability you need for privacy you could have kept anyway.

## How to apply

Split the pipeline at the boundary: a local step that reads the raw records and emits a de-identified version with a mapping kept locally, then the Claude step that works on the cleaned text, then a local re-identification step if the output has to reference real entities. Verify the redaction step against a sample by hand before trusting it, since a silent miss is a disclosure. Reach for it only where the data is genuinely restricted, a normal project does not need the extra hop.

## Related

[[narrow-mcp-tool-surface-over-shell-for-sensitive-work]], [[quiet-mode-env-vars-for-client-and-confidential-work]]
