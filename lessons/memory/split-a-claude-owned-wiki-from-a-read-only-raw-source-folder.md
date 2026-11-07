---
id: split-a-claude-owned-wiki-from-a-read-only-raw-source-folder
created: 2026-09-01
status: active
supersedes: null
category: memory
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-memory-system-compared-so-you-don-t-have-to_20260424.txt
---

# Split a Claude-Maintained Wiki Folder From a Read-Only Raw Source Folder

## TL;DR

Karpathy's LLM-wiki pattern uses two folders: raw/ holds your source documents (articles, transcripts, PDFs) that Claude only ever reads, and wiki/ is a folder Claude fully owns, writing every file and maintaining cross-references.

## Why it matters

Without this permission split, Claude can accidentally edit or lose your original source material while trying to update its own synthesis, and you lose a clean boundary between ground truth and Claude's derived notes.

## How to apply

Create a raw/ folder for dropped-in source documents and tell Claude never to write to it. Create a separate wiki/ folder that Claude owns completely, where it creates and updates markdown files and cross-references as it synthesizes the raw material.

## Related

[[markdown-wiki-knowledge-base-over-vector-rag]]
