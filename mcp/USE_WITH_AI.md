# Use Eremos Thai Bible with AI

Retrieve the published Thai text, instead of asking an assistant to reconstruct it from memory.

**Copy this server URL:**

```text
https://mcp.eremosapp.com/mcp
```

Streamable HTTP · read-only · no Eremos account, API key, or OAuth required.

The Eremos Translation is a complete **AI-assisted draft under review**, released under CC0. The connector reads public passages, searches Thai text, lists books, and retrieves published translation decisions. It does not edit Scripture or connect to private discipleship accounts. [Read the Bible without an AI account](https://bible.eremosapp.com).

## ChatGPT

In a ChatGPT account that permits custom MCP servers:

1. Open [Plugins](https://chatgpt.com/plugins), choose **+**, then **Add custom MCP server**.
2. Name it **Eremos Thai Bible**. Enter the server URL above and select no authentication.
3. Review the displayed connection warning, create the plugin, and inspect its four read-only tools.
4. Install it, start a conversation, and select it with **@** before trying the prompt below.

If those controls are unavailable, your client or workspace policy may not permit custom MCP servers. Check [OpenAI's current connection instructions](https://developers.openai.com/plugins/deploy/connect-chatgpt). A public package is available below; it is not a claim of approval in OpenAI's directory.

## Claude

Open **Customize → Connectors → + Add → Add custom connector**. Enter **Eremos Thai Bible** and the URL above. Continue through the detected settings, choose **No sign in**, leave credentials and request headers empty, and add the connector. Enable it for the conversation using **+ → Connectors**.

Team and Enterprise users may need an authorized administrator to add the connector first. Availability and limits vary by plan and policy; follow [Claude's current custom connector guide](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) if labels differ.

## Gemini CLI

Run this in your own shell with Gemini CLI installed:

```sh
gemini mcp add --transport http --scope user eremos-bible https://mcp.eremosapp.com/mcp
gemini mcp list
```

Restart Gemini CLI if it was already running, and use `/mcp` to inspect tools. Keep the normal tool confirmation prompts. Alternatively, merge this entry into `mcpServers` in `~/.gemini/settings.json`, preserving existing settings:

```json
{
  "mcpServers": {
    "eremos-bible": {
      "httpUrl": "https://mcp.eremosapp.com/mcp"
    }
  }
}
```

This is for **Gemini CLI**, not the Gemini consumer chat app. See [Gemini CLI's MCP documentation](https://geminicli.com/docs/tools/mcp-server/).

## Portable ChatGPT / Codex package

[Download eremos-thai-bible-1.0.0.zip](https://bible.eremosapp.com/ai/eremos-thai-bible-1.0.0.zip) · [OpenAI-specific ZIP](https://bible.eremosapp.com/ai/eremos-thai-bible-1.0.0-openai.zip) · [Inspect package source](plugin/) · [Rebuild instructions](PACKAGE.md)

The ZIP contains root `plugin.json`, `mcp.json`, and a quotation skill. In Codex, a local marketplace can point to the extracted folder; follow [OpenAI's package and local marketplace guide](https://developers.openai.com/plugins/build/plugins). The ZIP is for supported plugin import/distribution workflows, not a file to attach to an ordinary chat. Installing a package requires the recipient's own choice and any workspace permission.

## Try it

> Use Eremos Thai Bible to retrieve John 3:16–18. Quote the returned Thai exactly, name the translation, include the source link, and mention its draft-under-review status.

Compare with [John 3:16–18 in the reader](https://bible.eremosapp.com/th/john/3.html#v16).

- “List the books available in Eremos Thai Bible.”
- “Search Eremos Thai Bible for ความรัก, with a maximum of five results.”
- “Show Eremos's published translation notes for John 3:16, separately from the verse.”

## If it does not connect

Check the exact `/mcp` URL and Streamable HTTP transport. This server needs no password. Enable the connector and ask the assistant to call a tool explicitly; an answer with no tool call does not verify retrieval. If it still fails, report the client and error via [GitHub issues](https://github.com/btwinguitarists/eremos-translation/issues), without private chat content or credentials.

A browser GET to the endpoint is not an MCP test: clients initialize it with POST. Requests and search terms are sent to the hosted service. Use it for public Bible references and text, not sensitive personal information.

Each person must connect in a supported client. Registry listings do not automatically enable Eremos in every AI app. Exact quotations should retain the source and draft disclosure; explanations and paraphrases should be labeled separately.

Client instructions checked October 31, 2026.
