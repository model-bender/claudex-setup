---
id: paste-the-broken-callback-url-back-when-plugin-oauth-runs-on-a-server
created: 2026-11-22
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-fable-5-2-built-my-website-here-s-how-to-actually-put-it-online_usOWZyFSxsA_20261120.txt
---

# When a plugin's sign-in lands on a broken-looking page on a remote server, paste that page's full URL back into Claude Code

## TL;DR

Authorising a plugin or MCP server from Claude Code on a remote machine ends on a browser page that looks broken. That is expected: copy the whole address from the address bar and paste it into the terminal.

## Why it matters

The OAuth redirect points at a callback on the machine running Claude Code, which your laptop's browser cannot reach when Claude runs on a server, so the page fails to load. The address itself still carries what Claude needs. The creator stresses reading the fine print because the page looks like a failure. (The localhost explanation is from the docs, not the transcript.)

## How to apply

1. Trigger the plugin's first use (the video asks it to list the account's servers and domains). 2. Sign in and approve in the browser. 3. When the page fails to load, copy the full URL from the address bar. 4. Paste it at the prompt in the terminal.

Checked: Live docs code.claude.com/docs/en/mcp: 'If the browser redirect fails with a connection error after authenticating, paste the full callback URL from your browser's address bar into the URL prompt that appears in Claude Code', and the same for `claude mcp login` over SSH. String 'callback URL' present in the 2.1.330 binary (count 11).

## Related

[[authenticate-mcp-servers-from-the-cli]]
