# Eremos Thai Bible MCP server

Lets AI assistants (Claude, ChatGPT and others that support MCP) quote the Eremos Translation (Thai)
word for word instead of paraphrasing.

**Connect:** add a remote MCP server with the URL `https://mcp.eremosapp.com/mcp`
(Streamable HTTP, no sign-in, read-only).

## Connect and try it

1. In an MCP-compatible assistant, open its remote-server or connector settings.
2. Add **Eremos Thai Bible**, using the exact URL above and Streamable HTTP transport. No API key or OAuth sign-in is required by this server.
3. Enable the connector for the conversation. Availability of custom connectors depends on the client, plan, and workspace policy.
4. Ask: **“Use Eremos Thai Bible to retrieve John 3:16–18. Quote the returned Thai exactly, identify the translation, and include the source link.”**

For clients that accept an `mcpServers` configuration with HTTP URLs:

```json
{
  "mcpServers": {
    "eremos-bible": {
      "type": "http",
      "url": "https://mcp.eremosapp.com/mcp"
    }
  }
}
```

Configuration formats differ between clients; use your client's remote-MCP instructions if it does not accept this format. Do not enter personal account passwords or buy hosting to use this endpoint.

Other examples:

- “Retrieve สดุดี 23 from Eremos Thai Bible.”
- “Search the Eremos Thai text for ความรัก.”
- “Show the published translation decision notes for John 3:16, separately from the Scripture text.”

If the assistant answers without a tool call, ask it to use the enabled connector explicitly. A directory listing does not automatically connect the tool to every assistant. A GET request in a browser is not an MCP health check; clients initialize the server using POST.

## Tools and source

| Tool | What it does |
|---|---|
| `get_passage` | Thai text for a reference: `John 3:16`, `Ps 23`, `1 Cor 13:4-7`, `ยอห์น 3:16`, `JHN 3` |
| `search_text` | Verses containing Thai words, optionally within one book |
| `get_translation_notes` | The published decision record for one verse: Hebrew/Greek, the Thai chosen, the reason |
| `list_books` | All 66 books with English and Thai names, USFM codes, chapter counts |

The text is CC0 (public domain). It is a complete draft, translated from the Hebrew and Greek with
AI, machine-checked, with Thai review beginning; the server tells assistants to say so.

Data comes from the static verse API and whole-Bible file on https://bible.eremosapp.com, so the
server always serves the published text. No dependencies.

**Develop / deploy** (Cloudflare Workers): `npx wrangler dev --config mcp/wrangler.jsonc`,
`npx wrangler deploy --config mcp/wrangler.jsonc`. After book names change, run
`python3 scripts/build_mcp_books.py`.
