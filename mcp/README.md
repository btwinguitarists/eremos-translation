# Eremos Thai Bible MCP server

Lets AI assistants (Claude, ChatGPT and others that support MCP) quote the Eremos Translation (Thai)
word for word instead of paraphrasing.

**Connect:** add a remote MCP server with the URL `https://mcp.eremosapp.com/mcp`
(Streamable HTTP, no sign-in, read-only).

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
