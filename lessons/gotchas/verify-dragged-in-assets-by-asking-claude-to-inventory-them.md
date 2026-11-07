---
id: verify-dragged-in-assets-by-asking-claude-to-inventory-them
created: 2026-08-29
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/turn-claude-into-a-one-person-marketing-team-in-38-mins_yCACmFTiCto_20260824.txt
---

# When the desktop Files panel misrenders a dragged-in folder, ask Claude to inventory it: trust the read, not the panel

## TL;DR

Nested folders dragged into a Claude Code desktop project can render wrong or appear unreadable in the app's Files panel; before assuming the assets are missing, ask Claude to list exactly what it can see in that folder and confirm the count.

## Why it matters

The desktop app's Files view is a display layer, not ground truth: in the transcript a product-shots folder dragged into assets/ "appeared weird" and looked unreadable in the panel, but when asked directly, Claude read the directory and confirmed "yes, all 11 are there, here's the inventory". Acting on the panel would have meant re-copying files or restructuring the project for nothing; the actual failure mode to guard against is silently proceeding while assets genuinely aren't visible to the model.

## How to apply

After dragging folders of assets (images, PDFs, brand kits) into a desktop-app project, run a quick verification prompt: "Inside assets/ I dragged a folder called X with N files. Can you see all of them? List them." If Claude's inventory matches, ignore the panel glitch (or refresh); if it doesn't, fix the file placement before generating anything that depends on those assets.

## Related

[[attach-only-the-files-claude-design-needs]], [[at-mention-files-instead-of-asking-claude-to-find-them]]
